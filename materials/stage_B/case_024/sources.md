# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: Prizes](#s006)
- [S007: foundational-rules](#s007)
- [S008: Am I allowed to ...](#s008)
- [S009: FAQ](#s009)
- [S010: llm-agentic-legal-information-retrieval:thread:670127:opening](#s010)
- [S011: llm-agentic-legal-information-retrieval:thread:670127:3397010](#s011)
- [S012: llm-agentic-legal-information-retrieval:thread:670127:3397023](#s012)
- [S013: llm-agentic-legal-information-retrieval:thread:670127:3397094](#s013)
- [S014: llm-agentic-legal-information-retrieval:thread:670127:3397421](#s014)
- [S015: llm-agentic-legal-information-retrieval:thread:670127:3397552](#s015)
- [S016: llm-agentic-legal-information-retrieval:thread:670127:3397559](#s016)
- [S017: llm-agentic-legal-information-retrieval:thread:670127:3415286](#s017)
- [S018: llm-agentic-legal-information-retrieval:thread:670127:3415289](#s018)
- [S019: llm-agentic-legal-information-retrieval:thread:670127:3441999](#s019)
- [S020: llm-agentic-legal-information-retrieval:thread:670127:3398354](#s020)
- [S021: llm-agentic-legal-information-retrieval:thread:670127:3400590](#s021)
- [S022: llm-agentic-legal-information-retrieval:thread:681502:opening](#s022)
- [S023: llm-agentic-legal-information-retrieval:thread:681502:3460039](#s023)
- [S024: llm-agentic-legal-information-retrieval:thread:700882:opening](#s024)
- [S025: llm-agentic-legal-information-retrieval:thread:700882:3460038](#s025)

<a id="s001"></a>
## S001

- **source_id:** llm-agentic-legal-information-retrieval:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/data-description
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/0/text`

## Data

This tab describes the provided data files and their schemas. If you’re building a retriever, you’ll typically (1) learn from `train.csv`, (2) sanity-check on `val.csv`, (3) retrieve from `laws_de.csv` + `court_considerations.csv`, and (4) generate `submission.csv` for `test.csv`.

---

## Files

* **train.csv:** Public training queries (non-English!) with gold citation labels (semicolon-separated). Based on [**LEXam**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question).
* **val.csv:** Small validation set (10 English queries) with gold citations; doesn't match the train distribution.
* **test.csv:** Test queries only (no labels). Your notebook must generate predictions for these `query_id`s. It matches the val distribution. It has 40 English samples, 20 of them will be scored on the public leaderboard and 20 on the private leaderboard.
* **HIDDEN.csv**: Additional test data to verify potential cheating concerns like annotating test data and training on it.
* **laws_de.csv:** Retrieval corpus of Swiss federal law snippets (German), keyed by a canonical `citation` string.
* **court_considerations.csv (big!):** retrieval corpus of Swiss Federal Court decision considerations (German/French/Italian), keyed by a canonical `citation` string (includes leading *and* non-leading decisions), going back ca. 30 years. **Note:** You can start without this one if downloading is slow. Older decisions are missing and are not expected in the gold citations. We give no guarantees of completeness.
* **sample_submission.csv:**  Example of the required submission format.  

We recommend downloading these files into the `data` directory of the **[Starter Repo](https://github.com/Omnilex-AI/Omnilex-Agentic-Retrieval-Competition)**.

### LEXam (CC BY 4.0)

This competition dataset includes in train.csv material adapted from:

**LEXam: Benchmarking Legal Reasoning on 340 Law Exams**  
Yu Fan, Jingwei Ni, Jakob Merane, Yang Tian, Yoan Hermstrüwer, Yinya Huang, Mubashara Akhtar, Etienne Salimbeni, Florian Geering, Oliver Dreyer, Daniel Brunner, Markus Leippold, Mrinmaya Sachan, Alexander Stremitzer, Christoph Engel, Elliott Ash, Joel Niklaus (2025).  
Source: https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question  
Paper: https://arxiv.org/abs/2505.12864   
License: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/  
Modifications: Extracted citations from "answer" and removed most columns. Selected a subset of (row) items;  
No endorsement implied.

### Swiss legal sources (retrieval corpus)
This competition includes in laws_de.csv and court_considerations.csv excerpts of Swiss federal enactments and court decision texts sourced from official publications (e.g., Fedlex and the Swiss Federal Supreme Court’s official publication systems).  


Under Swiss law, official enactments and official decisions/reports of authorities are not protected by copyright ([Swiss Copyright Act, Art. 5](https://www.fedlex.admin.ch/eli/cc/1993/1798_1798_1798/en#art_5)). The excerpts are provided for research/competition purposes; no guarantee of completeness or officialness.

---

## Schemas

### `train.csv` / `val.csv`

| column           | type   | description                                                                               |
| ---------------- | ------ | ----------------------------------------------------------------------------------------- |
| `query_id`       | string | Unique ID (e.g., `train_0123`, `val_0007`)                                                |
| `query`          | string | Legal question in English                                                                 |
| `gold_citations` | string | Ground truth citations separated by `;` (e.g., `Art. 11 Abs. 2 OR;BGE 119 II 449 E. 3.4`) |

### `test.csv`

| column     | type   | description                   |
| ---------- | ------ | ----------------------------- |
| `query_id` | string | Unique ID (e.g., `test_0045`) |
| `query`    | string | Legal question in English     |

### `laws_de.csv`

| column     | type   | description                                                            |
| ---------- | ------ | ---------------------------------------------------------------------- |
| `citation` | string | Canonical identifier for the law snippet (use as the “ID” you predict) |
| `text`     | string | Full German text for that law chunk                                    |

### `court_considerations.csv`

| column     | type   | description                                                                         |
| ---------- | ------ | ----------------------------------------------------------------------------------- |
| `citation` | string | Canonical identifier for the decision / consideration (use as the “ID” you predict) |
| `text`     | string | Consideration text (German, French, or Italian)                                     |

---

## Submission format

Your notebook must write a `submission.csv` with:

* **one row per** `query_id` in `test.csv`
* **semicolon-separated** citations in `predicted_citations`
* **empty string allowed** if you predict no citations

```csv
query_id,predicted_citations
test_001,"Art. 11 Abs. 2 OR;BGE 139 I 2 E. 3.1"
test_002,"5A_800/2019 E 5."
test_003,""
```

###Retrieval granularity
Each row in laws_de.csv and court_considerations.csv represents one retrievable unit and one valid prediction ID.
Even if multiple rows originate from the same decision (e.g. BGE 139 I 2), they are treated as distinct citations if their canonical citation strings differ.

**Tip:** In the beginning, treat citations as **opaque, domain-specific IDs**. You do not need to parse them to compete; just output the correct canonical strings. But some understanding can help optimize your solution.

---

## Citation identifiers (optional details)

You’ll see multiple citation “families” in the labels and corpora:

### Federal law citations

For articles they look like:

* `Art. 1 ZGB`
* `Art. 117 StGB`

For paragraphs (articles that are split):

* `Art. 11 Abs. 2 OR`
* `Art. 45 Abs. 2 AHVG`

**Note:** For articles that are split into paragraphs the gold citations are the relevant paragraph citations and not full article citations. For example if `Art. 11 Abs. 2 OR` exists then `Art. 11 OR` can not be a valid gold citation.

### Federal Court decisions

Leading decisions may appear as:

* `BGE 116 Ia 56 E 1.`
* `BGE 121 III 38 E. 2b`
* `BGE 145 II 32 E. 3.1`

Non-leading (but still public) decisions can appear as docket-style identifiers, e.g.:

* `5A_800/2019 E 2.`
* `2C_123/2020 E 1.2.3`

For scoring, all of these are just citation IDs; your goal is to output the correct set per query.

---
## Data FAQ

### What does "ground truth" mean here?
Legal research doesn’t have a single, stable answer set. As the saying goes: “if you want three opinions ask two lawyers.” Disagreement is a feature of the domain, not just label noise (see “Legal Disagreement” paper: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9D4C5757ED50A48B1FBA759563C48DEC/S089765462200065Xa.pdf/legal-disagreement.pdf).

**Implications for you:**
- “Gold citations” are best treated as **high-quality references**, though they’re not infallible. We’ve observed cases where we disagree with the underlying data or interpretation.
- You should expect that's impossible to predict them perfectly
- Part of the task is to predict the opinion of the domain expert who annotated this data, rather than what a "perfect judge" would select as citations
- You can also consider it label noise 

### Why are the test set and especially the validation set small?
1. It's expensive to annotate much high-quality data
2. It may be slow for participants to do inference on many samples for this kind of task
3. You can consider it a few-shot transfer-learning task

### Can I predict citations that are not in the corpus?
Those won’t match anything and will be scored as false positives. Treat the corpus citation strings as the closed “vocabulary” of valid outputs.

### Are queries always in English? Are sources always in German?
Queries are English. Sources are mostly German; some court considerations may be French/Italian. Your system should be robust to cross-lingual retrieval.



<a id="s002"></a>
## S002

- **source_id:** llm-agentic-legal-information-retrieval:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/Description
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/1/text`

## Description

Legal research is ultimately an **information retrieval** problem: given a legal question, find the **most relevant sources** (statutes, cases, and other sources) that support the answer. In this competition, you will build an **LLM-powered (agentic) retrieval pipeline** for **Swiss law**.

### Getting started
**Start here:** **[Starter Repo](https://github.com/Omnilex-AI/Omnilex-Agentic-Retrieval-Competition)** with setup, baseline pipeline, [evaluation](https://github.com/Omnilex-AI/Omnilex-Agentic-Retrieval-Competition/blob/main/scripts/evaluate_submission.py), other helpers, and notebook templates.

### The task

For each query, output a **semicolon-separated list of citations** to the most relevant Swiss legal sources. Queries are written in **English**, while cited sources are often referenced in **German** (as in real Swiss practice). Your system can be any approach (BM25, vector embedding retrieval, reranking, multi-step agentic retrieval, citation-graph based, transfer learning, hybrid systems, etc.) as long as it produces the correct citation list in the required format.

This is a **code competition**: You will have to submit a Kaggle notebook that can reproduce your `submission.csv` in an offline environment (no internet). Notebooks intentionally create realistic constraints similar to production settings (bounded compute and privacy-sensitive domain). It has to run in at most [12 hours, which is a constraint given by Kaggle](https://www.kaggle.com/docs/notebooks#technical-specifications).  
**Note**: Submitting just a `submission.csv` is fine for testing but does not qualify for prizes. If you want to be eligible for prizes you will have to share your notebook with the host or publicly AFTER THE END of the competition and I recommend already submitting notebooks privately during the competition.
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3679848%2F35ca8e712cb51a1ff852a761003cc27a%2FScreenshot%202026-01-27%20161900.png?generation=1769527275756030&alt=media)

### Data

We provide three categories of data:

* **Training set:** [**LEXam**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question) (Fan et al., 2025) open-question queries with gold citations extracted from "answer" field.
 - Source: https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question
 - Paper: https://arxiv.org/abs/2505.12864
 - License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**  
  https://creativecommons.org/licenses/by/4.0/
 - No endorsement: The LEXam authors and Hugging Face do not endorse or sponsor this competition.
* **Test set:** queries only; final ranking is based on a **hidden** set of similar queries. The process used for creating this data is confidential, please do not publicly speculate about it.
* **Retrieval corpus:** Swiss federal laws and federal court decision considerations (the searchable sources)
 - Under Swiss law, official enactments and official decisions/reports of authorities are not protected by copyright ([Swiss Copyright Act, Art. 5](https://www.fedlex.admin.ch/eli/cc/1993/1798_1798_1798/en#art_5)). The excerpts are provided for research/competition purposes; no guarantee of completeness or official status.


See the "Data" tab for more details.

### Practical notes

* **Citations matter:** small formatting differences can cause mismatches. We use the citations from the Retrieval corpus. If you generate citations with an LLM they may have small mismatches.
* **No leakage:** the hidden test set is designed to avoid exact overlap with the training data and public data. So using all data and models accessible to you is allowed as long as you comply with the "Rules". See the "Rules" tab for further details.
* **Reproducibility:** top solutions may be reviewed; winners may be asked to share a short solution write-up if not provided in the submitted Notebook.



<a id="s003"></a>
## S003

- **source_id:** llm-agentic-legal-information-retrieval:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/Evaluation
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/2/text`

Submissions are scored using [**Macro F1**](https://en.wikipedia.org/wiki/F-score#:~:text=%5B29%5D-,Macro%20F1) computed per-query between your predicted citations and our gold citation set, then averaged across queries. This rewards systems that are adaptive to be consistently accurate across the full test distribution. For example the gold citation set may include more citations for more challenging legal questions.

* **Public leaderboard:** 50% of test queries (feedback during the competition)
* **Private leaderboard:** 50% of test queries (final ranking)

---

## Submission File
For each query_id in the test set, you must predict the set of gold_citations separated by ;. The file should contain a header and have the following format:
```
query_id,predicted_citations
test_001,"Art. 111 ZGB;Art. 114 ZGB;BGE 119 II 449 E. 3.4"
test_002,"BGE 116 Ia 56 E. 8.2.1;Art. 462 ZGB"
```
etc.

**Notes:**  
- Only citations exactly matching the strings in the retrieval corpus are considered correct.
- The order of citations within a row doesn't matter
- You can (and probably should to optimize above metric) provide a variable amount of citations.
- You can see the list of citations as the list of positives across the entire retrieval set.
- If you submit more different citations than there are in the gold set, there will definitely be some false positives in there


<a id="s004"></a>
## S004

- **source_id:** llm-agentic-legal-information-retrieval:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/rules
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/3/text`

## ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**See Section 3.18 for defined terms (rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the “Rules”). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, prizes will be awarded to Participants with the best scores, based on the merits of the data science solutions submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

---

# 1. COMPETITION-SPECIFIC TERMS

## 1. COMPETITION TITLE

**LLM Agentic Legal Information Retrieval**

## 2. COMPETITION SPONSOR

**Omnilex** (the “Competition Sponsor”)

## 3. COMPETITION SPONSOR ADDRESS

**Omnilex AG, Hohlstrasse 186, 8004, Zürich, Switzerland*

## 4. COMPETITION WEBSITE

[https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval)

## 5. TOTAL PRIZES AVAILABLE: **$10,000 USD**

* **First Prize:** $5,000
* **Second Prize:** $3,000
* **Third Prize:** $1,000
* **Most creative**: 1'000$ (Awarded to submission rated most creative by organizer, unlike other prices this solution may use extermal APIs and we're less strict on reproducibility)  

**Note:** These prizes are contingent on sharing the notebook with the host as described in www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/description and satisfying the conditions described in www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/am-i-allowed-to

## 6. WINNER LICENSE TYPE

**Open Source (OSI-approved, permissive; must allow commercial use).**
Unless otherwise stated by the Sponsor, winning solutions must be released under **Apache License 2.0** (Apache-2.0) or another OSI-approved permissive license that does not restrict commercial use.

## 7. DATA ACCESS AND USE

This Competition provides a retrieval corpus and datasets for training and evaluation, including:

* **Retrieval data/corpus:** Swiss federal laws and Swiss Federal Supreme Court decision considerations (as provided in the Competition Data)
* **Training data:** LEXam-style queries with gold citations
* **Test data:** queries only; labels are withheld and used for scoring

The Competition Data may include citations and materials in German and/or English. Participants are responsible for complying with all applicable laws and licenses relating to any data or models they use.

---

# 2. COMPETITION-SPECIFIC RULES

In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

## 2.1 TEAM LIMITS

a. The maximum Team size is **five (5)** members.
b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the Competition has been running.

## 2.2 SUBMISSION LIMITS

a. You may submit a maximum of **five (5)** Submissions per day.
b. You may select up to **two (2)** Final Submissions for judging.

## 2.3 COMPETITION TIMELINE

Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the Competition’s **Overview → Timeline** page.

## 2.4 COMPETITION DATA

### (a) Data Access and Use

**Competition Use and Non-Commercial & Academic Research (Option 2).**
You may access and use the Competition Data for **non-commercial purposes only**, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

**Additional terms:**

* You may **not** use the Competition Data to provide or improve a commercial product or service, or for commercial model training, unless you obtain prior written permission from the Competition Sponsor.
* You must comply with any licenses, notices, or attribution requirements included with the Competition Data.

### (b) Data Security

1. You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition.
2. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.
3. You may share **code** and **methods** publicly, but you may not share the Competition Data (including test queries, hidden labels, or any derived labels) outside permitted channels.

## 2.5 WINNER LICENSE

Under Section 2.8 (Winner’s Obligations) of the General Rules below, if you are a Competition winner:

### (a) Open Source license requirement

You hereby agree to license (and will license) your winning Submission and the source code used to generate the Submission under an **Open Source Initiative-approved license** (see [http://www.opensource.org](http://www.opensource.org)) that **in no event limits commercial use** of such code or model containing or depending on such code. Unless the Sponsor specifies otherwise, the Sponsor requests **Apache-2.0**.

### (b) Third-party software / models

1. For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the open-source license in the preceding Section for that software.
2. In the event that input data or pretrained models with an incompatible license are used to generate your winning solution, you do not need to grant an open-source license in the preceding Section for that data and/or model(s). However, you must clearly document all such dependencies and their licenses.

### (c) Reproducibility and solution description

You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8 (Winner’s Obligations). This may include a detailed description of methodology sufficient to reproduce the approach, including architecture, preprocessing, training details, hyperparameters, and links to a code repository with complete instructions.

---

If you want, I can also draft a **one-paragraph “Scope + prohibited use”** addendum that specifically addresses the most common legal-research competition risks (leakage via web search, using new scraped data after start date, and “human-in-the-loop” labeling).

 
####6. EXTERNAL DATA AND TOOLS

a. You may use data other than the Competition Data (“External Data”) to develop and test your Submissions. However, you will ensure the External Data is either publicly available and equally accessible to use by all Participants of the Competition for purposes of the competition at no cost to the other Participants, or satisfies the Reasonableness criteria as outlined in Section 2.6.b below. The ability to use External Data under this Section does not limit your other obligations under these Competition Rules, including but not limited to Section 2.8 (Winners Obligations). 

b. The use of external data and models is acceptable unless specifically prohibited by the Host. Because of the potential costs or restrictions (e.g., “geo restrictions”) associated with obtaining rights to use external data or certain software and associated tools, their use must be “reasonably accessible to all” and of “minimal cost”. Also, regardless of the cost challenges as they might affect all Participants during the course of the competition, the costs of potentially procuring a license for software used to generate a Submission, must also be considered. The Host will employ an assessment of whether or not the following criteria can exclude the use of the particular LLM, data set(s), or tool(s):

1. Are Participants being excluded from a competition because of the "excessive" costs for access to certain LLMs, external data, or tools that might be used by other Participants. The Host will assess the excessive cost concern by applying a “Reasonableness” standard (the “Reasonableness Standard”). The Reasonableness Standard will be determined and applied by the Host in light of things like cost thresholds and accessibility.

2. By way of example only, a small subscription charge to use additional elements of a large language model such as Gemini Advanced are acceptable if meeting the Reasonableness Standard of Sec. 8.2. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

c. Automated Machine Learning Tools (“AMLT”)

1. Individual Participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google toML, H2O Driverless AI, etc.) to create a Submission, provided that the Participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules. 

####7. ELIGIBILITY

a. Unless otherwise stated in the Competition-Specific Rules above or prohibited by internal policies of the Competition Entities, employees, interns, contractors, officers and directors of Competition Entities may enter and participate in the Competition, but are not eligible to win any Prizes. "Competition Entities" means the Competition Sponsor, Kaggle Inc., and their respective parent companies, subsidiaries and affiliates. If you are such a Participant from a Competition Entity, you are subject to all applicable internal policies of your employer with respect to your participation.

####8. WINNER’S OBLIGATIONS

a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:

1. Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code should follow [these documentation guidelines][5], must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. For avoidance of doubt, delivered software code should include training code, inference code, and a description of the required computational environment. 

a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).” 

b. Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules,

2. Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;

3. Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).

####9. GOVERNING LAW

a. Unless otherwise provided in the Competition Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.


<a id="s005"></a>
## S005

- **source_id:** llm-agentic-legal-information-retrieval:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/abstract
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/4/text`

This competition challenges you to build an LLM-powered [agentic](https://en.wikipedia.org/wiki/AI_agent) legal information retrieval system for Swiss law.

For each English legal question, your model must retrieve and output the most relevant Swiss legal sources (statutes, decisions, etc. mostly cited in German). The goal is to produce a set of citations that best matches the reference solution on a hidden test set.

You’ll get a public training dataset to develop your approach, and you’ll be evaluated on how accurately your predicted citations match the ground truth (citation-level Macro F1).


<a id="s006"></a>
## S006

- **source_id:** llm-agentic-legal-information-retrieval:page:5:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/Prizes
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/5/text`

Below prizes are provided by Omnilex, Swiss AI legal-tech startup

Total Prizes Available: 10'000$
- **1st Place** - 5'000$
- **2nd Place** - 3'000$
- **3rd Place** - 1'000$
- **Most creative** - 1'000$ (Awarded to submission rated most creative by organizer, unlike other prizes this solution may use external APIs and reproducibility requirements are relaxed)

**Note:** These prizes are contingent on satisfying the conditions described below in the [Am I allowed to ...](www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/am-i-allowed-to) section.

### Other Motivation
- **Learning**: Skills you will learn during this competition are very industry-relevant
- **Academic paper**: You are free to publish a paper related to this. If you do so consider contacting organizer ari.jordan@omnilex.ai for potential industry context and co-authorship.
- **Recruitment**: Top-performing participants may be invited for technical interviews with Omnilex. Feel free to check out our [AI Engineer -  Legal Search](https://illustrious-taxicab-a6d.notion.site/AI-Engineer-Legal-Search-2a8d9a91a45b80f88b95f0a01c5d7fb1) position.   
- **Fun**: Seeing LLM agents hopefully do what you want them to is super fun from my experience

Good luck! We are excited to see what solutions the community comes up with.


<a id="s007"></a>
## S007

- **source_id:** llm-agentic-legal-information-retrieval:page:6:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/foundational-rules
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/6/text`

The following Kaggle Competition Foundational Rules (“ Foundational Rules ”) apply to every competition regardless of whether the Sponsor creates competition-specific rules. Any competition-specific rules provided by the Sponsor are in addition to these rules, and in the case of any conflict or inconsistency, these Foundational Rules control and nullify contrary competition-specific rules.
###GENERAL COMPETITION RULES - BINDING AGREEMENT
####1. ELIGIBILITY
a. To be eligible to enter the Competition, you must be:

1. a registered account holder at Kaggle.com; 

2. the older of 18 years old or the age of majority in your jurisdiction of residence (unless otherwise agreed to by Competition Sponsor and appropriate parental/guardian consents have been obtained by Competition Sponsor); 

3. not a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, Syria, or North Korea; and

4. not a person or representative of an entity under U.S. export controls or sanctions (see: [https://www.treasury.gov/resourcecenter/sanctions/Programs/Pages/Programs.aspx][1]).

b. Competitions are open to residents of the United States and worldwide, except that if you are a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, Syria, North Korea, or are subject to U.S. export controls or sanctions, you may not enter the Competition. Other local rules and regulations may apply to you, so please check your local laws to ensure that you are eligible to participate in skills-based competitions. The Competition Host reserves the right to forego or award alternative Prizes where needed to comply with local laws. If a winner is located in a country where prizes cannot be awarded, then they are not eligible to receive a prize.

c. If you are entering as a representative of a company, educational institution or other legal entity, or on behalf of your employer, these rules are binding on you, individually, and the entity you represent or where you are an employee. If you are acting within the scope of your employment, or as an agent of another party, you warrant that such party or your employer has full knowledge of your actions and has consented thereto, including your potential receipt of a Prize. You further warrant that your actions do not violate your employer's or entity's policies and procedures.

   

d. The Competition Sponsor reserves the right to verify eligibility and to adjudicate on any dispute at any time. If you provide any false information relating to the Competition concerning your identity, residency, mailing address, telephone number, email address, ownership of right, or information required for entering the Competition, you may be immediately disqualified from the Competition.

####2. SPONSOR AND HOSTING PLATFORM

a. The Competition is sponsored by Competition Sponsor named above. The Competition is hosted on behalf of Competition Sponsor by Kaggle Inc. ("Kaggle"). Kaggle is an independent contractor of Competition Sponsor, and is not a party to this or any agreement between you and Competition Sponsor. You understand that Kaggle has no responsibility with respect to selecting the potential Competition winner(s) or awarding any Prizes. Kaggle will perform certain administrative functions relating to hosting the Competition, and you agree to abide by the provisions relating to Kaggle under these Rules. As a Kaggle.com account holder and user of the Kaggle competition platform, remember you have accepted and are subject to the Kaggle Terms of Service at [www.kaggle.com/terms][2] in addition to these Rules.

####3. COMPETITION PERIOD
a. For the purposes of Prizes, the Competition will run from the Start Date and time to the Final Submission Deadline (such duration the “Competition Period”). The Competition Timeline is subject to change, and Competition Sponsor may introduce additional hurdle deadlines during the Competition Period. Any updated or additional deadlines will be publicized on the Competition Website. It is your responsibility to check the Competition Website regularly to stay informed of any deadline changes. YOU ARE RESPONSIBLE FOR DETERMINING THE CORRESPONDING TIME ZONE IN YOUR LOCATION.

####4. COMPETITION ENTRY
a. NO PURCHASE NECESSARY TO ENTER OR WIN. To enter the Competition, you must register on the Competition Website prior to the Entry Deadline, and follow the instructions for developing and entering your Submission through the Competition Website. Your Submissions must be made in the manner and format, and in compliance with all other requirements, stated on the Competition Website (the "Requirements"). Submissions must be received before any Submission deadlines stated on the Competition Website. Submissions not received by the stated deadlines will not be eligible to receive a Prize.

b. Submissions may not use or incorporate information from hand labeling or human prediction of the validation dataset or test data records.

c. If the Competition is a multi-stage competition with temporally separate training and/or test data, one or more valid Submissions may be required during each Competition stage in the manner described on the Competition Website in order for the Submissions to be Prize eligible.

d. Submissions are void if they are in whole or part illegible, incomplete, damaged, altered, counterfeit, obtained through fraud, or late. Competition Sponsor reserves the right to disqualify any entrant who does not follow these Rules, including making a Submission that does not meet the Requirements. 

####5. INDIVIDUALS AND TEAMS
a. Individual Account. You may make Submissions only under one, unique Kaggle.com account. You will be disqualified if you make Submissions through more than one Kaggle account, or attempt to falsify an account to act as your proxy. You may submit up to the maximum number of Submissions per day as specified on the Competition Website. 

b. Teams. If permitted under the Competition Website guidelines, multiple individuals may collaborate as a Team; however, you may join or form only one Team. Each Team member must be a single individual with a separate Kaggle account. You must register individually for the Competition before joining a Team. You must confirm your Team membership to make it official by responding to the Team notification message sent to your Kaggle account. Team membership may not exceed the Maximum Team Size stated on the Competition Website.

c. Team Merger. Teams may request to merge via the Competition Website. Team mergers may be allowed provided that: (i) the combined Team does not exceed the Maximum Team Size; (ii) the number of Submissions made by the merging Teams does not exceed the number of Submissions permissible for one Team at the date of the merger request; (iii) the merger is completed before the earlier of: any merger deadline or the Competition deadline; and (iv) the proposed combined Team otherwise meets all the requirements of these Rules. 

d. Private Sharing. No private sharing outside of Teams. Privately sharing code or data outside of Teams is not permitted. It's okay to share code if made available to all Participants on the forums.

####6. SUBMISSION CODE REQUIREMENTS
a. Private Code Sharing. Unless otherwise specifically permitted under the Competition Website or Competition Specific Rules above, during the Competition Period, you are not allowed to privately share source or executable code developed in connection with or based upon the Competition Data or other source or executable code relevant to the Competition (“Competition Code”). This prohibition includes sharing Competition Code between separate Teams, unless a Team merger occurs. Any such sharing of Competition Code is a breach of these Competition Rules and may result in disqualification.

b. Public Code Sharing. You are permitted to publicly share Competition Code, provided that such public sharing does not violate the intellectual property rights of any third party. If you do choose to share Competition Code or other such code, you are required to share it on Kaggle.com on the discussion forum or notebooks associated specifically with the Competition for the benefit of all competitors. By so sharing, you are deemed to have licensed the shared code under an Open Source Initiative-approved license (see [www.opensource.org][3]) that in no event limits commercial use of such Competition Code or model containing or depending on such Competition Code.

c. Use of Open Source. Unless otherwise stated in the Specific Competition Rules above, if open source code is used in the model to generate the Submission, then you must only use open source code licensed under an Open Source Initiative-approved license (see [www.opensource.org][4]) that in no event limits commercial use of such code or model containing or depending on such code.

####7. DETERMINING WINNERS
a. Each Submission will be scored and ranked by the evaluation metric stated on the Competition Website. During the Competition Period, the current ranking will be visible on the Competition Website's Public Leaderboard. The potential winner(s) are determined solely by the leaderboard ranking on the Private Leaderboard, subject to compliance with these Rules. The Public Leaderboard will be based on the public test set and the Private Leaderboard will be based on the private test set.

b. In the event of a tie, the Submission that was entered first to the Competition will be the winner. In the event a potential winner is disqualified for any reason, the Submission that received the next highest score rank will be chosen as the potential winner.

####8. NOTIFICATION OF WINNERS & DISQUALIFICATION
a. The potential winner(s) will be notified by email.

 
b. If a potential winner (i) does not respond to the notification attempt within one (1) week from the first notification attempt or (ii) notifies Kaggle within one week after the Final Submission Deadline that the potential winner does not want to be nominated as a winner or does not want to receive a Prize, then, in each case (i) and (ii) such potential winner will not receive any Prize, and an alternate potential winner will be selected from among all eligible entries received based on the Competition’s judging criteria.

c. In case (i) and (ii) above Kaggle may disqualify the Participant.  However, in case (ii) above, if requested by Kaggle, such potential winner may provide code and documentation to verify the Participant’s compliance with these Rules. If the potential winner provides code and documentation to the satisfaction of Kaggle, the Participant will not be disqualified pursuant to this paragraph.

d. Competition Sponsor reserves the right to disqualify any Participant from the Competition if the Competition Sponsor reasonably believes that the Participant has attempted to undermine the legitimate operation of the Competition by cheating, deception, or other unfair playing practices or abuses, threatens or harasses any other Participants, Competition Sponsor or Kaggle.

e. A disqualified Participant may be removed from the Competition leaderboard, at Kaggle's sole discretion. If a Participant is removed from the Competition Leaderboard, additional winning features associated with the Kaggle competition platform, for example Kaggle points or medals, may also not be awarded.

f. The final leaderboard list will be publicly displayed at Kaggle.com. Determinations of Competition Sponsor are final and binding.

####9. PRIZES
a. Prize(s) are as described on the Competition Website and are only available for winning during the time period described on the Competition Website. The odds of winning any Prize depends on the number of eligible Submissions received during the Competition Period and the skill of the Participants. 

b. All Prizes are subject to Competition Sponsor's review and verification of the Participant’s eligibility and compliance with these Rules, and the compliance of the winning Submissions with the Submissions Requirements. In the event that the Submission demonstrates non-compliance with these Competition Rules, Competition Sponsor may at its discretion take either of the following actions: (i) disqualify the Submission(s); or (ii) require the potential winner to remediate within one week after notice all issues identified in the Submission(s) (including, without limitation, the resolution of license conflicts, the fulfillment of all obligations required by software licenses, and the removal of any software that violates the software restrictions).

c. A potential winner may decline to be nominated as a Competition winner in accordance with Section 3.8.

d. Potential winners must return all required Prize acceptance documents within two (2) weeks following notification of such required documents, or such potential winner will be deemed to have forfeited the prize and another potential winner will be selected. Prize(s) will be awarded within approximately thirty (30) days after receipt by Competition Sponsor or Kaggle of the required Prize acceptance documents. Transfer or assignment of a Prize is not allowed. 

e. You are not eligible to receive any Prize if you do not meet the Eligibility requirements in Section 2.7 and Section 3.1 above.

f. If a Team wins a monetary Prize, the Prize money will be allocated in even shares between the eligible Team members, unless the Team unanimously opts for a different Prize split and notifies Kaggle before Prizes are issued.

####10. TAXES
a. ALL TAXES IMPOSED ON PRIZES ARE THE SOLE RESPONSIBILITY OF THE WINNERS. Payments to potential winners are subject to the express requirement that they submit all documentation requested by Competition Sponsor or Kaggle for compliance with applicable state, federal, local and foreign (including provincial) tax reporting and withholding requirements. Prizes will be net of any taxes that Competition Sponsor is required by law to withhold. If a potential winner fails to provide any required documentation or comply with applicable laws, the Prize may be forfeited and Competition Sponsor may select an alternative potential winner. Any winners who are U.S. residents will receive an IRS Form-1099 in the amount of their Prize.

####11. GENERAL CONDITIONS
a. All federal, state, provincial and local laws and regulations apply.

####12. PUBLICITY
a. You agree that Competition Sponsor, Kaggle and its affiliates may use your name and likeness for advertising and promotional purposes without additional compensation, unless prohibited by law.

####13. PRIVACY
a. You acknowledge and agree that Competition Sponsor and Kaggle may collect, store, share and otherwise use personally identifiable information provided by you during the Kaggle account registration process and the Competition, including but not limited to, name, mailing address, phone number, and email address (“Personal Information”). Kaggle acts as an independent controller with regard to its collection, storage, sharing, and other use of this Personal Information, and will use this Personal Information in accordance with its Privacy Policy <[www.kaggle.com/privacy][6]>, including for administering the Competition. As a Kaggle.com account holder, you have the right to request access to, review, rectification, portability or deletion of any personal data held by Kaggle about you by logging into your account and/or contacting Kaggle Support at <[www.kaggle.com/contact][7]>.

b. As part of Competition Sponsor performing this contract between you and the Competition Sponsor, Kaggle will transfer your Personal Information to Competition Sponsor, which acts as an independent controller with regard to this Personal Information. As a controller of such Personal Information, Competition Sponsor agrees to comply with all U.S. and foreign data protection obligations with regard to your Personal Information. Kaggle will transfer your Personal Information to Competition Sponsor in the country specified in the Competition Sponsor Address listed above, which may be a country outside the country of your residence. Such country may not have privacy laws and regulations similar to those of the country of your residence.

####14. WARRANTY, INDEMNITY AND RELEASE 
a. You warrant that your Submission is your own original work and, as such, you are the sole and exclusive owner and rights holder of the Submission, and you have the right to make the Submission and grant all required licenses.  You agree not to make any Submission that: (i) infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; or (ii) otherwise violates any applicable U.S. or foreign state or federal law.

b. To the maximum extent permitted by law, you indemnify and agree to keep indemnified Competition Entities at all times from and against any liability, claims, demands, losses, damages, costs and expenses resulting from any of your acts, defaults or omissions and/or a breach of any warranty set forth herein. To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless the Competition Entities from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from: (a) your Submission or other material uploaded or otherwise provided by you that infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; (b) any misrepresentation made by you in connection with the Competition; (c) any non-compliance by you with these Rules or any applicable U.S. or foreign state or federal law; (d) claims brought by persons or entities other than the parties to these Rules arising from or related to your involvement with the Competition; and (e) your acceptance, possession, misuse or use of any Prize, or your participation in the Competition and any Competition-related activity.

c. You hereby release Competition Entities from any liability associated with: (a) any malfunction or other problem with the Competition Website; (b) any error in the collection, processing, or retention of any Submission; or (c) any typographical or other error in the printing, offering or announcement of any Prize or winners.

####15. INTERNET
a. Competition Entities are not responsible for any malfunction of the Competition Website or any late, lost, damaged, misdirected, incomplete, illegible, undeliverable, or destroyed Submissions or entry materials due to system errors, failed, incomplete or garbled computer or other telecommunication transmission malfunctions, hardware or software failures of any kind, lost or unavailable network connections, typographical or system/human errors and failures, technical malfunction(s) of any telephone network or lines, cable connections, satellite transmissions, servers or providers, or computer equipment, traffic congestion on the Internet or at the Competition Website, or any combination thereof, which may limit a Participant’s ability to participate.

####16. RIGHT TO CANCEL, MODIFY OR DISQUALIFY
a. If for any reason the Competition is not capable of running as planned, including infection by computer virus, bugs, tampering, unauthorized intervention, fraud, technical failures, or any other causes which corrupt or affect the administration, security, fairness, integrity, or proper conduct of the Competition, Competition Sponsor reserves the right to cancel, terminate, modify or suspend the Competition. Competition Sponsor further reserves the right to disqualify any Participant who tampers with the submission process or any other part of the Competition or Competition Website.  Any attempt by a Participant to deliberately damage any website, including the Competition Website, or undermine the legitimate operation of the Competition is a violation of criminal and civil laws. Should such an attempt be made, Competition Sponsor and Kaggle each reserves the right to seek damages from any such Participant to the fullest extent of the applicable law.

####17. NOT AN OFFER OR CONTRACT OF EMPLOYMENT
a. Under no circumstances will the entry of a Submission, the awarding of a Prize, or anything in these Rules be construed as an offer or contract of employment with Competition Sponsor or any of the Competition Entities. You acknowledge that you have submitted your Submission voluntarily and not in confidence or in trust. You acknowledge that no confidential, fiduciary, agency, employment or other similar relationship is created between you and Competition Sponsor or any of the Competition Entities by your acceptance of these Rules or your entry of your Submission.

####18. DEFINITIONS
a. "Competition Data" are the data or datasets available from the Competition Website for the purpose of use in the Competition, including any prototype or executable code provided on the Competition Website. The Competition Data will contain private and public test sets. Which data belongs to which set will not be made available to Participants. 

b. An “Entry” is when a Participant has joined, signed up, or accepted the rules of a competition. Entry is required to make a Submission to a competition.

c. A “Final Submission” is the Submission selected by the user, or automatically selected by Kaggle in the event not selected by the user, that is/are used for final placement on the competition leaderboard.

d. A “Participant” or “Participant User” is an individual who participates in a competition by entering the competition and making a Submission.

e. The “Private Leaderboard” is a ranked display of Participants’ Submission scores against the private test set. The Private Leaderboard determines the final standing in the competition.

f. The “Public Leaderboard” is a ranked display of Participants’ Submission scores against a representative sample of the test data. This leaderboard is visible throughout the competition.

g. A “Sponsor” is responsible for hosting the competition, which includes but is not limited to providing the data for the competition, determining winners, and enforcing competition rules.

h. A “Submission” is anything provided by the Participant to the Sponsor to be evaluated for competition purposes and determine leaderboard position. A Submission may be made as a model, notebook, prediction file, or other format as determined by the Sponsor.

i. A “Team” is one or more Participants participating together in a Kaggle competition, by officially merging together as a Team within the competition platform.

  [1]: https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx
  [2]: http://www.kaggle.com/terms
  [3]: http://www.opensource.org
  [4]: http://www.opensource.org
  [5]: https://www.kaggle.com/WinningModelDocumentationGuidelines
  [6]: http://www.kaggle.com/privacy
  [7]: http://www.kaggle.com/contact


<a id="s008"></a>
## S008

- **source_id:** llm-agentic-legal-information-retrieval:page:7:Am I allowed to ...
- **page_name:** Am I allowed to ...
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/Am I allowed to ...
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/7/text`

Consider these criteria:
- Your solution should be **reproducible**, i.e. the competition host can recreate your results with reasonable time and money
- Your solution should be **scalable**, i.e. getting it to do inference on more samples should be somewhat economically viable (max. 10$ inference cost per sample)
- Your solution should **generalize**, i.e. be expected to perform well on samples beyond the test set from the same distribution

Examples:  
1. Have domain expert annotating data manually? **No**, not scalable, not easily reproducible and if it's the test data they annotate it would not generalize.  
2. Fine-tune a model? **Yes**, if done in a reproducible way and typically this is scalable and generalizes.  
3. Scraping additional data? **Yes**, but please include or describe the code for this and upload the resulting data as Kaggle dataset so it can be reproducible. Careful with technical and legal limitations of this. Some websites can crash or block you when you scrape carelessly.

**Notes:**
- To verify generalization the competition host reserves the right to evaluate the notebook on a set of completely private queries that are **not** in the `test.csv`.
- Prizes are contingent on this re-evaluation + providing reproducible code for it.

If you are unsure about your solution meeting these criteria please reach out to  the competition host ari.jordan@omnilex.ai.




<a id="s009"></a>
## S009

- **source_id:** llm-agentic-legal-information-retrieval:page:8:FAQ
- **page_name:** FAQ
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/FAQ
- **retrieved_at:** 2026-10-13T13:35:19.387380+00:00
- **Archive locator:** `/task_documents/8/text`

See also the "Data FAQ" in the "Data" tab.

### What does “offline notebook” mean in practice?
Your submitted Kaggle notebook must reproduce submission.csv without internet access, in particular no external API calls. Any models/data you use must be available in the Kaggle environment (e.g., uploaded dataset, Kaggle packages, or preloaded model assets).
Examples of allowed resources:
- Pretrained HF models uploaded as Kaggle datasets
- Sentence-transformers, rerankers, or small LLMs that run locally
- Custom indexes built inside the notebook
- `pip install` of public libraries is allowed.  
On uncertainty please ask.

### Do I need to understand Swiss law to compete?
No. You can treat citations as opaque labels and focus on retrieval/reranking. Legal intuition can still help though (query expansion, disambiguation, choosing how many citations to return).



<a id="s010"></a>
## S010

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:opening
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127
- **thread_id:** 670127
- **comment_id:** opening
- **author_name:** 
- **author_role:** unknown
- **created_at:** 2026-01-26T08:03:10.850Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/0/text`

Few questions

1) How big is the hidden test set approximately which will run upon submission? 

2) I see no information regarding the runtime rules, is the submission run-time limit 12 hours?

3) What if there are extra citations predicted compared to the ground truth (say gold has 2, prediction has 3, out of which 2 are correct) ? Will the extra false positives be penalized and hurt the score further?


<a id="s011"></a>
## S011

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397010
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397010
- **thread_id:** 670127
- **comment_id:** 3397010
- **author_name:** Ari Jordan
- **author_role:** unknown
- **created_at:** 2026-01-26T09:32:21.797Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/1/text`

Hi,

Great questions!

1) It's 40 sample queries in total as can be seen in `test.csv`. Half of them are scored on public leaderboard and half on the private leaderboard.

2) Yes, it's the full 12 hour time limit given by Kaggle.

3) Yes, extra false positives be penalized and hurt the score.

I also clarified these things in the descriptions now.


<a id="s012"></a>
## S012

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397023
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397023
- **thread_id:** 670127
- **comment_id:** 3397023
- **parent_comment_id:** 3397010
- **author_name:** 
- **author_role:** unknown
- **created_at:** 2026-01-26T09:54:09.203Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/2/text`

Thank you. 

I have only a single follow up.
When you said this 
`It's 40 sample queries`
I can infer that there would be no "hidden test set" right? I am only worried about data leakage. If the private data is also present in the test.csv people can maybe take it to a real law practitioner and get the real answers, brute force finetuning on an LLM for some x epochs only those 40 queries alone and hack into the leaderboard. There is a high risk of this happening. 

Also [@rounddice](https://www.kaggle.com/rounddice) , I want to reach out to you privately, are you active on the email linked to your Kaggle account?


<a id="s013"></a>
## S013

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397094
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397094
- **thread_id:** 670127
- **comment_id:** 3397094
- **parent_comment_id:** 3397023
- **author_name:** Ari Jordan
- **author_role:** unknown
- **created_at:** 2026-01-26T13:17:37.903Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/3/text`

Thanks for your concern. Yes the private leaderboard queries are also present in the `test.csv`. But having a law practitioner annotate the test data is not allowed, as it would not be scalable, would not generalize and can not easily be reproduced. See also [www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/faq](http://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/faq) where I now added "Am I allowed to …?" to clarify this. You can email me at [ari.jordan@omnilex.ai](mailto:ari.jordan@omnilex.ai) or through Kaggle (Kaggle message will go to my private email).


<a id="s014"></a>
## S014

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397421
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397421
- **thread_id:** 670127
- **comment_id:** 3397421
- **parent_comment_id:** 3397023
- **author_name:** franky_0_pop
- **author_role:** unknown
- **created_at:** 2026-01-27T08:31:55.413Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/4/text`

But having private leaderboard queries makes it possible to “hack” the competition. For example: first, I would annotate private queries. Then I would automatically select the hyperparameters of the model that would give the highest metric score for the annotated private data. 
I think, you need to change the type of solution: instead of csv files there should be notebooks with unseen private data.


<a id="s015"></a>
## S015

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397552
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397552
- **thread_id:** 670127
- **comment_id:** 3397552
- **parent_comment_id:** 3397023
- **author_name:** Ari Jordan
- **author_role:** unknown
- **created_at:** 2026-01-27T15:13:19.283Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/6/text`

Thanks for the clarification. I adjusted the description to specify that I will evaluate on completely hidden data at the end of the competition. Unfortunately this competition type (Community) does not seem to allow forcing notebook submissions, see [https://www.kaggle.com/discussions/competition-hosting/397211](https://www.kaggle.com/discussions/competition-hosting/397211). I can only "force" it verbally.


<a id="s016"></a>
## S016

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3397559
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3397559
- **thread_id:** 670127
- **comment_id:** 3397559
- **parent_comment_id:** 3397023
- **author_name:** Mikhail Kondrashov
- **author_role:** unknown
- **created_at:** 2026-01-27T15:20:39.410Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/7/text`

Thanks a lot


<a id="s017"></a>
## S017

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3415286
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3415286
- **thread_id:** 670127
- **comment_id:** 3415286
- **parent_comment_id:** 3397023
- **author_name:** Ali_Haider_Ahmad
- **author_role:** unknown
- **created_at:** 2026-02-28T15:42:47.200Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/8/text`

[@rounddice](https://www.kaggle.com/rounddice) 
The competition interests me, but I (and many others) don't want to invest time in a competition where the results can be easily manipulated. There are dozens of ways one can manipulate the results, and it's 100% legal. At first glance, I think I can achieve a perfect result, and you can't disqualify the solution according to the Kagel rules.

At the very least, there should be completely hidden data.

Also, only 40 samples, even if hidden, are far too few to distinguish between different solutions.


<a id="s018"></a>
## S018

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3415289
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3415289
- **thread_id:** 670127
- **comment_id:** 3415289
- **parent_comment_id:** 3397023
- **author_name:** Ari Jordan
- **author_role:** unknown
- **created_at:** 2026-02-28T16:00:44.403Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/9/text`

Totally fair concern, leaderboard “gaming” is a real risk in small **community** comps.
A couple clarifications:

- This is a **Community** competition, so we are limited in what mechanics we can enforce (e.g., forced notebook-only) the way other formats can.

- There are additional competition rules beyond Kaggle’s defaults (see the [www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/am-i-allowed-to](http://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview/am-i-allowed-to) + FAQs).

If that still doesn’t meet your standards, I completely understand, you may want to focus on another competition.  

If you’re open to it, feel free to message/email me privately with the specific manipulation paths you’re worried about, and I’ll consider addressing what I can within the community format.


<a id="s019"></a>
## S019

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3441999
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3441999
- **thread_id:** 670127
- **comment_id:** 3441999
- **parent_comment_id:** 3397023
- **author_name:** Jaime Uclés
- **author_role:** unknown
- **created_at:** 2026-04-14T20:32:57.793Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/10/text`

So that means leaderboard is useless right? I mean you are going to reevaluate with another hidden test at the end


<a id="s020"></a>
## S020

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3398354
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3398354
- **thread_id:** 670127
- **comment_id:** 3398354
- **parent_comment_id:** 3397010
- **author_name:** jp
- **author_role:** unknown
- **created_at:** 2026-01-29T02:46:01.047Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/11/text`

hi, can you share the evaluation script for everybody?


<a id="s021"></a>
## S021

- **source_id:** llm-agentic-legal-information-retrieval:thread:670127:3400590
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/670127#comment-3400590
- **thread_id:** 670127
- **comment_id:** 3400590
- **parent_comment_id:** 3398354
- **author_name:** Ari Jordan
- **author_role:** unknown
- **created_at:** 2026-02-01T20:56:23.313Z
- **retrieved_at:** 2026-10-13T13:38:50.235813+00:00
- **Archive locator:** `/discussion/12/text`

The evaluation script can be found in the [starter repo](https://github.com/Omnilex-AI/Omnilex-Agentic-Retrieval-Competition/blob/main/scripts/evaluate_submission.py)


<a id="s022"></a>
## S022

- **source_id:** llm-agentic-legal-information-retrieval:thread:681502:opening
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/681502
- **thread_id:** 681502
- **comment_id:** opening
- **author_name:** Can
- **author_role:** unknown
- **created_at:** 2026-03-15T13:21:20.622Z
- **retrieved_at:** 2026-10-13T13:37:05.636486+00:00
- **Archive locator:** `/discussion/13/text`

Validation Set Recall Benchmarks - What are you seeing?

Hi everyone,I'm currently working on the retrieval pipeline and wanted to sync up on some baseline numbers for the validation set.

Using a Hybrid Search (embeddings + BM25) combined with some domain-specific heuristics, I'm currently hitting:

Recall@500: ~0.33

Corpus: 2.4M court records + laws

I’ve noticed a significant distribution shift between training and validation (more court cases in val), and my current bottleneck seems to be retrieving non-German (FR/IT) court decisions.

What are your Recall scores at different top_k levels (100, 500, 1000)? 

Are you using any specific cross-lingual techniques or two-stage retrieval to bridge the Law-to-Court gap?
Looking forward to hearing your insights!


<a id="s023"></a>
## S023

- **source_id:** llm-agentic-legal-information-retrieval:thread:681502:3460039
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/681502#comment-3460039
- **thread_id:** 681502
- **comment_id:** 3460039
- **author_name:** Dharun Prasanth S
- **author_role:** unknown
- **created_at:** 2026-05-18T15:17:06.720Z
- **retrieved_at:** 2026-10-13T13:37:05.636486+00:00
- **Archive locator:** `/discussion/14/text`

Direct dense/BM25 retrieval over the 2.4M court corpus didn't work for us (English query → German/French court text mismatch is too large), but we found a workaround: use your law predictions as anchors, find court rulings that cite those laws, then extract the OTHER laws those rulings cite — that "co-citation" approach surfaces relevant articles way better than retrieving courts directly.


<a id="s024"></a>
## S024

- **source_id:** llm-agentic-legal-information-retrieval:thread:700882:opening
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/700882
- **thread_id:** 700882
- **comment_id:** opening
- **author_name:** Rabeya Noor
- **author_role:** unknown
- **created_at:** 2026-05-18T09:55:50.889Z
- **retrieved_at:** 2026-10-13T13:36:15.684207+00:00
- **Archive locator:** `/discussion/15/text`

Fixed K kills your F1  - use a score threshold instead

One thing I noticed early on: most baselines here predict exactly 10 citations per query. That is a problem.

The gold citation counts in the training data average around 20-25 per query, with some queries requiring over 40. Predicting a hard cutoff of 10 means your recall is capped at roughly 40% before any retrieval even happens. Macro F1 cannot recover from that.

What works better is score-based thresholding. After reranking your candidates, keep all citations above a confidence score rather than keeping the top K. You can sweep thresholds on the validation set and find the value that maximizes your F1 directly.

One more thing that made a significant difference: the corpus is German but queries are English. Appending key Swiss legal abbreviations to the query text before BM25 search (ZGB, OR, StGB, BGer, BGG) gives a noticeable recall boost without any additional model overhead.

Happy to discuss if anyone is exploring similar directions.


<a id="s025"></a>
## S025

- **source_id:** llm-agentic-legal-information-retrieval:thread:700882:3460038
- **url:** https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/discussion/700882#comment-3460038
- **thread_id:** 700882
- **comment_id:** 3460038
- **author_name:** Dharun Prasanth S
- **author_role:** unknown
- **created_at:** 2026-05-18T15:14:33.300Z
- **retrieved_at:** 2026-10-13T13:36:15.684207+00:00
- **Archive locator:** `/discussion/16/text`

Their fixed-K critique applies to top-10 baselines, not your pipeline you're already at K=21-26 via dynamic K calibration; the abbreviation-injection trick is the actual useful piece worth testing as a free probe on your German BM25 retrieval.

