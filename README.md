# Human validation — Stages A and B

Review whether each task leaves two defensible evaluation interpretations open and resolves them clearly in Full A/B. Check source support and task quality. You do not need to solve tasks or run models or graders.

## 1. Clone the task packages (OPTIONAL)

Use [joso2/XYZ-eval on Hugging Face](https://huggingface.co/datasets/joso2/XYZ-eval/tree/main). From inside this `human validation` folder, with Git and Git LFS installed:

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/joso2/XYZ-eval XYZ-eval
git -C XYZ-eval checkout db936831dcd994fb83490b6cc921999f4af6fce6
git -C XYZ-eval rev-parse HEAD
```

Check that the last command prints the pinned revision. The saved upload record verifies this snapshot; live remote access was unavailable during handout preparation. It was private at verification: obtain read access from the owner and use your own Hugging Face credentials if required.

The snapshot has 37 tasks; **review only these 35 forms**, excluding Heart disease and Smoking. This clone skips large data downloads (the full snapshot is about 52.6 GB). Each task's `PUBLIC_FILES.md` explains how to fetch its public data if needed.

## 2. Fill in your own copy

Each reviewer keeps a separate copy of this handout. Open `forms/case_001.md`–`case_035.md` in a text editor: VS Code, Obsidian, or TextEdit in plain-text mode.

- Replace `ANSWER:` with your response; change `[ ]` to `[x]` to select an option.
- Complete **Stage A for every assigned task before any Stage B**. Read only the linked Ambiguous prompt and public files. Avoid Full A/B, discussions, private files, case cards, and model results.
- Save separate copies of your completed Stage A forms. Do not rewrite initial answers after seeing Stage B; use the later-corrections field.
- Complete Stage B using the linked Full A/B prompts, differences, and original source context. Source IDs such as `S003` are local to each task.
- Cite files and quotations or source IDs. Explain failures and required corrections. Use **Insufficient evidence** when you cannot verify a criterion.
- Work independently, without LLM-generated judgments or other reviewers' answers. Record familiarity, early exposure, and expertise limitations.

Readable public files and a complete inventory are bundled; large data remain in the clone. Record relevant files you did not inspect. Access is ordered, **not technically enforced blinding**. Record revealing paths or premature exposure in A4.


## 3. Return the forms

Return your completed forms, saved Stage A copies, and notes under your reviewer ID. Graders, execution isolation, hidden-label leakage, empirical witnesses, and behavior labels are outside this review.

`materials/` contains the evidence. Avoid `_coordinator/` during Stage A: its case mappings can reveal contrasts. All review judgments are blank.
