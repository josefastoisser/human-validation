You Are Bot

Build a model to predict whether a participant in a short dialogue is a bot.
People and bots may communicate in different styles and bots may imitate people.
Use the complete dialogue, including message order and speaker identity.

The data directory contains train.csv and validation.csv with is_bot labels
(0=human, 1=bot), test.csv without labels, three matching *_dialogues.json
files, DATA.md, and sample_submission.csv. Use labeled validation for model
selection. Predict both participants in every test dialogue.
There is no exactly-one-bot constraint: a dialogue may have two human participants.
Do not require probabilities in a dialogue to sum to one. The IDs join files;
do not use dialog_id or ID as model features. Message text and array order are
preserved from the supplied dialogues. All test participant rows receive equal
weight; there is no per-dialogue averaging, class weighting or thresholding by
the evaluator. The fixed evaluation references contain both classes.

Submissions are evaluated by pooled binary ROC AUC over all participant rows; higher is better. The positive class is bot (is_bot=1). AUC is the fraction of bot-human pairs where the bot has higher submitted probability, with half credit for exact ties. Use the submitted probabilities without clipping or rounding; constant predictions score 0.5.

Write _submission.csv in the workspace root, with exactly the UTF-8 CSV header
ID,is_bot and one row per test ID. is_bot must be a finite probability in [0,1],
with larger values indicating a greater probability of bot. Row order may vary;
missing, extra or duplicate IDs and malformed rows invalidate the submission.
Keep the reproducible training/prediction code in the workspace.
The runtime budget is 30 minutes, 2 CPUs and 4 GiB RAM. Use local data and
installed libraries. No network data or model-weight downloads are needed.
