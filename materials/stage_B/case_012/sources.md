# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: foundational-rules](#s006)
- [S007: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:opening](#s007)
- [S008: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:3300442](#s008)
- [S009: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:3291081](#s009)
- [S010: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:609026:opening](#s010)
- [S011: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:609026:3293562](#s011)
- [S012: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:opening](#s012)
- [S013: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3304678](#s013)
- [S014: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3304682](#s014)
- [S015: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3305075](#s015)
- [S016: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:opening](#s016)
- [S017: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3306634](#s017)
- [S018: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3307945](#s018)
- [S019: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3307948](#s019)
- [S020: acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613462:opening](#s020)

<a id="s001"></a>
## S001

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/data-description
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/0/text`

## Overview  

This competition is designed to evaluate *agentic (multi-step) retrieval* capabilities in financial AI. The central goal is to identify grounded evidence from large-scale SEC filings in order to answer complex institutional finance questions. To this end, participants are tasked to ***optimize a system prompt that maximize the ranking performance***. Unlike traditional retrieval tasks, this challenge is framed as a two-stage process.

In the first stage, **Document-Level Ranking**, participants must determine which type of SEC filing—such as 10-K, 10-Q, 8-K, DEF 14A, or an Earnings Transcript—is most likely to contain the relevant information for a given query. In the second stage, **Chunk-Level Ranking**, the task shifts to locating the most relevant passages within the selected document, with participants required to rank the Top-5 chunks that best support the answer.  

The dataset is drawn from expert-curated examples based on real SEC filings from the period 2023–2024. This ensures that questions and contexts are realistic and grounded in actual financial disclosure practices.  

All results must be submitted as a single consolidated **CSV file** that combines outputs from both retrieval tasks. Detailed specifications for the submission format are provided in a separate section.  

To ensure reproducibility, every submission must include a working notebook that can be executed in the **Databricks Free Edition** environment. The notebook link should be posted in the competition’s discussion tab as the standardized evaluation interface. For participants interested in enhanced functionality, optional integration with the **Upstage Solar LLM API** is also supported.  

***Notice: The dataset for competition will be accessable at the start of the competition.***

## Files

*   **document_ranking_kaggle_dev.jsonl** - the development set of document ranking task.
*   **chunk_ranking_kaggle_dev.jsonl** - the development set of chunk ranking task.

*   **document_ranking_kaggle_eval.jsonl** - the development set of document ranking task. (containing 200 samples)
*   **chunk_ranking_kaggle_eval.jsonl** - the development set of chunk ranking task. (containing 200 samples)

## Columns - Document Ranking Task

The following columns are provided for the **document-level ranking** dataset. This task requires ranking entire SEC filing types by their relative likelihood of containing the answer to a given financial question.

- `_id`: An unique identifier for each sample.

- `messages`: A JSON-style field containing the complete **user prompt**. This includes the instruction, the financial question, and the list of candidate document types to be ranked. The prompt specifies that the output must be a list of indices (e.g., `[4, 2, 1, 0, 3]`), covering all document types in ranked order.  

- `qrel`: A dictionary mapping document indices (`0` … `N-1`) to integer scores between 0 and 4, matches roughly with the **relative importance of each document type**.  
  - `4` = most relevant document type  
  - `3` = next most relevant  
  - `2` = moderately relevant  
  - `1` = weakly relevant  
  - `0` = least relevant document type  
  - In other words, every candidate document type receives a unique score from 0–4, reflecting its position in the ranking.  
  - **Important**: *qrel values are provided only in the development/training set. For the official test set, `qrel` is hidden and participants must predict the ranking themselves.*  

These fields define the input (prompt + candidate document types), the relative ground-truth ranking used in development, and the contextual metadata needed to interpret each example.

## Columns - Chunk Ranking Task

The following columns are provided for the **chunk-level ranking** dataset. This task requires ranking paragraph-level chunks within a single SEC filing to identify which passages contain the supporting evidence needed to answer the question.

- `messages`: A JSON-style field containing the full user prompt. This includes a simple instruction, the financial question, and the context of the document or chunks to be ranked.  
- `qrel`: A dictionary mapping chunk indices (`0` … `N-1`) to graded relevance labels, following a TREC-style convention.  
  - `0` = non-relevant (negative chunk)  
  - `1` = relevant (positive chunk)  
  - `2` = highly relevant (strong positive chunk)  
  These labels provide a finer-grained supervision signal compared to binary annotation.  
  - **Note**: `qrel` is only included in the development/training set for evaluation and model tuning. In the official test set, `qrel` values are hidden and participants must predict the relevance scores themselves.  

These fields collectively define the input (prompt + candidate chunks), the ground-truth labels used for evaluation in development, and the contextual metadata describing the example.


<a id="s002"></a>
## S002

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/Description
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/1/text`

In the **AI Agentic Retrieval Grand Challenge**, participants are tasked with developing systems capable of retrieving the most relevant evidence from raw SEC filings to answer institutional finance questions. The task is structured as a two-stage agentic retrieval problem: **Document-Level Ranking** and **Chunk-Level Ranking**. This two-step design prioritizes accuracy and qualities essential for deploying AI systems in investment research. Participants’ systems will be evaluated on their capacity to reason across both document-type ranking and chunk-level retrieval tasks. 

*All submissions must include a **reproducible notebook implemented within Databricks Free Edition workspaces**, with the notebook link uploaded in the discussion tab as the standardized evaluation interface. Optional integration with the Upstage API (Solar LLM) is allowed.*

## Task Overview
<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F7863652%2F6e3455da37771a24b6003d5eed85d076%2FPipeline-4(2)%209.13.16PM.png?generation=1756021014437025&alt=media" width="400"/>

For each **Document-Level Ranking** and **Chunk-Level Ranking** task, you are required to **optimize a system prompt** to rank as follows:
1.	**Document-Level Ranking** – Given a financial question, systems must rank candidate document types (10-K, 10-Q, 8-K, DEF-14A, earnings transcripts) by their likelihood of containing the adequate information for answering the question.
2.	**Chunk-Level Ranking** – Given a single document, systems must identify and rank the most relevant passages within the provided document, returning a ranked list of candidate chunks that contain the information needed for answering the question.



<a id="s003"></a>
## S003

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/Evaluation
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/2/text`

## Task Evaluation![task_evaluation](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F7863652%2F6e5405c50f64d9f28f6be300dae18f23%2FTasks-4(2)%209.13.22PM.png?generation=1756021154576940&alt=media)

The challenge consists of two sequential retrieval tasks. In the document-type ranking task, participants must rank all candidate document types based on their relevance to the input question. In the chunk-level ranking task, given the selected document, participants must rank the top 5 most relevant paragraph-level passages that contain the information necessary for answering the question.

Both tasks will be evaluated using standard ranking metrics, averaged across runs: **MRR@5** (Mean Reciprocal Rank), **MAP@5** (Mean Average Precision), and **nDCG@5** (Normalized Discounted Cumulative Gain). The leaderboard will display your **MAP@5** score.


## Submission File


For every **sample_id** in the test set, you are required to predict the probability of the **TARGET document or passage index** in the example. The submission file should contain two columns: **sample_id** and **target_index**.

Each **sample_id** should be associated with the top 5 **target_index** predictions, ordered by probability, with the most probable context listed first.

The submission file must include a header and follow this format:

```
sample_id, target_index
```

You are required to **submit a single `CSV` file** that consolidates the results from all datasets.

```
sample_id,target_index
chunk_q613509,92
chunk_q613509,91
chunk_q613509,9
chunk_q613509,94
chunk_q613509,104
    etc..
```


<a id="s004"></a>
## S004

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/rules
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/3/text`

To ensure fair competition management and prevent fraudulent activities, we have established the following rules for our competition.
## One account per participant
- Participants may join the competition individually or as part of a team, but each participant must be affiliated with only one team. The maximum team size is 5.
## Merging Team
- Merging teams is allowed freely until the final submission, as long as the combined team's total submission count does not exceed the maximum allowed on the day of the merge.
## Submission Limits
- Each team may submit up to 5 times per day. Any submissions to the Public Leaderboard after the 5th submission will not be reflected on the leaderboard. Only the results of the last submission will be considered in the final evaluation. The submission for the private leaderboard is limited to 5 times during the entire competition.
## Code & Report Submission
- To have a participant's results included in the final results, Each team must submit **a reproducible notebook implemented within Databricks Free Edition workspaces**, with the notebook link uploaded in the **discussion tab** as the standardized evaluation interface.


<a id="s005"></a>
## S005

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/abstract
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/4/text`

# Agentic Retrieval for Financial Documents (AI Grand Challenge on FinAgentBench)

> We provide all participants with a baseline guide [HERE](https://www.kaggle.com/code/jihoonkwon/baseline-for-agentic-retrieval-grand-challenge).
> As we show in the demo, even simple changes like swapping in different LLMs or adjusting prompting could lead to clear improvements. You do not need deep LLM expertise to participate.

The **AI Agentic Retrieval Grand Challenge at ICAIF ’25** is motivated by the need for financial AI systems that can move beyond what traditional methods can achieve in accuracy to deliver interpretable, evidence-grounded answers from complex SEC filings. Participants are tasked with **building retrieval systems** by ***optimizing a system prompt*** that can support complex institutional finance questions with character-level evidence attribution. This competition is built on **FinAgentBench**, a benchmark purpose-built to evaluate **multi-step, agentic retrieval**.
Each query requires reasoning across **two stages**: first, *selecting the most relevant document type* (Document-Level Ranking), and second, *identifying the most relevant passages within single document* (Chunk-Level Ranking). The dataset contains about 26K examples curated by expert financial analysts from real SEC filings (2023–2024). Participants must return ranked results for both **document-level and chunk-level ranking tasks**.

## Participants who impress with their solutions (and explain how they achieved them) will be invited as a presenter sharing their work at ICAIF ’25. 
Further details will be announced once sponsorship is confirmed.



<a id="s006"></a>
## S006

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/overview/foundational-rules
- **retrieved_at:** 2026-10-16T23:55:22.260973+00:00
- **Archive locator:** `/task_documents/5/text`

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


<a id="s007"></a>
## S007

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:opening
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/607948
- **thread_id:** 607948
- **comment_id:** opening
- **author_name:** Yiming Qian
- **author_role:** unknown
- **created_at:** 2025-09-17T05:44:11.715Z
- **retrieved_at:** 2026-10-16T23:59:42.483426+00:00
- **Archive locator:** `/discussion/0/text`

what is the evaluation metrics

What evaluation metrics do you use to measure the performance of the ranking algorithm?


<a id="s008"></a>
## S008

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:3300442
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/607948#comment-3300442
- **thread_id:** 607948
- **comment_id:** 3300442
- **author_name:** Joseph Thomas Thachil
- **author_role:** unknown
- **created_at:** 2025-10-10T12:55:07.393Z
- **retrieved_at:** 2026-10-16T23:59:42.483426+00:00
- **Archive locator:** `/discussion/1/text`

Hey [@jihoonkwon](https://www.kaggle.com/jihoonkwon) 

the data overview says leaderboard is on map@5

but the discussion here mentions ndcg@5

any guide on what we should aim at?


<a id="s009"></a>
## S009

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:607948:3291081
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/607948#comment-3291081
- **thread_id:** 607948
- **comment_id:** 3291081
- **author_name:** JIHOONKWON
- **author_role:** unknown
- **created_at:** 2025-09-19T01:01:28.057Z
- **retrieved_at:** 2026-10-16T23:59:42.483426+00:00
- **Archive locator:** `/discussion/2/text`

We use NDCG@5.


<a id="s010"></a>
## S010

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:609026:opening
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/609026
- **thread_id:** 609026
- **comment_id:** opening
- **author_name:** David Lau
- **author_role:** unknown
- **created_at:** 2025-09-23T08:24:53.111Z
- **retrieved_at:** 2026-10-16T23:57:50.064669+00:00
- **Archive locator:** `/discussion/3/text`

Clarification on the challenge

I'm new to Kaggle challenge but I'm very interested in the topic as I have been dealing with such questions for years (without AI).

My question is, are we supposed to use your code and just change the "system prompt" in order to get the result, or we can use a different approach, e.g., introducing some other workflow?

Thanks.


<a id="s011"></a>
## S011

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:609026:3293562
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/609026#comment-3293562
- **thread_id:** 609026
- **comment_id:** 3293562
- **author_name:** JIHOONKWON
- **author_role:** unknown
- **created_at:** 2025-09-24T06:03:02.280Z
- **retrieved_at:** 2026-10-16T23:57:50.064669+00:00
- **Archive locator:** `/discussion/4/text`

It is okay to use a different approach. What you need to do is provide justification for your approach. It is very important for getting a high score, but it is also essential to clearly show when and why your approach works well.


<a id="s012"></a>
## S012

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:opening
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/612625
- **thread_id:** 612625
- **comment_id:** opening
- **author_name:** DanT
- **author_role:** unknown
- **created_at:** 2025-10-21T03:24:46.268Z
- **retrieved_at:** 2026-10-16T23:56:39.588625+00:00
- **Archive locator:** `/discussion/5/text`

Deep Analysis on the Competition

Note: submission deadline in 1h, good luck to everyone. 

I'd like to share with you some insights after ~200h, and $200 of API spending: Databricks/OpenAI/Parasail closing in about 1B tokens spent 😅

ACM ICAIF 2025 Competition: Design & Technical Challenges

**Document Purpose**: Foundation for Kaggle submission justification

**Date**: 2025-10-21

1. Competition Structure

Task Definitions

**Document Ranking**:

- Input: Financial question + 5 fixed SEC filing types (DEF14A, 10-K, 10-Q, 8-K, Earnings)

- Output: Ranked list of all 5 document indices

- Ground truth: Graded relevance 0-4 (4=most relevant)

**Chunk Ranking**:

- Input: Financial question + 100-300 paragraph-level text chunks

- Output: Top-5 ranked list of most relevant chunk indices

- Ground truth: Graded relevance 0-2 (2=highly relevant), different than required output

Evaluation Metrics

All tasks scored independently using three metrics at top-5 positions:

- **MRR@5** (Mean Reciprocal Rank): Rewards first relevant result

- **MAP@5** (Mean Average Precision): Measures ranking of all relevant items

- **nDCG@5** (Normalized Discounted Cumulative Gain): Accounts for graded relevance with position discounting

The Leaderboard only shows MAP@5, which is not the full picture (also focus on nDCG@5 mentioned in Discussion topic by organizers)

2. Data Characteristics

Document Ranking

**Query Message Characteristics**:

- Consistent 155 tokens per message (range: 144-173)

- 79.1% queries use all 5 scores [0,1,2,3,4]

- **20.9% have ties** (should not happen as in competition instructions, but present in data)

**Score Distribution Non-Uniformity**:

Score
Frequency
Percentage

0
6,064
24.3%

1
5,367
21.5%

2
4,951
19.9%

3
4,605
18.5%

4
3,943
15.8%

Chunk Ranking

**Scale & Context Window**:

- Mean: 190 chunks per query, 65K tokens

- Range: 5-661 chunks, 2.7K-224K tokens

- **Critical**: 67.5% queries exceed 32K tokens (eval set)

- Individual chunks: Mean 335 tokens (range 1-71K), median 182 tokens

On data labelling:

- About <1% of labels are extremely short 1-3 tokens: in data collection, experts see the full document (e.g. 1 relevant chunk with one token "43", among ~200 scored as not relevant) vs. this data, we only see chunks.

- There are queries with >10 relevant chunks (max: 142)

**Distribution of Chunk Relevance dev-set**:

Metric
Value

Relevant chunks (score > 0)
5.1% of all chunks

Queries with only 1-2 relevant chunks
30.67% (needle-in-haystack)

Queries with >10 highly relevant chunks
4.25%

**Distribution of ground truth dev-set**:

Score
Frequency
Percentage

0 (irrelevant)
3,029,827
94.9%

1 (relevant)
118,778
3.7%

2 (highly relevant)
44,847
1.4%

**Token Distribution** (eval-set):

Context Window
Queries
Percentage

>32K
135
67.5%

>60K
106
53.0%

>128K
18
9.0%

3. Technical Challenges

Challenge 1: Needle-in-Haystack Problem

**Definition**: Sparse signal detection - finding 1-2 relevant chunks among 100-300 candidates.

**Quantitative Impact**:

- 30.67% of chunk queries have only 1-2 relevant chunks

- 5.1% overall chunk relevance rate (94.9% noise)

- 12.5% zero-score rate observed in early experiments (fail to find the needles in top-5 = 0x3 scores)

**Concrete Example** (Query q2e28fdef127e):

`Question: "What investor views emerged on KeyCorp's geographic expansion prospects?"
Total chunks: 
Relevant:  chunk (position / ~ % relative context)
Content: [] State- loan distribution
         Washington , | Ohio , |  York  | Colorado ,
`

**Failure Mechanism**:

- Lexical overlap: ZERO (question has "expansion", "prospects"; chunk has state names, numbers)

- Required inference: "Loan distribution by state" → "Geographic footprint" → "Expansion capability"

- Weak signal buried in noise → Dropped at filtering stage → Final score: 0.0

**Impact**: Even advanced LLMs struggle when relevant chunks lack direct keyword matches and require financial domain inference. Position does matter, needles in early/last relative positions have better chance - "lost in the middle".

Challenge 2: Context Window Constraints

**Problem**: 67.5% of chunk queries exceed 32K tokens (refer to Context Rot recent findings), 10% exceed 120k tokens

**Eval Set Statistics**:

Percentile
Message Tokens
Chunks

P50
63,756
160

P90
120,451
~300

Max
224,000
661

**Processing Constraint**:

- Most production LLMs: 32K-128K context windows

- Even 200K-1M context models face "lost in the middle" phenomenon

- Requires splitting into multiple parts for processing

**Trade-off**: More splits enable good processing early BUT create compound drop problem (Challenge 3).

Challenge 3: Multi-Stage Compound Drop Problem

**Definition**: Local filtering loses globally relevant chunks in multi-stage ranking.

**Dataflow Example** (5-part split):

`Query:  chunks,  relevant

Part :  chunks,  relevant → Rank  →  top → If relevant ranks th → DROPPED
Part :  chunks,  relevant → Rank  →  top → If relevant ranks th → DROPPED
...
Part :  chunks,  relevant →  process

:  part creates  opportunity
        Dropped chunks NEVER reach  ranking stage
`

**Experimental Evidence** (split size analysis, n=100):

Split Size
Local Recall
Zero-Score Rate

3K tokens/part (many splits)
75.35%
3.3%

15K tokens/part (optimal)
75.35%
~15-18%

30K tokens/part (fewer splits)
64.16%
28.6%

**Critical Finding**: Splitting enable 'divide and conquer' (insight from the organizers), but too many splits -> global pool dilution (next).

Challenge 4: Global Dilution Problem

**Definition**: Chunks surviving local filtering still face overwhelming competition in global pool.

**Concrete Example** (Query q4054d9fe6d42):

`:  chunks,  relevant, using top-k= (because each split now has few chunks)
 split →  parts 

 Stage:
  :  relevant chunks
  :  chunks
  :  relevant chunks → Sent to global pool ✓

 Pool:
   candidates:  parts ×  =  candidates
   density: / = .% relevant
  : / = .% irrelevant

 Re-Ranking (top- selection):
  :  relevant chunks
  :  relevant chunks

 Drop Rate:  →  = % of surviving chunks lost at global stage
 Score: .
`

**Mechanism**: Surviving chunks compete in global pool. Stronger competition with 'distractors' (seemingly relevant, or weakly relevant).

**Comparison** (same query):

` split →  parts

 Stage: ~ chunks survive ( dropped locally)
 Pool:  ×  =  candidates
 density: / = % relevant (vs .% for K)
 Selection: ~ relevant chunks
 Drop Rate:  →  = % (better than K's %)
 Score: .-. (x improvement)
`

**Insight**: Signal-to-noise ratio in later-stage pool determines final performance. There in an inverted-u curve when it comes to splitting (assume fixed top-k, I also tried dynamic k but more issues there).

Challenge 5: Semantic Gap

**Definition**: queries require inference fail more when context is fragmented across splits.

**Example Dataflow** (Query q2e28fdef127e):

` 

Part  (chunks ): Contains chunk  (state-level loan table)
  → ranks in isolation
  → No  linking  to 
  → Chunk  . (weak relevance)
  → Dropped from local top

Part  (chunks ): Contains chunks about  (conceptual   → part, never sees chunk  data

Part  (chunks ): Contains chunks about  (meeting transcript)
  → part, never sees chunk  data
 never synthesizes connection         () Geographic loan data [Part ]
        () Expansion strategy  [Part ]
        () Investor view framing [Part ]
        → Final . (complete failure)
`

**Impact**: Context fragmentation breaks holistic understanding needed for semantic inference in financial domain. 

**Hypothesis**:  if chunks are small and uniform (say 50-200 tokens)

`Single-stage ranking (  chunks):
  → LLM sees chunk  ( loan )
  → Also sees expansion strategy discussion
  → Also sees investor question framing
  → Can infer: 
  → Makes final top-
`

But this is not the reality. Extreme variance found in chunks' token counts, leptokurtic (1-71K), flood context window.

Challenge 6: Context Rot & "Lost in the middle"

**Definition**:  LLMs struggle to find needles when: (1) prompt is longer, and (2) relevant chunk is not in first-last 20% of context window.

**Why Extended Context Fails**:

`

   
   
   
   

   
   
   
   
   
`

**Attention Allocation Comparison**:

Strategy
Chunks/Context
Attention/Chunk
Global Pool
Global Attention

30-chunk parts
30
3.3%
50 candidates
2.0%

95-chunk parts
95
1.1%
475 candidates
0.2%

Extended (full)
309
0.3%
N/A
0.3%

**Empirical Validation**: Long-context models struggle, perform worse than splitting. Splitting is critical, should NOT fit everything in one query.

4. Architecture Trade-offs

Trade-off 1: Split Size Paradox

**Intuition**: Fewer splits → Fewer local competitions → Less compound drop risk.

**Reality**: Larger splits create saturated ranking tasks that degrade performance.

**Experimental Evidence** (2-split performance comparison):

Threshold
Chunks/Part
Tokens/Part
2-Split Local Recall

15K
~50-70
15K
**80.55%** (BEST)

30K
~80-100
30K
66.07% (-14.5pts)

45K
~100-150
45K
**54.41%** (WORST, -26.1pts)

**Mechanism**:

- **Prompt Length Effect**: 15K prompts preserve instruction retention; 45K prompts degrade clarity

- **Ranking Capacity**: K/N ratio critical - 10/50 (20%) captures needles better than 10/150 (7%)

- **Compound Drops**: More splits create more opportunities to drop, BUT better RECALL per split -> win

**Optimal Point**: ~15K threshold (50-70 chunks/part) balances all three factors.

Trade-off 2: Local Pool Paradox

**Naive Solution**: Increase local top-K from 5 to 10 to capture more relevant chunks.

**Why It Fails**:

`Example: =5  =10, given 10 equal splits
Local Ranking (Part-2, 18 chunks, =10):
  Position 6: Relevant chunk, score 0.73 ← CAPTURED with =10 ✓ (would drop with =5)

Global Ranking : 50 candidates -> 100 candidates:
  Relevant chunk STILL has score 0.73 (unchanged)
  But now competes with 90 instead of 40 chunks.
  → Relevant chunk ranks ~45th globally
  → DROPPED  final top-5 ✗
`

**Mathematical Formula**:

`

 :
  
  
   :  
`

**Critical Insight**: We cannot improve global outcomes without changing the scores in the 2nd stage -> re-ranking using math formula rarely works. This agrees with the baseline setup from the organizers.

**Solution**: Global re-scoring assigns NEW scores in full context:

- Stage 1 (local): Chunk gets 0.73 in limited context (18 chunks)

- Stage 2 (global): Model sees all 10 x 10 = 100 candidates, assigns NEW score 0.88 

- Result: Chunk becomes competitive, makes final top-5

**Empirical Validation**: Global re-scoring provides +5.8pts improvement over single-stage architecture.

Trade-off 3: BM25 Pre-filtering Catastrophe

**Proposed Approach**: Use BM25/embeddings to filter chunks before LLM ranking.

**Why It Fails**:

`Pipeline: BM25 → :
: 
Chunk : [TABLE] 

BM25 :
  Question : [, , , ]
  Chunk : [, , , , ]
  Lexical : MINIMAL ( weak match on geographic terms)
  BM25 : ~- out of  chunks

Filter to top-:  chunks
  → Chunk   in top-
  → DROPPED at Stage 
  → Never reaches LLM
  → Final : 
`

**Fundamental Error**: Financial questions require conceptual understanding:

- "Geographic expansion" = loan distribution by state (tables)

- "Revenue concentration" = customer segment breakdown (tables)

- "Margin pressure" = cost structure details (financial data)

**BM25/embeddings cannot infer these semantic connections** → Drops relevant chunks → Permanent information loss.

**Conclusion**: Lexical filtering BEFORE deep reasoning is more harmful than multi-stage LLM architecture. Only LLM can perform required semantic inference.

Trade-off 4: Extended Context Failure

**Assumption**: Longer context windows (200K) solve splitting problem by processing all chunks together.

**Reality**: Attention degradation worse than multi-stage processing.

**Evidence** (predicted performance for 309-chunk query):

`
   
   
   
   

   
   
   
`

**Implication**: More context creates MORE noise, not less. The needle gets buried deep.

Summary

Competition Constraints Drive Design

**Data Characteristics**:

- 67.5% queries exceed 32K tokens → Requires multi-part processing

- 30.67% queries have 1-2 relevant chunks among ~200-300 candidates → Needles-in-haystack

- 5.1% overall relevance rate → Overwhelming noisy

**Technical Challenges**:

- Sparse signal detection in high-noise environments

- Context window constraints requiring splitting

- Multi-stage compound drops (local filtering loses global relevance)

- Global dilution (surviving chunks face 92% drop rate in noisy pools)

- Semantic gaps (inference breaks when context fragments)

- Context rot (attention degradation in extended contexts)

Key Trade-offs

**What Fails**:

- Extended context single-stage: Context rot degrades performance

- BM25 pre-filtering: Drops inference-requiring chunks

- Large split sizes: Saturated ranking (100-150 chunks/split) performs worse than moderate (50-70 chunks/split)

- Pool expansion without re-scoring: Local scores determine global outcomes

**What Works**:

- Optimal split size (15K tokens, 50-70 chunks/part): Balances attention vs drops

- Global re-scoring: NEW scores in full context (+5.8pts improvement)

- Lexical-semantic fusion: BM25 boost (not filter) helps weak signals without dropping chunks

- Multi-stage architecture: Better than extended context despite compound drops

**Critical Design Principles**:  Optimize attention allocation within context rot limit while preserving high local recall at filtering stage.


<a id="s013"></a>
## S013

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3304678
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/612625#comment-3304678
- **thread_id:** 612625
- **comment_id:** 3304678
- **author_name:** Yuzhen Hu
- **author_role:** unknown
- **created_at:** 2025-10-21T04:28:02.913Z
- **retrieved_at:** 2026-10-16T23:56:39.588625+00:00
- **Archive locator:** `/discussion/6/text`

Wow, $200 for 200 hours — that’s dedication! Thank you for sharing!  I didn’t spend a penny on tokens, just fine-tuned downstream task ,but my GPU is  running so hot I’m getting roasted, and my electricity bill feels it .😂


<a id="s014"></a>
## S014

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3304682
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/612625#comment-3304682
- **thread_id:** 612625
- **comment_id:** 3304682
- **parent_comment_id:** 3304678
- **author_name:** DanT
- **author_role:** unknown
- **created_at:** 2025-10-21T04:41:23.620Z
- **retrieved_at:** 2026-10-16T23:56:39.588625+00:00
- **Archive locator:** `/discussion/7/text`

Nice, fine-tune with your GPU is cool. For me it was a chance to test backends also, can brag later that I win -200$ :) Did you notice issues with the labels? Some labels are out-of-context, about <1% relevant chunks have 1-3 tokens


<a id="s015"></a>
## S015

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:612625:3305075
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/612625#comment-3305075
- **thread_id:** 612625
- **comment_id:** 3305075
- **parent_comment_id:** 3304682
- **author_name:** Yuzhen Hu
- **author_role:** unknown
- **created_at:** 2025-10-22T00:24:42.000Z
- **retrieved_at:** 2026-10-16T23:56:39.588625+00:00
- **Archive locator:** `/discussion/8/text`

Yeah, exactly — because the text is split into chunks, some parts seem irrelevant ,only make sense with more context and domain knowledge.  judging relevance just from one chunk is tricky. I wanted to try adding chunk position and some context info to the model’s encoding, but I didn’t have enough time before the deadline.

Another challenge is that the content isn’t just about finance — it also includes topics like Apple, healthcare, and many other companies and area , So  finance domain isn’t enough to understand the overall context.


<a id="s016"></a>
## S016

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:opening
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/613060
- **thread_id:** 613060
- **comment_id:** opening
- **author_name:** DanT
- **author_role:** unknown
- **created_at:** 2025-10-24T00:39:44.716Z
- **retrieved_at:** 2026-10-16T23:55:55.138739+00:00
- **Archive locator:** `/discussion/9/text`

Competition Evaluation - Clarification

Dear organizers, thank you for your significant effort in running this challenge. Now that submissions have closed for 3 days, I have a few questions about the evaluation process.

**1. Evaluation Timeline**

What is the timeline for: (a) private leaderboard release, and (b) notebook submission deadline?

A specified deadline (e.g., "notebooks due 3 days after submission close") would ensure fairness and compliance, consistent with standard Kaggle and ML competition practices.

**2. Evaluation Components**

How do different components map to final standing: private leaderboard rank, reproducibility, methodology explanation?

Official statements emphasize that final outcomes depend on methodology justification and reproducible code, not solely on leaderboard scores.
"Every submission must include a working notebook": there is no other notebook disclosed by now. 

Without reproduction check, public leaderboard does not reflect reality: not only it's based only on 30% of eval data (small sample), it's not the correct metric per the rules (only MAP@5 vs. average of 3 scores).

We're curious to see the winning solutions and learn from them.

Thank you again for organizing the competition. I think all participants have enjoyed the challenge would appreciate some clarification. Of course I might misunderstand some rules, I'll be happy to hear your thoughts.

Side-note: why reproducible notebook is the standard of evaluation

Just in case some participants are curious about this.

Fact: most LLMs competitions, including the other ones currently held at ICAIF'25 (e.g. [finddr2025](https://finddr2025.github.io/)) have same standards for validating submissions (reproducible code + explanation)

Reason: easy ways to overfit both public and private leaderboard, as the eval-sets (the queries) are known at training time. 

Implication: accurate evaluation framework = re-run code on eval set (or a hidden one). This is why most LLMs competitions are 'code' competition.

So the rules of this competition are in fact well designed and conform to best practices.

Happy to hear your thoughts on this if anyone has any question or idea.

All the bests.


<a id="s017"></a>
## S017

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3306634
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/613060#comment-3306634
- **thread_id:** 613060
- **comment_id:** 3306634
- **author_name:** JIHOONKWON
- **author_role:** unknown
- **created_at:** 2025-10-25T00:44:24.517Z
- **retrieved_at:** 2026-10-16T23:55:55.138739+00:00
- **Archive locator:** `/discussion/10/text`

**What is the timeline for: (a) private leaderboard release, and (b) notebook submission deadline?**

We plan to release the private leaderboard this weekend.

Participants were expected to submit their notebooks by the official competition deadline.

However, since only few teams have uploaded their notebooks so far and the conference will be held on November 15, we have limited time for the review and presentation preparation process.

In this context, it was necessary to first contact the top-performing teams and those who submitted their notebooks early.

We will strongly encourage all invited teams to share their code and methodological details afterward to ensure the reproducibility and integrity of their work.

**How do different components map to final standing: private leaderboard rank, reproducibility, methodology explanation?**

Due to the time constraints, we kindly ask for your understanding that the evaluation of reproducibility and methodology will be primarily based on the materials shared and the explanations provided during the invited presentations and Q&A sessions.

In summary, the final standings will reflect:

- Private Leaderboard Rank -- main performance indicator

- Reproducibility & Methodology -- assessed through shared materials and presentation discussions

We appreciate the community’s understanding and cooperation in this process.


<a id="s018"></a>
## S018

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3307945
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/613060#comment-3307945
- **thread_id:** 613060
- **comment_id:** 3307945
- **parent_comment_id:** 3306634
- **author_name:** DanT
- **author_role:** unknown
- **created_at:** 2025-10-28T07:16:11.313Z
- **retrieved_at:** 2026-10-16T23:55:55.138739+00:00
- **Archive locator:** `/discussion/11/text`

Thank you for clarifying. I appreciate your transparency. 

Although there is a significant shift in evaluation method, I believe that you got to make a difficult decision given the circumstance.

Best wishes for future challenges.


<a id="s019"></a>
## S019

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613060:3307948
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/613060#comment-3307948
- **thread_id:** 613060
- **comment_id:** 3307948
- **parent_comment_id:** 3306634
- **author_name:** DanT
- **author_role:** unknown
- **created_at:** 2025-10-28T07:21:48.630Z
- **retrieved_at:** 2026-10-16T23:55:55.138739+00:00
- **Archive locator:** `/discussion/13/text`

P/S: I'll send you an email for administrative reason


<a id="s020"></a>
## S020

- **source_id:** acm-icaif-25-ai-agentic-retrieval-grand-challenge:thread:613462:opening
- **url:** https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/discussion/613462
- **thread_id:** 613462
- **comment_id:** opening
- **author_name:** JIHOONKWON
- **author_role:** unknown
- **created_at:** 2025-10-27T02:47:24.894Z
- **retrieved_at:** 2026-10-16T23:55:40.925759+00:00
- **Archive locator:** `/discussion/15/text`

Competition Wrap-Up Announcement

🏆 Competition Wrap-Up Announcement

We’re delighted to announce that our competition has successfully concluded with remarkable participation and engagement across the community!

- **155 Entrants**

- **75 Participants**

- **50 Teams**

- **763 Submissions**

Your enthusiasm, creativity, and dedication have made this challenge one of the most active and successful events we’ve hosted to date.  

We sincerely appreciate your passion and effort throughout the competition.  

Due to the overwhelming interest and volume of inquiries, we apologize if we couldn’t respond to every message in time — thank you for your understanding and patience.

📊 Private Leaderboard Release

We **release the private leaderboard **.

Our intention was for participants to **complete their notebook submissions by the official deadline**.  

However, since only a few teams have uploaded their notebooks so far — and with the upcoming **conference on November 15**, we have limited time to complete the review and presentation preparation process.

Given this situation, we first contacted:

- **Top-performing teams** based on the public leaderboard  

- **Teams that submitted their notebooks early**

We will **strongly encourage all invited teams** to share their code and methodological details afterward to ensure the **reproducibility and integrity** of their work.

Due to time constraints, the **reproducibility and methodology evaluation** will primarily be based on the **materials shared** and the **presentations/Q&A sessions** of the invited teams.  

We kindly ask for your understanding of this approach.

💬 Methodology & Feedback Sharing

While the competition itself concludes, the collaboration and learning continue.  

Anyone who wishes to **share their methodology** is warmly encouraged to post it on the **Discussion Tab** or **Code Tab**.  

If you have any **feedback or suggestions regarding the dataset**, please feel free to:

- Post on the **Discussion Tab** of the competition page, or  

- Email us directly at **support [at] linqalpha [dot] com**

Your insights are invaluable for improving future datasets and competitions.

Thank you once again for making this competition such a success.  

We look forward to celebrating the results together and seeing many of you at the **conference on November 15**!

