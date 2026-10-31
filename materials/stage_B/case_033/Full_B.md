Predict the pupil center (x,y) from event-camera recordings. Write _submission.csv with exactly row_id,x,y, one finite numeric pair for every row of data/test.csv, in its given order. Retain every row_id. Coordinates are continuous pixels in the downsampled 80×60 sensor space.

The evaluation reports p10 accuracy (the fraction with Euclidean error strictly less than 10 pixels) and mean Euclidean pupil-center error in pixels.

The score to optimize is mean Euclidean error; minimize it. P10 accuracy is reported as a diagnostic and does not break ties.

Use the same 20 Hz frames and coordinates throughout. Read data/DATA.md for event timestamps, frame alignment, train/validation inputs, coordinate transforms, and blink conventions. Every test frame is scored, including blinks and incomplete final intervals. Pool all frames equally across recordings and activity types; do not average per-recording or per-activity scores. Predictions are scored as supplied, without clipping, interpolation, coordinate rescaling or reordering. Missing, extra, duplicate, reordered or nonfinite rows fail validation. Finite coordinates outside the image are accepted without clipping. Training and public validation labels are provided; test reference coordinates are withheld.

Create your implementation and the final prediction artifact in the workspace. Use the supplied inputs and the available local runtime within the allotted budget.
