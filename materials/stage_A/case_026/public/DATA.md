# Bounded food geometry data

train.csv and validation.csv have object_id,food_name,scene_ids,image_paths,
rgb_paths,mesh_path. Test rows omit mesh_path. Lists are separated by semicolons.
scenes.csv gives scene_id,scene_name,object_ids,image_path,rgb_path. Original
photographs are byte-identical archive copies under photographs/. RGB arrays
under rgb/ are EXIF-transposed RGB uint8, bilinear resized to maximum side 384,
using recorded Pillow version. No bounding boxes, camera calibration or test
geometry were used to make these arrays. All groups share these same pixels.

Original training and validation OBJ meshes are unchanged under meshes/train/
and meshes/validation/. train_points.npz and validation_points.npz contain their
fixed 16,384 source-surface samples, with the common public seed and sampling
convention. They are derived public annotations. Test meshes/points, archives,
source discussions, transforms, sample_solution.csv and original evaluation
scripts are not included. The source sample_solution values are placeholders.

sample_submission.csv is a valid geometric smoke template with paths relative to
it, using sample_meshes/<object_id>.obj. To put the template at workspace root,
prefix its paths with data/. Real submissions choose their own relative OBJ paths.
Those sample ellipsoids do not use test geometry. mesh_tools.py provides geometry
I/O, sampling and primitives without scoring-normalization rules. baseline.py is
an optional CPU contour/size-prior pilot, not a strong pretrained 3D pipeline.
It uses source-table food order for left-to-right component association and reports
fallbacks. It averages both available broccoli observations. It consumes decoded
RGB arrays, so Pillow is needed only for preparation, not baseline execution.

There are 21/4/9 unique train/validation/test objects. Test scenes are 2,6,13,14;
scenes 2 and 6 share broccoli 5 and form one group. A source object is scored once,
regardless of its image count. Only three test scene groups support uncertainty
estimation. The local split reuses released source meshes; it is not the original
competition’s public/private partition. Source coordinates are treated as mm per
the volume script (mm^3 * 1e-3 gives mL). Stored meshes and precomputed samples
retain the source coordinates; score normalization is separate from file storage.
No independent physical calibration is applied.

The local pilot evaluates geometry only and allows primitives as diagnostics;
original competition phase/ranking and primitive-eligibility requirements are
outside this reconstructed contract. All conditions use the same local contract.
Source: Kaggle 3D Reconstruction from Monocular Multi-Food Images, source data
and collection described using MetaFood3D (Chen et al., 2024, arXiv:2409.01966).
This reconstruction groups/splits released objects, deduplicates byte-identical
scene photographs and supplies deterministic surface samples/decoded images.
No source endorsement is implied; independent release/access review is pending.
