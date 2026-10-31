# Public files for Stage A

The task prompt and public text files below are exact copies from the pinned dataset snapshot. In the agent workspace, this package's `public/` directory is mounted as `data/`.

This lightweight handout copies UTF-8 documentation, helper code, configuration, notebooks, and small tabular/JSON files up to 256 KiB each. Bulk retrieval corpora are represented by at most two unchanged example files. It does **not** contain every public file. The [complete inventory](public_inventory.csv) lists all public files, their sizes and hashes, and whether they were copied. Record any relevant uninspected files in A4; missing evidence should not be treated as a pass.

To inspect other public files, use the pinned Hugging Face clone and the per-case paths below. Do not open adjacent A/B, private, or researcher-only files during Stage A. Some original directory names reveal possible metrics; record any such cue in A4. This review uses ordered access, not technically enforced blinding.

## Included public text files

- [DATA.md](<public/DATA.md>)
- [corpora/00bec4ec2c7fae1f83c4e829b153d16e6a4eff0fb86c7f303bc51163026c90c7.json](<public/corpora/00bec4ec2c7fae1f83c4e829b153d16e6a4eff0fb86c7f303bc51163026c90c7.json>)
- [corpora/0156f3844588447c6fc6a19b4f24229d8f3d7cfef40dfac8a3457917368bb054.json](<public/corpora/0156f3844588447c6fc6a19b4f24229d8f3d7cfef40dfac8a3457917368bb054.json>)
- [sample_submission.csv](<public/sample_submission.csv>)
- [test.csv](<public/test.csv>)

## Public folder in the pinned clone

`XYZ-eval/acm-icaif-25-ai-agentic-retrieval-grand-challenge/decision-9ba0b405cac5726df15e/packages-final/public/`

If Git LFS left pointer files, fetch this case's public data from inside the `human validation` folder:

```sh
git -C XYZ-eval lfs pull --include="acm-icaif-25-ai-agentic-retrieval-grand-challenge/decision-9ba0b405cac5726df15e/packages-final/public/**" --exclude=""
```

A small file beginning `version https://git-lfs.github.com/spec/v1` is a pointer, not the dataset content.
