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
- [S007: barista-bench:thread:670740:opening](#s007)
- [S008: barista-bench:thread:670740:3398882](#s008)
- [S009: barista-bench:thread:670740:3399219](#s009)
- [S010: barista-bench:thread:670955:opening](#s010)
- [S011: barista-bench:thread:673699:opening](#s011)
- [S012: barista-bench:thread:673699:3413838](#s012)
- [S013: barista-bench:thread:674356:opening](#s013)
- [S014: barista-bench:thread:674356:3408421](#s014)
- [S015: barista-bench:thread:679759:opening](#s015)

<a id="s001"></a>
## S001

- **source_id:** barista-bench:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/data-description
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
- **Archive locator:** `/task_documents/0/text`

# **The Dataset (V3)**

We have generated 4,000 complex point-of-sale scenarios designed to test Agentic State Tracking, Arithmetic, and Long-Context Reasoning.

train.csv: 500 labeled examples (Order + Correct JSON) containing the new list-based schema. Use this for few-shot prompting or fine-tuning.

test.csv: 3,500 unlabelled orders. This is the target for the leaderboard.

menu.md: The official Rulebook. It contains base prices, size upcharges, and modifier rules. You must provide this to your model to solve the arithmetic.

# **Schema (Critical Update)**

Orders now contain multiple distinct items. Your model must output a valid JSON Object containing a list of items and the grand total.

**Sample JSON format**
`{
  "items": [
    {
      "name": "Latte",
      "size": "Grande",
      "quantity": 2,
      "modifiers": ["Oat Milk", "Vanilla Syrup"]
    },
    {
      "name": "Blueberry Muffin",
      "size": null,
      "quantity": 1,
      "modifiers": []
    }
  ],
  "total_price": 18.25
}`

**Level 1 (Multi-Item Aggregation):**
Input: "I'll take two Lattes and a Bagel."
Challenge: Correctly identifying distinct items and their quantities.

**Level 2 (The Arithmetic Test):**
Input: "Give me three Venti Mochas with Oat Milk."
Challenge: Calculating 3 * (Base + Size + Oat Cost) correctly.

**Level 3 (Nightmare Mode):**
Input: "Two Lattes... actually make that three. Add vanilla... wait, no vanilla. And a Croissant... actually scratch the Croissant."
Challenge: State Tracking. The model must handle corrections (changing 2 to 3), cancellations (removing the Croissant entirely), and logic negations (removing the Vanilla) before calculating the final price.


<a id="s002"></a>
## S002

- **source_id:** barista-bench:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/Description
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
- **Archive locator:** `/task_documents/1/text`

# **🧠 Why This Matters (The "Vertical AI" Problem)**

Most "Reasoning" benchmarks focus on math problems or riddles. BaristaBench focuses on Business Logic:

*State Tracking*: If the user says "Add Vanilla," then later says "Actually, make it Caramel," the model must update the state (remove Vanilla, add Caramel).

*Constraint Satisfaction*: Rules must be followed. (e.g., Milk substitutions cost money, but removing foam is free. Substitutions replace the default ingredient, additions stack.)

*Strict Arithmetic*: There is no "close enough." If the price is off by $0.01, the answer is wrong.

If a small model (7B parameters) can solve this efficiently, it proves it is ready for real-world "Vertical AI" tasks like booking agents, CRM updates, and financial data entry.


<a id="s003"></a>
## S003

- **source_id:** barista-bench:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/Evaluation
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
- **Archive locator:** `/task_documents/2/text`

# **📏 Evaluation**

This competition uses a Custom Exact-Match Metric.

Your submission will be scored based on the Accuracy of your JSON output. To get a point for a row, your JSON must match the ground truth perfectly on:

✅ Total Price (Exact match required)

✅ Drink Name & Size

✅ List of Modifiers (Order does not matter, but content does)

Note: Hallucinated keys or invalid JSON formats will result in a score of 0 for that row.

# **🚀 How to Participate**

Read the Menu: Check menu.md to understand the pricing logic.

Start a Notebook: Load the data and a base model (like Llama-3 or Gemma).

Prompt Engineering: Write a System Prompt that teaches the model how to think step-by-step.

Submit: Generate your submission.csv and climb the leaderboard!

Can you beat models like GPT-5 using a smaller, more efficient model? Good luck!

# **🚫 A Note on Manual Labeling & Data Leakage**

Manual Labeling: Since the test set is 3,500 rows, it is theoretically possible for a human to manually label the data. **Please don't.** This is a benchmark for Artificial Intelligence. If you manually label the data, you have proved nothing other than that you have free time.

Data Contamination: Do not include the test set questions in your training data (fine-tuning). This is considered data leakage.

Verification: Top solutions may be asked to share their inference code to verify the results were generated by a model.


<a id="s004"></a>
## S004

- **source_id:** barista-bench:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/rules
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
- **Archive locator:** `/task_documents/3/text`

ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.
See Section 3.18 for defined terms
The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.
You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.
1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

 BaristaBench: The Reasoning Challenge
2. COMPETITION SPONSOR

 BaristaBench Community Host
3. COMPETITION SPONSOR ADDRESS

 N/A (Online Community Competition)
4. COMPETITION WEBSITE

 https://www.kaggle.com/competitions/barista-bench
5. TOTAL PRIZES AVAILABLE: $0 (Knowledge and Community Recognition)

First Prize: Leaderboard Position & Community Recognition
Second Prize: Leaderboard Position & Community Recognition
Third Prize: Leaderboard Position & Community Recognition
6. WINNER LICENSE TYPE

 Open Source
7. DATA ACCESS AND USE

 Competition Use, Academic Research, and Commercial Use
2. COMPETITION-SPECIFIC RULES
In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:
1. TEAM LIMITS
a. The maximum Team size is five (5).

b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the competition has been running.

2. SUBMISSION LIMITS
a. You may submit a maximum of ten (10) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

3. COMPETITION TIMELINE
a. Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s Overview > Timeline page.

4. COMPETITION DATA
a. Data Access and Use. 

Competition Use and Commercial are checked: You may access and use the Competition Data for any purpose, whether commercial or non-commercial, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

b. Data Security. 

You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.

5. WINNER LICENSE
a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

Open Source: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org] (http://www.opensource.org)) that in no event limits commercial use of such code or model containing or depending on such code. 

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.
6. EXTERNAL DATA AND TOOLS
a. You may use data other than the Competition Data (“External Data”) to develop and test your Submissions. However, you will ensure the External Data is either publicly available and equally accessible to use by all Participants of the Competition for purposes of the competition at no cost to the other Participants, or satisfies the Reasonableness criteria as outlined in Section 2.6.b below. The ability to use External Data under this Section does not limit your other obligations under these Competition Rules, including but not limited to Section 2.8 (Winners Obligations). 

b. The use of external data and models is acceptable unless specifically prohibited by the Host. Because of the potential costs or restrictions (e.g., “geo restrictions”) associated with obtaining rights to use external data or certain software and associated tools, their use must be “reasonably accessible to all” and of “minimal cost”. Also, regardless of the cost challenges as they might affect all Participants during the course of the competition, the costs of potentially procuring a license for software used to generate a Submission, must also be considered. The Host will employ an assessment of whether or not the following criteria can exclude the use of the particular LLM, data set(s), or tool(s):

Are Participants being excluded from a competition because of the "excessive" costs for access to certain LLMs, external data, or tools that might be used by other Participants. The Host will assess the excessive cost concern by applying a “Reasonableness” standard (the “Reasonableness Standard”). The Reasonableness Standard will be determined and applied by the Host in light of things like cost thresholds and accessibility.

By way of example only, a small subscription charge to use additional elements of a large language model such as Gemini Advanced are acceptable if meeting the Reasonableness Standard of Sec. 8.2. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

c. Automated Machine Learning Tools (“AMLT”)

Individual Participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google toML, H2O Driverless AI, etc.) to create a Submission, provided that the Participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules. 

7. ELIGIBILITY
a. Unless otherwise stated in the Competition-Specific Rules above or prohibited by internal policies of the Competition Entities, employees, interns, contractors, officers and directors of Competition Entities may enter and participate in the Competition, but are not eligible to win any Prizes. "Competition Entities" means the Competition Sponsor, Kaggle Inc., and their respective parent companies, subsidiaries and affiliates. If you are such a Participant from a Competition Entity, you are subject to all applicable internal policies of your employer with respect to your participation.

8. WINNER’S OBLIGATIONS
a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:

Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code should follow [these documentation guidelines][5], must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. For avoidance of doubt, delivered software code should include training code, inference code, and a description of the required computational environment.
a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).” 

b. Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules,

Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;

Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).

9. GOVERNING LAW
a. Unless otherwise provided in the Competition Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.


<a id="s005"></a>
## S005

- **source_id:** barista-bench:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/abstract
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
- **Archive locator:** `/task_documents/4/text`

#**☕ BaristaBench: The Agentic State-Tracking Challenge**

"I'll have a Venti Latte, actually make that Decaf, with Oat Milk... oh, and no foam."

We all know LLMs can write poetry and pass the Bar Exam. But can they work the morning rush at a coffee shop without losing money?

BaristaBench is a new community benchmark designed to test Agentic State Tracking, Arithmetic, and Constraint Satisfaction. While the scenario is fun, the problem is technical: can a model maintain a mental "state" of an order, modify it based on messy natural language updates, and output a strictly formatted JSON result with 100% arithmetic precision?

## **🎯 The Goal**
Your task is to build an AI Agent (or prompt-engineer an LLM) that acts as a Point-of-Sale (POS) system.

**🏆 The "Efficiency" Challenge**
While we welcome submissions from massive models (GPT-4, Claude 3.5, Llama-3-70B), the real prestige in this benchmark is doing more with less.

We encourage participants to tag their submissions/notebooks after the competition ends in the Discussion/Code board with:

**🛡️ < 10B Params**: Best score using a model runnable on consumer hardware (e.g., Llama-3-8B, Qwen-7B, Mistral).

**⚡ Open Weight**: Best score using fully open-source models.

**🦖 Godzilla Mode**: Best score regardless of compute/cost.

You will be given a customer's spoken order. These orders are not clean—customers might change their minds, ask for modifiers, cancel items, or speak in a non-linear way.


<a id="s006"></a>
## S006

- **source_id:** barista-bench:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/barista-bench/overview/foundational-rules
- **retrieved_at:** 2026-10-13T13:41:08.669453+00:00
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

- **source_id:** barista-bench:thread:670740:opening
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/670740
- **thread_id:** 670740
- **comment_id:** opening
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-01-29T13:19:38.210Z
- **retrieved_at:** 2026-10-13T13:41:52.972329+00:00
- **Archive locator:** `/discussion/0/text`

🚨 DATASET UPDATE (V2): Multi-Item Mode & New JSON Schema

Hi everyone,
Thank you for your patience while we investigated the logic errors in the previous dataset version. We have deployed the fixes for the negation logic, and we decided to take this opportunity to significantly upgrade the difficulty of the benchmark to better simulate real-world agentic tasks.

Here is what has changed:

- 📦 From Single Drink to Full Orders
The AI is no longer just making one cup of coffee. Orders now simulate full receipts involving multiple distinct items with quantities.
Old: "I'll have a Latte with Oat Milk."
New: "Give me two Grande Lattes with Oat Milk, and start me off with a Blueberry Muffin."

- 📝 Major Schema Change
The output JSON format has changed to support lists. You must update your parsers/prompts, or you will score 0.
New example JSON Structure:
{
"items": [
{
  "name": "Latte",
  "size": "Grande",
  "quantity": 2,
  "modifiers": ["Oat Milk"]
},
{
  "name": "Blueberry Muffin",
  "size": null,
  "quantity": 1,
  "modifiers": []
}
],
"total_price": 14.35
}

Note: The items list order does not matter for scoring, but the content of each item must be exact.

- 🧮 Increased Arithmetic Difficulty
The math requirement is now significantly harder. Your model must perform:
Per-Item Logic: (Base Price + Size Upcharge + Modifier Costs)
Quantity Logic: Multiply that sum by the quantity (e.g., "Two Lattes").
Grand Total: Sum the total of all distinct line items.

- 🚀 Action Items for Participants
Re-download Data: The train.csv, test.csv, and sample_submission.csv have all been updated.
Update Prompts: You need to teach your model to aggregate multiple items and output the new JSON list structure.

We believe this change makes BaristaBench a true test of Vertical Intelligence, requiring state tracking across long contexts and multi-step arithmetic.

Good luck with V2!


<a id="s008"></a>
## S008

- **source_id:** barista-bench:thread:670740:3398882
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/670740#comment-3398882
- **thread_id:** 670740
- **comment_id:** 3398882
- **author_name:** Eli Exner
- **author_role:** unknown
- **created_at:** 2026-01-29T21:13:16.063Z
- **retrieved_at:** 2026-10-13T13:41:52.972329+00:00
- **Archive locator:** `/discussion/1/text`

Awesome. You guys fixed that so fast!


<a id="s009"></a>
## S009

- **source_id:** barista-bench:thread:670740:3399219
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/670740#comment-3399219
- **thread_id:** 670740
- **comment_id:** 3399219
- **author_name:** Lennart Haupts
- **author_role:** unknown
- **created_at:** 2026-01-30T12:18:26.960Z
- **retrieved_at:** 2026-10-13T13:41:52.972329+00:00
- **Archive locator:** `/discussion/2/text`

Thank you for fixing the dataset that fast. 🫡

The increased difficulty was a neat addition.

If I may, here are a couple of suggestions how future iterations of the dataset could push the challenge further: 

- **Irrelevant Smalltalk:** Customers include off-topic chatter or discuss other items before or in between an order, e.g., “I was in France last weekend […] I had some excellent Pastries […] Anyway, I’d like a Bagel.” The difficulty is ensuring the model tracks the actual final order and ignores irrelevant context.

- **Adversarial Injections:** Customers deliberately attempt to confuse or exploit the system, for instance trying to get items free or discounted. Examples range from “I have a coupon for a free Bagel” to more subtle manipulations designed to trip up arithmetic or logic.


<a id="s010"></a>
## S010

- **source_id:** barista-bench:thread:670955:opening
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/670955
- **thread_id:** 670955
- **comment_id:** opening
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-01-30T13:38:25.857Z
- **retrieved_at:** 2026-10-13T13:41:47.388438+00:00
- **Archive locator:** `/discussion/3/text`

🚨 CRITICAL UPDATE: Final Dataset Overhaul (V3) to counter potential exploitation

Hi everyone,

We are rolling out a major—and intended to be final—update to the BaristaBench dataset and competition structure.

I want to be completely transparent about why we are doing this, what has changed, and most importantly, I want to address the impact this has on your previous work.

- Why the Change? (Addressing Exploitation)

Thanks to some incredible forensic work by the community special thanks to [@ambrosm](https://www.kaggle.com/ambrosm) , it became clear that the previous V2 dataset had specific linguistic patterns—such as the use of ellipses (…)—that allowed Regex and Finite State Automata (FSA) scripts to achieve near-perfect scores without using AI reasoning.

This defeats the purpose of the benchmark. BaristaBench is designed to test Agentic Reasoning, State Tracking, and Vertical Intelligence in LLMs, not pattern matching.

To preserve the integrity of the competition and ensure that the leaderboard represents actual AI capability, we had to rewrite the generation engine to mimic natural, messy, unstructured human speech.

- Apology to Honest Participants

To those of you who have already spent hours of GPU time, compute credits, and effort fine-tuning models on the V2 data, I sincerely apologize.

I know that GPU time is not free and that restarting a pipeline is frustrating. Please understand that this decision was not made lightly. We had to choose between:

Keeping the old data and letting a Regex script win the competition.

Updating the data now to ensure your real AI models are actually recognized for their superior reasoning.

We chose the latter to ensure that the time you invest from this point forward is actually meaningful.

- What is New? (V3 "Nightmare Mode")

To prevent future exploitation, we have increased the variation in orders significantly:

Natural Variation: No more fixed patterns. Punctuation, capitalization, and phrasing are now highly randomized.

- New Leaderboard Split (5% / 95%)

You will notice the Leaderboard is now split: 5% Public / 95% Private.

Why?
This is to prevent Leaderboard Probing.

With a large Public test set, it is easy to overfit or guess the answers to improve your score without actually improving the model.

By hiding 95% of the data, we ensure that the final winner is the model that generalizes best to unseen instructions, rather than the model that memorized the test set.

- Moving Forward

This is the final planned update for the dataset structure. The schema and logic you see today are what will be used for the duration of the benchmark.

Thank you for sticking with us, and thank you to the community members (including [@eliexner](https://www.kaggle.com/eliexner) [@lennarthaupts](https://www.kaggle.com/lennarthaupts) and [@ambrosm](https://www.kaggle.com/ambrosm)) who helped stress-test the data. As to some of your suggestions, I am looking into implementing them in a possible future Version 2 of the BaristaBench: The Reasoning Challenge series of community competitions. For now, let’s see who can crack the new BaristaBench customer logic!

Good luck,
PxlPau


<a id="s011"></a>
## S011

- **source_id:** barista-bench:thread:673699:opening
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/673699
- **thread_id:** 673699
- **comment_id:** opening
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-02-16T14:02:48.945Z
- **retrieved_at:** 2026-10-13T13:41:41.920838+00:00
- **Archive locator:** `/discussion/4/text`

🚨 [ACTION REQUIRED] Final Code Verification & Leaderboard Reveal

Hi everyone,

We have observed some incredible performance on the BaristaBench leaderboard, with scores reaching near perfection. To ensure the integrity of the final standings and to confirm that these results are achieved through algorithmic reasoning rather than manual labeling, we are initiating a Code Verification Process.

🛑 Who Must Submit?

All participants who wish to be eligible for the final Private Leaderboard rankings must verify their submission.

If you do not submit your code for verification, your score will be invalidated and removed from the final leaderboard.

📝 What is Required?

You must provide the following two items to me privately:

The Code/Notebook: The exact script or notebook used to generate your best selected submission. We must be able to run this code to reproduce your output file.

A Short Description: A brief explanation (3-5 sentences) of your approach. 

📅 The Deadline

You have until March 2, 2026, at 12:00 AM UTC to submit your verification materials.

Verification Window: Mar 2 – Mar 7.

Final Leaderboard Reveal: Immediately following the end of the verification window.

🔒 How to Share (Privately)

Do NOT post your solution publicly in the code yet. Add me as a viewer in your Kaggle Notebook privately.
Optionally, send me a direct message via my profile to confirm you have shared it.

⚠️ Verification Criteria

Reproducibility: The code must be capable of generating the submission file you uploaded.

No Manual Labeling: Any evidence of manual data entry, hard-coded answers for specific Test IDs, or human-in-the-loop labeling will result in immediate disqualification.

External Data: If you used external data, it must be disclosed in your description.

We are excited to see the innovative methods you have used to crack BaristaBench! Thank you for helping us keep BaristaBench a fair and rigorous benchmark.

Good luck,
PxlPau


<a id="s012"></a>
## S012

- **source_id:** barista-bench:thread:673699:3413838
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/673699#comment-3413838
- **thread_id:** 673699
- **comment_id:** 3413838
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-02-25T10:20:42.877Z
- **retrieved_at:** 2026-10-13T13:41:41.920838+00:00
- **Archive locator:** `/discussion/5/text`

Friendly reminder to please submit your code to me for verification of your scores :)


<a id="s013"></a>
## S013

- **source_id:** barista-bench:thread:674356:opening
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/674356
- **thread_id:** 674356
- **comment_id:** opening
- **author_name:** Francis Ganong
- **author_role:** unknown
- **created_at:** 2026-02-20T01:06:03.363Z
- **retrieved_at:** 2026-10-13T13:41:36.025002+00:00
- **Archive locator:** `/discussion/6/text`

Is scoring sensitive to capitalization?

My system outputs json where the values are sometimes capitalized differently.  Is scoring sensititve to capitalization in the attribute values?
(is the scoring routine available somewhere?)


<a id="s014"></a>
## S014

- **source_id:** barista-bench:thread:674356:3408421
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/674356#comment-3408421
- **thread_id:** 674356
- **comment_id:** 3408421
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-02-20T15:16:47.637Z
- **retrieved_at:** 2026-10-13T13:41:36.025002+00:00
- **Archive locator:** `/discussion/7/text`

Nope. The scoring metric will automatically convert your values to lower case. :D


<a id="s015"></a>
## S015

- **source_id:** barista-bench:thread:679759:opening
- **url:** https://www.kaggle.com/competitions/barista-bench/discussion/679759
- **thread_id:** 679759
- **comment_id:** opening
- **author_name:** PxlPau
- **author_role:** unknown
- **created_at:** 2026-03-03T14:47:22.577Z
- **retrieved_at:** 2026-10-13T13:41:19.468084+00:00
- **Archive locator:** `/discussion/8/text`

☕ FINAL RESULTS OF THE BARISTABENCH CHALLENGE

After reviewing the private code submissions, it is clear that the community did spend a lot of effort trying to process the data and develop innovative solutions to interpret human language orders efficiently and accurately.

As promised, we have applied the 1000-point Verification Bonus to all participants who submitted their methodology. This ensures that the verified, reproducible solutions take their rightful place at the top of the leaderboard.

🏆 The Final Verified Leaderboard

🥇 1    Jerod Harbor    1100.000 NLP Compiler
🥈 2    kakuteki    1099.639    Optimized Batch Inference
🥉 3    Team Ladybug    1098.556    Hybrid LLM + State Machine
🎖️ 4    Jason Karpeles  1095.398    High-Precision Reasoning
🎖️ 5    Can 1092.691    Fine-Tuned Llama-3-8B (Unsloth)
🎖️ 6    ahmed Maalej    1090.436    RAG-Retriever + Llama 3.3 70B
🎖️ 7    Oscar Le    1085.443    Qwen 2.5 7B LoRA + DSL
🎖️ 8    Sujith K    1073.503    Fine-Tuned Qwen + vLLM + Rule Parser
🎖️ 9    Talha Sage  1063.428    Advanced Few-Shot & CoT
🎖️ 10    Reo Neo 1057.984    Two-Stage Agent Workflow
🎖️ 11    Lennart Haupts  1052.902    Gemma-2-9B + Majority Voting

🧠 Methodology Highlights

We saw four distinct methods in the winning solutions:

- The NLP Compiler (Jerod Harbor)

Jerod achieved a perfect 100% accuracy by treating the order text as a formal language. He built a sophisticated Python-based tokenization engine and state resolver. By meticulously mapping every possible linguistic variation to a deterministic pricing engine, he proved that for a closed-logic system, a well-crafted compiler is still the ultimate Boss of accuracy.

- Hybrid Agent (Team Ladybug, Lennart Haupts, Reo Neo)

Most Production-Ready approach.

Ladybug used an LLM to convert speech into a JSON Action Sequence (e.g., ADD_ITEM, REMOVE_MODIFIER), which was then executed by a deterministic state machine.

Lennart Haupts implemented a POS Compiler using Gemma-2-9B with Majority Voting. By generating 4 samples per order and picking the most common result, he neutralized LLM hallucinations.

Reo Neo implemented a highly disciplined Two-Staged Workflow that decoupled intent from execution. His agent first Took the Order (parsing natural language into a structured intermediate state) before moving to Calculate Price (deterministic arithmetic).

- Fine-Tuning (Can, Sujith K, Oscar Le)

Instead of relying on large general models, these participants used LoRA and Unsloth to bake the BaristaBench rules directly into the weights of smaller models like Llama-3-8B and Qwen-7B.

Oscar Le took it a step further by training the model to output a custom DSL (Domain Specific Language), which was then parsed into the final JSON.

- Retriever-Augmented Approach (Ahmed Maalej)

Ahmed used an SBERT/TF-IDF Retriever to find the most similar examples in train.csv before sending them to Llama 3.3 70B. This Dynamic Few-Shot method ensured the model always had the most relevant context for every complex order.

🏁 Final Thoughts

BaristaBench started as a simple test of "Can AI make coffee?" It ended as a collection of ingenious solutions to process human orders efficiently and accurately.

The diversity of solutions shows how the future of AI agents isn't just about bigger models, but about smarter and hopefully smaller (and more efficient) architectures.

Thank you to everyone for your incredible effort, your honesty in sharing code, and for making this one of the most rigorous community benchmarks on Kaggle.

The competition is now closed. The leaderboard is final.

Happy coding (and coffee drinking)!
PxlPau

