# Rank business-travel flight options

Build a model that ranks the flight options within each search session by how
likely the traveler is to choose them. Each `ranker_id` identifies one complete
session. Exactly one option in each labeled session has `selected=1`; the other
options have `selected=0`.

Use `data/train.csv` and the later labeled `data/validation.csv` for development.
Predict the still later sessions in `data/test.csv`. Keep sessions intact when
validating. Every supplied session includes all its original options. The files
contain the same feature columns; `selected` is absent from test. `Id` identifies
an option, `profileId` a traveler, and `companyID` the traveler's company.
`requestDate` records the search time; the `legs*` columns describe flight times,
routes, carriers and services. `totalPrice` and `taxes` describe cost; the
`miniRules*` columns describe cancellation/exchange terms, and
`pricingInfo_isAccessTP` indicates travel-policy compliance. Blank cells are
missing values. Additional field descriptions are in `data/FEATURES.md`.

Submit `_submission.csv` with exactly `Id,ranker_id,selected`, in the same row
order as test. In a submission, `selected` means the integer rank, not the binary
training label: rank 1 is best. For every session with N options, assign a complete
permutation of 1 through N. Include all sessions and all options, irrespective of
which sessions contribute to scoring. `data/sample_submission.csv` shows the
required format; its ranks follow source row order and are not reference answers.

Evaluation uses HitRate@3: a session is a hit if its actually selected option
receives rank 1, 2 or 3. The score is the arithmetic mean of these binary hits over
the evaluated sessions, with equal weight per evaluated session. Higher is better.
Retain your implementation and report your validation procedure and final result.

Coverage rule: sessions with >10 options. Only complete sessions containing more than 10 options contribute to the score.
