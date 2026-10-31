# Solar filament instance segmentation

Identify solar filaments in the supplied H-alpha grayscale observations. 

Read data/train.csv, data/test.csv and data/DATA.md. Original JPEGs and decoded
uint8 NumPy arrays have 2048 x 2048 pixels. Training annotations retain the original
independent annotator records and segmentation polygons, alongside their COCO RLE
conversions. Test rows identify physical images; submit one prediction set per
physical image. The physical ID is its filename stem, without an annotator-batch
prefix. Only segmentation determines this score; chirality, spines and boxes are
retained source metadata.

Write /workspace/_submission.csv with exactly filament_id,segmentation_rle.
Each row is a nonempty predicted instance. Its filament_id is
physical_image_id_suffix, with a unique nonempty suffix. Use only supplied test
image IDs. Order may vary. COCO compressed ASCII RLE counts scan column-major
over 2048 x 2048 binary masks; data/mask_codec.py supplies format helpers. At most
256 instances per physical image are permitted. Overlapping masks and duplicate
geometry with distinct IDs are allowed. Omitted images mean no predictions, and
the header-only sample is a valid empty-set template. Keep your implementation
in the workspace.

The evaluation constructs one merged reference per physical image and score it
once. For each explicit annotator record, first union all of that record's
original instance masks into one foreground mask. Each annotator then supplies
at most one foreground vote per pixel, even where its own instances overlap.
The eligible annotators are exactly the records explicitly supplied for that
physical image. Do not infer missing records or count them as negative votes.
An explicit record with no instances remains eligible and contributes a zero
foreground vote. A physical image without any explicit records has unknown
reference truth and is outside this labeled evaluation fixture.

Combine these whole-image foreground votes into one binary reference mask. Derive
reference instances from its 4-connected foreground components, without size
filtering. Order component IDs by their smallest column-major pixel index.
No cross-annotator filament correspondence or instance-ID alignment is used.
An empty merged mask has zero instances; the image remains in the evaluation.
Original annotation files stay unchanged during evaluation.

Use class-agnostic Panoptic Quality: one-to-one matching maximizing summed IoU
among pairs with IoU strictly greater than 0.5. Sort reference/submission IDs and
choose the lexicographically earliest optimal partner sequence, with unmatched
last, for tied objectives. Unmatched predictions are FP, unmatched references FN.
PQ = sum(matched IoU)/(TP + 0.5*FP + 0.5*FN). Both instance sets empty scores 1;
exactly one empty scores 0. Score the full image domain with no crop, background
class, minimum area, class weighting, probability threshold or qualitative rubric.
Average equally over every physical image in the fixed evaluation set. Higher
PQ is better.
