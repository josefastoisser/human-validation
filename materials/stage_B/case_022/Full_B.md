BioReasoning: expression-response prediction

Predict the observed expression-response label of a target gene after a gene
perturbation, using data derived from mouse bone marrow-derived macrophages.
Each row is a (pert, gene) pair. The observed labels are up (upregulated), down
(downregulated), or none (not significantly differentially expressed). The source
labels use FDR < 5% and shrunken log2 fold-change thresholds of +log2(1.5) for up
and -log2(1.5) for down; none does not meet those differential-expression criteria.

data/train.csv has labels for cohort C0. data/validation.csv has labels for
cohorts C1 and C2, available for model selection. data/test.csv has the features
for C3 and C4 with no labels. Each row includes id, pert, gene and cohort.
The cohort names are neutral identifiers for fixed hash partitions. Perturbation
identities are disjoint across cohorts, as are target-gene identities on their
own axis. Symbols can occur in different roles; the partition is axis-specific.
Do not use id or cohort as predictive features; cohort identifies populations
for evaluation. Use the labeled training data to build your predictive models.

The common score is (DE AUROC + DIR AUROC)/2, maximized in [0,1].
For DE, reference positive means label is up or down; the score is
prediction_up + prediction_down. For DIR, retain only rows labeled up or down;
reference positive means up, and the score is prediction_up divided by
(prediction_up + prediction_down). If that denominator is zero, replace it
with 1 before dividing, so the resulting DIR score is zero. AUROC awards half
credit to exactly tied positive-negative pairs. No clipping or rounding is used.
Both component scores and scores for each individual test cohort are reported.
Reference populations must support both classes for each component; otherwise
the evaluation setup is invalid. All rows within a scored population have equal
weight. Cohort scores are diagnostics; pooling means compute AUROCs after
combining rows, not average the individual cohort AUROCs.

Scored population: the final score pools ALL test rows in C3 and C4 before computing both AUROCs. For validation selection, pool C1 and C2 before computing both AUROCs. Predictions for ALL test rows in C3 and C4 are required and validated.

Write _submission.csv at the workspace root with exactly the UTF-8 CSV columns
id,prediction_up,prediction_down, and one row for EVERY test ID in C3 and C4.
Row order may vary. Submit finite nonnegative probabilities <=1 whose sum is
<=1; the remainder is the probability of none. Missing, extra or duplicate IDs
and malformed rows invalidate the entire submission. All test predictions are
validated even when only part of the submitted population determines the score.
Preserve your reproducible training and prediction code in the workspace.
Budget: 30 minutes, 2 CPUs, 4 GiB RAM. Use local data and installed libraries;
no data or pretrained model downloads are needed.
