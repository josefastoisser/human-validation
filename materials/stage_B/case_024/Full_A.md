Swiss legal citation retrieval

For each legal question, retrieve the relevant Swiss statutes and court decisions.
Use the supplied source-training-language queries. train.csv contains 648 labeled
queries; validation.csv contains 185 labeled queries for model selection. test.csv
contains 231 questions without labels. This is a local reconstruction from the
public training population, not the original English competition test benchmark.
The corpus.sqlite database contains the full available source corpus and explicit
article/case bundles; DATA.md describes its schema and read-only access. search.py
is an optional local search helper. The database contains no query labels.

Write _submission.csv in the workspace root with exactly the UTF-8 CSV header
query_id,predicted_citations. Include every test query ID exactly once and no other
IDs. Query order may vary. Each field is a semicolon-separated citation list; an
empty string is allowed. Citations are case-sensitive opaque IDs. Strip/collapse
whitespace only, ignore order, and deduplicate to a set. Exact ID equality is
required, without fuzzy matching or article/paragraph credit. A bundle ID matches
only that exact reference ID; its member IDs do not automatically receive credit.
The raw field may have at most 10,000 Unicode characters and at most 200
semicolon-separated parts BEFORE normalization or deduplication, including empty
parts. Both caps apply in that order. Thus at most 200 distinct nonempty citations
are possible. Malformed fields, over-limit rows, missing/extra/duplicate query IDs
or wrong columns invalidate the entire artifact. An unknown citation never
matches a reference. Keep reproducible prediction code in the workspace.

The objective measures citation-set overlap with fixed reference sets, averaged
equally across test queries, maximized on [0,1].
For each query, TP=|P intersect G|, FP=|P minus G|, FN=|G minus P|.
The score is 2TP/(2TP+FP+FN). Unmatched predictions count as false positives.
Both sets empty scores 1; empty gold with nonempty predictions scores 0;
empty predictions with nonempty gold scores 0. Average per-query scores equally.

Budget: 30 minutes, 2 CPUs, 4 GiB RAM. Use local data and installed libraries;
no external data or model-weight downloads are needed.
