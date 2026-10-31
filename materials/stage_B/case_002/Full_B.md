# Solar Filament Segmentation Challenge: reconstructed Dice component

Identify filament instances in full-disk H-alpha solar observations. MAGFiLO
contains manually annotated filament segmentations. This local task is a proposed reconstruction of
the earlier Mean Dice scoring component. It scores prediction masks alone.

Develop your method using `data/train.csv` and `data/train_annotations.json`.
Predict filaments for all observation IDs in `data/test.csv`. The 2048 x 2048
images remain at their original resolution. Grayscale uint8 NumPy files are
provided alongside unchanged JPEGs. Paths in the CSVs are relative to `data/`.
Multiple independent annotation batches for the same physical observation have
separate local observation IDs; predictions may be reused for those identical
images. Full data and encoding instructions are in `data/DATA.md`.

Write `_submission.csv` in the workspace root, with exactly the header
`filament_id,segmentation_rle`. Each row represents one predicted instance.
Use the local observation ID followed by `_` and a nonempty unique suffix as
`filament_id`. `segmentation_rle` is a COCO compressed RLE counts string for a
2048 x 2048 binary mask, scanned in column-major order. CSV quoting/escaping is
allowed for the counts string. `data/mask_codec.py` provides encoding/decoding.
Omit rows for observations with no predicted instances; a header-only submission
is valid. Empty masks are also valid but cannot form a positive-overlap match.
Unknown observation IDs, duplicate filament IDs and invalid RLE are rejected.
A maximum of 256 submitted instances per observation is allowed. All chirality
categories count as filaments; chirality does not enter scoring.
Save your modeling implementation in the workspace too.

The score is Mean Dice, with higher values better. Every evaluation observation
is scored on the full 2048 x 2048 pixel domain, without a solar-disk scoring mask.
Include both complementary foreground and background classes in every matched
instance pair. Background inclusion is fixed. Each class has numerator twice
its intersection area and denominator the sum of its reference and predicted
areas. A class with denominator zero has zero pooled terms and is omitted from
a mean of defined class ratios; it is not assigned a numerical zero ratio.
The evaluation unit is a matched instance pair. For each observation, choose a one-to-one matching that
maximizes the sum of foreground IoUs over pairs with strictly positive overlap.
Break exact ties by sorted reference ID, then sorted submitted filament ID;
prefer an earlier feasible matched partner, with unmatched ordered last.
Compute the assignment once and keep it fixed when computing Dice. Only matched
pairs enter the mean; unmatched instances add no terms. Average matched-pair
scores equally within each observation, then average observation scores equally
across the entire test set. An observation with no matched pairs scores 0,
including both-empty, one-sided-empty and all-disjoint cases. These matching,
averaging and empty-case conventions are fixed for this local reconstruction.

Use macro class averaging for each matched instance pair. Compute the Dice ratio of each included class and take their equal arithmetic mean over defined ratios. When both class denominators are nonzero, D = (2*TP/(2*TP+FP+FN) + 2*TN/(2*TN+FP+FN))/2.
