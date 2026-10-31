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
is valid. Empty masks are also valid and treated as absent predictions.
Unknown observation IDs, duplicate filament IDs and invalid RLE are rejected.
A maximum of 256 submitted instances per observation is allowed. All chirality
categories count as filaments; chirality does not enter scoring.
Save your modeling implementation in the workspace too.

The score is Mean Dice, with higher values better. Every evaluation observation
is scored on the full 2048 x 2048 pixel domain, without a solar-disk scoring mask.
For a nonempty reference/prediction pair, Dice is twice the intersection area
divided by the sum of foreground mask areas; background is excluded. For each
observation, choose a one-to-one matching that maximizes the sum of these Dice
values over pairs with strictly positive overlap. Break exact ties by sorted
reference ID, then sorted submitted filament ID; prefer an earlier feasible
matched partner, with unmatched ordered last. Compute this assignment once.
Zero-area prediction rows are treated as absent predictions. On observations
with reference instances, unmatched predictions do not directly enter the
average. An observation with reference instances but no matched pairs scores 0.
An observation with no reference instances scores 1 if there are no nonempty
predictions, and 0 otherwise. Average observation scores equally across the
entire fixed test set. These shared conventions are researcher specifications
for this proposed local reconstruction.

Average Dice over matched pairs only. For an observation with references and matches, divide the sum of matched-pair Dice by the number of matched pairs; unmatched reference instances are omitted.
