Rank financial document types and financial text chunks for answering each question. Use the provided train and validation relevance labels to construct a ranking system; rank the fixed test candidates. No API is needed. Submit one fixed ranked output per sample_id.

Inputs are data/train.csv, data/validation.csv, data/test.csv, and JSON candidate corpora under data/corpora/. Each input row gives sample_id, task, question and corpus (the filename stem); labeled rows also contain the qrel JSON mapping candidate index to integer grade. Test grades are private. Candidate text is shared unlabelled input. Document questions have five candidates; chunks have variable candidate counts.

Write submission.csv with exactly the header sample_id,target_index. Provide exactly five distinct valid indices for every test sample. Rank is the appearance order within each sample, best first. No missing or extra samples are allowed. Indices are canonical nonnegative integer strings. Rank all five document types and the best five chunks. The sample demonstrates schema only.

Reported ranking metrics include MRR@5, MAP@5, and graded nDCG@5. For MAP@5 and graded nDCG@5, calculate a score for each sample_id, then take the arithmetic mean with equal weight per sample_id. Each sample_id is one question/candidate-set row; different rows sharing the same question text count separately. There is no task-level reweighting or averaging over repeated runs. Higher is better. Equal scores remain ties.

MAP@5: let b=1[grade>0], R=count of positive candidates. AP@5 is sum over ranks r=1..5 of b_r times (number of positives through r)/r, divided by min(R,5); zero when R=0. MAP is the mean AP.
Graded nDCG@5: gain=2^grade-1, discount=1/log2(r+1). Divide top-five discounted gain by the ideal discounted gain using the five largest grades from all candidates. Zero when ideal gain is zero. Average per-query nDCG.

Execution budget: 30 minutes, 2 CPUs, 4 GiB RAM. Available Python includes numpy, scipy, pandas and scikit-learn; no downloads are required.

Metric rule: graded nDCG@5. Score-based ordering uses graded nDCG@5; the other metrics do not govern ordering.
