# Metadata extraction from proteomics publications

Convert the provided scientific publication texts into SDRF metadata entities.
This local task is a discussion-grounded reconstruction of automatic metadata
scoring, not a historical leaderboard replay or expert-adjudicated final ranking.

Read data/train.csv, data/test.csv, data/SCHEMA.json and data/DATA.md. Publication
JSON files are under data/publications/. Training prediction values are JSON
objects containing unique annotation values with original SDRF column names.
Test inputs identify the publication documents and have no outcome annotations.

Write /workspace/_submission.csv with exactly two columns: PXD,prediction.
Each held-out PXD must occur exactly once; row order may vary. prediction is a
JSON object mapping exact allowed metadata headers to lists of strings. Example
shape: {"Comment[Instrument]":["AC=MS:1001911;NT=Q Exactive"]}.
Missing metadata keys represent empty predictions; empty lists are permitted.
Unknown keys are invalid. Duplicate JSON keys and duplicate PXD rows are invalid.
Each PXD is limited to 10,000 values and each value to 10,000 characters.
The sample submission contains empty objects as a schema template. Keep your
implementation in the workspace.

Scoring operates on unique annotation entities per (PXD,column), not sample-row
alignment. The evaluated column set and coverage mask are fixed from the
reference. ID, PXD, Raw Data File and Usage are not scored. A reference pair
whose only non-null values are Not Applicable is excluded, regardless of your
predictions. Empty strings and literal nan, after trim/casefold, are null.
Duplicate suffix headers such as Characteristics[Modification].1 remain
separate metadata fields. Missing predictions cannot remove evaluated pairs.

Values may be free text or ontology notation. Well-formed ontology notation
consists of semicolon-separated key=value fields with exactly one nonempty NT
and at most one nonempty AC. Field keys NT and AC are uppercase; accession
identifiers retain case. Other well-formed fields are ignored. Values without
NT, duplicate fields or malformed encodings are interpreted as literal text.
For names, use the NT component of a well-formed encoding and plain text
otherwise. Trim and case-fold names.

Within each evaluated pair, cluster the combined reference and predicted names
using connected components: add an edge whenever normalized Levenshtein
similarity 1-distance/max_length is at least 0.80. Identical names have
similarity 1. This threshold is inclusive. Name matches must share a component.
Duplicate entities under the matching rule count once. Use maximum-cardinality
one-to-one entity matching; reference entities without an accession need only
the name match. Other entity requirements follow the matching specification.

For each evaluated pair, F1 = 2*matches/(reference_entity_count +
predicted_entity_count). Both empty sets have F1=1; one empty set and one
nonempty set have F1=0. The score to maximize is the equal-weight mean F1 over
the same fixed reference-defined pairs. This local score excludes adaptive
final thresholds and expert review.

Name rule: NT sufficient. A matching harmonized name is enough. Ignore AC
in both reference and prediction values, including absent or incorrect AC.
Deduplicate entities by harmonized name component and compare those sets.
