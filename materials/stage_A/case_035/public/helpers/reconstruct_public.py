"""Deterministic, input-only depth/silhouette smoke-test reconstruction.

No withheld 3D reference geometry, pretrained models, or network services are read.
Provided public segmentation annotations are used when available.
The native macOS image decoder is an optional substitute for Pillow, not a model.
"""
from __future__ import annotations

import ctypes
import csv
import hashlib
import io
import importlib.util
import json
from pathlib import Path
import sys
import zipfile

import numpy as np
from scipy import ndimage


def decode_rgb(payload: bytes) -> np.ndarray:
    """Decode RGB without installation; use Pillow or native macOS ImageIO."""
    try:
        from PIL import Image
    except ImportError:
        Image = None
    if Image is not None:
        with Image.open(io.BytesIO(payload)) as image:
            return np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    if sys.platform != "darwin":
        raise RuntimeError("Image decoding needs already-installed Pillow or macOS ImageIO; no automatic installation.")
    cf = ctypes.CDLL("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")
    cg = ctypes.CDLL("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")
    im = ctypes.CDLL("/System/Library/Frameworks/ImageIO.framework/ImageIO")
    pointer, size = ctypes.c_void_p, ctypes.c_size_t
    cf.CFDataCreate.argtypes = [pointer, pointer, ctypes.c_long]
    cf.CFDataCreate.restype = pointer
    cf.CFRelease.argtypes = [pointer]
    im.CGImageSourceCreateWithData.argtypes = [pointer, pointer]
    im.CGImageSourceCreateWithData.restype = pointer
    im.CGImageSourceCreateImageAtIndex.argtypes = [pointer, size, pointer]
    im.CGImageSourceCreateImageAtIndex.restype = pointer
    for name in ["CGImageGetWidth", "CGImageGetHeight"]:
        getattr(cg, name).argtypes = [pointer]
        getattr(cg, name).restype = size
    cg.CGColorSpaceCreateDeviceRGB.restype = pointer
    cg.CGBitmapContextCreate.argtypes = [pointer, size, size, size, size, pointer, ctypes.c_uint32]
    cg.CGBitmapContextCreate.restype = pointer

    class Point(ctypes.Structure):
        _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

    class Size(ctypes.Structure):
        _fields_ = [("width", ctypes.c_double), ("height", ctypes.c_double)]

    class Rect(ctypes.Structure):
        _fields_ = [("origin", Point), ("size", Size)]

    cg.CGContextDrawImage.argtypes = [pointer, Rect, pointer]
    for name in ["CGImageRelease", "CGColorSpaceRelease", "CGContextRelease"]:
        getattr(cg, name).argtypes = [pointer]
    data = source = image = colors = context = None
    try:
        buffer = ctypes.create_string_buffer(payload)
        data = cf.CFDataCreate(None, buffer, len(payload))
        source = im.CGImageSourceCreateWithData(data, None) if data else None
        image = im.CGImageSourceCreateImageAtIndex(source, 0, None) if source else None
        if not image:
            raise ValueError("Native decoder could not decode image")
        width, height = cg.CGImageGetWidth(image), cg.CGImageGetHeight(image)
        if not (0 < width <= 12000 and 0 < height <= 12000 and width * height <= 30_000_000):
            raise ValueError("Unexpected image dimensions")
        raster = np.zeros((height, width, 4), dtype=np.uint8)
        colors = cg.CGColorSpaceCreateDeviceRGB()
        # Explicit RGBA bytes: premultiplied-alpha-last | 32-bit-big-endian.
        context = cg.CGBitmapContextCreate(raster.ctypes.data, width, height, 8, width * 4, colors, 0x4001)
        if not context:
            raise ValueError("Native RGB bitmap allocation failed")
        cg.CGContextDrawImage(context, Rect(Point(0, 0), Size(width, height)), image)
        return raster[:, :, :3].copy()
    finally:
        if context:
            cg.CGContextRelease(context)
        if colors:
            cg.CGColorSpaceRelease(colors)
        if image:
            cg.CGImageRelease(image)
        if source:
            cf.CFRelease(source)
        if data:
            cf.CFRelease(data)


PARAMETERS = {
    "method": "single_public_frame_weak_perspective_depth_heightfield_v1",
    "frame_choice": "lexicographically first Original frame with matching Depth; no scoring or reference access",
    "maximum_image_dimension": 480,
    "checkerboard_square_side_m": 0.012,
    "depth_decoder": "3 * continuous RGB HSV hue normalized to [0,1), meters; primary Record3D convention",
    "depth_documentation": "https://github.com/marek-simonik/record3d-simple-wifi-streaming-demo",
    "depth_discrepancy": "Saved conversion helper uses OpenCV uint8 HSV divided by255, whose hue range differs. This baseline explicitly uses the primary normalized-hue convention instead; it is not claimed byte-equivalent to that helper.",
    "camera_model": "Weak perspective; isotropic image-plane scale estimated from visible colored physical squares and decoded table-depth slope. Camera intrinsics/extrinsics unavailable. No GT scaling.",
    "plane": "Six-step robust affine depth fit to valid pixels outside a dilated foreground mask",
    "mask_fallback": "Largest connected RGB region above a saturation threshold estimated from border pixels (at least0.35), after fixed closing/opening; large internal holes retained. Used only when a public source mask is missing.",
    "grid_cells_long_axis": 64,
    "smoothing_sigma_pixels": 0.8,
    "underside": "Unobserved underside is closed against the estimated tabletop; no claim that this recovers underside detail.",
    "assessment_scope": "Modest real-input smoke-test reconstruction only, not a historical submission, trained model, competitive baseline, candidate bank or consequence witness.",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rgb_hsv(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Continuous normalized HSV; explicitly not OpenCV's uint8 H/255."""
    a = rgb.astype(np.float64) / 255.0
    high, low = a.max(axis=2), a.min(axis=2)
    delta = high - low
    safe = np.maximum(delta, 1e-12)
    red, green, blue = np.moveaxis(a, 2, 0)
    winner = a.argmax(axis=2)
    hue = np.choose(winner, [(green-blue)/safe, 2+(blue-red)/safe, 4+(red-green)/safe])
    hue = np.mod(hue / 6.0, 1.0)
    hue[delta == 0] = 0
    return hue, delta / np.maximum(high, 1e-12), high


def colored_square_calibration(rgb: np.ndarray) -> tuple[dict, np.ndarray]:
    """Find a compact multi-hue cluster of similarly sized colored squares.

    This uses the public physical color checkerboard, not food/reference sizes.
    A failure is explicit: there is no arbitrary object-scale fallback.
    """
    hue, saturation, value = rgb_hsv(rgb)
    colored = ndimage.binary_opening((saturation > .45) & (value > .4), structure=np.ones((2, 2)))
    labels, _ = ndimage.label(colored)
    candidates = []
    for label, box in enumerate(ndimage.find_objects(labels), start=1):
        if box is None:
            continue
        local = labels[box] == label
        area = int(local.sum())
        bh, bw = local.shape
        if not (25 <= area <= rgb.shape[0]*rgb.shape[1]*.008 and .3 < bh/max(bw,1) < 3.3 and area/(bh*bw) > .55):
            continue
        yy, xx = np.nonzero(local)
        candidates.append({"label": label, "area": area, "center": np.array([yy.mean()+box[0].start, xx.mean()+box[1].start]), "hue": float(np.median(hue[box][local]))})
    groups = []
    remaining = set(range(len(candidates)))
    while remaining:
        group = {min(remaining)}
        pending = list(group)
        remaining -= group
        while pending:
            current = pending.pop()
            a = candidates[current]
            linked = {j for j in remaining if max(a["area"],candidates[j]["area"])/min(a["area"],candidates[j]["area"]) < 2.8 and np.linalg.norm(a["center"]-candidates[j]["center"]) < 8*np.sqrt(max(a["area"],candidates[j]["area"]))}
            group |= linked
            remaining -= linked
            pending.extend(sorted(linked))
        hues = {int(candidates[j]["hue"]*12) % 12 for j in group}
        if len(group) >= 4 and len(hues) >= 3:
            groups.append((len(group), -float(np.std([np.log(candidates[j]["area"]) for j in group])), group))
    if not groups:
        raise ValueError("PUBLIC_CHECKERBOARD_COLOR_SQUARES_NOT_DETECTED; no invented physical scale")
    _, _, group = max(groups, key=lambda row: (row[0],row[1]))
    chosen = [candidates[j] for j in sorted(group)]
    board = np.isin(labels, [x["label"] for x in chosen])
    area = float(np.median([x["area"] for x in chosen]))
    yy, xx = np.nonzero(board)
    details = {"detected_colored_squares": len(chosen), "median_projected_square_area_px": area, "square_area_range_px": [min(x["area"] for x in chosen),max(x["area"] for x in chosen)], "color_hue_bins_12": sorted({int(x["hue"]*12)%12 for x in chosen}), "bounding_box_yx": [int(yy.min()),int(xx.min()),int(yy.max()+1),int(xx.max()+1)], "initial_meters_per_pixel": PARAMETERS["checkerboard_square_side_m"]/np.sqrt(area)}
    return details, board


def foreground_from_rgb(rgb: np.ndarray, board: np.ndarray) -> np.ndarray:
    _, saturation, value = rgb_hsv(rgb)
    border=np.ones(saturation.shape,dtype=bool)
    margin=max(2,int(min(saturation.shape)*.08))
    border[margin:-margin,margin:-margin]=False
    baseline=float(np.median(saturation[border]))
    spread=float(np.median(np.abs(saturation[border]-baseline)))
    threshold=max(.35,min(.65,baseline+3*1.4826*spread))
    mask = (saturation > threshold) & (value > .16)
    yy, xx = np.nonzero(board)
    mask[max(0,yy.min()-5):yy.max()+6,max(0,xx.min()-5):xx.max()+6] = False
    mask = ndimage.binary_closing(mask, structure=np.ones((5,5)))
    mask = ndimage.binary_opening(mask, structure=np.ones((2,2)))
    labels, number = ndimage.label(mask)
    if number == 0:
        raise ValueError("NO_IMAGE_DERIVED_FOREGROUND")
    counts = np.bincount(labels.ravel());counts[0] = 0
    mask = labels == int(counts.argmax())
    # Fill only small texture holes, preserving a real bagel/food hole.
    holes = ndimage.binary_fill_holes(mask) & ~mask
    hole_labels, _ = ndimage.label(holes)
    sizes = np.bincount(hole_labels.ravel())
    small = (sizes <= max(8, int(mask.sum()*.003)))
    small[0] = False
    mask |= small[hole_labels]
    return mask


def robust_depth_plane(depth: np.ndarray, valid: np.ndarray, foreground: np.ndarray) -> tuple[np.ndarray, dict]:
    height,width = depth.shape
    yy,xx = np.indices(depth.shape,dtype=float)
    usable = valid & ~ndimage.binary_dilation(foreground, iterations=8)
    usable &= (xx > .04*width)&(xx < .96*width)&(yy > .04*height)&(yy < .96*height)
    take = usable & ((xx.astype(int)%3)==0)&((yy.astype(int)%3)==0)
    if take.sum() < 50:
        raise ValueError("INSUFFICIENT_PUBLIC_BACKGROUND_DEPTH_FOR_PLANE")
    x = np.column_stack([(xx[take]-width/2)/width,(yy[take]-height/2)/height,np.ones(take.sum())])
    target = depth[take]
    weights = np.ones(target.size)
    for _ in range(6):
        root = np.sqrt(weights)
        coefficient = np.linalg.lstsq(x*root[:,None],target*root,rcond=None)[0]
        residual = target-x@coefficient
        scale = max(float(np.median(np.abs(residual-np.median(residual))))*1.4826, .0005)
        weights = np.minimum(1,1.5*scale/np.maximum(np.abs(residual),1e-12))
    coefficient = np.array([coefficient[0]/width,coefficient[1]/height,coefficient[2]])
    return coefficient,{"background_depth_samples":int(take.sum()),"plane_depth_slope_m_per_pixel":[float(coefficient[0]),float(coefficient[1])],"plane_center_depth_m":float(coefficient[2]),"robust_residual_scale_m":scale}


def mesh_from_arrays(rgb: np.ndarray, depth_rgb: np.ndarray, source_mask: np.ndarray | None) -> tuple[np.ndarray,np.ndarray,dict]:
    if rgb.shape != depth_rgb.shape:
        raise ValueError("RGB_DEPTH_RASTER_MISMATCH")
    calibration, board = colored_square_calibration(rgb)
    if source_mask is not None:
        foreground = source_mask.astype(bool)
        mask_route = "provided_public_mask_threshold127"
    else:
        foreground = foreground_from_rgb(rgb,board)
        mask_route = "RGB_saturation_component_fallback; source_mask_missing"
    if foreground.shape != rgb.shape[:2] or foreground.sum() < 20:
        raise ValueError("EMPTY_OR_INCOMPATIBLE_PUBLIC_FOREGROUND")
    hue,saturation,value = rgb_hsv(depth_rgb)
    depth = 3*hue
    # Author documentation marks red as invalid; JPEG may create wrap-around.
    valid = (saturation > .25)&(value > .12)&(hue > .002)&(hue < .98)
    if valid.sum() < 100:
        raise ValueError("INSUFFICIENT_VALID_PUBLIC_DEPTH")
    high = np.quantile(depth[valid],.995)
    valid &= depth <= high
    coefficient,plane_report = robust_depth_plane(depth,valid,foreground)
    # A projected square on an affine-depth plane has area
    # pixel_area * mpp * sqrt(mpp^2 + ||depth_gradient||^2).
    # Solve for isotropic image-plane scale using the known physical square.
    target_area_per_pixel = PARAMETERS["checkerboard_square_side_m"]**2/calibration["median_projected_square_area_px"]
    gradient2 = float(coefficient[0]**2+coefficient[1]**2)
    root = np.sqrt(gradient2**2+4*target_area_per_pixel**2)
    scale2 = 2*target_area_per_pixel**2/(gradient2+root)
    mpp = float(np.sqrt(scale2))
    if not np.isfinite(mpp) or mpp <= 0:
        raise ValueError("PUBLIC_PHYSICAL_SCALE_INVALID")
    calibration["slope_corrected_meters_per_pixel"] = mpp
    calibration["calibration_assumption"] = "Each detected colored patch is one0.012m square; weak-perspective isotropic pixel axes; approximate saturation-boundary area. No private geometry or fitted similarity scale."
    nearest = ndimage.distance_transform_edt(~valid,return_distances=False,return_indices=True)
    filled = depth[tuple(nearest)]
    smoothed = ndimage.gaussian_filter(ndimage.median_filter(filled,size=3),PARAMETERS["smoothing_sigma_pixels"])
    h,w = depth.shape
    yy,xx = np.indices(depth.shape,dtype=float)
    xyz = np.stack([(xx-w/2)*mpp,-(yy-h/2)*mpp,-smoothed],axis=-1)
    normal = np.array([coefficient[0]/mpp,-coefficient[1]/mpp,1.0]);normal/=np.linalg.norm(normal)
    ex = np.array([1.,0.,0.])-normal*normal[0];ex/=np.linalg.norm(ex)
    ey = np.cross(normal,ex)
    center = np.array([np.median(xyz[:,:,0][foreground]),np.median(xyz[:,:,1][foreground]),-coefficient[2]])
    local = np.stack([(xyz-center)@ex,(xyz-center)@ey,(xyz-center)@normal],axis=-1)
    # Place the fitted tabletop at z=0; recover the source-estimated top only.
    plane_origin = np.array([0.,0.,-coefficient[2]])
    local[:,:,2] = (xyz-plane_origin)@normal
    local[:,:,2] = np.maximum(local[:,:,2],0)
    fy,fx = np.nonzero(foreground)
    stride = max(1,int(np.ceil(max(fy.ptp() if hasattr(fy,"ptp") else np.ptp(fy),np.ptp(fx))/PARAMETERS["grid_cells_long_axis"])))
    ys = np.arange(max(0,int(fy.min())-1),min(h,int(fy.max())+2),stride)
    xs = np.arange(max(0,int(fx.min())-1),min(w,int(fx.max())+2),stride)
    gy,gx = np.meshgrid(ys,xs,indexing="ij")
    inside = foreground[gy,gx]
    index = np.full(inside.shape,-1,dtype=int);index[inside]=np.arange(int(inside.sum()))
    vertices = local[gy[inside],gx[inside]]
    top_faces = []
    for i in range(len(ys)-1):
        for j in range(len(xs)-1):
            corners=[index[i,j],index[i,j+1],index[i+1,j],index[i+1,j+1]]
            for tri in [(corners[0],corners[2],corners[1]),(corners[1],corners[2],corners[3])]:
                if min(tri)>=0:top_faces.append(tri)
    if not top_faces:
        raise ValueError("NO_FOREGROUND_GRID_TRIANGLES")
    top_faces=np.asarray(top_faces,dtype=np.int64)
    used=np.unique(top_faces);remap=np.full(len(vertices),-1,dtype=int);remap[used]=np.arange(len(used));vertices=vertices[used];top_faces=remap[top_faces]
    count=len(vertices);bottom=vertices.copy();bottom[:,2]=0
    all_vertices=np.vstack([vertices,bottom]);all_faces=[tuple(x) for x in top_faces]
    all_faces.extend(tuple(x[::-1]+count) for x in top_faces)
    edges={}
    for face in top_faces:
        for a,b in zip(face,np.roll(face,-1)):
            key=tuple(sorted((int(a),int(b))));edges.setdefault(key,[]).append((int(a),int(b)))
    boundary=0
    for oriented in edges.values():
        if len(oriented)==1:
            a,b=oriented[0];all_faces.extend([(b,a,a+count),(b,a+count,b+count)]);boundary+=1
    all_faces=np.asarray(all_faces,dtype=np.int64)
    cross=np.cross(all_vertices[all_faces[:,1]]-all_vertices[all_faces[:,0]],all_vertices[all_faces[:,2]]-all_vertices[all_faces[:,0]])
    keep=np.linalg.norm(cross,axis=1)>1e-14
    all_faces=all_faces[keep]
    used=np.unique(all_faces);remap=np.full(len(all_vertices),-1,dtype=int);remap[used]=np.arange(len(used));all_vertices=all_vertices[used];all_faces=remap[all_faces]
    report={"mask_route":mask_route,"foreground_pixels":int(foreground.sum()),"valid_depth_fraction":float(valid.mean()),"valid_depth_inside_mask_fraction":float(valid[foreground].mean()),"depth_range_valid_m":[float(depth[valid].min()),float(depth[valid].max())],"calibration":calibration,"table_plane":plane_report,"grid_stride_pixels":stride,"mesh_vertices":len(all_vertices),"mesh_triangles":len(all_faces),"mesh_bounds_m":[all_vertices.min(0).tolist(),all_vertices.max(0).tolist()],"top_height_quantiles_m":np.quantile(vertices[:,2],[0,.5,.95,1]).tolist(),"zero_area_closure_faces_removed":int((~keep).sum()),"limitations":["Single-view visible depth surface only; no multiview fusion.","Unobserved underside closed at estimated tabletop.","No recovered camera intrinsics: weak-perspective model and square detection approximate physical geometry.","Depth interpretation explicitly differs from saved uint8 OpenCV helper."]}
    return all_vertices,all_faces,report


def build_baseline(inputs_zip: Path, test_csv: Path, output_root: Path) -> dict:
    """Write public meshes and compact input arrays, returning full provenance.

    A bound existing baseline_inputs.npz cache avoids JPEG/Pillow dependency on
    Linux. The cache contains only selected public image pixels and public masks.
    Callers must preserve the returned record outside the agent's public tree.
    """
    inputs_zip,test_csv,output_root=map(Path,[inputs_zip,test_csv,output_root])
    with test_csv.open(newline="") as stream:
        rows=list(csv.DictReader(stream))
    ids=[row["id"] for row in rows]
    if not ids or len(ids)!=len(set(ids)):
        raise ValueError("EMPTY_OR_DUPLICATE_PUBLIC_TEST_IDS")
    source={"inputs_zip_sha256":sha256_file(inputs_zip),"test_csv_sha256":sha256_file(test_csv)}
    array_path=output_root/'baseline_inputs.npz';meta_path=output_root/'baseline_inputs.json'
    records=[];arrays={};calibration_documents=[]
    decoder='Pillow RGB conversion' if importlib.util.find_spec('PIL') else 'macOS native ImageIO/CoreGraphics RGBA decoder via ctypes'
    decoder_host={'platform':sys.platform,'python':sys.version.split()[0]}
    if array_path.is_file() and meta_path.is_file():
        metadata=json.loads(meta_path.read_text())
        if metadata.get('source')!=source or metadata.get('ids')!=ids or metadata.get('arrays_sha256')!=sha256_file(array_path):
            raise ValueError("FROZEN_PUBLIC_INPUT_ARRAY_CACHE_BINDING_MISMATCH")
        with np.load(array_path,allow_pickle=False) as loaded:
            arrays={key:loaded[key].copy() for key in loaded.files}
        records=metadata['records'];decoder=metadata['decoder']
        decoder_host=metadata.get('decoder_host',{'platform':'not_recorded_in_older_development_cache'})
        calibration_documents=metadata.get('calibration_documents',[])
    else:
        with zipfile.ZipFile(inputs_zip) as archive:
            names=archive.namelist()
            for name in names:
                if Path(name).name.lower()=='checkerboard.pdf':
                    payload=archive.read(name)
                    calibration_documents.append({'member':name,'sha256':hashlib.sha256(payload).hexdigest(),'bytes':len(payload),'used_fact':'Printed square side1.2cm=0.012m; no reference mesh dimension used.'})
            for row in rows:
                object_id=row['id'];prefix=row['input_directory'].rstrip('/')+'/'
                originals=sorted(n for n in names if n.startswith(prefix+'Original/') and Path(n).suffix.lower() in ['.jpg','.jpeg','.png'])
                depths=sorted(n for n in names if n.startswith(prefix+'Depth/') and Path(n).suffix.lower() in ['.jpg','.jpeg','.png'])
                masks=sorted(n for n in names if n.startswith(prefix+'Mask/') and Path(n).suffix.lower() in ['.jpg','.jpeg','.png'])
                if not originals or not depths:
                    raise ValueError(f'MISSING_PUBLIC_RGB_OR_DEPTH:{object_id}')
                original=originals[0]
                frame=Path(original).stem.removesuffix('_original')
                depth=next((n for n in depths if Path(n).stem in [frame+'_depth','depth']),None)
                mask=next((n for n in masks if Path(n).stem.startswith(frame+'_original_segmented_mask')),None)
                if depth is None:
                    raise ValueError(f'NO_MATCHING_PUBLIC_DEPTH:{object_id}')
                used=[];decoded={}
                for category,name in [('rgb',original),('depth_rgb',depth),('mask',mask)]:
                    if name is None:continue
                    payload=archive.read(name);image=decode_rgb(payload)
                    used.append({'member':name,'sha256':hashlib.sha256(payload).hexdigest(),'bytes':len(payload),'decoded_shape':list(image.shape)})
                    decoded[category]=image
                full_shape=decoded['rgb'].shape
                if any(image.shape[:2]!=full_shape[:2] for image in decoded.values()):
                    raise ValueError(f'PUBLIC_RASTER_SHAPES_DIFFER:{object_id}')
                stride=max(1,int(np.ceil(max(full_shape[:2])/PARAMETERS['maximum_image_dimension'])))
                for category,image in decoded.items():
                    reduced=image[::stride,::stride]
                    arrays[f'object_{object_id}_{category}']=(reduced.mean(2)>127).astype(np.uint8) if category=='mask' else reduced
                records.append({'id':object_id,'selected_frame':original,'used_members':used,'pixel_stride':stride,'reduced_rgb_shape':list(arrays[f'object_{object_id}_rgb'].shape),'source_mask_present':mask is not None,'missing_mask_assumption':None if mask else PARAMETERS['mask_fallback']})
        output_root.mkdir(parents=True,exist_ok=True)
        np.savez_compressed(array_path,**arrays)
        metadata={'source':source,'ids':ids,'records':records,'decoder':decoder,'decoder_host':decoder_host,'calibration_documents':calibration_documents,'arrays_sha256':sha256_file(array_path),'contains':'Public RGB, hue-encoded depth RGB, and thresholded public segmentation annotations only; no withheld 3D target geometry or target-derived model outputs','normalization':'Deterministic nearest-pixel stride to maximum dimension480; mask threshold127; source member bytes/hashes retained inrecords.'}
        meta_path.write_text(json.dumps(metadata,indent=2,sort_keys=True)+'\n')
    mesh_root=output_root/'meshes';mesh_root.mkdir(parents=True,exist_ok=True)
    output_records=[]
    for record in records:
        object_id=record['id'];key=f'object_{object_id}_'
        try:
            vertices,faces,details=mesh_from_arrays(arrays[key+'rgb'],arrays[key+'depth_rgb'],arrays.get(key+'mask'))
        except ValueError as error:
            raise ValueError(f'PUBLIC_RECONSTRUCTION_OBJECT_{object_id}:{error}') from error
        path=mesh_root/f'{object_id}.obj'
        with path.open('w') as stream:
            stream.write('# Input-only depth/silhouette smoke-test mesh; units meters; not a competition submission\n')
            for xyz in vertices:stream.write('v '+' '.join(format(float(x),'.9g') for x in xyz)+'\n')
            for face in faces:stream.write('f '+' '.join(str(int(x)+1) for x in face)+'\n')
        output_records.append({**record,**details,'mesh_path':f'meshes/{object_id}.obj','mesh_sha256':sha256_file(path),'mesh_bytes':path.stat().st_size})
    identity=output_root/'identity.json'
    if identity.is_file():
        transform=json.loads(identity.read_text())
        if not np.array_equal(np.asarray(transform),np.eye(4)):
            raise ValueError('EXISTING_PUBLIC_IDENTITY_IS_NOT_IDENTITY')
    else:
        identity.write_text(json.dumps(np.eye(4).tolist(),indent=2)+'\n')
    return {'source':source,'parameters':PARAMETERS,'decoder':decoder,'decoder_origin_host':decoder_host,'public_calibration_documents':calibration_documents,'frozen_public_arrays':{'path':'baseline_inputs.npz','sha256':sha256_file(array_path),'bytes':array_path.stat().st_size,'metadata_path':'baseline_inputs.json','metadata_sha256':sha256_file(meta_path)},'object_count':len(output_records),'objects':output_records,'reference_geometry_read':False,'ground_truth_scale_fitted':False,'external_models_or_APIs':False,'trained_models':False,'consequence_or_ranking_claim':False,'runtime_platform':sys.platform,'numpy_version':np.__version__}


def main() -> int:
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs-zip',type=Path,required=True)
    parser.add_argument('--test-csv',type=Path,required=True)
    parser.add_argument('--output-root',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    report=build_baseline(args.inputs_zip,args.test_csv,args.output_root)
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'object_count':report['object_count'],'report':str(args.report),'public_array_bytes':report['frozen_public_arrays']['bytes']}))
    return 0


if __name__=='__main__':
    raise SystemExit(main())

