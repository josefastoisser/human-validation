Develop a model capable of identifying individual animals from images. For each test query, predict its gallery identity when the animal is present in train.csv, or new_individual when it is absent. Use the supplied labeled validation queries to select your model and rejection settings.

Read data/DATA.md for file layouts. Write _submission.csv with exactly image_id,identity in the row order of data/sample_submission.csv. Identity predictions are strings starting LynxID2025_, SalamanderID2025_, or SeaTurtleID2022_, or new_individual.

Evaluation computes BAKS separately within each dataset/species: the mean, over true known individuals, of the fraction of their queries predicted with their exact identity. BAUS is the mean, over true unknown individuals, of the fraction of their queries predicted new_individual. Unknown ground-truth identities remain distinct for balancing. An absent known or unknown component is set to zero. Compute a combined component score within each species, then average the three species scores equally. Higher scores are better.

You have 30 minutes, 2 CPUs and 4 GiB RAM. Use the local assets; no network access or pretrained weights are supplied.
