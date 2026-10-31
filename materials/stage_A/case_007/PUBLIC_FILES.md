# Public files for Stage A

The task prompt and public text files below are exact copies from the pinned dataset snapshot. In the agent workspace, this package's `public/` directory is mounted as `data/`.

This lightweight handout copies UTF-8 documentation, helper code, configuration, notebooks, and small tabular/JSON files up to 256 KiB each. Bulk retrieval corpora are represented by at most two unchanged example files. It does **not** contain every public file. The [complete inventory](public_inventory.csv) lists all public files, their sizes and hashes, and whether they were copied. Record any relevant uninspected files in A4; missing evidence should not be treated as a pass.

To inspect other public files, use the pinned Hugging Face clone and the per-case paths below. Do not open adjacent A/B, private, or researcher-only files during Stage A. Some original directory names reveal possible metrics; record any such cue in A4. This review uses ordered access, not technically enforced blinding.

## Included public text files

- [DATA.md](<public/DATA.md>)

## Public folder in the pinned clone

`XYZ-eval/cyrillic-morphological-induction-grand-challenge/decision-a4b6b23c702351af4cb6/packages-final/public/`

If Git LFS left pointer files, fetch this case's public data from inside the `human validation` folder:

```sh
git -C XYZ-eval lfs pull --include="cyrillic-morphological-induction-grand-challenge/decision-a4b6b23c702351af4cb6/packages-final/public/**" --exclude=""
```

A small file beginning `version https://git-lfs.github.com/spec/v1` is a pointer, not the dataset content.
