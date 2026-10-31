# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: rules](#s002)
- [S003: abstract](#s003)
- [S004: foundational-rules](#s004)

<a id="s001"></a>
## S001

- **source_id:** alt-score-data-science-competition:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/alt-score-data-science-competition/overview/data-description
- **retrieved_at:** 2026-10-20T08:35:55.898851+00:00
- **Archive locator:** `/task_documents/0/text`

# **Dataset Description**

This section provides a detailed description of the data files and the information they contain. Understanding the dataset is crucial for effective feature engineering and predictive modeling. Below, you'll find the answers to common questions and an explanation of each file and column included in the dataset.

## **Files**
1. **`train.csv`** - The training set, containing H3 hexagon IDs and their corresponding cost of living values.
   - **Columns:**
     - `hex_id`: The H3 hexagon index representing a geographic area.
     - `cost_of_living`: A value between 0 and 1 indicating the cost of living in that hexagon area.

3. **`mobility.parquet`** - A dataset containing device-level mobility data, provided in Parquet format. Use this data to derive features for your model.
   - **Columns:**
     - `device_id`: An anonymized identifier for each mobile device.
     - `lat`: Latitude of the recorded location.
     - `lon`: Longitude of the recorded location.
     - `timestamp`: Timestamp indicating when the data point was recorded.

4. **`test.csv`** - A sample submission file provided to guide you in formatting your final predictions. Use this as a reference to ensure your submission matches the required structure.
   - **Columns:**
     - `hex_id`: The H3 hexagon index corresponding to a geographic area.
     - `cost_of_living`: Your predicted value for the cost of living, ranging from 0 to 1.

## **Columns in `train.csv`**
- **`hex_id`**: An H3 hexagon index that corresponds to a geographic area. Each hexagon covers a portion of the map and serves as a spatial aggregation unit for your predictions.
- **`cost_of_living`**: A value between 0 and 1 representing the cost of living for the respective hexagon area.

## **Columns in `test.csv`**
- **`hex_id`**: An H3 hexagon index that corresponds to a geographic area.
- **`cost_of_living`**: This column is empty and should be filled with your predictions.

## **Columns in `mobility_data.parquet`**
- **`device_id`**: A unique anonymized identifier for each mobile device in the dataset.
- **`lat`**: The latitude where the device was observed.
- **`lon`**: The longitude where the device was observed.
- **`timestamp`**: A UNIX timestamp representing the precise time when the observation occurred.

## **Frequently Asked Questions**
1. **What files do I need?**
   - You will primarily work with `train.csv` to build your model and `test.csv` to generate predictions. Use `mobility_data.parquet` to extract features that could improve the predictive power of your model.
   
2. **What should I expect the data format to be?**
   - The data files are in CSV and Parquet formats. Each row in `train.csv` and `test.csv` corresponds to a geographic area, while `mobility_data.parquet` contains device-level observations. Predictions are submitted as a CSV file matching the format in `test.csv`.

3. **What am I predicting?**
   - You are predicting the `cost_of_living`, a value between 0 and 1, for each geographic hexagon (`hex_id`) in the `test.csv` file.

4. **What acronyms will I encounter?**
   - **H3**: A geospatial indexing system that divides the world into hexagonal cells, used for representing geographic areas.
   - **CSV**: Comma-separated values, the format for `train.csv` and `test.csv`.
   - **Parquet**: A columnar storage file format, used for `mobility_data.parquet`.

## **Submission Example**
Below is an example of the expected CSV format for your submission:

```csv
hex_id,cost_of_living
8a2a1072b59ffff,0.45
8a2a1072a7bffff,0.60
8a2a1072959ffff,0.33
8a2a1072b0fffff,0.75
8a2a107282bffff,0.25
```



<a id="s002"></a>
## S002

- **source_id:** alt-score-data-science-competition:page:1:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/alt-score-data-science-competition/overview/rules
- **retrieved_at:** 2026-10-20T08:35:55.898851+00:00
- **Archive locator:** `/task_documents/1/text`

# **Competition Rules**

To ensure a fair and engaging competition, please adhere to the following rules. These guidelines are set to create a level playing field for all participants while encouraging creativity and transparency.

## **General Rules**
1. **Data Usage:**
   - Participants are encouraged to use external data sources to enrich their models. Any additional data used must be publicly available or shared openly with a source link.
   - Do not attempt to re-identify anonymized data or use private datasets that cannot be shared with the broader community.

2. **Submissions:**
   - Each team is allowed a maximum of 20 submissions per day.
   - Your final submission should be a CSV file following the format outlined in the competition details. The file should contain the columns `hex_id` and `cost_of_living`.
   
3. **Code and Model Requirements:**
   - Participants will be asked to show the GitHub repository with all the code used for the competition when called to interview. The code should be in Python, well-organized.
   - The repository should be public or accessible to the competition organizers. It must include a `README.md` file that details your methodology, data sources, and any feature engineering steps.
   - Ensure that your code does not include any malicious elements.

## **Evaluation Criteria**
1. **Primary Metric:** The primary evaluation metric is **Mean Absolute Error (MAE)**, which will measure the accuracy of your predictions for `cost_of_living`.
2. **Secondary Metrics:**
   - **Feature Engineering**: The creativity and effectiveness of feature engineering will be closely examined. This includes the use of external variables, meaningful transformations, and feature selection.
   - **Predictive Power**: We will assess the strength of the features you create in predicting the target variable.
   - **Code Quality**: Your code will be reviewed for clarity, organization, efficiency, and reproducibility.
   

## **Leaderboard Rules**
1. The public leaderboard will be based on 50% of the test data, with the remaining 50% reserved for the final evaluation on the private leaderboard.
2. The leaderboard rankings during the competition are provisional and may change based on the final evaluation using the private test set.

## **Intellectual Property**
1. By participating in the competition, you agree that the code, models, and data processing techniques you submit may be reviewed and potentially shared as learning material or examples.

## **Prohibited Actions**
1. Do not engage in any form of **collusion**, including sharing code or predictions between teams.
2. **Cheating** or using unfair methods to manipulate the leaderboard, such as exploiting bugs, is strictly prohibited.
3. Avoid any form of **reverse engineering** of the dataset to access private or sensitive information.
4. Any attempt to tamper with the competition platform, submission system, or evaluation process will result in disqualification.


## **Support and Questions**
- A discussion forum will be available for participants to ask questions, share insights, and discuss the competition.
- The competition organizers will monitor the forum and provide clarifications as needed. However, organizers will not provide direct assistance with code or models.
- If you have any concerns or suspect rule violations, please report them directly to the organizers through the provided contact channels.

## **Final Decision**
The competition organizers' decisions are final and binding in all matters related to the competition, including rule clarifications and dispute resolutions.

## **Good Luck!**
We wish all participants the best of luck!



<a id="s003"></a>
## S003

- **source_id:** alt-score-data-science-competition:page:2:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/alt-score-data-science-competition/overview/abstract
- **retrieved_at:** 2026-10-20T08:35:55.898851+00:00
- **Archive locator:** `/task_documents/2/text`

This challenge is about as close as you can get to a day at AltScore - immersed in data, writing code, and focused on hitting a goal. 

You’ll face plenty of uncertainty, and the options aren’t endless, so you have to be resourceful. It’s about making sense of raw information, turning complexity into something useful, and finding that balance between creativity and accuracy. Every choice matters as you adjust your models, fine-tune your features, and learn as you go. It’s a chance to show how you handle real-world problems where the path to the answer isn’t always clear.

## **Objective**
Participants are challenged to estimate the **cost of living** (a value between 0 and 1) in different regions of LATAM based on mobility data. You will be provided with a dataset that contains anonymized device-level information, including geographic coordinates and timestamps. Your task is to transform this data into meaningful features that can accurately predict the cost of living.

## **Dataset Provided**
- **Columns:**
  - `device_id`: An anonymized identifier for each mobile device.
  - `lat`: Latitude of the recorded location.
  - `lon`: Longitude of the recorded location.
  - `timestamp`: The time of the record.
  
Participants are encouraged to utilize external datasets and variables to enrich their predictions. You have complete freedom to incorporate any additional sources of information you think could improve your model's performance.

## **Submission Format**
Your submission should be a CSV file with the following columns:
- **`hex_id`**: The H3 hexagon index that represents a specific geographic area.
- **`cost_of_living`**: Your predicted value for the cost of living in that hexagon, ranging between 0 and 1.


## **Guidelines**
- **Feature Engineering Focus**: We are particularly interested in the creativity and quality of your feature engineering. How well you transform and enrich the data will be a key factor in evaluation.
- **Predictive Power**: In addition to feature engineering, we also care about the predictive power of the features you create. The features should have a strong relationship with the target variable and demonstrate clear predictive capabilities.
- **Use of External Variables**: Feel free to use additional data sources you believe could be relevant to determining cost of living.
- **Model Flexibility**: We are less concerned with the specific model you use. Whether it's a simple linear regression or a complex ensemble method, what matters most is how well you utilize and engineer features from the provided dataset and any external variables you choose to include.

## **Evaluation Metrics**
1. **Feature Engineering and research**: The emphasis will be on the quality of feature engineering, including the predictive power of the features and how participants derive insights from the raw data and external sources.
2. **Root Mean Squared Error (RMSE)**: Predictions will be evaluated using RMSE to measure the accuracy of cost-of-living predictions.
3. **Code Quality**: If called to an interview, candidates must show a GitHub repository with all the code used for the competition, **written in Python**. This repo will be reviewed for code quality, organization, reproducibility, and understanding of the problem.

## **Resources**
Participants will be provided with:
- A dataset containing device-level location information.
- A dataset with examples of hex_id and it's cost_of_living to be used as a train dataset.
- A dataset with only hex_id that should be completed with the cost_of_living for submission.
- Documentation and sample scripts to get started with H3 hexagon aggregation.

## **Submission Example**
Below is an example of the expected CSV format for your submission:

```csv
hex_id,cost_of_living
8a2a1072b59ffff,0.45
8a2a1072a7bffff,0.60
8a2a1072959ffff,0.33
8a2a1072b0fffff,0.75
8a2a107282bffff,0.25
```

# **Frequently Asked Questions**

## **What is the H3 Methodology?**
H3 is a geospatial indexing system that divides the world into a grid of hexagonal cells. Each cell is identified by a unique index, which allows for consistent spatial aggregation and analysis. The H3 system is particularly useful for geographic data, as hexagons provide a uniform way to represent areas with minimal distortion compared to square grids.

For a detailed explanation of the H3 methodology, you can refer to the official [H3 documentation](https://h3geo.org/docs/).

### **How Do I Convert Latitude and Longitude to an H3 Index in Python?**
Below is a Python snippet using the `h3` library to convert latitude and longitude coordinates to an H3 index:

```python
# First, make sure to install the h3-py library:
# pip install h3

import h3

# Example coordinates
latitude = 37.7749 
longitude = -122.4194 
resolution = 9  # H3 resolution level (higher means smaller hexagons)

# Convert lat/lon to an H3 index
h3_index = h3.latlng_to_cell(latitude, longitude, resolution)

print(f"H3 Index: {h3_index}")
```



<a id="s004"></a>
## S004

- **source_id:** alt-score-data-science-competition:page:3:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/alt-score-data-science-competition/overview/foundational-rules
- **retrieved_at:** 2026-10-20T08:35:55.898851+00:00
- **Archive locator:** `/task_documents/3/text`

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

