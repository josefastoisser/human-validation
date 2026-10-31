Create prediction intervals for house sale_price using the supplied property and transaction features. Aim for narrow intervals with nominal marginal coverage of 90%.

Public data/train.csv contains labeled training transactions; data/calibration.csv is a separate labeled calibration set; data/validation.csv is labeled public validation for model/interval selection. data/test.csv contains the same feature columns without sale_price. Original string IDs are retained. Coordinate groups are separated across all four partitions to keep repeated property-location sales together. All observed dates may occur in multiple partitions; this is not a future-time forecasting evaluation. No parcel identifiers are supplied, so coordinate groups are a conservative proxy rather than guaranteed property identities.

For each test ID, write submission.csv or _submission.csv with exact header id,pi_lower,pi_upper and rows in data/sample_submission.csv order. Bounds must be finite numeric values with pi_lower<=pi_upper. Zero-width intervals and negative lower bounds are allowed. Missing/extra/duplicate/misordered IDs, wrong columns, crossed intervals and nonfinite bounds are invalid. All conditions use the same output contract and reference labels.

For each reference sale price y and bounds l,u, Winkler loss is (u-l)+20*max(l-y,0)+20*max(y-u,0). The evaluation loss is the unweighted arithmetic mean over all supplied held-out rows. This uses alpha=.1, corresponding to nominal 90% coverage. Smaller loss is better. Empirical coverage is the unweighted fraction of rows with l<=y<=u; endpoints are inclusive. Coverage is not rounded.

Fit preprocessing and models on training data, calibrate with the supplied calibration data, and use public validation for interval/model choices. Hidden test labels are unavailable. Use only local data and installed Python numpy, pandas, scipy and scikit-learn; do not acquire external data, labels or dependencies. You have 30 minutes, 2 CPUs and 4 GiB RAM.

No separate empirical-coverage requirement applies. Every format-valid submission is ranked solely by mean Winkler loss, including coverage below 90%.
