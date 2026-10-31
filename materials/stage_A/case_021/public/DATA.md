# Public data

Each CSV row describes a participant. ID is dialog_id + "_" + participant_index.
Both participant indices (0 and 1) have rows even when only one participant has
spoken. IDs are join keys, not model features. is_bot=1 means bot; 0 means human.
train.csv and validation.csv are labeled; test.csv has no labels. Validation is
available for model selection and test probabilities are the required output.

train_dialogues.json, validation_dialogues.json and test_dialogues.json map each
dialog_id to its complete original message array. Each message has text, message
(the original message number) and participant_index. Preserve the array order
when processing a dialogue. Text includes original punctuation and languages.
The CSV participant_index tells you whose bot probability to predict; the entire
dialogue may be used. No forced one-bot pairing is valid: both participants may
be human. sample_submission.csv is a constant training-prevalence template.

The partitions keep whole normalized transcripts, including globally swapped
speaker duplicates, together. Training near-duplicates of held-out dialogues
are removed using a fixed text-only rule. Only labeled source training
dialogues are used.
