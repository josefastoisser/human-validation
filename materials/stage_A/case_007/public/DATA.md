Input data derive from the public Cyrillic Morphological Induction Grand Challenge 2026 CSVs.
Data license: Creative Commons Attribution-ShareAlike 3.0; source https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge
train.csv has id,lemma_ru,pos,feats,dialect,lemma_frequency,yat_flag,form_vvz.
test.csv has the same feature columns without form_vvz. IDs use train:/dev: namespaces.
wug_seeds.csv has lemma_ru,pos,feats,dialect,yat_flag,form_vvz and provides one SEV cell
per seeded lexeme. POS is N/V/ADJ; dialect is SEV/POM/KAM. lemma_frequency is positive
and yat_flag is lexical. Preserve Cyrillic Unicode and stress marks as provided.
This local labeled holdout withholds full selected paradigms, apart from deliberate one-cell
seed context; other transfer/completion contexts are available by task design. Reference
forms are not exposed for test cells. The original competition's hidden test labels are
unavailable; this local task preserves source train/dev annotations, including their noise.
sample_submission.csv gives complete IDs with placeholder form а. Predict every ID once.
