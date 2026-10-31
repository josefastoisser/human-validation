# Local physical-image data

train.csv contains id,image_path,jpeg_path,annotation_file. test.csv contains
id,image_path,jpeg_path. Each ID is one physical filename stem, with no annotator
prefix. images/*.jpeg are unchanged archive bytes; images/*.npy are decoded
grayscale uint8 arrays at the same 2048 x 2048 resolution, not cropped or resized.
Load them with numpy.load(..., allow_pickle=False).

train_annotations.json retains each original COCO image record and all of its
original annotation dictionaries, plus derived segmentation_rle values
under instances. An independent annotator record is identified by its original
COCO image ID. All annotator records for each selected physical image are kept
together. Category, spine, box and area metadata are retained; the target is
segmentation. Test references are not public.

This local subset has 24 labeled training and 12 held-out physical images.
Every supplied physical image has multiple explicit annotator records.
validation_split.csv provides a fixed recommended partition of the labeled
images: 16 fit and 8 validation. Their observing dates are disjoint. All
24 labels remain public; after validation you may refit on all 24 images.
Retain all annotator records of each physical image in the same partition. Observing dates are disjoint between
training and evaluation. Exact source JPEG duplicates were checked throughout
the supplied training corpus. Tracking the same solar structure across observing
dates is not possible from the supplied metadata, so object-disjoint evaluation
is not established. Official test labels are not used.

The CSV prediction contract is filament_id,segmentation_rle, one row per nonempty
instance. IDs use physical_image_id_uniqueSuffix. Counts use canonical COCO
compressed ASCII RLE, column-major, starting with a background count and summing
to 2048*2048. They are neither base64 nor start/length pairs. Omitted observations
mean no predicted instances; the header-only sample is valid. Empty encoded masks
are invalid; use no rows for an empty predicted set. At most 256 instances per
physical image are allowed. Mask overlaps and repeated geometry are allowed with
distinct IDs. Ordering and suffix values do not determine correspondence.

mask_codec.py provides only format conversion, with COCO-LICENSE.txt covering its
adapted algorithms. Use it to encode a binary mask or rasterize supplied polygons.
No evaluator, discussion, alternate prompt or test annotations are included here.
