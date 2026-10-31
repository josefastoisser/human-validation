Predict the correct target-language form for each test example using the provided Russian lemma,
grammatical information, dialect label, and other features. The target language is synthetic.
Use the labeled data in data/train.csv and data/wug_seeds.csv to learn the relationship.
Predict every row in data/test.csv and save UTF-8 _submission.csv with exactly the columns
id,form_vvz. Each test ID must occur once; row order is immaterial. Extra/missing/duplicate IDs
or malformed CSV make the complete artifact invalid. Empty predicted forms are valid.

The local quantitative score is 0.9 * weighted Exact Match + 0.1 * (1 - weighted CER), maximized.
Strings are compared exactly as decoded: no Unicode normalization, case folding, trimming or
accent removal. Levenshtein distance has unit insert/delete/substitute costs on Unicode code
points including combining accents. CER is the weighted mean of each row's distance divided
by the nonempty reference's code-point length; CER is not clipped. Exact Match uses the same
positive weights and denominator. Empty predictions incur deletions.

Both component metrics use the same strictly positive row weights, normalized by the sum
of weights over all evaluated rows. Scoring covers every test row in the fixed local holdout.
Weighting is per row: lemmas with more evaluated forms receive more total weight.
Read data/DATA.md for the input schema.

Row weights: transfer=1, completion=2, wug=3, unseen=4.
Classify available labeled context by lexeme (lemma_ru,pos) and cell (lemma_ru,pos,feats).
Transfer has that cell in another dialect of regular train evidence; completion has the
lexeme in train but no such cell; wug has only one SEV seed; unseen has no train or seed
lexeme evidence. Exact target keys are withheld and regular/seed lexeme sets do not overlap.
