# Generated order prediction data

The original competition explicitly describes the orders as generated scenarios.
These are not recorded customer conversations. This package uses only labeled
public training rows as a fixed local holdout. No source orders or reference
annotations are regenerated, manually corrected or synthesized here.

train.csv contains source order text and its original expected_json label.
test.csv contains source order text without its annotation. Related normalized
orders and repeated canonical final receipts are assigned to the same split.
menu.md is copied verbatim from the downloaded source, including its V2 heading;
current source documentation describes the order data as V3. The local task
explicitly permits Trenta for every drink at the existing +$1.50 adjustment,
overriding the menu's cold-only restriction to match the supplied receipts.
This shared adaptation applies to all conditions. Original labels remain fixed.

The original unlabeled 3,500-row official test set and its sample predictions
are not treated as verified truth. The local sample consists of empty receipts
and exists only to illustrate the required submission format.

Task wording uses recovered discussion and current documents as reconstruction
material; historical wording, account-linked authority and the official scoring
implementation remain unverified.
