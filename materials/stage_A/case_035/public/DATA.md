# P16 source inputs and sample reconstruction
All 18 corrected reference object IDs are retained, excluding source scenes 12
and 15 per the saved May31 correction. No new evaluation partition was sampled.
inputs.zip contains every corrected-tree RGB/depth/mask JPG for those IDs, plus
the original Checkerboard.pdf and mat.pdf. Each member preserves its exact bytes.
Read members using zipfile.ZipFile(...). No reference geometry is public here.
train.csv is an empty schema: no training reference labels were invented.
The sample CSV, identity.json and meshes/ contain a deterministic modest
reconstruction generated from these public images/depths/masks only. This is a
working format and grading smoke test, not a historical competition submission,
a strong baseline, a target label, or evidence of a ranking reversal. The five
hard objects have no supplied masks; baseline provenance records segmentation
and calibration assumptions. No scanner reference is used to build the sample.
The source depth decoder is included under helpers/. The checkerboard specifies
1.2cm squares. No per-camera intrinsics/extrinsics were recovered.
The archived helper divides OpenCV's uint8 hue by255; the primary Record3D
convention instead maps normalized hue in[0,1) to depth in[0,3) metres. This local
task fixes the normalized convention and retains the source
helper as provenance. Baseline code and frozen public arrays disclose this
correction; no reference geometry was used to tune it.
Host-only proper rigid registration follows ALIGNMENT.md. It addresses arbitrary
scanner pose but does not rescale meshes or reveal reference geometry.
Reference files/clouds, grading code and research sources remain host-private.
This local scenario evaluates geometry only, not volume or combined phase ranks.
Credit the CVPR2024 MetaFood challenge. Saved source rules restrict other uses;
the exact wording is retained in the researcher evidence for rights review.
