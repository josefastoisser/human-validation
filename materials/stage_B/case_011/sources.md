# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: Submission](#s006)
- [S007: foundational-rules](#s007)
- [S008: Tips](#s008)
- [S009: Prizes](#s009)
- [S010: drw-crypto-market-prediction:thread:580062:opening](#s010)
- [S011: drw-crypto-market-prediction:thread:580062:3207103](#s011)
- [S012: drw-crypto-market-prediction:thread:580062:3207107](#s012)
- [S013: drw-crypto-market-prediction:thread:580062:3219347](#s013)
- [S014: drw-crypto-market-prediction:thread:580062:3207131](#s014)
- [S015: drw-crypto-market-prediction:thread:580062:3207139](#s015)
- [S016: drw-crypto-market-prediction:thread:580062:3207210](#s016)
- [S017: drw-crypto-market-prediction:thread:580062:3208903](#s017)
- [S018: drw-crypto-market-prediction:thread:580062:3210837](#s018)
- [S019: drw-crypto-market-prediction:thread:580062:3208666](#s019)
- [S020: drw-crypto-market-prediction:thread:580062:3207410](#s020)
- [S021: drw-crypto-market-prediction:thread:580062:3207324](#s021)
- [S022: drw-crypto-market-prediction:thread:580062:3208738](#s022)
- [S023: drw-crypto-market-prediction:thread:580062:3207300](#s023)
- [S024: drw-crypto-market-prediction:thread:580062:3208315](#s024)
- [S025: drw-crypto-market-prediction:thread:580062:3208341](#s025)
- [S026: drw-crypto-market-prediction:thread:580062:3207147](#s026)
- [S027: drw-crypto-market-prediction:thread:580062:3207148](#s027)
- [S028: drw-crypto-market-prediction:thread:580067:opening](#s028)
- [S029: drw-crypto-market-prediction:thread:580170:opening](#s029)
- [S030: drw-crypto-market-prediction:thread:580170:3221918](#s030)
- [S031: drw-crypto-market-prediction:thread:580170:3213509](#s031)
- [S032: drw-crypto-market-prediction:thread:580170:3212061](#s032)
- [S033: drw-crypto-market-prediction:thread:580170:3210113](#s033)
- [S034: drw-crypto-market-prediction:thread:580170:3209741](#s034)
- [S035: drw-crypto-market-prediction:thread:580170:3209407](#s035)
- [S036: drw-crypto-market-prediction:thread:580170:3209422](#s036)
- [S037: drw-crypto-market-prediction:thread:580170:3247065](#s037)
- [S038: drw-crypto-market-prediction:thread:580170:3239660](#s038)
- [S039: drw-crypto-market-prediction:thread:580170:3218368](#s039)
- [S040: drw-crypto-market-prediction:thread:580170:3211361](#s040)
- [S041: drw-crypto-market-prediction:thread:580170:3210906](#s041)
- [S042: drw-crypto-market-prediction:thread:580170:3209766](#s042)
- [S043: drw-crypto-market-prediction:thread:580170:3209385](#s043)
- [S044: drw-crypto-market-prediction:thread:580744:opening](#s044)
- [S045: drw-crypto-market-prediction:thread:580744:3209948](#s045)
- [S046: drw-crypto-market-prediction:thread:590804:opening](#s046)
- [S047: drw-crypto-market-prediction:thread:590804:3253397](#s047)
- [S048: drw-crypto-market-prediction:thread:590804:3253482](#s048)
- [S049: drw-crypto-market-prediction:thread:590804:3253604](#s049)
- [S050: drw-crypto-market-prediction:thread:590804:3253378](#s050)

<a id="s001"></a>
## S001

- **source_id:** drw-crypto-market-prediction:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/data-description
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/0/text`

In this competition, the dataset comprises minute-level historical data for the crypto market. Your challenge is to predict future crypto market price movements.

This is a community forecasting competition, and you can submit your predictions either as CSV files or through Kaggle Notebooks. For more details on using Kaggle Notebooks, refer to [this link](https://www.kaggle.com/docs/notebooks).

The public leaderboard during the competition will not be scored and serves only for authoring your model submissions using the public testing data. Once the active submission phase ends, we will update the private leaderboard using **more recent data**, and this will be used to determine the final team rankings.

## Files

## **train.parquet**  
The training dataset containing all historical market data along with the corresponding labels.  

- `timestamp`: The timestamp index representing the minute associated with each row.  
- `bid_qty`: The total quantity buyers are willing to purchase at the best (highest) bid price at the given timestamp.
- `ask_qty`: The total quantity sellers are offering to sell at the best (lowest) ask price at the given timestamp.
- `buy_qty`: The total trading quantity executed at the best ask price during the given minute.  
- `sell_qty`: The total trading quantity executed at the best bid price during the given minute.  
- `volume`: The total traded volume during the minute.  
- `X_{1,...,780}`: A set of anonymized market features derived from proprietary data sources.  
- `label`: The target variable representing the anonymized market price movement to be predicted.  

## **test.parquet**  
The test dataset has the same feature structure as train.parquet, with the following differences:  

- `timestamp`: To prevent future peeking, all timestamps are masked, shuffled, and replaced with a unique `ID`.
- `label`: All labels in the test set are set to 0.  

## **sample_submission.csv**  
A sample file demonstrating the expected submission format. Your submission must have the same number of rows as this sample file and follow its structure to be considered valid.  



<a id="s002"></a>
## S002

- **source_id:** drw-crypto-market-prediction:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/Description
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/1/text`

The cryptocurrency market represents one of the most dynamic and rapidly evolving financial landscapes, offering a wealth of opportunities for those who can extract meaningful insights from its vast streams of data. However, market information in crypto has an inherently low signal-to-noise ratio making it exceptionally difficult to identify predictive patterns. Price movements are shaped by a complex interplay of liquidity, order flow dynamics, sentiment shifts, and structural inefficiencies, requiring sophisticated quantitative techniques to decode.

At DRW, we have been at the forefront of financial innovation for over three decades, embracing cutting-edge technology and rigorous quantitative research to optimize trading strategies. Through Cumberland, our dedicated crypto trading arm, we were among the earliest institutional participants in the digital asset space, helping to shape market structure and improve efficiency. As one of the largest liquidity providers in crypto, we thrive on developing proprietary trading strategies that adapt to the ever-changing market environment.

In this competition, we invite you to build a model capable of predicting short-term crypto future price movements using our production feature data alongside publicly available market volume statistics. The proprietary production features we provide are integral to our trading strategies, capturing subtle market signals that help us navigate and seize opportunities in real time. Moreover, these production features, combined with public data describing the broader market state, create a rich and challenging dataset for data mining and modeling. Your task is to integrate these diverse sources of information into a single directional signal that effectively predicts crypto future price movements.

Through this challenge, we aim to replicate the real-world problems we tackle at DRW every day—leveraging advanced machine learning techniques to extract structure from noisy, high-dimensional market data. The most successful solutions will provide a learning model that efficiently incorporates both explicit patterns and implicit interactions between all data features to refine price movement predictions.

We look forward to seeing how the Kaggle community approaches this problem and how different modeling techniques can enhance our understanding of market dynamics. If you're excited by complex, high-impact challenges beyond predictive modeling, DRW offers a diverse range of opportunities at the intersection of quantitative research, technology, and trading strategy development.



<a id="s003"></a>
## S003

- **source_id:** drw-crypto-market-prediction:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/Evaluation
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/2/text`

Submissions will be evaluated based on the [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) between the labels and your predicted values over the private testing set.


<a id="s004"></a>
## S004

- **source_id:** drw-crypto-market-prediction:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/rules
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/3/text`

### One account per participant

You cannot sign up to Kaggle from multiple accounts and therefore you cannot submit from multiple accounts.

### No private sharing outside teams

Privately sharing code or data outside of teams is not permitted. It's okay to share code if made available to all participants on the forums.

### Team Mergers

Team mergers are allowed and can be performed by the team leader. In order to merge, the combined team must have a total submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of submissions per day multiplied by the number of days the competition has been running.

### Team Limits

The maximum team size is 5.

### Submission Limits

- You may submit a maximum of 5 entries per day.
- You may select up to 2 final submissions for judging.

### Competition Timeline

Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s **Overview** page.


### COMPETITION-SPECIFIC TERMS

### COMPETITION TITLE: DRW - Crypto Market Prediction

### COMPETITION SPONSOR: DRW Holdings, LLC
### COMPETITION SPONSOR ADDRESS: 540 W Madison St Suite 2500, Chicago, IL 60661, United States
### COMPETITION WEBSITE: https://www.kaggle.com/competitions/drw-crypto-market-prediction

### TOTAL PRIZES AVAILABLE: $25,000

| Prize Rank | Prize Amount |
|------------|--------------|
| First Prize | $5,000 |
| Second Prize | $5,000 |
| Third Prize | $5,000 |
| Fourth Prize | $5,000 |
| Fifth Prize | $5,000 |

### WINNER LICENSE TYPE: Non-exclusive license

### DATA ACCESS AND USE: Competition use only

Competitions are open to residents of the United States and worldwide, except that if you are a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, Syria, North Korea, or are subject to U.S. export controls or sanctions, you may not enter the Competition. Other local rules and regulations may apply to you, so please check your local laws to ensure that you are eligible to participate in skills-based competitions. The Competition Sponsor reserves the right to award alternative Prizes where needed to comply with local laws.

### ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

The Competition named above is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. Your competition submissions ("Submissions") must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.

### A. COMPETITION-SPECIFIC RULES

In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

#### 1. WINNER LICENSE

Under Section 11 (Winners Obligations) of the General Rules below, you hereby grant and will grant Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

**Non-Exclusive:**  
You hereby grant and will grant to Competition Sponsor and its designees a worldwide, non-exclusive, sub-licensable, transferable, fully paid-up, royalty-free, perpetual, irrevocable right to use, reproduce, distribute, create derivative works of, publicly perform, publicly display, digitally perform, make, have made, sell, offer for sale and import your winning Submission and the source code used to generate the Submission, in any media now known or developed in the future, for any purpose whatsoever, commercial or otherwise, without further approval by or payment to you. To the extent your Submission makes use of generally commercially available software not owned by you that you used to generate your Submission, but that can be procured by the Competition Sponsor without undue expense, you do not grant the license in the preceding sentence to that software.

#### 2. AUTOMATED MACHINE LEARNING TOOLS (AMLT)

Individual participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google AutoML, H2O Driverless AI, etc.) to create a Submission, provided that the participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules.

The following provision is added to the end of Section 11 of the General Competition Rules below:  
*"Individual participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section A.1 (Winners License), Section B.11 (Winners Obligations), and Section B.17 (Warranty, Indemnity, and Release)."*



<a id="s005"></a>
## S005

- **source_id:** drw-crypto-market-prediction:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/abstract
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/4/text`

You are invited to develop a model capable of predicting crypto market price movements using our production data. Accurate directional signals derived through quantitative methods can significantly enhance our trading strategies and enable more precise market opportunity identification.


<a id="s006"></a>
## S006

- **source_id:** drw-crypto-market-prediction:page:5:Submission
- **page_name:** Submission
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/Submission
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/5/text`

You are required to generate predictions for the **label** variable for each row in the dataset. The expected submission format is provided in *sample_submission.csv* at the [Data](https://www.kaggle.com/competitions/drw-crypto-market-prediction/data) page.

As this is a **community competition** and does not adhere to the **code competition** format, participants may submit predictions as a CSV file for evaluation. However, we strongly encourage submitting a Kaggle Notebook to ensure reproducibility.


<a id="s007"></a>
## S007

- **source_id:** drw-crypto-market-prediction:page:6:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/foundational-rules
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
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

- **source_id:** drw-crypto-market-prediction:page:7:Tips
- **page_name:** Tips
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/Tips
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/7/text`

1. The training dataset covers the period from March 1, 2023, to February 29, 2024. The test data comes after the training period, though its timestamps are masked. Since data relevance matters, **you don’t have to use the entire training set**—feel free to focus on a specific window, such as only the most recent months, if that works better for your model.  

2. You’re welcome to use all the data we provide, as well as any freely and publicly available external datasets—including pre-trained models—to support your analysis and solution development.

3. Efforts in this competition can be directed toward two key aspects:  

- Data Exploration and Feature Analysis - Understanding the characteristics of the anonymized proprietary features and extracting meaningful insights from public market data through data mining and statistical analysis.
- Advanced Modeling Techniques - Developing machine learning models that effectively select, capture and integrate as much information as possible from all the available features.  



<a id="s009"></a>
## S009

- **source_id:** drw-crypto-market-prediction:page:8:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/overview/Prizes
- **retrieved_at:** 2026-10-17T04:26:24.628362+00:00
- **Archive locator:** `/task_documents/8/text`

Total Prizes Available: $25,000, equally shared among the top 5 teams
- **1st Place** - $5,000
- **2nd Place** - $5,000
- **3rd Place** - $5,000
- **4th Place** - $5,000
- **5th Place** - $5,000

**Note:** For top-performing teams eligible for prizes, submission of a Jupyter Notebook capable of successfully generating the prediction output is mandatory to qualify for the award. We will conduct a code review to verify the reproducibility of results and ensure that no future peeking occurred during predictions. Failure to provide a compliant notebook may result in disqualification from prize eligibility. DRW reserves the right, at its sole discretion, to review submitted code and disqualify any participant found to be engaging in such practices.

**Avoid Future Peaking:**
1. You are **NOT** allowed to use the test dataset to aid the modeling process, as all test data—except for the current test data point to predict—contains future information that would not be available at prediction time in a real-world setting.

2. Similar to the note about using future data, any external dataset containing future information will be considered a rule violation. So make sure everything you use would have been available at the time of test data prediction!


<a id="s010"></a>
## S010

- **source_id:** drw-crypto-market-prediction:thread:580062:opening
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062
- **thread_id:** 580062
- **comment_id:** opening
- **author_name:** narsil (jobs-in-data.com)
- **author_role:** unknown
- **created_at:** 2025-05-22T07:56:38.578Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/0/text`

Masking timestamps in the test dataset

I understand why timestamps in the test set were masked. 

But this prevents the most relevant feature engineering techniques - capturing trends in prices, volume, bid-ask spreads.

Typically in any time-series forecasting, the strongest features are the ones related to lagged target features - where the lag window depends on the timing of data availability during inference. But we cannot use them here. 

the only proper way to do that is via time series API, but i guess that is only available in featured competitions


<a id="s011"></a>
## S011

- **source_id:** drw-crypto-market-prediction:thread:580062:3207103
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207103
- **thread_id:** 580062
- **comment_id:** 3207103
- **author_name:** william.wu
- **author_role:** unknown
- **created_at:** 2025-05-22T08:33:26.723Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/1/text`

To prevent future peeking, all timestamps are masked, shuffled, and replaced with a unique ID.

This means we cannot utilize any rolling features or time-series models. 🤔


<a id="s012"></a>
## S012

- **source_id:** drw-crypto-market-prediction:thread:580062:3207107
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207107
- **thread_id:** 580062
- **comment_id:** 3207107
- **parent_comment_id:** 3207103
- **author_name:** narsil (jobs-in-data.com)
- **author_role:** unknown
- **created_at:** 2025-05-22T08:39:41.517Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/2/text`

That is exactly the point


<a id="s013"></a>
## S013

- **source_id:** drw-crypto-market-prediction:thread:580062:3219347
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3219347
- **thread_id:** 580062
- **comment_id:** 3219347
- **parent_comment_id:** 3207107
- **author_name:** motono0223
- **author_role:** unknown
- **created_at:** 2025-06-07T14:52:17.017Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/3/text`

I agree with your opinions.

I wrote the discussion to suggest for test data structure.

[https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/583522](https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/583522)


<a id="s014"></a>
## S014

- **source_id:** drw-crypto-market-prediction:thread:580062:3207131
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207131
- **thread_id:** 580062
- **comment_id:** 3207131
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2025-05-22T09:26:40.950Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/4/text`

Ironically, some people would probably try to reverse engineer timestamps and they might even succeed too


<a id="s015"></a>
## S015

- **source_id:** drw-crypto-market-prediction:thread:580062:3207139
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207139
- **thread_id:** 580062
- **comment_id:** 3207139
- **parent_comment_id:** 3207131
- **author_name:** william.wu
- **author_role:** unknown
- **created_at:** 2025-05-22T09:36:38.683Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/5/text`

Just keep in mind that, similar to the note about using future data, any external dataset containing future information will be considered a rule violation. So make sure everything you use would have been available at the time of prediction!

Reverse engineering timestamps without access to future data is challenging, yet achievable with future data. However, I'm uncertain how the organizer can ascertain whether the model has been trained on and memorized this future data.


<a id="s016"></a>
## S016

- **source_id:** drw-crypto-market-prediction:thread:580062:3207210
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207210
- **thread_id:** 580062
- **comment_id:** 3207210
- **parent_comment_id:** 3207131
- **author_name:** narsil (jobs-in-data.com)
- **author_role:** unknown
- **created_at:** 2025-05-22T12:07:32.373Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/6/text`

This is exactly what is going to happen


<a id="s017"></a>
## S017

- **source_id:** drw-crypto-market-prediction:thread:580062:3208903
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3208903
- **thread_id:** 580062
- **comment_id:** 3208903
- **parent_comment_id:** 3207131
- **author_name:** Meet Babariya
- **author_role:** unknown
- **created_at:** 2025-05-24T22:31:05.477Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/7/text`

if that's actually possible, is that allowed according to competition rules?


<a id="s018"></a>
## S018

- **source_id:** drw-crypto-market-prediction:thread:580062:3210837
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3210837
- **thread_id:** 580062
- **comment_id:** 3210837
- **parent_comment_id:** 3208903
- **author_name:** Ravi Ramakrishnan
- **author_role:** unknown
- **created_at:** 2025-05-27T18:07:17.323Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/8/text`

I think yes.

Time can be predicted using a model and nothing prevents us from training more models [@meetbabariya](https://www.kaggle.com/meetbabariya)


<a id="s019"></a>
## S019

- **source_id:** drw-crypto-market-prediction:thread:580062:3208666
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3208666
- **thread_id:** 580062
- **comment_id:** 3208666
- **author_name:** Snehal
- **author_role:** unknown
- **created_at:** 2025-05-24T12:56:13.420Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/9/text`

[@narsil](https://www.kaggle.com/narsil) thank you for this thread. first thing that came into mind was typical time series FE, I was wondering how to get started when timestamps are masked in test data.


<a id="s020"></a>
## S020

- **source_id:** drw-crypto-market-prediction:thread:580062:3207410
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207410
- **thread_id:** 580062
- **comment_id:** 3207410
- **author_name:** g john rao
- **author_role:** unknown
- **created_at:** 2025-05-22T17:28:17.917Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/10/text`

maybe it's about working with the instantaneous market state, a different kind of challenge


<a id="s021"></a>
## S021

- **source_id:** drw-crypto-market-prediction:thread:580062:3207324
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207324
- **thread_id:** 580062
- **comment_id:** 3207324
- **author_name:** Ayush Khaire
- **author_role:** unknown
- **created_at:** 2025-05-22T15:28:09.193Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/11/text`

[@narsil](https://www.kaggle.com/narsil) sir , is this more likely a regression problem rather than a time series competition ? I unnderstand they masked test timestamps , but even tho they are not sorted I guess unlike train data . so for me it sounds a regression problem , how to handle things , any guidence plaase ? I am new at time series . How to properly approach and handle it ?


<a id="s022"></a>
## S022

- **source_id:** drw-crypto-market-prediction:thread:580062:3208738
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3208738
- **thread_id:** 580062
- **comment_id:** 3208738
- **parent_comment_id:** 3207324
- **author_name:** AndrewGuanzc
- **author_role:** unknown
- **created_at:** 2025-05-24T15:40:39.147Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/12/text`

I guess this is a **regression problem**!


<a id="s023"></a>
## S023

- **source_id:** drw-crypto-market-prediction:thread:580062:3207300
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207300
- **thread_id:** 580062
- **comment_id:** 3207300
- **author_name:** Quentin Adatte
- **author_role:** unknown
- **created_at:** 2025-05-22T14:50:32.067Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/13/text`

I was thinking the same, so basically here, we simply have 800 features that needs to be independently mapped to a value between 0 and 1. Is that correct?


<a id="s024"></a>
## S024

- **source_id:** drw-crypto-market-prediction:thread:580062:3208315
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3208315
- **thread_id:** 580062
- **comment_id:** 3208315
- **parent_comment_id:** 3207300
- **author_name:** akash_patel001
- **author_role:** unknown
- **created_at:** 2025-05-23T21:28:57.977Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/14/text`

I don't think we have a constraint of 0 to 1; we can map them on any scale. They are checked using Pearson correlation, so the range doesn't matter.


<a id="s025"></a>
## S025

- **source_id:** drw-crypto-market-prediction:thread:580062:3208341
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3208341
- **thread_id:** 580062
- **comment_id:** 3208341
- **parent_comment_id:** 3208315
- **author_name:** Quentin Adatte
- **author_role:** unknown
- **created_at:** 2025-05-23T23:33:19.267Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/15/text`

Yeah I confirm we dont, I was mislead by one of my plots, sorry!


<a id="s026"></a>
## S026

- **source_id:** drw-crypto-market-prediction:thread:580062:3207147
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207147
- **thread_id:** 580062
- **comment_id:** 3207147
- **author_name:** Ethan
- **author_role:** unknown
- **created_at:** 2025-05-22T09:42:54.723Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/16/text`

Does the ID in the test file maintain the chronological order?


<a id="s027"></a>
## S027

- **source_id:** drw-crypto-market-prediction:thread:580062:3207148
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580062#comment-3207148
- **thread_id:** 580062
- **comment_id:** 3207148
- **parent_comment_id:** 3207147
- **author_name:** yunsuxiaozi
- **author_role:** unknown
- **created_at:** 2025-05-22T09:44:43.033Z
- **retrieved_at:** 2026-10-17T05:09:10.702594+00:00
- **Archive locator:** `/discussion/17/text`

timestamp: To prevent future peeking, all timestamps are masked, shuffled, and replaced with a unique ID.


<a id="s028"></a>
## S028

- **source_id:** drw-crypto-market-prediction:thread:580067:opening
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580067
- **thread_id:** 580067
- **comment_id:** opening
- **author_name:** yunsuxiaozi
- **author_role:** unknown
- **created_at:** 2025-05-22T08:20:57.387Z
- **retrieved_at:** 2026-10-17T05:08:56.503515+00:00
- **Archive locator:** `/discussion/18/text`

Baseline Starter LB:0.058 Wow!

` pandas  pd
 polars  pl
 lightgbm  LGBMRegressor
train=pl.read_parquet()
train=train.to_pandas()
test=pl.read_parquet()
test=test.to_pandas()
()
train.head()

NUNIQUE1=[c  c  train.columns  train[c].nunique()==]
train.drop(NUNIQUE1+[],axis=,inplace=)
test.drop(NUNIQUE1+[],axis=,inplace=)
train.head()

FEATURES=[c  c  train.columns  c!=]
model=LGBMRegressor()
model.fit(train[FEATURES].values,train[].values)
test_preds=model.predict(test[FEATURES].values)
(test_preds[:])

sub=pd.read_csv()
sub[]=test_preds
sub.to_csv(,index=)
sub.head()
`


<a id="s029"></a>
## S029

- **source_id:** drw-crypto-market-prediction:thread:580170:opening
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170
- **thread_id:** 580170
- **comment_id:** opening
- **author_name:** Ravi Ramakrishnan
- **author_role:** unknown
- **created_at:** 2025-05-22T23:29:45.463Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/19/text`

Starter materials and references 

Hello all,

Wishing you the best for the competition! This is my favourite data science topic, as a Finance post-grad and I am excited to witness such a competition after a long wait! Hope the below materials help you onboard well and efficiently-

[Jane Street Market Prediction](https://www.kaggle.com/competitions/jane-street-market-prediction/overview)

Most voted kernels

- [https://www.kaggle.com/code/carlmcbrideellis/jane-street-eda-of-day-0-and-feature-importance](https://www.kaggle.com/code/carlmcbrideellis/jane-street-eda-of-day-0-and-feature-importance)

- [https://www.kaggle.com/code/hamditarek/market-prediction-xgboost-with-gpu-fit-in-1min](https://www.kaggle.com/code/hamditarek/market-prediction-xgboost-with-gpu-fit-in-1min)

- [https://www.kaggle.com/code/aimind/bottleneck-encoder-mlp-keras-tuner-8601c5](https://www.kaggle.com/code/aimind/bottleneck-encoder-mlp-keras-tuner-8601c5)

- [https://www.kaggle.com/code/gogo827jz/jane-street-neural-network-starter](https://www.kaggle.com/code/gogo827jz/jane-street-neural-network-starter)

- [https://www.kaggle.com/code/muhammadmelsherbini/jane-street-extensive-eda-pca-starter](https://www.kaggle.com/code/muhammadmelsherbini/jane-street-extensive-eda-pca-starter)

- [https://www.kaggle.com/code/tarlannazarov/own-jane-street-with-keras-nn](https://www.kaggle.com/code/tarlannazarov/own-jane-street-with-keras-nn)

- [https://www.kaggle.com/code/odins0n/exploring-time-series-plots-beginners-guide](https://www.kaggle.com/code/odins0n/exploring-time-series-plots-beginners-guide)

- [https://www.kaggle.com/code/jorijnsmit/found-the-holy-grail-grouptimeseriessplit](https://www.kaggle.com/code/jorijnsmit/found-the-holy-grail-grouptimeseriessplit)

- [https://www.kaggle.com/code/snippsy/bottleneck-encoder-mlp-keras-tuner](https://www.kaggle.com/code/snippsy/bottleneck-encoder-mlp-keras-tuner)

- [https://www.kaggle.com/code/a763337092/blending-tensorflow-and-pytorch](https://www.kaggle.com/code/a763337092/blending-tensorflow-and-pytorch)

Top ranked solutions

- [https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224348](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224348) -- rank 1

- [https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224713](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224713) -- rank 3

- [https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/226837](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/226837) -- rank 10

- [https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/269181](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/269181) -- rank 15

- [https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224079](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224079) -- rank 23

[Jane Street Real-Time Market Data Forecasting](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting)

Most voted kernels

- [https://www.kaggle.com/code/yuanzhezhou/jane-street-baseline-lgb-xgb-and-catboost](https://www.kaggle.com/code/yuanzhezhou/jane-street-baseline-lgb-xgb-and-catboost)

- [https://www.kaggle.com/code/allegich/jane-street-time-series-analysis-eda-ensemble](https://www.kaggle.com/code/allegich/jane-street-time-series-analysis-eda-ensemble)

- [https://www.kaggle.com/code/voix97/jane-street-rmf-inference-nn-xgb](https://www.kaggle.com/code/voix97/jane-street-rmf-inference-nn-xgb)

- [https://www.kaggle.com/code/motono0223/eda-jane-street-real-time-market-data-forecasting](https://www.kaggle.com/code/motono0223/eda-jane-street-real-time-market-data-forecasting)

- [https://www.kaggle.com/code/yongsukprasertsuk/0-008-js-rmf-ensemble-xgb-nn-tabm-ridge](https://www.kaggle.com/code/yongsukprasertsuk/0-008-js-rmf-ensemble-xgb-nn-tabm-ridge)

- [https://www.kaggle.com/code/eivolkova/public-lb-6th](https://www.kaggle.com/code/eivolkova/public-lb-6th)

- [https://www.kaggle.com/code/simonedegasperis/online-retrain-poc](https://www.kaggle.com/code/simonedegasperis/online-retrain-poc)

- [https://www.kaggle.com/code/motono0223/js24-inference-gbdt-with-lags-singlemodel](https://www.kaggle.com/code/motono0223/js24-inference-gbdt-with-lags-singlemodel)

[Optiver- Trading at the Close](https://www.kaggle.com/competitions/optiver-trading-at-the-close)

Kernels- most voted

- [https://www.kaggle.com/code/ravi20076/optiver-baseline-models](https://www.kaggle.com/code/ravi20076/optiver-baseline-models)

- [https://www.kaggle.com/code/yuanzhezhou/baseline-lgb-xgb-and-catboost](https://www.kaggle.com/code/yuanzhezhou/baseline-lgb-xgb-and-catboost)

- [https://www.kaggle.com/code/a27182818/explain-the-data-lightgbm-baseline](https://www.kaggle.com/code/a27182818/explain-the-data-lightgbm-baseline)

- [https://www.kaggle.com/code/lblhandsome/optiver-robust-best-single-model](https://www.kaggle.com/code/lblhandsome/optiver-robust-best-single-model)

- [https://www.kaggle.com/code/verracodeguacas/fold-cv](https://www.kaggle.com/code/verracodeguacas/fold-cv)

- [https://www.kaggle.com/code/peizhengwang/best-public-score](https://www.kaggle.com/code/peizhengwang/best-public-score)

- [https://www.kaggle.com/code/siddhvr/optiver-trading-at-the-close-sub](https://www.kaggle.com/code/siddhvr/optiver-trading-at-the-close-sub)

High scoring approaches and discussions-

- [https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/487446](https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/487446)

- [https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/486868](https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/486868)

- [https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/462653](https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/462653)

- [https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/486086](https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/486086)

[Enefit - Predict Energy Behavior of Prosumers](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers)

Kernels- most voted

- [https://www.kaggle.com/code/rafiko1/enefit-xgboost-starter](https://www.kaggle.com/code/rafiko1/enefit-xgboost-starter)

- [https://www.kaggle.com/code/vitalykudelya/explain-dataset-and-baseline](https://www.kaggle.com/code/vitalykudelya/explain-dataset-and-baseline)

- [https://www.kaggle.com/code/vincentschuler/enefit-baseline-cross-validation](https://www.kaggle.com/code/vincentschuler/enefit-baseline-cross-validation)

- [https://www.kaggle.com/code/greysky/enefit-generic-notebook](https://www.kaggle.com/code/greysky/enefit-generic-notebook)

- [https://www.kaggle.com/code/vitalykudelya/enefit-target-diff](https://www.kaggle.com/code/vitalykudelya/enefit-target-diff)

- [https://www.kaggle.com/code/ahmedabdulwahab/pandas-data-description-and-starters-guide](https://www.kaggle.com/code/ahmedabdulwahab/pandas-data-description-and-starters-guide)

High scoring approaches and discussions-

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472793](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472793)

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499938](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499938)

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499397](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499397)

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499649](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/499649)

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472537](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472537)

- [https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472537](https://www.kaggle.com/competitions/predict-energy-behavior-of-prosumers/discussion/472537)

Playground Time Series Forecasting challenges

[Season3-Episode 20](https://www.kaggle.com/competitions/playground-series-s3e20)

Kernels- most voted

- [https://www.kaggle.com/code/ambrosm/pss3e20-eda-which-makes-sense](https://www.kaggle.com/code/ambrosm/pss3e20-eda-which-makes-sense)

- [https://www.kaggle.com/code/kacperrabczewski/rwanda-co2-step-by-step-guide](https://www.kaggle.com/code/kacperrabczewski/rwanda-co2-step-by-step-guide)

- [https://www.kaggle.com/code/yaaangzhou/pg-s3-e20-eda-modeling](https://www.kaggle.com/code/yaaangzhou/pg-s3-e20-eda-modeling)

- [https://www.kaggle.com/code/dmitryuarov/ps3e20-rwanda-emission-advanced-fe-20-88](https://www.kaggle.com/code/dmitryuarov/ps3e20-rwanda-emission-advanced-fe-20-88)

- [https://www.kaggle.com/code/iqbalsyahakbar/ps3e20-time-series-for-beginners](https://www.kaggle.com/code/iqbalsyahakbar/ps3e20-time-series-for-beginners)

[Season3-Episode 19](https://www.kaggle.com/competitions/playground-series-s3e19)

Kernels- most voted

- [https://www.kaggle.com/code/tumpanjawat/s3e19-course-eda-fe-lightgbm](https://www.kaggle.com/code/tumpanjawat/s3e19-course-eda-fe-lightgbm)

- [https://www.kaggle.com/code/iqbalsyahakbar/ps3e19-time-series-for-beginners](https://www.kaggle.com/code/iqbalsyahakbar/ps3e19-time-series-for-beginners)

- [https://www.kaggle.com/code/ivyzang/1st-place-solution-less-is-more](https://www.kaggle.com/code/ivyzang/1st-place-solution-less-is-more)

- [https://www.kaggle.com/code/tetsutani/ps3e19-eda-ensemble-ml-pipeline-rnn-by-skorch](https://www.kaggle.com/code/tetsutani/ps3e19-eda-ensemble-ml-pipeline-rnn-by-skorch)

- [https://www.kaggle.com/code/kacperrabczewski/last-minute-forecasting](https://www.kaggle.com/code/kacperrabczewski/last-minute-forecasting)

[TPS- September2022](https://www.kaggle.com/competitions/tabular-playground-series-sep-2022)

Kernels- most voted

- [https://www.kaggle.com/code/azminetoushikwasi/time-series-analysis-forecasting](https://www.kaggle.com/code/azminetoushikwasi/time-series-analysis-forecasting)

- [https://www.kaggle.com/code/cabaxiom/tps-sep-22-eda-and-linear-regression-baseline](https://www.kaggle.com/code/cabaxiom/tps-sep-22-eda-and-linear-regression-baseline)

- [https://www.kaggle.com/code/khashayarrahimi94/why-you-should-not-use-correlation](https://www.kaggle.com/code/khashayarrahimi94/why-you-should-not-use-correlation)

- [https://www.kaggle.com/code/vencerlanz09/tps-eda-9-models-explanation](https://www.kaggle.com/code/vencerlanz09/tps-eda-9-models-explanation)

- [https://www.kaggle.com/code/samuelcortinhas/tps-sept-22-timeseries-analysis](https://www.kaggle.com/code/samuelcortinhas/tps-sept-22-timeseries-analysis)

[TPS- January2022](https://www.kaggle.com/competitions/tabular-playground-series-jan-2022)

Kernels- most voted

- [https://www.kaggle.com/code/ambrosm/tpsjan22-03-linear-model](https://www.kaggle.com/code/ambrosm/tpsjan22-03-linear-model)

- [https://www.kaggle.com/code/ambrosm/tpsjan22-01-eda-which-makes-sense](https://www.kaggle.com/code/ambrosm/tpsjan22-01-eda-which-makes-sense)

- [https://www.kaggle.com/code/usharengaraju/tensorflow-tf-data-keraspreprocessinglayers-w-b](https://www.kaggle.com/code/usharengaraju/tensorflow-tf-data-keraspreprocessinglayers-w-b)

- [https://www.kaggle.com/code/teckmengwong/tps2201-hybrid-time-series](https://www.kaggle.com/code/teckmengwong/tps2201-hybrid-time-series)

- [https://www.kaggle.com/code/lordozvlad/tps-jan-fast-pycaret-with-scikit-learn-intelex](https://www.kaggle.com/code/lordozvlad/tps-jan-fast-pycaret-with-scikit-learn-intelex)

[GoDaddy - Microbusiness Density Forecasting](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/overview)

Kernels- most voted

- [https://www.kaggle.com/code/titericz/better-xgb-baseline](https://www.kaggle.com/code/titericz/better-xgb-baseline)

- [https://www.kaggle.com/code/cdeotte/linear-regression-baseline-lb-1-092](https://www.kaggle.com/code/cdeotte/linear-regression-baseline-lb-1-092)

- [https://www.kaggle.com/code/tanmay111999/gdmbf-ar-ma-arma-arima-sarima-auto-arima](https://www.kaggle.com/code/tanmay111999/gdmbf-ar-ma-arma-arima-sarima-auto-arima)

- [https://www.kaggle.com/code/cdeotte/seasonal-model-with-validation-lb-1-091](https://www.kaggle.com/code/cdeotte/seasonal-model-with-validation-lb-1-091)

- [https://www.kaggle.com/code/kimtaehun/complete-baseline-code-with-various-ml-model](https://www.kaggle.com/code/kimtaehun/complete-baseline-code-with-various-ml-model)

High scoring approaches and discussions-

- [https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/395131](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/395131) -- rank1

- [https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/395264](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/395264) -- rank2

- [https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/418287](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/418287) -- rank3

- [https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/394821](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/394821) -- rank4

Miscellaneous kernel references on time series-

- [https://www.kaggle.com/code/ravi20076/optiver-baseline-models](https://www.kaggle.com/code/ravi20076/optiver-baseline-models)

- [https://www.kaggle.com/code/kanncaa1/time-series-prediction-tutorial-with-eda](https://www.kaggle.com/code/kanncaa1/time-series-prediction-tutorial-with-eda)

- [https://www.kaggle.com/code/freespirit08/time-series-for-beginners-with-arima](https://www.kaggle.com/code/freespirit08/time-series-for-beginners-with-arima)

- [https://www.kaggle.com/code/robikscube/time-series-forecasting-with-prophet](https://www.kaggle.com/code/robikscube/time-series-forecasting-with-prophet)

- [https://www.kaggle.com/code/iamleonie/intro-to-time-series-forecasting](https://www.kaggle.com/code/iamleonie/intro-to-time-series-forecasting)

- [https://www.kaggle.com/code/robikscube/time-series-forecasting-with-machine-learning-yt](https://www.kaggle.com/code/robikscube/time-series-forecasting-with-machine-learning-yt)

- [https://www.kaggle.com/code/rohanrao/a-modern-time-series-tutorial](https://www.kaggle.com/code/rohanrao/a-modern-time-series-tutorial)

- [https://www.kaggle.com/code/cdeotte/time-series-eda](https://www.kaggle.com/code/cdeotte/time-series-eda)

- [https://www.kaggle.com/code/janiobachmann/s-p-500-time-series-forecasting-with-prophet](https://www.kaggle.com/code/janiobachmann/s-p-500-time-series-forecasting-with-prophet)

- [https://www.kaggle.com/code/robikscube/pt2-time-series-forecasting-with-xgboost](https://www.kaggle.com/code/robikscube/pt2-time-series-forecasting-with-xgboost)

Wishing you the best for the assignment and happy learning!


<a id="s030"></a>
## S030

- **source_id:** drw-crypto-market-prediction:thread:580170:3221918
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3221918
- **thread_id:** 580170
- **comment_id:** 3221918
- **author_name:** four-seven Dong
- **author_role:** unknown
- **created_at:** 2025-06-11T15:40:42.113Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/20/text`

Thanks so much for the sharing, bro! Your compilation really helped me a lot!


<a id="s031"></a>
## S031

- **source_id:** drw-crypto-market-prediction:thread:580170:3213509
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3213509
- **thread_id:** 580170
- **comment_id:** 3213509
- **author_name:** Vishal Painjane
- **author_role:** unknown
- **created_at:** 2025-05-30T05:32:06.973Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/21/text`

This is something that I really needed 🙌. Thank you sir..!


<a id="s032"></a>
## S032

- **source_id:** drw-crypto-market-prediction:thread:580170:3212061
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3212061
- **thread_id:** 580170
- **comment_id:** 3212061
- **author_name:** Amirhossein
- **author_role:** unknown
- **created_at:** 2025-05-29T08:54:55.990Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/22/text`

kind of fantastic


<a id="s033"></a>
## S033

- **source_id:** drw-crypto-market-prediction:thread:580170:3210113
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3210113
- **thread_id:** 580170
- **comment_id:** 3210113
- **author_name:** Dmitry Kiryukhin
- **author_role:** unknown
- **created_at:** 2025-05-26T18:30:39.513Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/23/text`

Amazing work bro, thanks for your information. Do you have winner-position in leaderboard for Playground Time Series Forecasting challenges?


<a id="s034"></a>
## S034

- **source_id:** drw-crypto-market-prediction:thread:580170:3209741
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3209741
- **thread_id:** 580170
- **comment_id:** 3209741
- **author_name:** Nenad Balaneskovic
- **author_role:** unknown
- **created_at:** 2025-05-26T08:50:21.747Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/24/text`

This is a great compilation! Thank you very much for sharing!


<a id="s035"></a>
## S035

- **source_id:** drw-crypto-market-prediction:thread:580170:3209407
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3209407
- **thread_id:** 580170
- **comment_id:** 3209407
- **author_name:** Harshith Vaddiparthy
- **author_role:** unknown
- **created_at:** 2025-05-25T18:19:20.083Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/25/text`

Excellent compilation [@ravi20076](https://www.kaggle.com/ravi20076)! This is exactly what the community needs. Building on your fantastic resource list, I'd like to add some **crypto-specific considerations** and **advanced techniques** that could be particularly valuable for this competition:

🚀 **Crypto-Specific Enhancements**

**1. Microstructure Features for Crypto Markets:**

- Order book imbalance ratios

- Bid-ask spread dynamics

- Volume-weighted average price (VWAP) deviations

- Tick-by-tick momentum indicators

- Cross-exchange arbitrage signals

**2. Volatility Regime Detection:**

`
 sklearn.mixture  GaussianMixture

volatility_regimes = GaussianMixture(n_components=).fit(rolling_volatility)
`

**3. Multi-timeframe Feature Engineering:**

- 1-minute, 5-minute, 15-minute, 1-hour aggregations

- Fractal dimension analysis across timeframes

- Wavelet decomposition for multi-resolution analysis

🧠 **Advanced Model Architectures**

**1. Transformer-based Approaches:**

- Temporal Fusion Transformers (TFT) for multi-horizon forecasting

- Attention mechanisms for feature importance

- Positional encoding for time-aware learning

**2. Graph Neural Networks:**

- Model cross-asset correlations as graph structures

- Capture market contagion effects

- Dynamic graph learning for evolving relationships

**3. Ensemble Strategies:**

- Bayesian Model Averaging with uncertainty quantification

- Dynamic ensemble weights based on market regime

- Multi-objective optimization (return vs. risk)

📊 **Validation Strategies for Crypto**

**1. Time-Aware Cross-Validation:**

`
 sklearn.model_selection  TimeSeriesSplit

`

**2. Walk-Forward Analysis:**

- Rolling window retraining

- Adaptive lookback periods

- Online learning with concept drift detection

🔧 **Implementation Tips**

**1. Feature Selection for High-Frequency Data:**

- Mutual Information with time lags

- Recursive Feature Elimination with cross-validation

- SHAP values for interpretability

**2. Risk Management Integration:**

- Kelly Criterion for position sizing

- Value-at-Risk (VaR) constraints

- Maximum Drawdown controls

**3. Computational Efficiency:**

- Polars for fast data processing

- Numba JIT compilation for custom indicators

- GPU acceleration with CuPy/RAPIDS

📚 **Additional Resources**

**Crypto-Specific Papers:**

- "Deep Learning for Cryptocurrency Forecasting" (2021)

- "High-Frequency Trading in Cryptocurrency Markets" (2022)

- "Market Microstructure in Digital Asset Markets" (2023)

**Advanced Time Series Libraries:**

- `darts` - Modern forecasting library

- `sktime` - Unified time series ML

- `tslearn` - Time series clustering/classification

This competition is a perfect opportunity to combine traditional quantitative finance techniques with modern ML approaches. The key is balancing model complexity with interpretability, especially given the unique characteristics of crypto markets.

Happy modeling, and may the best algorithm win! 🏆


<a id="s036"></a>
## S036

- **source_id:** drw-crypto-market-prediction:thread:580170:3209422
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3209422
- **thread_id:** 580170
- **comment_id:** 3209422
- **parent_comment_id:** 3209407
- **author_name:** Ravi Ramakrishnan
- **author_role:** unknown
- **created_at:** 2025-05-25T19:04:01.347Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/26/text`

[@harshithvaddiparthy](https://www.kaggle.com/harshithvaddiparthy) thanks for the added resources. 

Considering that the test data is not in temporal order, do you think these models will work? Perhaps they will work well for a good offline CV scheme though.


<a id="s037"></a>
## S037

- **source_id:** drw-crypto-market-prediction:thread:580170:3247065
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3247065
- **thread_id:** 580170
- **comment_id:** 3247065
- **author_name:** Taylor S. Amarel
- **author_role:** unknown
- **created_at:** 2025-07-12T03:22:50.983Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/27/text`

The Jane street code is fascinating to review!


<a id="s038"></a>
## S038

- **source_id:** drw-crypto-market-prediction:thread:580170:3239660
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3239660
- **thread_id:** 580170
- **comment_id:** 3239660
- **author_name:** YingJunMao
- **author_role:** unknown
- **created_at:** 2025-07-03T03:07:19.137Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/28/text`

Thanks for sharing


<a id="s039"></a>
## S039

- **source_id:** drw-crypto-market-prediction:thread:580170:3218368
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3218368
- **thread_id:** 580170
- **comment_id:** 3218368
- **author_name:** Xiaolei Lian
- **author_role:** unknown
- **created_at:** 2025-06-06T05:45:28.857Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/29/text`

Thanks for sharing!!


<a id="s040"></a>
## S040

- **source_id:** drw-crypto-market-prediction:thread:580170:3211361
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3211361
- **thread_id:** 580170
- **comment_id:** 3211361
- **author_name:** Olowe Daniel
- **author_role:** unknown
- **created_at:** 2025-05-28T10:45:43.870Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/30/text`

Thanks for the educational resources!


<a id="s041"></a>
## S041

- **source_id:** drw-crypto-market-prediction:thread:580170:3210906
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3210906
- **thread_id:** 580170
- **comment_id:** 3210906
- **author_name:** Zak Rashad
- **author_role:** unknown
- **created_at:** 2025-05-27T20:46:07.253Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/31/text`

This is super helpful, thank you!


<a id="s042"></a>
## S042

- **source_id:** drw-crypto-market-prediction:thread:580170:3209766
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3209766
- **thread_id:** 580170
- **comment_id:** 3209766
- **author_name:** Ms. Nancy Al Aswad
- **author_role:** unknown
- **created_at:** 2025-05-26T09:32:25.330Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/32/text`

Thanks for sharing


<a id="s043"></a>
## S043

- **source_id:** drw-crypto-market-prediction:thread:580170:3209385
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580170#comment-3209385
- **thread_id:** 580170
- **comment_id:** 3209385
- **author_name:** Stable Space
- **author_role:** unknown
- **created_at:** 2025-05-25T17:37:42.490Z
- **retrieved_at:** 2026-10-17T05:08:28.115515+00:00
- **Archive locator:** `/discussion/33/text`

Thanks for sharing


<a id="s044"></a>
## S044

- **source_id:** drw-crypto-market-prediction:thread:580744:opening
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580744
- **thread_id:** 580744
- **comment_id:** opening
- **author_name:** TheOneTheOnly
- **author_role:** unknown
- **created_at:** 2025-05-26T08:43:38.571Z
- **retrieved_at:** 2026-10-17T05:02:28.183119+00:00
- **Archive locator:** `/discussion/34/text`

What is the compatition evaluation metric?

Hi guys 

after a few speculation I come to a conclusion of R^2 ? I'm not sure tbh. Can someone please clarify ? 

thanks in advance.


<a id="s045"></a>
## S045

- **source_id:** drw-crypto-market-prediction:thread:580744:3209948
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/580744#comment-3209948
- **thread_id:** 580744
- **comment_id:** 3209948
- **author_name:** linux.do
- **author_role:** unknown
- **created_at:** 2025-05-26T14:38:40.713Z
- **retrieved_at:** 2026-10-17T05:02:28.183119+00:00
- **Archive locator:** `/discussion/35/text`

[www.kaggle.com/competitions/drw-crypto-market-prediction/overview/evaluation](www.kaggle.com/competitions/drw-crypto-market-prediction/overview/evaluation)


<a id="s046"></a>
## S046

- **source_id:** drw-crypto-market-prediction:thread:590804:opening
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/590804
- **thread_id:** 590804
- **comment_id:** opening
- **author_name:** lyraaa
- **author_role:** unknown
- **created_at:** 2025-07-23T05:48:49.742Z
- **retrieved_at:** 2026-10-17T04:32:37.867437+00:00
- **Archive locator:** `/discussion/36/text`

What's your r2_score of your prediction when your pearson coeff is below 0.15?

I got negative r2_score when the pearson coeff is about 0.1, not sure what's the problem.


<a id="s047"></a>
## S047

- **source_id:** drw-crypto-market-prediction:thread:590804:3253397
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/590804#comment-3253397
- **thread_id:** 590804
- **comment_id:** 3253397
- **author_name:** EL Younes
- **author_role:** unknown
- **created_at:** 2025-07-24T15:35:41.620Z
- **retrieved_at:** 2026-10-17T04:32:37.867437+00:00
- **Archive locator:** `/discussion/37/text`

You can expect an overestimation of R², as it is approximately equal to the square of the Pearson correlation. In your case, when your Pearson correlation is below 0.15, R²<(0.15)²~0.0225


<a id="s048"></a>
## S048

- **source_id:** drw-crypto-market-prediction:thread:590804:3253482
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/590804#comment-3253482
- **thread_id:** 590804
- **comment_id:** 3253482
- **author_name:** YannFb
- **author_role:** unknown
- **created_at:** 2025-07-24T19:01:34.527Z
- **retrieved_at:** 2026-10-17T04:32:37.867437+00:00
- **Archive locator:** `/discussion/38/text`

It depends on how you define r2. It can be either 1 - SSR/SST or (pearson)^2. In the former case  you can indeed have negative r2, and it is not an appropriate measure of fit anymore.


<a id="s049"></a>
## S049

- **source_id:** drw-crypto-market-prediction:thread:590804:3253604
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/590804#comment-3253604
- **thread_id:** 590804
- **comment_id:** 3253604
- **parent_comment_id:** 3253482
- **author_name:** lyraaa
- **author_role:** unknown
- **created_at:** 2025-07-25T01:50:18.263Z
- **retrieved_at:** 2026-10-17T04:32:37.867437+00:00
- **Archive locator:** `/discussion/39/text`

Yeah, I use 1 - SSR/SST. Why isn't it an appropriate measure of fit? Negative r2 means the prediction is worse than the average of the labels(which is about 0, actually I also use 0 instead of averaged label in 1-SSR/SST, it's still negative). Does it mean the prediction has some power in predicting sign (positive or negative), but it doesn't do good job in predicting amplitude?


<a id="s050"></a>
## S050

- **source_id:** drw-crypto-market-prediction:thread:590804:3253378
- **url:** https://www.kaggle.com/competitions/drw-crypto-market-prediction/discussion/590804#comment-3253378
- **thread_id:** 590804
- **comment_id:** 3253378
- **author_name:** Alex Zhongs
- **author_role:** unknown
- **created_at:** 2025-07-24T15:00:01.847Z
- **retrieved_at:** 2026-10-17T04:32:37.867437+00:00
- **Archive locator:** `/discussion/40/text`

I also found r2 and Pearson not correlated in the given dataset

