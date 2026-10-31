Food geometry reconstruction

Reconstruct each requested food object from its associated scene photograph(s).
The public data has 21 training meshes, 4 validation meshes and 9 test objects.
Scene names, object IDs, food names and image associations are supplied. Broccoli
object 5 appears in scenes 2 and 6: use either or both photos, but submit one mesh
for object 5. This exception makes the pilot not strictly single-view for every
object. Use train meshes to fit settings and validation references to select them.
Test references are unavailable. Keep source coordinates in millimeters, following
the source volume-script convention; this is not metrological calibration.

Submit _submission.csv at the workspace root, with exactly object_id,mesh_path.
Every test object ID must occur exactly once; no extra, duplicate or missing IDs.
Paths are relative to this CSV, must stay inside its directory, have no symlinks
or parent traversal, and end in <object_id>.obj. Provide finite triangular OBJ
geometry with positive total surface area and nonzero sampled RMS radius.
Optional vertex RGB colors, materials, texture and normal declarations are ignored,
never externally loaded.
Malformed/out-of-range faces, empty meshes or nonfinite coordinates invalidate
the entire artifact under either rule. Across the entire artifact, allow at most
2,000,000 vertices and 4,000,000 faces. No submitted transform file is required.
Preserve reproducible prediction code and every referenced OBJ file.

Use the supplied deterministic geometry convention. For each object, sample
16,384 area-weighted surface points with PCG64 seed 2026+object_id. Face order
is source/file order; draw face choices first, then two uniforms per sample;
sqrt(u) barycentric sampling. Zero-area triangles have zero sampling probability.
Center each cloud by its sample mean; RMS radius is sqrt(mean squared norm).
For evaluation, normalize the centered clouds before fitting the rotation.
Before alignment, divide the reference cloud by its own RMS radius r_G and the prediction cloud by its own RMS radius r_P. This removes uniform scale.
Fit only a proper rotation between the normalized clouds; do not fit a reflection,
an additional scale, or a translation.
Enumerate the 24 determinant-positive signed permutation rotations in lexicographic
axis-permutation order, then sign order (-1,+1). For each, perform up to 20
prediction-to-reference Euclidean nearest-neighbor / fixed-origin Kabsch updates.
Stop if correspondences are unchanged or max(abs(R-I))<=1e-10. Use numpy SVD
with a determinant correction to forbid reflection. Score each final alignment
by mean distance prediction-to-reference PLUS mean distance reference-to-prediction,
using exact cKDTree Euclidean neighbors. Keep the smallest score, earliest exact
tie. Average equally over UNIQUE objects. The resulting Chamfer distance is
minimized; diagnostic
utility 1/(1+distance) is fixed for either rule. A candidate's sampled points are
fixed by its mesh bytes and seed, never selected from stochastic trials.

This scorer is a deterministic reconstruction for a bounded geometry pilot.
It is not the original stochastic submission-transform / lowest-library procedure.
The target is geometry, not nutrition accuracy. DATA.md documents all public files.
Budget: 30 minutes, 2 CPUs, 4 GiB RAM. Use local data and installed libraries;
no external data or model-weight downloads are needed.
