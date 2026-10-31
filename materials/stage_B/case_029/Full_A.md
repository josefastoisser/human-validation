Identify Spanish 5W1H content spans in the supplied news text fragments.
Labels: WHAT (event/fact), WHO (participant), WHEN (time), WHERE (place),
WHY (reason), HOW (manner). Train and validation contain labeled examples.
Produce predictions for every row of data/test.csv and save submission.csv in
the workspace root. Use CSV columns ID,TEXT,TAGS in that order. Preserve IDs and
TEXT exactly. TAGS is a strict JSON array; each entry has exactly start,end,tag.
Use uppercase labels and integer Unicode code-point offsets [start,end), with
0 <= start < end <= len(TEXT). Do not normalize the supplied text. Empty arrays
and overlaps of distinct spans are allowed; repeated identical typed spans are
invalid. Supply every test ID exactly once, without extra IDs. CSV row order
does not matter. The order of tags can resolve equal-start/label matching ties.

Evaluation pools typed-span match counts across all test fragments. Exact
same-type, same-boundary matches are assigned first. Remaining gold spans are
processed in stable (start,label) order. Each takes the shortest remaining
overlapping prediction of the same type, with stable ties. The scorer accepts
endpoint contact as overlap. Each prediction and gold span is used at most once.
Remaining exact-boundary wrong-type pairs receive no credit. The denominator is
the number of predictions plus the number of gold spans; full exact credit is 1.
An empty total denominator scores 0. Maximize the resulting pooled F1.

You may use the supplied offline baseline.py or implement another extractor.
Python, NumPy, SciPy and scikit-learn are available. No internet access or model
download is needed. Save your implementation and a short method.md alongside
submission.csv. The available execution budget is specified by the runner.

For scoring, partial-overlap credit is 0.5. Maximize. The score is 2*(exact + 0.5*partial)/(predicted + gold).
