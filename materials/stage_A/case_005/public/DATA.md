# Publication-to-metadata entity task

train.csv indexes 88 labeled PXD studies and their publication paths. Its
prediction column contains unique original human SDRF cell values grouped by
exact metadata headers. test.csv indexes 14 held-out PXD studies and documents.
Publication JSON bytes are copied from the existing competition archive.
SCHEMA.json gives allowed metadata headers and the prediction transport schema.

The local transport is one CSV row per PXD with a JSON object of entity lists,
rather than many sample/raw-file rows. The competition scores unique metadata
values per PXD and column. Sample alignment, raw-file names and Usage are not
prediction targets here. Original held-out annotations remain private and their
contents are unchanged. No synthetic annotation targets are used.

Related studies with the same normalized publication title or body are assigned
together. The same public data and raw annotation source are used under all
conditions. The official unlabeled test set is not used for local grading.

Task and metric wording are reconstructed, with common implementation details
fixed for this local comparison. This package does not reproduce expert review
or assert the original deployed competition scorer. The template is empty and
is provided for format illustration, not as a model or a performance target.
