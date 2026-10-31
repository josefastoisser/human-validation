China real estate: sector-level transaction-amount forecasting

Predict monthly TOTAL new-house transaction amounts for each of 96 sectors.
The target is total monetary value in 10,000 Chinese yuan, not price per square
meter. Source amount_new_house_transactions is mapped to the public history
and output column new_house_transaction_amount. Source documentation specifies
zero for an absent sector-month target record; these zeros are included in the
provided labeled history. The future row grid is complete.

This task uses a univariate/panel subset of the source task: target histories,
sector/month identifiers, and known calendar year and month only. train.csv
covers January 2019 through July 2022; validation.csv contains labeled August
2022 through July 2023; test.csv contains only identifiers/calendar inputs for
August 2023 through July 2024. DATA.md describes the schema.

Use a fixed-origin forecast. Validation forecasts must fit only history through
July 2022. Validation labels may select model settings. Final test forecasts
may refit using train+validation history through July 2023. Forecast all twelve
test months at that single origin. Do not use actual targets or contemporaneous
transaction quantities from ANY test month to forecast later test months.
Lags after the origin must come from your own forecasts, not future actuals.

The common evaluation is a two-stage scaled absolute-percentage-error score,
maximized. For a selected set of rows, e=abs(prediction-target)/target when the
target is positive. If the target is zero, e=0 exactly when the prediction is
zero, otherwise e=infinity. If more than 30% of selected rows have e>1, the
score is 0. Otherwise q is the fraction with e<=1, and the score is
1 - mean(e among rows with e<=1)/q. e=1 is an inlier and exactly 30% outliers
does not trigger the gate. Pool rows equally. Do not clip negative valid scores:
the range is [-3/7,1], and the gate's zero can outrank a negative passing score.
Report the raw score; .7*score+.3 is a fixed diagnostic utility only.

Scored horizon: the final score uses ALL twelve test months, August 2023 through July 2024. For validation selection, apply the same rule to all twelve months August 2022 through July 2023.

Write _submission.csv at the workspace root, with exactly the UTF-8 CSV header
id,new_house_transaction_amount and all 1,152 test rows in the SAME ID ORDER as
sample_submission.csv. Predict finite nonnegative values for every test row,
including months that may not determine the score. Missing, duplicate, extra,
reordered IDs or invalid values invalidate the entire submission under either
rule. Preserve the reproducible forecasting code in the workspace.
Budget: 30 minutes, 2 CPUs and 4 GiB RAM. Use local data and installed libraries;
no external data or model-weight downloads are needed.
