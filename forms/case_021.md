# Task review — case_021

Fill this Markdown file in a text editor. Replace `ANSWER:` with your response; change `[ ]` to `[x]` to select an option. Cite a filename and quotation or a Stage B source ID such as `S003`.

- Reviewer ID: ANSWER:
- Date: ANSWER:
- Relevant expertise: ANSWER:
- Prior familiarity with this task/source or its evaluation rule: ANSWER:
- Dataset revision: `db936831dcd994fb83490b6cc921999f4af6fce6`
- Form version: `AB-1.1`

## Stage A — inspect the Ambiguous package first

Read [the Ambiguous prompt](../materials/stage_A/case_021/prompt.md), then [the public-file guide](../materials/stage_A/case_021/PUBLIC_FILES.md) and the supplied public documentation/helpers it lists. Inspect additional public data if needed. Do not open Stage B, Full A/B, original source discussions, graders, case cards, or model results yet. Complete Stage A for all assigned tasks before starting any Stage B.

### A1. What does the task ask you to do?

In 2–3 sentences, describe the inputs, prediction target, and required submission. Identify any unclear non-evaluation requirement or contradiction. An unspecified evaluation choice does not by itself make the whole task unintelligible.

ANSWER:

Evidence (file and quotation): ANSWER:

### A2. What evaluation choices, if any, remain unresolved?

Do not assume an ambiguity must exist. List any unresolved choice that could affect solution selection or how outputs are preferred. Give plausible interpretations and their evidential or domain basis. Write “none identified” if appropriate.

ANSWER:

Evidence: ANSWER:

### A3. What supplied evidence already resolves or constrains those choices?

Check instructions, examples, schema, public documentation, and helper code. Distinguish a uniquely specified rule from a conventional default or a suggestive cue. Note conflicting clues and whether a targeted clarification would resolve a remaining choice.

ANSWER:

Evidence: ANSWER:

### A4. Record review coverage and prior exposure

- Files/data inspected: ANSWER:
- Relevant files not inspected, unavailable files, or unresolved language/domain limitations: ANSWER:
- Had you already seen the intended A/B contrast, later sources, another review, or model outcomes? [ ] No [ ] Yes [ ] Unsure
- If yes/unsure, describe what and when, including any revealing file/path names: ANSWER:
- Stage A completed and saved at (date/time): ANSWER:

---

**STOP. Save Stage A before continuing. Keep a separate copy of the completed Stage A forms before opening any Stage B material. Do not rewrite the initial answers after seeing the alternatives. Record later corrections below.**

---

## Stage B — compare specifications and inspect original sources

Open [Full A](../materials/stage_B/case_021/Full_A.md), [Full B](../materials/stage_B/case_021/Full_B.md), [the prompt differences](../materials/stage_B/case_021/prompt_differences.diff), and [the original source context](../materials/stage_B/case_021/sources.md).

- Stable case ID: `28`
- Stable task ID: `you-are-bot::decision-e4c9047d6a77b63180e0`
- Package in the pinned Hugging Face clone: `you-are-bot/decision-e4c9047d6a77b63180e0/packages-final`
- Review concerns this exact frozen package. It does not establish that every historical experimental run used the same version.

For each judgment, select one option and explain it with evidence. “Insufficient evidence” is a valid answer, not a pass. One source may support a broad ambiguity without establishing either exact local formula.

### B1. State the intended difference in your own words

- Rule A: ANSWER:
- Rule B: ANSWER:
- What evaluation choice changes, and what conventions remain fixed? ANSWER:

### B2. Is A defensible under the Ambiguous package?

Assess compatibility with *all* supplied evidence, not just the omission of a metric name. An alternative need not be equally likely, but must have a defensible basis rather than being an arbitrary invented rule.

- Judgment: [ ] Yes [ ] No [ ] Insufficient evidence
- Evidence, rationale, and any contradicting clue: ANSWER:

### B3. Is B defensible under the Ambiguous package?

- Judgment: [ ] Yes [ ] No [ ] Insufficient evidence
- Evidence, rationale, and any contradicting clue: ANSWER:

### B4. Does Full A resolve the tested choice clearly?

- Judgment: [ ] Yes [ ] No [ ] Insufficient evidence
- Cite the resolving wording. List any missing convention that changes the meaning of the tested rule: ANSWER:

### B5. Does Full B resolve the tested choice clearly?

- Judgment: [ ] Yes [ ] No [ ] Insufficient evidence
- Cite the resolving wording. List any missing convention that changes the meaning of the tested rule: ANSWER:

### B6. Are A and B substantively different evaluation preferences?

Explain how two valid outputs could be preferred differently, including a tie becoming a preference. A conceptual or small worked example is enough here. Equivalent computations, reporting-unit changes, or a strictly increasing transformation alone do not qualify. Do not inspect private graders or saved witness/model scores in this review.

- Judgment: [ ] Yes [ ] No [ ] Insufficient evidence
- Explanation/example and its assumptions: ANSWER:
- Could a strong output plausibly satisfy both interpretations? [ ] Yes [ ] No [ ] Cannot determine
- Explanation (this answer is descriptive, not an admission requirement): ANSWER:

### B7. What does the original evidence establish?

Select one source-motivation category for the *tested decision*, with citations:

- [ ] A participant directly asked about/disputed the tested decision
- [ ] A participant asked about a related decision; the local contrast changes/adds an axis
- [ ] Task documentation motivates the contrast; no direct/related question established
- [ ] Insufficient evidence to classify

Evidence (source IDs, original wording, dates when available): ANSWER:

Classify each exact local rule separately. A source question is not proof that both exact formulas were historically official.

- A: [ ] Verified authoritative specification [ ] Documented interpretation, authority unverified [ ] Researcher operationalization grounded in sources/domain conventions [ ] Insufficient evidence
- Evidence for A, including the basis for any authority claim: ANSWER:
- B: [ ] Verified authoritative specification [ ] Documented interpretation, authority unverified [ ] Researcher operationalization grounded in sources/domain conventions [ ] Insufficient evidence
- Evidence for B, including the basis for any authority claim: ANSWER:

### B8. Is the reconstruction faithful and appropriately limited?

Identify what was removed, added, or fixed relative to the original task. Does it preserve a coherent task and a defensible evaluation uncertainty? Separate ambiguity in the local package from claims about the historical competition. Do not infer a historical pre-clarification state from current pages alone.

- Reconstruction adequately supported: [ ] Yes [ ] No [ ] Insufficient evidence
- Omissions/adaptations and their consequences: ANSWER:
- Historical ambiguity: [ ] Supported for an identified period [ ] Contradicted for the claimed period [ ] Not established by available records
- Evidence, period, and limits: ANSWER:

### B9. Final Stage A/B disposition

- [ ] Accept for the text/source criteria reviewed here
- [ ] Revise and review again
- [ ] Reject this contrast for the stated ambiguity criterion
- [ ] Cannot determine without additional evidence/expertise

- Main reason and evidence: ANSWER:
- Required fixes: quote the exact wording/file and suggest the smallest correction. State “none” if none: ANSWER:
- Fix severity: [ ] None [ ] Minor wording/provenance clarification [ ] Substantive validity issue [ ] Cannot determine
- Corrections to initial Stage A answers after seeing B (leave the original answers intact): ANSWER:
- Stage B completed at (date/time): ANSWER:
- Review completed independently, without using an LLM to generate judgments or seeing another reviewer's answers: [ ] Yes [ ] No — explain: ANSWER:

This form does not validate grader correctness, executed isolation, hidden-label separation, saved preference witnesses, practical score gains, or agent behavior annotations. Those require the separate technical/behavioral review.
