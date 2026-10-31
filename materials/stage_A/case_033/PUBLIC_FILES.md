# Public files for Stage A

The task prompt and public text files below are exact copies from the pinned dataset snapshot. In the agent workspace, this package's `public/` directory is mounted as `data/`.

This lightweight handout copies UTF-8 documentation, helper code, configuration, notebooks, and small tabular/JSON files up to 256 KiB each. Bulk retrieval corpora are represented by at most two unchanged example files. It does **not** contain every public file. The [complete inventory](public_inventory.csv) lists all public files, their sizes and hashes, and whether they were copied. Record any relevant uninspected files in A4; missing evidence should not be treated as a pass.

To inspect other public files, use the pinned Hugging Face clone and the per-case paths below. Do not open adjacent A/B, private, or researcher-only files during Stage A. Some original directory names reveal possible metrics; record any such cue in A4. This review uses ordered access, not technically enforced blinding.

## Included public text files

- [DATA.md](<public/DATA.md>)
- [labels100hz/10_1.txt](<public/labels100hz/10_1.txt>)
- [labels100hz/10_3.txt](<public/labels100hz/10_3.txt>)
- [labels100hz/11_1.txt](<public/labels100hz/11_1.txt>)
- [labels100hz/11_2.txt](<public/labels100hz/11_2.txt>)
- [labels100hz/11_4.txt](<public/labels100hz/11_4.txt>)
- [labels100hz/13_1.txt](<public/labels100hz/13_1.txt>)
- [labels100hz/2_1.txt](<public/labels100hz/2_1.txt>)
- [labels100hz/2_3.txt](<public/labels100hz/2_3.txt>)
- [labels100hz/2_4.txt](<public/labels100hz/2_4.txt>)
- [labels100hz/2_5.txt](<public/labels100hz/2_5.txt>)
- [labels100hz/4_1.txt](<public/labels100hz/4_1.txt>)
- [labels100hz/4_3.txt](<public/labels100hz/4_3.txt>)
- [labels100hz/4_4.txt](<public/labels100hz/4_4.txt>)
- [labels100hz/4_5.txt](<public/labels100hz/4_5.txt>)
- [labels100hz/5_1.txt](<public/labels100hz/5_1.txt>)
- [labels100hz/6_2.txt](<public/labels100hz/6_2.txt>)
- [labels100hz/6_3.txt](<public/labels100hz/6_3.txt>)
- [labels100hz/6_5.txt](<public/labels100hz/6_5.txt>)
- [labels100hz/7_1.txt](<public/labels100hz/7_1.txt>)
- [labels100hz/7_2.txt](<public/labels100hz/7_2.txt>)
- [labels100hz/7_3.txt](<public/labels100hz/7_3.txt>)
- [labels100hz/7_4.txt](<public/labels100hz/7_4.txt>)
- [labels100hz/8_1.txt](<public/labels100hz/8_1.txt>)
- [labels100hz/8_4.txt](<public/labels100hz/8_4.txt>)
- [labels100hz/8_5.txt](<public/labels100hz/8_5.txt>)
- [labels100hz/9_1.txt](<public/labels100hz/9_1.txt>)
- [labels100hz/9_2.txt](<public/labels100hz/9_2.txt>)
- [labels100hz/9_3.txt](<public/labels100hz/9_3.txt>)
- [labels100hz/9_4.txt](<public/labels100hz/9_4.txt>)
- [labels100hz/9_5.txt](<public/labels100hz/9_5.txt>)
- [sample_submission.csv](<public/sample_submission.csv>)
- [test.csv](<public/test.csv>)
- [validation.csv](<public/validation.csv>)

## Public folder in the pinned clone

`XYZ-eval/event-based-eye-tracking-ais2024/researcher-64d637fc5be570e2163e/packages-final/public/`

If Git LFS left pointer files, fetch this case's public data from inside the `human validation` folder:

```sh
git -C XYZ-eval lfs pull --include="event-based-eye-tracking-ais2024/researcher-64d637fc5be570e2163e/packages-final/public/**" --exclude=""
```

A small file beginning `version https://git-lfs.github.com/spec/v1` is a pointer, not the dataset content.
