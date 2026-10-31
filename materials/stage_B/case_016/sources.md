# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Competition Description](#s002)
- [S003: rules](#s003)
- [S004: abstract](#s004)
- [S005: foundational-rules](#s005)
- [S006: Other Resources](#s006)
- [S007: Evaluation](#s007)
- [S008: Timeline](#s008)
- [S009: CVPR25 and CLEF25 Context](#s009)
- [S010: Citation](#s010)
- [S011: animal-clef-2025:thread:575740:opening](#s011)
- [S012: animal-clef-2025:thread:575740:3190394](#s012)
- [S013: animal-clef-2025:thread:575740:3190890](#s013)
- [S014: animal-clef-2025:thread:575838:opening](#s014)
- [S015: animal-clef-2025:thread:575838:3191104](#s015)
- [S016: animal-clef-2025:thread:575849:opening](#s016)
- [S017: animal-clef-2025:thread:575849:3191048](#s017)
- [S018: animal-clef-2025:thread:575849:3191107](#s018)
- [S019: animal-clef-2025:thread:575849:3191110](#s019)
- [S020: animal-clef-2025:thread:575849:3192882](#s020)
- [S021: animal-clef-2025:thread:575849:3191133](#s021)
- [S022: animal-clef-2025:thread:575849:3191146](#s022)
- [S023: animal-clef-2025:thread:575849:3191767](#s023)
- [S024: animal-clef-2025:thread:578201:opening](#s024)
- [S025: animal-clef-2025:thread:578201:3219173](#s025)
- [S026: animal-clef-2025:thread:578201:3219572](#s026)
- [S027: animal-clef-2025:thread:578201:3217428](#s027)
- [S028: animal-clef-2025:thread:578201:3217786](#s028)
- [S029: animal-clef-2025:thread:578201:3206225](#s029)
- [S030: animal-clef-2025:thread:578201:3206896](#s030)
- [S031: animal-clef-2025:thread:579843:opening](#s031)
- [S032: animal-clef-2025:thread:579843:3206897](#s032)
- [S033: animal-clef-2025:thread:579843:3207748](#s033)
- [S034: animal-clef-2025:thread:579843:3206870](#s034)
- [S035: animal-clef-2025:thread:579843:3207750](#s035)

<a id="s001"></a>
## S001

- **source_id:** animal-clef-2025:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/data-description
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/0/text`

The objective of this competition is to develop a model capable of identifying individual animals from images. For pre-training, we provide a new large-scale dataset [WildlifeReID-10k](https://www.kaggle.com/datasets/wildlifedatasets/wildlifereid-10k) with 10k identities and around 140k images. 
For testing, we have curated a dataset consisting of never-seen data of three species: (i)🐢 loggerhead sea turtles (Zakynthos, Greece), (ii) 🦎 salamanders (Czech Republic), and (iii) 🐆 Eurasian lynxes (Czech Republic). 

**The test dataset is split into two main subsets:**
- **📂 Database** – Contains labeled data about the individuals.
- **🔍 Query** – Consists of images for identification, where the task is to determine whether the individual is known (present in the database) or new (not present in the database).

## File Structure

The dataset is organized into structured directories to allow easy access and processing. It consists of labeled images for known individuals (*Database*) and unlabeled images (*Query*) requiring identification, metadata, and a sample submission file.  

- **📂 `images/{SeaTurtleID2022, SalamanderID2025, LynxID2025}/database/`** – Contains labeled images of known individuals, serving as the reference set.  
- **🔍 `images/{SeaTurtleID2022, SalamanderID2025, LynxID2025}/query/`** – Contains images to be identified.
- **📄 `metadata.csv`** – Provides dataset metadata, including database-query splits and individual identities.  
- **📑 `sample_submission.csv`** – A sample submission file illustrating the required format for predictions.  

## Data loading and description

Please check the provided [notebook](https://www.kaggle.com/code/wildlifedatasets/animalclef2025). The simplest way of loading the dataset is via the [wildlife-datasets](https://github.com/WildlifeDatasets/wildlife-datasets) package via

```
from wildlife_datasets.datasets import AnimalCLEF2025

dataset = AnimalCLEF2025(root)
```

This is the dataset with metadata

```
datasets.metadata
```

containing the following columns:

*   `image_id` - id of the image. Only for internal purposes.
*   `path` - path of the image.
*   `date` - date when the image was taken (can be missing).
*   `orientation` - orientation of the relevant body part (can be missing).
*   `species` - which species the photo depicts.
*   `dataset` - which of the 3 datasets the image belongs to.

## Sample submission

The above-mentioned notebook provides the function `create_sample_submission`, which creates the sample submission. For each query image (in rows), it needs to be predicted whether the individual is in the database (and then to predict its identity) or not (and then predict it as new_individual).


<a id="s002"></a>
## S002

- **source_id:** animal-clef-2025:page:1:Competition Description
- **page_name:** Competition Description
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/Competition Description
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/1/text`


## Motivation

Animal re-identification is crucial for studying various aspects of wildlife, including tracking populations, monitoring movements, examining behaviors, and managing species. Despite variations in how animal re-identification is defined and approached across studies, its objective remains consistent. The primary aim is to accurately and efficiently identify individual animals within a species by recognizing unique traits, such as markings, patterns, or other distinctive features. Automating this process allows for collecting detailed, large-scale data on population dynamics, migration routes, habitat use, and behaviors. This data empowers researchers to track movements, assess population sizes, and observe demographic changes, providing invaluable insights into species dynamics. Such information is essential for identifying biodiversity threats and crafting evidence-based conservation strategies. Despite great progress in machine learning, many models for animal re-identification still struggle with overfitting. They often focus too much on background details - like lighting or landscape - rather than the animal's unique features. As a result, these models perform well in familiar environments but fail in new or varied conditions. This limitation makes it harder to accurately identify animals in diverse habitats, reducing the models' usefulness in real-world conservation efforts. Improving their ability to generalize is essential for more reliable animal identification.

## What will you learn?

You will learn about the exciting field of animal re-identification and learn to recognize individual wild animals. You will learn how to create images such as the one below. It shows a test image of an unknown loggerhead sea turtle (left) and an image from the training set of a known sea turtle Nerea (or t266 in scientific notation). It also shows the automatically extracted keypoints and their matches between both images. Visual analysis of both the matches and the post-occular scutes reveals that both turtles are indeed the same. Therefore, we managed to identify the unknown turtle as Nerea.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F12294787%2F235ea09aaf82b9ec51a65a5c8a338c47%2FMatches.png?generation=1737379938870017&alt=media)


<a id="s003"></a>
## S003

- **source_id:** animal-clef-2025:page:2:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/rules
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/2/text`

##ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**[See Section 3.18 for defined terms](rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions  must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

 AnimalCLEF25 @ CVPR-FGVC & LifeCLEF
2. COMPETITION SPONSOR

 University of West Bohemia in Pilsen, Czechia
3. COMPETITION SPONSOR ADDRESS

 Univerzitni 8, 301 00, Pilsen, Czechia
4. COMPETITION WEBSITE

 https://www.imageclef.org/AnimalCLEF2025
5. TOTAL PRIZES AVAILABLE: 

 Kudos
6. WINNER LICENSE TYPE

 Open Source
7. DATA ACCESS AND USE

 Competition Use and Non-Commercial & Academic Research. See Section 4a for additional rules.

###2. COMPETITION-SPECIFIC RULES 
In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

####1. TEAM LIMITS
a. The maximum Team size is five (10).

b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the competition has been running.

####2. SUBMISSION LIMITS
a. You may submit a maximum of five (5) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

####3. COMPETITION TIMELINE
a. Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s Overview > Timeline page.

####4. COMPETITION DATA

a. Data Access and Use.

1. Competition Use and Non-Commercial & Academic Research: You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

2. The user of this dataset must follow the provided license of SeaTurtleID2022 and acknowledge the accompanying paper. In particular, it prohibits commercial applications and being re-uploaded. If WildlifeReID-10k was used as a training database, its license file must be followed.

b. Data Security. 

1. You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.

####5. WINNER LICENSE 

a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

1. Open Source: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org] (http://www.opensource.org)) that in no event limits commercial use of such code or model containing or depending on such code. 

2. For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the license in the preceding Section for that software. 

3. In the event that input data or pretrained models with an incompatible license are used to generate your winning solution, you do not need to grant an open source license in the preceding Section for that data and/or model(s). 

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.
 
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


<a id="s004"></a>
## S004

- **source_id:** animal-clef-2025:page:3:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/abstract
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/3/text`

This challenge is all about individual animal identification of the following three species: (i)🐢 loggerhead sea turtles (Zakynthos, Greece), (ii) 🦎 salamanders (Czech Republic), and (iii) 🐆 Eurasian lynxes (Czech Republic). Your goal will be to design a model that, for each image, determines whether the depicted animal is new (not present in the training dataset) or known (in which case, its identity must be provided).

Participants may decide to work with the relatively small provided dataset or to boost the model performance by employing the [WildlifeReID-10k:](https://arxiv.org/pdf/2406.09211) dataset: a collection of 36 existing wildlife re-identification datasets, with additional processing and diverse species such as marine turtles, primates, birds, African herbivores, marine mammals, and domestic animals. WildlifeReID-10k contains approximately 140,000 images of over 10,000 individuals. 


<a id="s005"></a>
## S005

- **source_id:** animal-clef-2025:page:4:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/foundational-rules
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/4/text`

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


<a id="s006"></a>
## S006

- **source_id:** animal-clef-2025:page:5:Other Resources
- **page_name:** Other Resources
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/Other Resources
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/5/text`

**Besides this Kaggle page, make sure to check these other resources:**

**Relevant tools and papers**:
- [WildlifeReID-10k Dataset Paper](https://arxiv.org/abs/2406.09211)
- [WildlifeDatasets](https://github.com/WildlifeDatasets/wildlife-datasets)
- [WildlifeTools](https://github.com/WildlifeDatasets/wildlife-tools)
- [MegaDescriptor](https://openaccess.thecvf.com/content/WACV2024/papers/Cermak_WildlifeDatasets_An_Open-Source_Toolkit_for_Animal_Re-Identification_WACV_2024_paper.pdf)
- [WildFusion](https://arxiv.org/pdf/2408.12934)

**Other competitions and workshops related info:**
- [LifeCLEF 2025 website](https://www.imageclef.org/LifeCLEF2025) for more information about LifeCLEF challenges and working notes submission procedure.
- [FGVC12 website](https://sites.google.com/view/fgvc12) for more information about the FGVC12 workshop.


<a id="s007"></a>
## S007

- **source_id:** animal-clef-2025:page:6:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/Evaluation
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/6/text`

## Submission File

The submission file contains only two columns. The first column is image_id (corresponds to the metadata of all query images) and is always fixed, as shown in the sample_submission file. The second column is either the `new_individual` or prediction of the new individual (always in the form `LynxID2025_???`, `SalamanderID2025_???`, `SeaTurtleID2022_???`). This [notebook](https://www.kaggle.com/code/wildlifedatasets/animalclef2025) notebook provides the function `create_sample_submission`, which creates the sample submission from predictions.

## Evaluation metrics

There are two metrics computed:

* BAKS (balanced accuracy on known samples) - computes the accuracy for individuals which are known (in the database). It is balanced over classes (individuals).
* BAUS (balanced accuracy on unknown samples) - computes the accuracy for individuals which are unknown (not in the database). It is balanced over classes (individuals).

The final accuracy is the *geometric* mean of the two accuracies. We decided to use the geometric mean `np.sqrt(x*y)` instead of the arithmetic mean `0.5*(x+y)` because the submission predicting all images as new individuals achieves 0% BAKS but 100% BAUS and its arithmetic mean would be 50% even though the model is useless. We provide a [full implementation of the evaluation metric](https://www.kaggle.com/code/wildlifedatasets/balanced-accuracy).


<a id="s008"></a>
## S008

- **source_id:** animal-clef-2025:page:7:Timeline
- **page_name:** Timeline
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/Timeline
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/7/text`

- **December 2024**: [Registration opens for all LifeCLEF challenges] (https://clef2025-labs-registration.dei.unipd.it/registrationForm.php) **❗Required for each team❗**
- **28 February 2025**: Competition Start
- ~~12 May 2025~~ **19 May 2025**: Competition Deadline
- ~~31 May 2025~~ **7 June 2025**: Deadline for submission of working note papers by participants [CEUR-WS proceedings]
- **23 June 2025**: Notification of acceptance - working note papers [CEUR-WS proceedings].
- **30 June 2025**: Camera-ready deadline for working note papers.
- **9-12 Sept 2025**: CLEF 2025 Madrid - Spain.

_All deadlines are at 11:59 PM CET of the corresponding day unless otherwise stated._ 

**The competition organizers reserve the right to update the contest timeline if they deem it necessary.**


<a id="s009"></a>
## S009

- **source_id:** animal-clef-2025:page:8:CVPR25 and CLEF25 Context
- **page_name:** CVPR25 and CLEF25 Context
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/CVPR25 and CLEF25 Context
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/8/text`

**This competition is held jointly as part of:**

- the [LifeCLEF 2025](https://www.imageclef.org/LifeCLEF2025) lab of the [CLEF 2025](http://clef2025.clef-initiative.eu) conference, and of
- the [FGVC12](https://sites.google.com/view/fgvc12) workshop organized in conjunction with [CVPR 2025](http://cvpr.thecvf.com) conference.

**Being part of scientific research, the participants are encouraged to participate to both events.
In particular, only participants who submitted a working note paper to LifeCLEF (see below) will be part of the officially published ranking used for scientific communication.**

FGVC12 at CVPR 2025
-------------------

This competition is part of the **Fine-Grained Visual Categorization [FGVC12](https://sites.google.com/view/fgvc12) workshop** at the Computer Vision and Pattern Recognition Conference [CVPR 2025](http://cvpr.thecvf.com). The task results will be presented at the workshop, and the contribution of the winning team(s) will be highlighted. Attending the workshop is not required to participate in the competition.

**CVPR 2025 will take place in Nashville, USA, on June 11-15, 2025.**  

A list of the other FGVC12 competitions [here](https://sites.google.com/view/fgvc12/competitions).

LifeCLEF 2025 at CLEF 2025
-------------

LifeCLEF lab is part of the Conference and Labs of the Evaluation Forum ([CLEF](http://www.clef-initiative.eu)).  
CLEF consists of independent peer-reviewed workshops on a broad range of challenges in multilingual and multimodal information access evaluation and benchmarking activities in various labs designed to test different aspects of mono and cross-language Information retrieval systems.  
**CLEF 2025 will take place in Madrid, Spain, on September 9-12, 2025.**  
You can find more details on the [CLEF 2025 website](http://clef2025.clef-initiative.eu).


<a id="s010"></a>
## S010

- **source_id:** animal-clef-2025:page:9:Citation
- **page_name:** Citation
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/overview/Citation
- **retrieved_at:** 2026-10-17T10:24:38.769982+00:00
- **Archive locator:** `/task_documents/9/text`

The user of this dataset must follow the provided license of [SeaTurtleID2022](https://www.kaggle.com/datasets/wildlifedatasets/seaturtleid2022) and acknowledge the accompanying [paper](https://openaccess.thecvf.com/content/WACV2024/html/Adam_SeaTurtleID2022_A_Long-Span_Dataset_for_Reliable_Sea_Turtle_Re-Identification_WACV_2024_paper.html). In particular, it prohibits commercial applications and being re-uploaded. If [WildlifeReID-10k](https://www.kaggle.com/datasets/wildlifedatasets/wildlifereid-10k) was used as a training database, its license file must be followed.

```
@inproceedings{adam2024seaturtleid2022,
  title={SeaTurtleID2022: A long-span dataset for reliable sea turtle re-identification},
  author={Adam, Luk{\'a}{\v{s}} and {\v{C}}erm{\'a}k, Vojt{\v{e}}ch and Papafitsoros, Kostas and Picek, Lukas},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={7146--7156},
  year={2024}
}
```

```
@inproceedings{vcermak2024wildlifedatasets,
  title={WildlifeDatasets: An open-source toolkit for animal re-identification},
  author={{\v{C}}erm{\'a}k, Vojt{\v{e}}ch and Picek, Lukas and Adam, Luk{\'a}{\v{s}} and Papafitsoros, Kostas},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={5953--5963},
  year={2024}
}
```
```
@article{adam2024wildlifereid,
  title={WildlifeReID-10k: Wildlife re-identification dataset with 10k individual animals},
  author={Adam, Luk{\'a}{\v{s}} and {\v{C}}erm{\'a}k, Vojt{\v{e}}ch and Papafitsoros, Kostas and Picek, Lukas},
  journal={arXiv preprint arXiv:2406.09211},
  year={2024}
}
```


<a id="s011"></a>
## S011

- **source_id:** animal-clef-2025:thread:575740:opening
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575740
- **thread_id:** 575740
- **comment_id:** opening
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-04-30T15:25:46.744Z
- **retrieved_at:** 2026-10-17T10:28:04.194616+00:00
- **Archive locator:** `/discussion/0/text`

The baseline model

Hello, I wanna ask where can I find the baseline model which I need to compare with its metric


<a id="s012"></a>
## S012

- **source_id:** animal-clef-2025:thread:575740:3190394
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575740#comment-3190394
- **thread_id:** 575740
- **comment_id:** 3190394
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-04-30T15:51:58.810Z
- **retrieved_at:** 2026-10-17T10:28:04.194616+00:00
- **Archive locator:** `/discussion/1/text`

Hi [@hathawaytan](https://www.kaggle.com/hathawaytan),

I'm not really sure if I understand what you mean. However, if you are referring to the models labeled on the leaderboard as "baselines," you can find the code in the [Code tab](https://www.kaggle.com/competitions/animal-clef-2025/code) right on top.

Best,

Lukas


<a id="s013"></a>
## S013

- **source_id:** animal-clef-2025:thread:575740:3190890
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575740#comment-3190890
- **thread_id:** 575740
- **comment_id:** 3190890
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-05-01T06:14:09.340Z
- **retrieved_at:** 2026-10-17T10:28:04.194616+00:00
- **Archive locator:** `/discussion/2/text`

thank you very much


<a id="s014"></a>
## S014

- **source_id:** animal-clef-2025:thread:575838:opening
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575838
- **thread_id:** 575838
- **comment_id:** opening
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-05-01T06:13:04.857Z
- **retrieved_at:** 2026-10-17T10:27:50.142647+00:00
- **Archive locator:** `/discussion/3/text`

where to get the solution.csv to calculate score 

Hello, I wonder where can I get the solution.csv to calculate score for testing before I submit my result


<a id="s015"></a>
## S015

- **source_id:** animal-clef-2025:thread:575838:3191104
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575838#comment-3191104
- **thread_id:** 575838
- **comment_id:** 3191104
- **author_name:** wildlifedatasets
- **author_role:** unknown
- **created_at:** 2025-05-01T11:45:58.963Z
- **retrieved_at:** 2026-10-17T10:27:50.142647+00:00
- **Archive locator:** `/discussion/4/text`

Hello, it is not possible to compute the score on the test data (we would need to release the labels, which would kill the point of the competition). You can use the [provided script](https://www.kaggle.com/code/wildlifedatasets/balanced-accuracy) to compute the score on the training data.

Lukas


<a id="s016"></a>
## S016

- **source_id:** animal-clef-2025:thread:575849:opening
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849
- **thread_id:** 575849
- **comment_id:** opening
- **author_name:** Atharva Deoresad
- **author_role:** unknown
- **created_at:** 2025-05-01T07:28:46.433Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/5/text`

Where can I find the solution csv/dataframe ?

Where can I find the solution csv/dataframe  uesd in the balanced accuracy code.Please help with the same or suggest where can I find the ground truth.


<a id="s017"></a>
## S017

- **source_id:** animal-clef-2025:thread:575849:3191048
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191048
- **thread_id:** 575849
- **comment_id:** 3191048
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-05-01T10:10:42.083Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/6/text`

Hi [@atharvadeoresad](https://www.kaggle.com/atharvadeoresad) ,

Thank you for your question! The ground-truth labels for this competition are not available to participants. That is intentional to ensure a fair contest. There is no CSV or dataframe you can download to compute balanced accuracy on your own.

You can only submit your predictions through the competition’s evaluation system and see your score on the public leaderboard. Once the competition ends, we might release the true labels or a reference solution. Until then, they remain hidden.

Best,

Lukas


<a id="s018"></a>
## S018

- **source_id:** animal-clef-2025:thread:575849:3191107
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191107
- **thread_id:** 575849
- **comment_id:** 3191107
- **parent_comment_id:** 3191048
- **author_name:** Atharva Deoresad
- **author_role:** unknown
- **created_at:** 2025-05-01T11:49:14.203Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/7/text`

Thank you so much for your reply .Can you please tell whether the final evaluation will be done using BAKS and BAUS ?


<a id="s019"></a>
## S019

- **source_id:** animal-clef-2025:thread:575849:3191110
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191110
- **thread_id:** 575849
- **comment_id:** 3191110
- **parent_comment_id:** 3191107
- **author_name:** wildlifedatasets
- **author_role:** unknown
- **created_at:** 2025-05-01T11:53:48.093Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/8/text`

[@atharvadeoresad](https://www.kaggle.com/atharvadeoresad) Yes, it will use [this script](https://www.kaggle.com/code/wildlifedatasets/balanced-accuracy) which computes the geometric mean of BAKS and BAUS.

Lukas


<a id="s020"></a>
## S020

- **source_id:** animal-clef-2025:thread:575849:3192882
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3192882
- **thread_id:** 575849
- **comment_id:** 3192882
- **parent_comment_id:** 3191107
- **author_name:** Atharva Deoresad
- **author_role:** unknown
- **created_at:** 2025-05-03T13:41:45.580Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/9/text`

okay ,but how to evaluate as ground truth is not provided which might help us make the model more accurate ?


<a id="s021"></a>
## S021

- **source_id:** animal-clef-2025:thread:575849:3191133
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191133
- **thread_id:** 575849
- **comment_id:** 3191133
- **parent_comment_id:** 3191048
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-05-01T12:52:37.987Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/10/text`

Could I use the competition and evaluation system to run programs after the task ends? Just want to calculate metrics without setting up the environment by myself🤣


<a id="s022"></a>
## S022

- **source_id:** animal-clef-2025:thread:575849:3191146
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191146
- **thread_id:** 575849
- **comment_id:** 3191146
- **parent_comment_id:** 3191133
- **author_name:** wildlifedatasets
- **author_role:** unknown
- **created_at:** 2025-05-01T13:11:17.167Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/11/text`

Sure, no problem :)


<a id="s023"></a>
## S023

- **source_id:** animal-clef-2025:thread:575849:3191767
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/575849#comment-3191767
- **thread_id:** 575849
- **comment_id:** 3191767
- **parent_comment_id:** 3191133
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-05-02T05:50:20.370Z
- **retrieved_at:** 2026-10-17T10:27:21.981669+00:00
- **Archive locator:** `/discussion/12/text`

thanks for your reply！


<a id="s024"></a>
## S024

- **source_id:** animal-clef-2025:thread:578201:opening
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201
- **thread_id:** 578201
- **comment_id:** opening
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-05-09T09:30:47.492Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/13/text`

🚨 Working Notes Submission & Competition Deadline Update 🚨

Dear AnimalCLEF25 participants,

Thank you once again for your incredible efforts in AnimalCLEF25!

We’re reaching out to inform you that **both the competition deadline and the working notes submission deadline have been officially postponed**, due to a delay in the release of the 2025 author instructions. We want to ensure all teams have enough time to prepare their working notes properly. **Once we have the detailed instructions, we will let you know!**

🗓️ Updated Timeline:

-  ➡️ **19 May 2025**: Competition Deadline  

-  ➡️ **7 June 2025**: Deadline for submission of working note papers by participants (CEUR-WS proceedings)

The remaining deadlines (notification of acceptance and camera-ready submission) are kept the same.

As a reminder, **all participants** are encouraged to submit a working note detailing their methods and results. Even if you're not in the Top 10. 

If you have any questions, don’t hesitate to ask in this thread.

Best,

Lukas


<a id="s025"></a>
## S025

- **source_id:** animal-clef-2025:thread:578201:3219173
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3219173
- **thread_id:** 578201
- **comment_id:** 3219173
- **author_name:** jalandrre
- **author_role:** unknown
- **created_at:** 2025-06-07T08:33:22.787Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/14/text`

Could I ask whether the working note should be submitted as a LaTeX zip file, or is it sufficient to submit just the PDF?


<a id="s026"></a>
## S026

- **source_id:** animal-clef-2025:thread:578201:3219572
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3219572
- **thread_id:** 578201
- **comment_id:** 3219572
- **parent_comment_id:** 3219173
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-06-08T01:30:21.713Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/15/text`

Hi [@jalandrre](https://www.kaggle.com/jalandrre) ,

Please, submit just a PDF file. 

Best,

Lukas


<a id="s027"></a>
## S027

- **source_id:** animal-clef-2025:thread:578201:3217428
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3217428
- **thread_id:** 578201
- **comment_id:** 3217428
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-06-05T02:23:27.510Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/16/text`

hello I‘dlike to ask how many pages should the working notebook have


<a id="s028"></a>
## S028

- **source_id:** animal-clef-2025:thread:578201:3217786
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3217786
- **thread_id:** 578201
- **comment_id:** 3217786
- **parent_comment_id:** 3217428
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-06-05T11:58:37.080Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/17/text`

Dear [@hathawaytan](https://www.kaggle.com/hathawaytan),

There is no need to ask the same question in multiple threads. Please, try to keep the discussion consolidated in one place so it's easier for everyone to follow and respond effectively. Bellow I'm including response from the other thread.

Best,

Lukas

  There is no page limit, but you should follow standard structure and include sufficient detail, and if possible, ablation studies. As a reference, here you have selected previously accepted FungiCLEF and GeoLifeCLEF working notes below:   

  
  
- [FungiCLEF 2024; winner, Stefan Wolf et al.](https://ceur-ws.org/Vol-3740/paper-212.pdf)

  
- [FungiCLEF 2024; 2nd place, Jack Etheredge](https://ceur-ws.org/Vol-3740/paper-195.pdf)

  
- [GeoLifeCLEF 2022; 2nd place, B. Kellenberg et T. Devis](https://ceur-ws.org/Vol-3180/paper-167.pdf)

  
- [GeoLifeCLEF 2023; winner, H.Q. Ung et al.](https://ceur-ws.org/Vol-3497/paper-181.pdf)


<a id="s029"></a>
## S029

- **source_id:** animal-clef-2025:thread:578201:3206225
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3206225
- **thread_id:** 578201
- **comment_id:** 3206225
- **author_name:** Hathaway Tan
- **author_role:** unknown
- **created_at:** 2025-05-21T03:59:16.127Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/18/text`

Hello, I'd like to ask whether the true labels of dataset will release and when the template will be provided ?


<a id="s030"></a>
## S030

- **source_id:** animal-clef-2025:thread:578201:3206896
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/578201#comment-3206896
- **thread_id:** 578201
- **comment_id:** 3206896
- **parent_comment_id:** 3206225
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-05-21T22:52:35.740Z
- **retrieved_at:** 2026-10-17T10:25:01.560138+00:00
- **Archive locator:** `/discussion/19/text`

Dear [@hathawaytan](https://www.kaggle.com/hathawaytan) , 

Sadly, the true labels won't be available any time soon.

You can read more about the template etc. in [this post](https://www.kaggle.com/competitions/animal-clef-2025/discussion/569663).

Best,

Lukas


<a id="s031"></a>
## S031

- **source_id:** animal-clef-2025:thread:579843:opening
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/579843
- **thread_id:** 579843
- **comment_id:** opening
- **author_name:** Ionut Visan
- **author_role:** unknown
- **created_at:** 2025-05-20T18:53:08.885Z
- **retrieved_at:** 2026-10-17T10:26:39.828826+00:00
- **Archive locator:** `/discussion/20/text`

0.62300_solution

[https://github.com/visan-ionut/Animal_Clef_2025](https://github.com/visan-ionut/Animal_Clef_2025)


<a id="s032"></a>
## S032

- **source_id:** animal-clef-2025:thread:579843:3206897
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/579843#comment-3206897
- **thread_id:** 579843
- **comment_id:** 3206897
- **author_name:** picekl
- **author_role:** unknown
- **created_at:** 2025-05-21T22:54:04.320Z
- **retrieved_at:** 2026-10-17T10:26:39.828826+00:00
- **Archive locator:** `/discussion/21/text`

Dear [@ionutvisan](https://www.kaggle.com/ionutvisan) ,

Great work and Congratulations on 6th place! 

Will you consider submitting a working note?

Best,

Lukas


<a id="s033"></a>
## S033

- **source_id:** animal-clef-2025:thread:579843:3207748
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/579843#comment-3207748
- **thread_id:** 579843
- **comment_id:** 3207748
- **parent_comment_id:** 3206897
- **author_name:** Ionut Visan
- **author_role:** unknown
- **created_at:** 2025-05-23T07:31:10.160Z
- **retrieved_at:** 2026-10-17T10:26:39.828826+00:00
- **Archive locator:** `/discussion/22/text`

Hi [@picekl](https://www.kaggle.com/picekl),

Sure, I will try to come back with a detailed paper on the solution.

Have a nice day.


<a id="s034"></a>
## S034

- **source_id:** animal-clef-2025:thread:579843:3206870
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/579843#comment-3206870
- **thread_id:** 579843
- **comment_id:** 3206870
- **author_name:** Daniel Valyano
- **author_role:** unknown
- **created_at:** 2025-05-21T21:28:08.090Z
- **retrieved_at:** 2026-10-17T10:26:39.828826+00:00
- **Archive locator:** `/discussion/23/text`

[@ionutvisan](https://www.kaggle.com/ionutvisan) huge amount of work done, thank you for sharing and congrats on the 6th place in this competition, man.


<a id="s035"></a>
## S035

- **source_id:** animal-clef-2025:thread:579843:3207750
- **url:** https://www.kaggle.com/competitions/animal-clef-2025/discussion/579843#comment-3207750
- **thread_id:** 579843
- **comment_id:** 3207750
- **parent_comment_id:** 3206870
- **author_name:** Ionut Visan
- **author_role:** unknown
- **created_at:** 2025-05-23T07:32:04.677Z
- **retrieved_at:** 2026-10-17T10:26:39.828826+00:00
- **Archive locator:** `/discussion/24/text`

Thanks [@danielvalyano](https://www.kaggle.com/danielvalyano)

