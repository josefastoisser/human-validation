# Food mesh reconstruction
Reconstruct a 3D food mesh for every object in test.csv from its supplied images,
depth views and masks. Individual unchanged source inputs are members of
inputs.zip, under the input_directory given in test.csv. See DATA.md.
Decode hue-encoded depth as 3 times continuous RGB HSV hue in [0,1), in
metres. The source-derived baseline arrays and DATA.md use this convention;
the archived helper's uint8 hue scaling is
retained for provenance rather than used as the decoding specification.

Submit _submission.csv with exact columns id,mesh_path,transform_path. Include
every test object ID exactly once; row order is immaterial. mesh_path names an
OBJ file and transform_path names a JSON 4x4 proper rigid matrix. Paths must be
relative to the workspace and cannot traverse outside it or use symlinks.
Each mesh must have finite XYZ coordinates, at least one stored vertex, valid
face indices, and at least one positive-area triangle under the fan convention.
Every submitted vertex entry, including duplicates and unused vertices, is kept.
The accepted OBJ geometry is xyz (optional homogeneous w=1); appearance/group
records are ignored. Polygon faces use their stored index ordering.

Use unchanged corrected-source coordinate units. A transform is [R,t;0,1],
applied as points @ R.T + t. The absolute admission tolerance for orthogonality,
determinant +1 and the final homogeneous row is 1e-8. No scaling, shear,
reflection, geometry repair or mesh simplification is performed by evaluation.
After the submitted rigid transform, the host applies one deterministic,
surface-based rigid registration to the private reference. ALIGNMENT.md defines
its fixed procedure. Registration is fitted once per submitted mesh and
reference pair using the fixed procedure. Reference geometry and scale remain
unchanged.

For point sets X,Z, directed distance d(X,Z) is the arithmetic mean over all
x in X of min_z ||x-z||_2. Symmetric Chamfer is d(X,Z)+d(Z,X), using unsquared
Euclidean distances. The score is minus the equal arithmetic mean of the
object-level symmetric distances, so higher is better. The host registration's
bounded search over rigid initializations is defined in ALIGNMENT.md.

SAMPLING.md defines the fixed conditional surface-sampling protocol. That protocol
uses exactly 500,000 points per mesh, with zero-area triangle fans discarded only
from the sampling view. Stored vertex entries are never removed or merged.

S_B=-mean_objects CD(H(T(sample500k(P_mesh))),sample500k(Y_mesh)); T is the submitted rigid transform and H is the shared host-fitted rigid transform. Sample the exact original mesh-file bytes before applying T and H; use the deterministic area-uniform 500,000-point protocol in SAMPLING.md for both meshes.
