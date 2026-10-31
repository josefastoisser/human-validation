# Public forecasting data

train.csv and validation.csv contain id, month, sector, year, month_of_year and
new_house_transaction_amount. test.csv has the same identifiers/calendar columns
but no target. month is YYYY-MM; id is YYYY Mon_sector n with English month
abbreviations. sector labels and calendar fields are known before the forecast.
sample_submission.csv supplies the frozen ID order and an all-zero template.

The source column amount_new_house_transactions is total new-house transaction
amount in 10,000 yuan. It is mapped to new_house_transaction_amount in public
history and submissions; it is not price per square meter. Source documentation
defines absent sector-month target records as zero. The labeled files contain
these zeros. No test-row missing-record indicators are supplied.

History January 2019-July 2022 fits validation forecasts for August 2022-July
2023. Use the validation labels to select settings, without fitting validation
forecasts using those labels. Final test forecasts may refit on all public
history through July 2023, then forecast August 2023-July 2024 at one fixed origin.
Every test month remains unobserved at that origin. Forecast-generated recursive
lags are allowed; updates from actual early test-month outcomes are not.

Only target history, identifiers and known calendar variables are provided.
Original transaction-derived fields, nearby-sector files, retrospective POI,
annual statistics and their unverified publication times are excluded.
