"""CPU contour-to-primitive pilot; fitting uses only public training geometry."""
import argparse
import csv
import json
from pathlib import Path
import time
import numpy as np
from scipy import ndimage
from mesh_tools import primitive,write_obj,center

def read_csv(path):
    with Path(path).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

def scene_components(rgb,n):
    x=rgb.astype(float)/255.;h,w=x.shape[:2];yy,xx=np.mgrid[:h,:w]
    chroma=x.max(2)-x.min(2);value=x.max(2)
    roi=(xx>w*.10)&(xx<w*.88)&(yy>h*.28)&(yy<h*.87)
    mask=roi&(chroma/(value+.001)>.26)&(value>.18)
    mask=ndimage.binary_opening(mask,iterations=1);mask=ndimage.binary_closing(mask,iterations=2)
    labels,count=ndimage.label(mask);parts=[]
    for lab,sl in enumerate(ndimage.find_objects(labels),1):
        if sl is None:continue
        pixels=labels[sl]==lab;area=int(pixels.sum())
        if area<max(12,h*w*.0008):continue
        iy,ix=np.where(labels==lab);xy=np.column_stack((ix,iy));cov=np.cov(xy,rowvar=False);axes=np.sqrt(np.maximum(np.linalg.eigvalsh(cov),1.));color=x[iy,ix].mean(0)
        parts.append({'x':float(ix.mean()/w),'y':float(iy.mean()/h),'area':area/(w*h),'major':float(axes[-1]/w),'minor':float(axes[0]/w),'color':color.tolist(),'fallback':False})
    # Deterministic generic fallbacks make failures visible, not privately corrected.
    parts=sorted(parts,key=lambda p:(-p['area'],p['x'],p['y']))[:n]
    while len(parts)<n:
        parts.append({'x':.35+.15*len(parts),'y':.6,'area':.03,'major':.12,'minor':.07,'color':[.5,.4,.25],'fallback':True})
    return sorted(parts,key=lambda p:(p['x'],p['y']))

def descriptors(data):
    result={};audits={}
    for scene in read_csv(data/'scenes.csv'):
        ids=[int(i) for i in scene['object_ids'].split(';')];rgb=np.load(data/scene['rgb_path'],allow_pickle=False)
        components=scene_components(rgb,len(ids));audits[scene['scene_id']]=components
        # Source table order assigned to left-to-right components, without manual boxes.
        for oid,part in zip(ids,components):result.setdefault(oid,[]).append(part)
    desc={}
    for oid,parts in result.items():
        desc[oid]={k:np.mean([p[k] for p in parts],axis=0).tolist() for k in ['area','major','minor','color']}
        desc[oid]['fallback']=any(p['fallback'] for p in parts)
    return desc,audits

def features(d):return np.array([1.,np.log(max(d['major'],.001)),np.log(max(d['minor'],.001)),np.log(max(d['area'],.00001)),*d['color']])

def fit_priors(data,desc):
    train=read_csv(data/'train.csv')
    with np.load(data/'train_points.npz',allow_pickle=False) as points:
        y=np.array([np.log(center(points[r['object_id']])[1]) for r in train])
    x=np.array([features(desc[int(r['object_id'])]) for r in train]);penalty=np.eye(x.shape[1])*10.;penalty[0,0]=0
    coefficients=np.linalg.solve(x.T@x+penalty,x.T@y)
    return {'median_radius':float(np.exp(np.median(y))),'coefficients':coefficients.tolist(),'train_ids':[int(r['object_id']) for r in train]}

def generate(data,rows,out,kind,height,scale,desc,priors):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);manifest=[]
    for row in rows:
        oid=int(row['object_id']);d=desc[oid];ratio=float(np.clip(d['minor']/max(d['major'],.001),.15,1.))
        axes=np.array([1.,ratio,height])
        radius=priors['median_radius'] if scale=='median' else float(np.exp(features(d)@np.array(priors['coefficients']))) if scale=='ridge' else 1.
        # Uniform surface-RMS scale, derived from analytic primitive surface samples.
        v,f=primitive(axes,kind)
        from mesh_tools import sample_surface
        tri=v[f];area=np.linalg.norm(np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]),axis=1)*.5
        cloud=sample_surface((v,f,area),oid);r=center(cloud)[1]
        v*=radius/r;write_obj(out/'meshes'/(str(oid)+'.obj'),v,f)
        manifest.append({'object_id':oid,'mesh_path':'meshes/'+str(oid)+'.obj'})
    with (out/'_submission.csv').open('w',encoding='utf-8',newline='') as stream:
        w=csv.DictWriter(stream,fieldnames=['object_id','mesh_path'],lineterminator='\n');w.writeheader();w.writerows(manifest)
    return out/'_submission.csv'

def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path('data'));p.add_argument('--output',type=Path,required=True);p.add_argument('--kind',choices=['ellipsoid','boxy'],default='ellipsoid');p.add_argument('--height',type=float,default=.5);p.add_argument('--scale',choices=['median','ridge','unit'],default='ridge');a=p.parse_args();start=time.monotonic();d,audit=descriptors(a.data);prior=fit_priors(a.data,d);f=generate(a.data,read_csv(a.data/'test.csv'),a.output,a.kind,a.height,a.scale,d,prior);print(json.dumps({'manifest':str(f),'seconds':time.monotonic()-start,'fallback_objects':[oid for oid,x in d.items() if x['fallback']]}))

if __name__=='__main__':main()
