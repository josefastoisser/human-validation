# Public data

Each row is one observed perturbation/target-gene pair with mouse gene symbols.
id joins files; pert is the perturbed gene; gene is the target whose observed
expression-response label is predicted. label is up, down or none. The source
labels use FDR <5% and shrunken log2 fold-change cutoffs +/-log2(1.5) for up/down.

train.csv contains C0 with labels. validation.csv contains C1 and C2 with labels.
test.csv contains C3 and C4 without labels. sample_submission.csv supplies the
required IDs and a constant training-class-prior template. Every test ID must
have finite prediction_up and prediction_down in [0,1] summing to at most one.

The five cohorts are fixed hash partitions, with no perturbation identity shared
across cohorts on the perturbation axis and no target-gene identity shared across
cohorts on the target axis. The same symbol can occur in different roles across
cohorts. Use id as a join key and cohort as a population key, not model features.
The task is predicting observed response labels; no additional perturbation
mechanism assumption is needed to interpret these local files.
