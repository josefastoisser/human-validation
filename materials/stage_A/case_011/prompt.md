# Crypto market prediction

Build a model that predicts the `label` variable from minute-level crypto market features.
The target is an anonymized future price-movement signal. Use the supplied public
historical examples and produce predictions for every row of `data/test.csv`.

`data/train.csv`, `data/calibration.csv` and `data/validation.csv` contain labeled
historical observations in that chronological order. They are available for model
development. `data/DATA.md` describes the fields and the temporal data boundary.
Use only the supplied information. Do not fit preprocessing or a model on test
inputs or derive features from other test rows; process each test row using the
fitted pipeline and that row's features.

Save a CSV named `_submission.csv` in the workspace root with exactly `ID,prediction`.
Supply every test ID exactly once and no other IDs. Row order is immaterial. Values
must be finite numbers, and the complete prediction vector must be nonconstant.
The submission template illustrates the format; its placeholder values are not a
model or a validation result. The evaluator uses submitted values directly, with
no fitted calibration, clipping or other transformation. You may fit a calibration
transform on public labeled data before submission. Higher evaluation scores are better.

Retain the implementation and provide a brief report describing the validation,
selected solution and how to reproduce its predictions.
