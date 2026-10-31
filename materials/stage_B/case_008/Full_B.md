# Solar filament instance segmentation

Identify solar filaments in the supplied H-alpha grayscale observations.

Read data/train.csv, data/test.csv and data/DATA.md. Original JPEGs and decoded
uint8 NumPy arrays are provided at 2048 x 2048 pixels. Training annotations retain
the original independent annotator records and segmentation polygons, with COCO
RLE conversions. Test rows identify physical images, with one prediction set per
image. Category/chirality, spines and boxes are source metadata; only segmentation
foreground instances determine this score. The physical image ID is its filename
stem, not an annotator-batch ID.

Write /workspace/_submission.csv with exactly filament_id,segmentation_rle.
Each row is a predicted instance; its filament_id is physical_image_id_suffix
with a unique nonempty suffix. Order may vary. Include only supplied test image
IDs. Use canonical COCO compressed ASCII RLE counts in column-major order for
2048 x 2048 binary masks. data/mask_codec.py supplies format helpers. Instance
masks must be nonempty; overlapping masks and duplicate geometries with different
IDs are allowed. At most 256 instances are permitted per physical image. Omitted
images mean no predictions. The header-only sample is a valid empty-set template.
Keep your implementation in the workspace.

The common quantitative metric is class-agnostic Panoptic Quality (PQ). Match
predicted and reference instances one-to-one using only IoU strictly greater
than 0.5. Choose the matching maximizing the sum of IoUs. Sort reference IDs and
submitted filament IDs, and choose the lexicographically earliest optimal partner
sequence, with unmatched last, if objectives tie. Unmatched predictions are FP
and unmatched references are FN. PQ = sum(matched IoU)/(TP + 0.5*FP + 0.5*FN).
Both instance sets empty scores 1; just one empty scores 0. Higher PQ is better.
All pixels are included in each foreground mask's IoU; no scoring crop, background
class, size filtering, chirality comparison or qualitative judging is applied.
Physical images receive equal weight in the final mean.

Reference annotations can contain multiple independent annotator sets per
physical image. If references are merged, the fixed construction is pixelwise
union of all annotator instance masks followed by 4-connected foreground
components, with no component-size filter. Order these merged components by their
smallest column-major pixel index. Original annotator instance masks are obtained
by the same COCO polygon rasterization, and stored annotation files stay
unchanged in every scenario.

Reference aggregation: score annotators separately.
For each physical image, score the same submitted instance set independently
against every annotator's original instance set. Average these PQ scores equally
over annotators within that image, then equally over physical images. Do not
merge annotator masks or split their original instances into components.
