# BaristaBench: order state tracking and pricing

Interpret each generated customer order using data/menu.md. Produce the final
receipt after all additions, replacements, cancellations and quantity changes.
Compute the total from base prices, size adjustments, modifier costs and final
quantities. This local task is a discussion-grounded reconstruction, not a
verified historical leaderboard implementation. The source orders are generated
scenarios, not observed customer conversations.

Local size rule: Trenta is allowed for every drink with the menu's +$1.50
size adjustment. This overrides the "Cold drinks only" restriction in menu.md.

Read data/train.csv (id,order,expected_json), data/test.csv (id,order),
data/menu.md and data/DATA.md. Write /workspace/_submission.csv with exactly
id,predicted_json columns, each test ID once, no other IDs. Row order may vary.
Each predicted_json cell contains one JSON object with exactly items and
total_price. The items value is a list; each item has exactly name, size,
quantity and modifiers. name is a string; size is a string or null; quantity is
a positive JSON integer excluding booleans; modifiers is a list of strings.
total_price is a finite JSON number excluding booleans.

Duplicate object keys, missing/extra keys, nonfinite numbers and incorrect types
are invalid JSON/schema rows. Such rows receive zero accuracy credit and remain
in the fixed denominator. CSV header, duplicate/missing/extra ID and malformed
CSV errors invalidate the submission artifact separately. The sample file is
an empty-receipt format template; it is not a set of test answers.

The score to maximize is the mean full-row exact-match indicator over all test
IDs. Match every complete item, quantity, modifier and total price. Object-key
order is irrelevant. Compare items as a multiset of complete items and modifiers
as multisets; preserve all duplicate multiplicities. Null sizes and empty lists
remain unchanged. Two empty receipts can match.

Total prices are parsed as decimal numbers and compared by exact mathematical
equality, without rounding or tolerance: 5, 5.00 and 5e0 are equal, but an
additional decimal error is not forgiven. Quantities must be valid integers and
match exactly. String content is compared using the applicable matching
specification. No whitespace trimming, synonym mapping or fuzzy matching is
applied. JSON keys must have the exact spelling and case specified above.
Neither formatting differences nor key/list ordering create a mismatch.

The reference labels are fixed. The local score excludes verification bonuses,
code-review eligibility and final prize selection. Keep implementation code in
the workspace.
