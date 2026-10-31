These are original auto.am-source vehicle attributes and price labels from the authenticated competition CSVs. No original-price transformation or label repair is performed. Official test.csv is unlabeled and its sample prices are NOT references. This local task holds out labeled source-training rows; all rows are retained across train/development/evaluation. Id values are derived from physical source row positions solely for alignment. Year is a vehicle characteristic, not a listing/sale timestamp. Exact normalized feature groups stay together; reviewed limitations do not certify vehicle/time independence. running includes explicit km/miles units. Other feature units are not inferred from plausible magnitudes.

Reviewed source-bound provenance follows:
{
  "price_currency": "Unknown; do not infer USD/AMD or convert.",
  "raw_price_scale": "Exact numeric price field from authenticated source train.csv, unchanged. Numeric source units are the experiment units.",
  "target_semantics": "Estimate the source website-recorded price field from vehicle attributes. Asking versus realized transaction semantics is unverified; no transaction/financial benefit claim.",
  "research_use_basis": "Private local work explicitly requested by the user. Source Gratitude acknowledges auto.am consent to competition website-data use; broader third-party local-use/release rights are not newly established by this construction.",
  "grouping_time_review": "All nine normalized features define target-independent conservative groups. Same-feature rows stay together. These may be different vehicles; changed-attribute relistings, true vehicle identity, sellers and dates are unavailable. Neither year nor row ID is treated as a listing timestamp. No vehicle/time independence is claimed."
}
