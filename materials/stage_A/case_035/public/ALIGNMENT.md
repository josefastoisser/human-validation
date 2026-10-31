Host registration uses rotation and translation only. Produce
your mesh at metric scale in metres from the supplied physical references; host
registration never fits scale, shear or reflection. Your admitted proper-rigid
4x4 submitted transform T is applied first in the column-vector convention.
The host then computes one common transform H and applies H@T to the mesh.

Registration uses 4,096 deterministic area-based surface landmarks per mesh,
independent of subsequent scoring representation. Triangulate each original
polygon as a file-order fan, discard zero-area fans in this registration view,
and retain positive fans in file order. Compute float64 areas and cumulative
sum; normalize to a CDF with last entry 1. Draw i=0..4095 at CDF midpoint
u0=(i+0.5)/4096 using searchsorted(side=right). For barycentric channels c=1,2,
hash exact original OBJ bytes followed by the domain bytes with hexadecimal
005031362e726567697374726174696f6e2e61726561343039362e763100 and
struct.pack(">QB",i,c). Interpret the first 8 SHA256 digest bytes as a big-endian
integer k, and set u=(2*k+1)/2**65, rounded to float64. Interpolate with weights
(1-sqrt(u1),sqrt(u1)*(1-u2),sqrt(u1)*u2). Apply submitted T to candidate
landmarks. Reference landmarks use the unchanged source mesh.

Center each landmark cloud and calculate covariance principal axes ordered by
descending eigenvalue; make each basis right handed. Initialize all 24 proper
signed principal-axis permutations between candidate and reference, in
lexicographic axis-permutation/sign order, plus centroid-translated identity.
For each start run at most 20 untrimmed point-to-point ICP iterations: find exact
nearest reference landmarks and solve proper-rotation Kabsch for all candidate
landmarks, with determinant +1 and no scale. Stop if rotation and translation
maximum-entry changes are both<=1e-11. Nearest neighbors use cKDTree k=1,p=2,
eps=0,workers=1. Evaluate each start before and after ICP using the sum of the
two directional unsquared mean nearest-neighbor distances on the same 4,096
registration landmarks. Select the lowest objective; exact ties retain the
first considered matrix. Identical landmark arrays return identity only after
verifying that identity has objective exactly 0. No global optimum is promised.
Reuse the exact selected H for every scoring representation of this submission;
do not refit alignment against scoring-specific vertices or surface samples.

