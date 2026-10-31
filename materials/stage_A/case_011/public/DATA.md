# Supplied data

Each row is a minute-level market observation. `ID` is an identifier; `timestamp`
is a chronological index. Neither is a target. `bid_qty`, `ask_qty`, `buy_qty`,
`sell_qty`, `volume` describe market quantities. `X1` ... `X780` names identify
anonymous numeric market features; this package contains 128 of these fields.
The source feature descriptions and target horizon are not further disclosed.
`label` is the unmodified anonymized target and appears only in labeled files.
Empty feature entries, if present, are missing values.

The labeled files are chronological: train, calibration, validation. Test follows
them. At each boundary, 24 hours of the earlier partition have been removed.
The exact future horizon is undisclosed; this guard does not establish independence
of nearby labels. Use temporal validation and avoid claims of independent rows.
No target transformation or normalization was applied. Fit preprocessing on public
labeled training data only. Do not use test rows to fit preprocessing, calibrate,
train, choose a model or construct cross-row features. Only supplied data is allowed.

All three labeled files may be used to build the final model; reserve public data
for honest validation before refitting. `sample_submission.csv` contains alternating
small placeholders only. Keep the output labels in `prediction`, not `label`.
