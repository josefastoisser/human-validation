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
- [S008: cyrillic-morphological-induction-grand-challenge:thread:742791:opening](#s008)
- [S009: cyrillic-morphological-induction-grand-challenge:thread:742791:3527914](#s009)
- [S010: cyrillic-morphological-induction-grand-challenge:thread:743893:opening](#s010)

<a id="s001"></a>
## S001

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/data-description
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/0/text`

## Files

* **train.csv** - labeled training examples
* **dev.csv** - additional labeled development examples
* **wug_seeds.csv** - limited labeled seed examples
* **test_features.csv** - test examples for which `form_vvz` must be predicted
* **sample_submission.csv** - a sample submission file in the correct format

## Columns

* `id` - unique row identifier
* `lemma_ru` - Russian source lemma
* `pos` - part of speech
* `feats` - grammatical feature bundle
* `dialect` - target dialect
* `lemma_frequency` - frequency value associated with the source lemma
* `yat_flag` - binary lexical feature
* `form_vvz` - target form in the synthetic language; provided only in labeled data

`wug_seeds.csv` contains a subset of the above columns and provides labeled seed examples for selected lemmas.


<a id="s002"></a>
## S002

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/Description
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/1/text`

Most NLP tasks are built around languages with existing dictionaries, corpora, and years of linguistic research. In this competition, the target language is synthetic and was created for the challenge
Your task is to predict the correct target-language form for each test example using the provided Russian lemma, grammatical information, dialect label, and other features. Labeled training and development data are provided to help you learn the relationship between the source information and the target forms.

This competition is designed to test how well a system can learn and generalize within an unfamiliar linguistic setting.



<a id="s003"></a>
## S003

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/Evaluation
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/2/text`

Submissions are evaluated using a weighted combination of Exact Match and Character Error Rate (CER):

$$
\text{Score} = 0.9 \times \text{Weighted Exact Match} + 0.1 \times (1 - \text{Weighted CER})
$$


## Submission File

For each `id` in the test set, predict the corresponding `form_vvz`. The file should contain a header and have the following format:

    id,form_vvz
    1,а
    2,а
    3,а
    etc.

See `sample_submission.csv` for the required format.


<a id="s004"></a>
## S004

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/rules
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/3/text`

## ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**[See Section 3.18 for defined terms](rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

Cyrillic Morphological Induction Grand Challenge 2026

2. COMPETITION SPONSOR

[TBD]

3. COMPETITION SPONSOR ADDRESS

[TBD]

4. COMPETITION WEBSITE

https://www.kaggle.com/competitions/cyrillic-morphological-induction-2026

5. TOTAL PRIZES AVAILABLE: $200

First Prize: $200

No Second or Third Prize.

6. WINNER LICENSE TYPE

Non-Exclusive

7. DATA ACCESS AND USE

Competition Use and Commercial.

The Competition Data is subject to the Creative Commons Attribution-ShareAlike 3.0 license.

### 2. COMPETITION-SPECIFIC RULES

In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

#### 1. TEAM LIMITS

a. The maximum Team size is two (2).

b. Team mergers are allowed and can be performed by the Team leader. The Team Merger Deadline is September 18, 2026 at 11:59 PM UTC. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline.

#### 2. SUBMISSION LIMITS

a. You may submit a maximum of three (5) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

#### 3. COMPETITION TIMELINE

a. Competition Timeline dates, including the Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, are reflected on the competition’s Overview > Timeline page.

#### 4. COMPETITION DATA

a. Data Access and Use.

The Competition Data may be used for participating in the Competition, academic research, education, and other commercial or non-commercial purposes subject to the applicable dataset license.

The Competition Data is also subject to the Creative Commons Attribution-ShareAlike 3.0 license.

b. Data Security.

Participants must comply with the applicable Competition Rules and dataset license.

#### 5. WINNER LICENSE

a. Under Section 2.8 (Winner’s Obligations) of the General Rules below, the Competition winner grants the Competition Sponsor the Non-Exclusive license specified by Kaggle.

b. The winner may be required to provide a detailed description of how the winning Submission was generated, together with sufficient code and documentation to reproduce the result.

Winner verification materials may be provided privately to the Competition Sponsor. Public release of the winning solution, code, or methodology is not required.

#### 6. EXTERNAL DATA AND TOOLS

a. Publicly available External Data may be used to develop and test Submissions provided that it is reasonably accessible to Participants.

b. External models, pretrained models, LLMs, and other tools may be used provided that they satisfy Kaggle’s Reasonableness Standard.

c. Automated Machine Learning Tools may be used in accordance with Kaggle’s standard Competition Rules.

d. Prize winners must disclose any External Data, pretrained models, LLMs, or other external resources materially used to produce the winning Submission.

#### 7. ELIGIBILITY

a. Standard Kaggle eligibility requirements apply.

#### 8. WINNER’S OBLIGATIONS

a. As a condition of receiving the Prize, the winning Team must privately provide the Competition Sponsor with sufficient code, documentation, and computational environment information to reproduce the winning Submission.

b. This should include relevant training and inference code, required dependencies, and disclosure of external data, models, or tools materially used.

c. Public disclosure of the winning solution is not required.

#### 9. GOVERNING LAW

a. Unless otherwise provided in the Competition-Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.


<a id="s005"></a>
## S005

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/abstract
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/4/text`

The goal of this competition is to predict inflected forms in a synthetic Cyrillic language from Russian lemmas, grammatical information, and provided examples. Can you learn an unfamiliar morphological system well enough to generalize to forms you have never seen before?


<a id="s006"></a>
## S006

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:5:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/Prizes
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/5/text`

Total Prizes Available: $200
- **1st Place** - $200
- **2nd Place** - None
- **3rd Place** - None


<a id="s007"></a>
## S007

- **source_id:** cyrillic-morphological-induction-grand-challenge:page:6:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/overview/foundational-rules
- **retrieved_at:** 2026-10-08T20:09:49.410168+00:00
- **Archive locator:** `/task_documents/6/text`

The following Kaggle Competition Foundational Rules (“ Foundational Rules ”) apply to every competition regardless of whether the Sponsor creates competition-specific rules. Any competition-specific rules provided by the Sponsor are in addition to these rules, and in the case of any conflict or inconsistency, these Foundational Rules control and nullify contrary competition-specific rules.
###GENERAL COMPETITION RULES - BINDING AGREEMENT
####1. ELIGIBILITY
a. To be eligible to enter the Competition, you must be:

1. a registered account holder at Kaggle.com; 

2. the older of 18 years old or the age of majority in your jurisdiction of residence (unless otherwise agreed to by Competition Sponsor and appropriate parental/guardian consents have been obtained by Competition Sponsor); 

3. not a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, or North Korea; and

4. not a person or representative of an entity under U.S. export controls or sanctions (see: [https://www.treasury.gov/resourcecenter/sanctions/Programs/Pages/Programs.aspx][1]).

b. Competitions are open to residents of the United States and worldwide, except that if you are a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, North Korea, or are subject to U.S. export controls or sanctions, you may not enter the Competition. Other local rules and regulations may apply to you, so please check your local laws to ensure that you are eligible to participate in skills-based competitions. The Competition Host reserves the right to forego or award alternative Prizes where needed to comply with local laws. If a winner is located in a country where prizes cannot be awarded, then they are not eligible to receive a prize.

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

- **source_id:** cyrillic-morphological-induction-grand-challenge:thread:742791:opening
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/discussion/742791
- **thread_id:** 742791
- **comment_id:** opening
- **author_name:** Mario Nicolae
- **author_role:** unknown
- **created_at:** 2026-09-23T13:40:54.767Z
- **retrieved_at:** 2026-10-08T20:10:04.596852+00:00
- **Archive locator:** `/discussion/0/text`

Score Evaluation

Hi, thanks for the competition. The evaluation page says the score is 0.9 × weighted exact match + 0.1 × (1 − weighted CER). Could you clarify how the row weights are defined (e.g. by lemma category, dialect, or frequency), and whether the public/private split is a random sample of rows or grouped by lemma? It would help everyone validate locally. Thanks!


<a id="s009"></a>
## S009

- **source_id:** cyrillic-morphological-induction-grand-challenge:thread:742791:3527914
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/discussion/742791#comment-3527914
- **thread_id:** 742791
- **comment_id:** 3527914
- **author_name:** sazoooon
- **author_role:** unknown
- **created_at:** 2026-09-25T01:28:16.333Z
- **retrieved_at:** 2026-10-08T20:10:04.596852+00:00
- **Archive locator:** `/discussion/1/text`

Hi Mario, thanks for your question!

The evaluation uses four predefined test strata with fixed row weights of 1, 2, 3 and 4, based on the type of generalization being evaluated. Weights are not determined directly by lemma frequency. Both Exact Match and CER use the same weighting scheme.

The public/private split is randomized at the row level and is not grouped by lemma.


<a id="s010"></a>
## S010

- **source_id:** cyrillic-morphological-induction-grand-challenge:thread:743893:opening
- **url:** https://www.kaggle.com/competitions/cyrillic-morphological-induction-grand-challenge/discussion/743893
- **thread_id:** 743893
- **comment_id:** opening
- **author_name:** Md. Hamid Hosen
- **author_role:** unknown
- **created_at:** 2026-09-27T15:25:51.650Z
- **retrieved_at:** 2026-10-08T20:09:55.259542+00:00
- **Archive locator:** `/discussion/2/text`

14th Place Solution: Char Transformers + Explicit Stress-Paradigm Inference

**Team Hack2Publish** (hosen42, esfersami50)

Results

Private LB
Public LB

**Final A:** `var_complete_poe` (selected)
**0.67529**
0.68003

**Final B:** `sub_final_v4` (selected)
0.67500
0.67968

**Position**
**14th of 66**
13th of 66*

* The public leaderboard shows our best public score across all submissions, 0.68648. That score came from a leak-based submission made before the host's ruling (section 13). It was not selected. Both final submissions are clean, and the private score of 0.67529 is Final A's.

TL;DR

- **Generation.** Five character-level transformer seq2seq models generate beam candidates. Each model sees the lemma, the target tags and the other known forms of the same lemma.

- **The key finding.** Stress is not random per cell: each lemma follows one hidden stress paradigm. An explicit paradigm model turns a lemma's observed forms into a prior over the stress class of the requested cell.

- **Selection.** We decide the stress class first, from neural class mass × paradigm prior, jointly across the dialect rows of a cell. Only then do we pick the spelling inside that class.

- **Smaller gains.** Segment-specific decision rules, a length prior, class-conditioned local models pooled inside the chosen class, noise-cleaned context and three post-fixes.

- **Validation.** Every change that improved our lemma-grouped holdout also improved the private score. The private score rose monotonically from 0.65085 to 0.67529 across our pipeline versions.

- **Where the score is lost.** Almost all remaining error is the stress of new lemmas, where a single seed form carries little information.

1. Task and data

The task is to generate an inflected form of a synthetic Cyrillic language (`form_vvz`) from a Russian lemma, part of speech, grammatical features, dialect (SEV, POM, KAM), lemma frequency and a yat flag.

File
Rows
Role

`train.csv`
300,000
labelled

`dev.csv`
20,000
labelled

`wug_seeds.csv`
4,800
one labelled form per new lemma

`test_features.csv`
60,000
to predict

What we learned about the language:

- **Stress** is a combining acute accent (U+0301) on exactly one vowel. An exact match needs both the spelling and the stress.

- **Regular sound rules:**

- akanye (unstressed о → а);

- SEV reverses pleophony (оро → ра, ере → рѣ, оло → ла);

- KAM keeps ськ and writes и for unstressed е and in LOC -и;

- SEV and POM turn ск into сьц;

- `yat_flag` marks ѣ stems.

- **Noise:** about 1.7% of labelled rows are random-word substitutions, where the form belongs to a different lemma, plus some character typos.

The test set mixes four regimes, which we derived from the files:

Regime
Evidence available
Test rows

Transfer
same lemma and cell seen in another dialect
18,000

Completion
other cells of the lemma are known
15,000

Wug
one SEV seed form (N;ACC;SG or V;PRS;3;SG) for each of 4,800 new noun/verb lemmas
18,260

Unseen
nothing (1,200 new adjective lemmas)
8,740

KAM is over-represented in the test set, about a third of the wug and unseen rows.

2. Decoding the metric with probe submissions

The Evaluation page gives `Score = 0.9 × WeightedEM + 0.1 × (1 − WeightedCER)`, but not the row weights. On day one we spent four submissions on probes:

- an all-"а" file (0.00755), which isolates the CER part;

- files keeping only one subset of the predictions: SEV transfer (0.05868), POM transfer (0.06001) and high-frequency rows (0.00098).

Together they fit segment weights of about **1 / 2 / 3 / 4** for transfer / completion / wug / unseen. Wug and unseen therefore carry about 65% of the score.

Later, a wug-only probe (0.22776) and an unseen-only probe (0.10940) of the same pipeline put test exact match at about 0.54 on wug and 0.38 on unseen. That told us precisely where the missing points were.

3. Validation

The holdout mimics the test:

- 500 wug-like noun/verb lemmas, keeping only the SEV seed cell;

- 250 unseen adjective lemmas, keeping nothing;

- dev rows split into transfer and completion by whether (lemma, feats) is seen in train;

- scoring with the test's segment weights and row counts.

Every change was validated there before we submitted it. Final A scores 0.65981 on this holdout, by segment:

Transfer
Completion
Wug
Unseen

0.960
0.955
0.496
0.403

Two caveats:

- The holdout is harsher than the test on wug, because train rows contain substitution noise while the test wug seeds are clean.

- The same holdout informed many decisions, so it overstates small gains.

4. The key insight: hidden stress paradigms

Stress looked random per cell at first. But across full training paradigms, each lemma follows one of a limited set of recurring stress patterns over its cells. Given the other cells of a lemma, a held-out cell's stress class is predictable about 91–97% of the time. From a single wug seed it is about 48%, and for an unseen lemma only the population prior (about 40%) remains.

We represent stress in two ways:

- **cur5:** initial stress, or distance from the last vowel (5 classes).

- **3way:** initial, stem-final or ending stress relative to the lemma stem. The stem boundary is found with a stem-vowel rule corrected for SEV pleophony. Masks handle short stems, where two classes coincide. This fit the data better than cur5 and gave the largest single gain: holdout +0.013, public +0.0096, private +0.0080.

The paradigm model is k-medoids over the stress-class vectors of training lemmas (cur5: K=600 × 6 seeds; 3way: K=300 × 3 seeds). Given a lemma's observed cells, the posterior over medoids yields `P(class | observed forms)` for the requested cell.

5. Candidate generation

- **Model:** a character transformer encoder-decoder.

- **Encoder input:** target tags (dialect, feature parts, yat, log-frequency bucket), the lemma characters, and up to 6 (v1) or 12 (v3) other known forms of the same lemma. Each context form carries its own tags, and a marker flags a same-feature form from another dialect.

- **Context sampling during training** mimics the four regimes: other dialects of the same cell, missing cells, seed only, or nothing.

- **v1:** d=320, 5 layers, 14.6M parameters, 3 seeds, beam 5.

- **v3:** d=384, 6 layers, about 25M parameters, 2 seeds, beam 8.

- Both were trained on Kaggle GPUs, a few hours per run.

- **Ensembling:** beam probabilities are normalized per model, averaged over the five models, and identical strings are merged into one candidate mass.

On its own the ensemble reaches only about 0.50 dev exact match: it never learned to infer the stress paradigm, and a bigger model did not change that. But the gold form is in the beam 97–98% of the time in every regime. The remaining work was selection.

6. Stress decision and spelling selection

For each (lemma, feats) cell, the rows of all dialects are decided together, since the stress class is shared across dialects about 93% of the time:

`class = argmax_c [ Σ_rows log M_row(c) + λ · log P(c | observed forms) ]
`

`M_row(c)` is the candidate mass of stress class `c`. Prior weights were chosen on the holdout; for new lemmas λ=2 beat 1, 4 and 0.5 with cur5.

Regime
Representation
λ
Decision

Transfer
cur5, K=600 × 6
2
joint across dialects

Completion
3way, candidate mass reweighted by the cur5 prior (product of experts)
5
joint

Wug
3way
5
joint

Unseen
cur5
2
per row

Inside the chosen class, the spelling is:

`y = argmax_y [ log M(y) + 0.6 · log P(len(y) − len(lemma) | POS, feats, dialect) ]
`

7. Local class-conditioned models

We also trained small character transformers (5–10M parameters) that take the stress class as an input token. They ran locally on an Apple-silicon GPU (MPS), at about 13 minutes per epoch.

- **Pooling:** for each row we decode them with the chosen class token and pool their beams with the main candidates of that class, at weight 0.5.

- **Final A** uses three local models (seeds 0, 1 and 3). **Final B** adds two more (seeds 4 and 5, with a longer context and a different size).

- **Pooling at the candidate level helped;** merging at the level of final answers hurt:

Holdout
Public
Private

Candidate-level pooling
+0.0077
+0.0009
+0.0020

Answer-level merges
—
0.66562 and 0.66513 (vs 0.66653)
0.66099 and 0.66180 (vs 0.66205)

8. Noise-cleaned context

A detector flags substitution noise in train and dev: rows whose form is unrelated to both its lemma and its sibling forms. Flagged rows are dropped from the paradigm context, and the detector uses released labelled data only. This added +0.001 on the holdout.

9. Post-fixes

We added three narrow rules for residual error types found on the holdout:

- the candidate must keep the lemma's consonant skeleton;

- an adjective's long form must equal its short form plus the ending;

- geminates must be kept.

On the holdout they fixed 17 transfer, 17 completion, 7 wug and 40 unseen rows, and broke none. On the test they changed only 76 rows.

10. Score progression: holdout, public and private

Version
Holdout
Public
Private

Copy the same cell from another dialect (baseline)
—
0.21939
0.22053

v1 ensemble + paradigm re-ranking
—
0.65492
0.65085

Joint stress decision per (lemma, feats), K=300 × 3
—
0.66360
0.66135

+ v3 models (5-model ensemble)
—
0.66653
0.66205

Prior weight 2 for new lemmas
0.63898
0.66783
0.66315

Candidate-level pooling with 2 local models
—
0.66871
0.66511

3way representation for completion and wug, per-row unseen, length prior
0.65362
0.67826
0.67308

Noise-cleaned context + 3 local models
—
0.67904
0.67415

Post-fixes
—
0.67963
0.67455

**Product of experts for completion (Final A)**
**0.65981**
**0.68003**
**0.67529**

5 local models in the pool (Final B)
—
0.67968
0.67500

What the private leaderboard showed:

- **Every step improved private.** The private score never went down across these versions, from 0.65085 to 0.67529.

- **Private tracked public closely.** It was 0.002–0.005 below public for every clean version, so we lost almost nothing in the shake-up. Four teams above us dropped 0.009–0.016.

- **Final A beat Final B on both boards.** The two finals differ on only 93 of the 60,000 rows, so choosing B added very little hedge.

11. What did not work

- **Predicting the paradigm from surface data:** the lemma string, character n-grams, frequency rank, row ids, hashes (md5, sha, crc32 mod K) and yat gave no signal.

- **Real Russian stress** (StressRNN dictionary + pymorphy3) agreed with this language's stress only at chance level.

- **Reconstructing a seeded random assignment** of paradigms (numpy/Python/PCG generators, several orderings, string-seeded RNGs) found nothing significant.

- **Better class models for wug:** EM latent-class mixtures, other K values, nonparametric Bayes over full patterns and a dedicated stress classifier. None beat the paradigm prior plus neural evidence.

- **Joint inference and consistency constraints:** joint inference across a lemma's cells from neural class masses, dialect-consistency decoding and stem-prefix consensus were neutral or slightly negative.

- **Product of experts for wug and unseen** was worse: wug 0.492 → 0.485, unseen 0.394 → 0.383. It only helps completion.

- **Rescoring the whole candidate pool** with the neural models (teacher forcing) gained nothing.

- **Bigger models:** a bigger local model spelled no better, and a bigger Kaggle model alone was no better than v1.

- **Tuning λ against the public board:** variants changed 800–900 rows, but the true effect was far below public-LB noise. We kept the holdout-optimal values.

12. Where the score is lost

With the right stress class, holdout exact match is 0.988 / 0.990 / 0.977 / 0.964 for transfer / completion / wug / unseen.

Stress-class accuracy is:

- about 0.97 on training lemmas, close to the label-noise level;

- about 0.50 for wug;

- about 0.42 for unseen.

Seed-only class accuracy for wug stops around 0.47–0.49 however it is modelled. Unseen adjective stress looks close to uniform over the three 3way classes. Most of the remaining gap is information the data does not contain, not a modelling gap.

13. The copied-forms issue

While cleaning the noise we found that some substitution-noise rows in train and dev are exact copies of hidden test forms, and we reported it publicly on the forum. Before the host ruled, we tested it in three submissions; the best scored 0.68648 public and 0.68233 private. The host then ruled that deliberately exploiting these copies is not permitted, and we excluded all of that work. Neither final selection uses it: both were built before any leak-related code existed. The 14th place above is the result of the clean pipeline.

14. Lessons

- **Separate generating candidates from deciding the stress.** The network alone never learned paradigm inference; an explicit model did.

- **Spend a few early submissions on probes** to decode the metric. Knowing that wug and unseen carry about 65% of the score set our priorities for the whole week.

- **Build validation that mirrors each test regime** and trust it over the public board. Our holdout-validated steps all carried over to private, while public differences below about 0.003 were noise.

