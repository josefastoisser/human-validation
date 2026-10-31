# Wildfire threat forecasting

This local task is a discussion-grounded reconstruction using the competition's
public labeled wildfire data. It is not a verified snapshot of the original
January documentation. Shared metric conventions below define this local task.

When a wildfire ignites, emergency managers must prioritize incidents and
estimate risk within actionable time windows. Use early-incident features to
predict four cumulative probabilities that a fire comes within 5 km of an
evacuation-zone centroid by 12, 24, 48 and 72 hours. Features describe the first
five hours after the initial perimeter observation. The time origin for targets
is the end of that five-hour window.

Read data/train.csv, data/test.csv, data/metaData.csv and data/DATA.md. Training
rows include event and time_to_hit_hours; test rows contain features only.
An observed event has event=1 and an observed time. A censored observation has
event=0 and a last-observed time; outcomes after that time are unknown. Do not
infer chronological order from anonymized event_id values.

Write /workspace/_submission.csv with exactly these columns in this order:
event_id,prob_12h,prob_24h,prob_48h,prob_72h.
Include each test ID exactly once, with no other IDs. Row order may vary.
Probabilities must be finite, within [0,1], and satisfy
prob_12h <= prob_24h <= prob_48h <= prob_72h on every row.
The sample is a format template. Keep implementation code in the workspace.

The score to maximize is:
Hybrid = 0.3 * C-index + 0.7 * (1 - Weighted Brier Score).

C-index measures urgency ranking. Comparable pairs have an observed event at
the strictly earlier time. Equal-time pairs are excluded. Higher risk for the
earlier event earns 1, equal risk earns 0.5, and lower risk earns 0.
The C-index is total credit divided by comparable pair count. Use the same
(time_to_hit_hours,event) annotations for risk rankings, without truncation by
forecast horizon, inverse-censoring weights, or clipping a value below 0.5.

For Brier at each H in {24,48,72}, include every observed event. Its label is 1
if time_to_hit_hours <= H and 0 otherwise. Include a censored row only if its
last-observed time >= H, with label 0; exclude it if that time < H. Brier@H is
the unweighted mean squared error of prob_Hh on those eligible rows.
Weighted Brier = 0.3 * Brier@24h + 0.4 * Brier@48h + 0.3 * Brier@72h.
The evaluation set has nonzero comparable pairs and nonempty eligible rows at
every Brier horizon. The same fixed annotations and masks are used throughout.

C-index horizon rule: equal four-horizon average. Compute C-index separately
from prob_12h, prob_24h, prob_48h and prob_72h against the same fixed
(time_to_hit_hours,event) annotations and comparable pairs. Use the arithmetic
mean of these four C-indices in the hybrid score.
