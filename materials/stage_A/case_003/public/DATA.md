# Local solar-filament data

All images and scoring masks are 2048 x 2048. images/*.jpeg are unchanged archive
bytes. images/*.npy are decoded grayscale uint8 pixels at the same resolution;
load with numpy.load(..., allow_pickle=False). No crop, resize or coverage mask
is applied to references. Each CSV observation ID is the original annotator-batch
image ID. Multiple batches of a physical image share an image path and stay on
the same side of the split. Each batch is treated as an evaluation observation
and receives equal weight. All its filament instances are retained; annotation
batches are never pooled or switched between scoring rules.

train.csv has id,image_path,jpeg_path,annotation_file. train_annotations.json is
a list of observation objects containing original COCO image/annotation records
and derived COCO RLE instances (reference_id,segmentation_rle). Category/chirality,
spine and box attributes are provided as source metadata; only segmentation
polygons define the targets. No test annotations are public. test.csv contains
id,image_path,jpeg_path. Use the original batch ID as the local observation ID.

The submission CSV header is exactly filament_id,segmentation_rle. Use
observation_id_uniqueSuffix, with one row per instance. Any nonempty suffix is
allowed. Counts are COCO compressed ASCII RLE, scanned column-major, starting
with a background count. All counts must sum to 2048*2048. This is neither base64
nor row-major start/length RLE. CSV quoting is permitted where needed.
mask_codec.py provides encode(mask), decode(counts) and polygon conversion;
its format helpers contain no grading rules. COCO-LICENSE.txt covers those
adapted helpers. Omitted observations mean no predictions. A header-only CSV is
valid, so the sample is an empty-instance template rather than a good solution.
Empty encoded masks are valid; there is no probability threshold in the grader.
The public files contain no discussion/evaluator links or later metric update.
