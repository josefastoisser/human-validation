# Local wildfire data

The public files derive from the existing competition archive. train.csv has
172 labeled fire events with 34 features; test.csv has 49 fire events with the
same features and event_id, without outcome annotations. metaData.csv is the
original dictionary. sample_submission.csv gives the required schema with
0.5 placeholders. It is not a prediction baseline or a target file.

Targets represent time and observation status after the initial five-hour
feature window. Censored rows are not established negatives after their last
observation. Refer to task.md for exact scoring and validation conventions.

Each event_id is an anonymized fire identifier, without temporal meaning.
Hour, weekday and month are cyclic metadata, not full observation timestamps.
No numeric features are rescaled or imputed during package preparation.
Original official test rows have no supplied annotations and are not part of
this local evaluation. Training and local evaluation fires are disjoint.

Task wording is reconstructed from recovered competition pages and discussion,
with shared implementation conventions fixed for this local comparison.
It is not a verified historical document or an original Kaggle grader.
