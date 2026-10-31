# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Prizes](#s002)
- [S003: Description](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: foundational-rules](#s006)
- [S007: Starter notebook](#s007)
- [S008: Evaluation](#s008)
- [S009: prediction-interval-competition-ii-house-price:thread:574706:opening](#s009)
- [S010: prediction-interval-competition-ii-house-price:thread:574706:3186059](#s010)
- [S011: prediction-interval-competition-ii-house-price:thread:574706:3186111](#s011)
- [S012: prediction-interval-competition-ii-house-price:thread:574706:3216049](#s012)
- [S013: prediction-interval-competition-ii-house-price:thread:574706:3224553](#s013)
- [S014: prediction-interval-competition-ii-house-price:thread:574706:3224747](#s014)
- [S015: prediction-interval-competition-ii-house-price:thread:574759:opening](#s015)
- [S016: prediction-interval-competition-ii-house-price:thread:574759:3225473](#s016)
- [S017: prediction-interval-competition-ii-house-price:thread:575081:opening](#s017)
- [S018: prediction-interval-competition-ii-house-price:thread:575081:3219204](#s018)
- [S019: prediction-interval-competition-ii-house-price:thread:575081:3215243](#s019)
- [S020: prediction-interval-competition-ii-house-price:thread:575081:3187682](#s020)
- [S021: prediction-interval-competition-ii-house-price:thread:575081:3187840](#s021)
- [S022: prediction-interval-competition-ii-house-price:thread:575081:3187580](#s022)
- [S023: prediction-interval-competition-ii-house-price:thread:575452:opening](#s023)
- [S024: prediction-interval-competition-ii-house-price:thread:575452:3235455](#s024)
- [S025: prediction-interval-competition-ii-house-price:thread:575452:3238123](#s025)
- [S026: prediction-interval-competition-ii-house-price:thread:575452:3215768](#s026)
- [S027: prediction-interval-competition-ii-house-price:thread:575452:3224751](#s027)
- [S028: prediction-interval-competition-ii-house-price:thread:575452:3224755](#s028)

<a id="s001"></a>
## S001

- **source_id:** prediction-interval-competition-ii-house-price:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/data-description
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/0/text`

## Files

*   **dataset.csv** - the data to be used for training / local validation
*   **test.csv** - the test set for which predictions should be made
*   **sample_submission.csv** - a sample submission file in the correct format



*   The target column is `sale_price`


<a id="s002"></a>
## S002

- **source_id:** prediction-interval-competition-ii-house-price:page:1:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/Prizes
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/1/text`

The three winners will win 10 digital books each and a place on a course, [see here for details](https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452).


<a id="s003"></a>
## S003

- **source_id:** prediction-interval-competition-ii-house-price:page:2:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/Description
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/2/text`

As mentioned, in regression it is not unusual to focus on what are called *point predictions* (representing central tendency). However, in this competition we are interested in producing a prediction interval (an indication of dispersion).

Our task is to create a regression model having the narrowest (most "efficient") overall prediction intervals


<a id="s004"></a>
## S004

- **source_id:** prediction-interval-competition-ii-house-price:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/rules
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/3/text`

 - Don't cheat
 - Have fun
 - If you fork a public notebook or find it to be useful, please consider upvoting it.
 - Although this is a competition, winning `!=` learning; learning `==` winning!


<a id="s005"></a>
## S005

- **source_id:** prediction-interval-competition-ii-house-price:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/abstract
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/4/text`

Welcome to the **Prediction interval competition II: House price** competition, where the objective is to create a regression model for the sale price of a house that overall has the narrowest prediction intervals. 

The evaluation of this competition is a little different (see the metric below); in many machine learning contests involving regression it is not unusual to focus on what are called *point predictions* (expectation values) \\(\hat{Y}\\). However, in this competition we are uninterested in the expectation value, but rather in producing a prediction interval,  \\(\hat{C_{\alpha}}\\). Indeed prediction intervals are often of greater practical interest than point predictions, which only form part of the story.

**Closing date:** July 27 2025


<a id="s006"></a>
## S006

- **source_id:** prediction-interval-competition-ii-house-price:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/foundational-rules
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
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

- **source_id:** prediction-interval-competition-ii-house-price:page:6:Starter notebook
- **page_name:** Starter notebook
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/Starter notebook
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/6/text`

A starter notebook, which includes an example of local evaluation of the competition metric, can be found here: [PI-II: Demo QRF](https://www.kaggle.com/code/reidjohnson/pi-ii-demo-qrf).


<a id="s008"></a>
## S008

- **source_id:** prediction-interval-competition-ii-house-price:page:7:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/overview/Evaluation
- **retrieved_at:** 2026-10-17T06:13:36.097042+00:00
- **Archive locator:** `/task_documents/7/text`

We shall assess the overall performance of our model using the mean of the [Winkler Interval score](https://otexts.com/fpp3/distaccuracy.html#winkler-score) which, for an individual interval, is given by:

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F4051350%2F226123d3441a9f94476942a008eb0ccd%2FWinkler_Interval_Score.png?generation=1699777753946637&alt=media)

where \\(y\\) is the true value, \\(u\\) is the upper prediction interval, \\(l\\) is the lower prediction interval, and \\(\alpha\\) is (100-coverage%)/100.

## Coverage
In this competition the aim is a nominal marginal coverage of **90%** (*i.e.* \\(\alpha = 0.1\\)). That is to say that 90% of the prediction intervals contain the true value (`y_true`).


## Submission file format
For each `id` in the test set, you must submit a lower and upper value for the prediction interval for each row.
The file must contain a header row `id,pi_lower,pi_upper` and have the following format:


```
id,pi_lower,pi_upper
200000,18000.6,24000.5
200001,21000.3,26000.7
200002,2000.9,4000.1
...
```

**Note**: Contestants are limited to **1 submission** to the competition Leaderboard **per day**. This is a deliberate choice so as to reduce potential `leaderboard probing' and encourage local evaluation.


<a id="s009"></a>
## S009

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:opening
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706
- **thread_id:** 574706
- **comment_id:** opening
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-04-23T12:04:37.397Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/0/text`

Welcome to Prediction interval competition II: House price

Welcome to the **House price prediction intervals competition**. In this competition rather than focusing on calculating point predictions we shall instead be concerned with producing [prediction intervals](https://en.wikipedia.org/wiki/Prediction_interval). Indeed prediction intervals are often of greater practical interest than point predictions, which only tell part of the story. The aim of the competition is to create a model with the narrowest mean prediction interval for the house price data.  To get started one can make use of the [starter notebook](https://www.kaggle.com/code/reidjohnson/pi-ii-demo-qrf) which uses the [quantile-forest](https://zillow.github.io/quantile-forest/) package. The metric for this competition is the mean [Winkler Interval score](https://www.otexts.com/fpp3/distaccuracy.html#winkler-score) where the specified coverage is 90%.

Prizes:

The three winners will win 5 digital books each, [see here for details](https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452).

All the best!


<a id="s010"></a>
## S010

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:3186059
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706#comment-3186059
- **thread_id:** 574706
- **comment_id:** 3186059
- **author_name:** yunsuxiaozi
- **author_role:** unknown
- **created_at:** 2025-04-24T06:48:28.817Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/1/text`

Note: Contestants are limited to 1 submission to the competition Leaderboard per day. This is a deliberate choice so as to reduce potential `leaderboard probing' and encourage local evaluation.

Hello, I would like to ask, what is the source of your dataset? Is there any public way to obtain the labels of the test set? If possible, then this request is meaningless.


<a id="s011"></a>
## S011

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:3186111
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706#comment-3186111
- **thread_id:** 574706
- **comment_id:** 3186111
- **parent_comment_id:** 3186059
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-04-24T07:57:06.030Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/2/text`

Dear [@yunsuxiaozi](https://www.kaggle.com/yunsuxiaozi) 

Without directly answering your question, for completeness I reproduce here the rules of the competition:

  
  
- Don't cheat

  
- Have fun

  
- If you fork a public notebook or find it to be useful, please consider upvoting it.

  
- Although this is a competition, winning `!=` learning; learning `==` winning!

  

Indeed think this competition represents a magnificent opportunity not often seen in Kaggle competitions to try out perhaps less familiar techniques such as [quantile regression](https://en.wikipedia.org/wiki/Quantile_regression) and [conformal prediction](https://en.wikipedia.org/wiki/Conformal_prediction). There will be prizes for this competition, and a criteria for winning said prizes is that winners notebooks/techniques will be reviewed in detail by the hosts beforehand. 

So, at the end of the day if somebody decides to try to take shortcuts they will come to realize, sooner or later, that the only person they really cheated was themselves. My advice; make the most, and not the least of this competition!

All the best and good luck!

carl


<a id="s012"></a>
## S012

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:3216049
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706#comment-3216049
- **thread_id:** 574706
- **comment_id:** 3216049
- **parent_comment_id:** 3186111
- **author_name:** Aasir Waseer
- **author_role:** unknown
- **created_at:** 2025-06-03T03:43:29.453Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/3/text`

Make it at least 2 submissions a day please.


<a id="s013"></a>
## S013

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:3224553
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706#comment-3224553
- **thread_id:** 574706
- **comment_id:** 3224553
- **parent_comment_id:** 3224543
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-06-15T04:41:29.467Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/6/text`

Dear [@nina2025](https://www.kaggle.com/nina2025) 

As mentioned:

  Contestants are limited to 1 submission to the competition Leaderboard per day. This is a deliberate choice so as to reduce potential `leaderboard probing' and encourage local evaluation.

All the best,

carl


<a id="s014"></a>
## S014

- **source_id:** prediction-interval-competition-ii-house-price:thread:574706:3224747
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574706#comment-3224747
- **thread_id:** 574706
- **comment_id:** 3224747
- **parent_comment_id:** 3224553
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-06-15T12:01:37.553Z
- **retrieved_at:** 2026-10-17T06:14:35.608717+00:00
- **Archive locator:** `/discussion/9/text`

Dear [@nina2025](https://www.kaggle.com/nina2025) 

  "And tell me what "probing" means"

Probing means iteratively fine tuning / optimizing ones submissions based solely on the Public leaderboard score and/or making a detailed investigation of  the contents of the test data. This represents extremely poor ML methodology, and contestants are highly encouraged to perform testing via a held-out validation set or cross validation. 

For further reading I recommend the review [Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning" by Sebastian Raschka (opens in a new tab)">"Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning" by Sebastian Raschka](https://arxiv.org/pdf/1811.12808).

All the best,

carl


<a id="s015"></a>
## S015

- **source_id:** prediction-interval-competition-ii-house-price:thread:574759:opening
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574759
- **thread_id:** 574759
- **comment_id:** opening
- **author_name:** Ravi Ramakrishnan
- **author_role:** unknown
- **created_at:** 2025-04-23T19:30:35.552Z
- **retrieved_at:** 2026-10-17T06:20:00.087870+00:00
- **Archive locator:** `/discussion/12/text`

Some artefacts for perusal

Hello all,

All the best for the competition! Hope the below references are of value here to start the assignment- 

[Prediction interval competition I: Birth weight](https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight)

Kernels

- [https://www.kaggle.com/code/paddykb/lgbm-mapie-birth-weight-oh-my](https://www.kaggle.com/code/paddykb/lgbm-mapie-birth-weight-oh-my)

- [https://www.kaggle.com/code/oscarm524/prediction-interval-eda-modeling-submission](https://www.kaggle.com/code/oscarm524/prediction-interval-eda-modeling-submission)

- [https://www.kaggle.com/code/ambrosm/pibw-divide-and-conquer](https://www.kaggle.com/code/ambrosm/pibw-divide-and-conquer)

- [https://www.kaggle.com/code/maiernator/exploration-of-baby-data-finetuned-catboost](https://www.kaggle.com/code/maiernator/exploration-of-baby-data-finetuned-catboost)

- [https://www.kaggle.com/code/yutodennou/competition-catboost](https://www.kaggle.com/code/yutodennou/competition-catboost)

Solution approaches

- [https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/485766](https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/485766) -- rank1

- [https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/496813](https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/496813) -- rank2

- [https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/487293](https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/487293) -- rank3

- [https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/491921](https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/discussion/491921) -- rank6

[House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

Kernels

- [https://www.kaggle.com/code/serigne/stacked-regressions-top-4-on-leaderboard](https://www.kaggle.com/code/serigne/stacked-regressions-top-4-on-leaderboard)

- [https://www.kaggle.com/code/apapiu/regularized-linear-models](https://www.kaggle.com/code/apapiu/regularized-linear-models)

- [https://www.kaggle.com/code/erikbruin/house-prices-lasso-xgboost-and-a-detailed-eda](https://www.kaggle.com/code/erikbruin/house-prices-lasso-xgboost-and-a-detailed-eda)

- [https://www.kaggle.com/code/dansbecker/handling-missing-values](https://www.kaggle.com/code/dansbecker/handling-missing-values)

- [https://www.kaggle.com/code/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition](https://www.kaggle.com/code/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition)

- [https://www.kaggle.com/code/juliencs/a-study-on-regression-applied-to-the-ames-dataset](https://www.kaggle.com/code/juliencs/a-study-on-regression-applied-to-the-ames-dataset)

- [https://www.kaggle.com/code/emrearslan123/house-price-prediction](https://www.kaggle.com/code/emrearslan123/house-price-prediction)

[Regression with a Tabular Paris Housing Price Dataset](https://www.kaggle.com/competitions/playground-series-s3e6)

Kernels

- [https://www.kaggle.com/code/abhi011097/ps-s3-e6-complete-eda-model-evaluation](https://www.kaggle.com/code/abhi011097/ps-s3-e6-complete-eda-model-evaluation)

- [https://www.kaggle.com/code/manthanx/ps3e6-xgboost-feature-selection-ensemble](https://www.kaggle.com/code/manthanx/ps3e6-xgboost-feature-selection-ensemble)

- [https://www.kaggle.com/code/gaytri29/regression19](https://www.kaggle.com/code/gaytri29/regression19)

- [https://www.kaggle.com/code/gopimali/eda-pycaret-bayesian](https://www.kaggle.com/code/gopimali/eda-pycaret-bayesian)

- [https://www.kaggle.com/code/kimtaehun/simple-baseline-with-brief-eda-lgbm](https://www.kaggle.com/code/kimtaehun/simple-baseline-with-brief-eda-lgbm)

Solution approaches

- [https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389140](https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389140)

- [https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389145](https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389145)

- [https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389139](https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389139)

- [https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389151](https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389151)

- [https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389391](https://www.kaggle.com/competitions/playground-series-s3e6/discussion/389391)

All the best! Happy learning and regards!


<a id="s016"></a>
## S016

- **source_id:** prediction-interval-competition-ii-house-price:thread:574759:3225473
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574759#comment-3225473
- **thread_id:** 574759
- **comment_id:** 3225473
- **author_name:** Prem Mishra_TIET
- **author_role:** unknown
- **created_at:** 2025-06-16T12:57:35.157Z
- **retrieved_at:** 2026-10-17T06:20:00.087870+00:00
- **Archive locator:** `/discussion/13/text`

nice …..


<a id="s017"></a>
## S017

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:opening
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081
- **thread_id:** 575081
- **comment_id:** opening
- **author_name:** Thomas Meißner
- **author_role:** unknown
- **created_at:** 2025-04-25T18:44:05.730Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/14/text`

How to punish missing coverage

Hi,

in the overview is written the following:

`In this competition the aim  a nominal marginal coverage of % (i.e. 𝛼=
). That  to say that at least % of the prediction intervals contain the true value (y_true).
`

From what I saw so far I could easily tune for a good Winkler score while having a coverage that is relatively far away from the desired 90%. Out of curiosity I wonder what might be good strategies to account for the coverage during hyperparameter tuning. Three ideas came to my mind:

**1.) Prune non-coverage runs**

This would be the extreme. Here we could assign an artificially high metric and return this or call optuna's prune [method](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.pruners.MedianPruner.html#optuna.pruners.MedianPruner.prune).

This would have the risk of not having any good run and thus a failing pipeline.

**2.) Multiobjective tuning**

Optuna has the functionality to tune for multiple objectives ([docs](https://optuna.readthedocs.io/en/stable/tutorial/20_recipes/002_multi_objective.html)), but here I was not sure this can be used for this purpose. So we could set both metrics (Winker score & coverage) and let Optuna tune both. Afterwards we would chose the best out of both worlds.

**3. Penalized Winkler score**

This is something i played with in my notebook. Instead of tuning for Winkler I tried to tune for a penalized version where worse coverage negatively impacts the winker score. Code example:

`winkler_sc, coverage = winkler_score(
                y_test, 
                preds.loc[:, ], 
                preds.loc[:, ], 
                return_coverage=

()

 winkler_sc ** ( - coverage) 
`

This is a very naive way of doing it I guess and so far in more than 50 trials the best one has been: `Winkler=522167.6250, Coverage=0.8523`, so this would need lots of refinement.

Curious to hear if anyone has an idea for this (or a better formula)


<a id="s018"></a>
## S018

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:3219204
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081#comment-3219204
- **thread_id:** 575081
- **comment_id:** 3219204
- **author_name:** DanteTheAbstract
- **author_role:** unknown
- **created_at:** 2025-06-07T09:41:30.070Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/15/text`

Since we are limited to one submission per day, experimenting is painfully slow. I have only tried the third option you mentioned above. So far my cv results show that increased coverage comes at the cost of lower `winkler score`.  

Unless coverage is particularly low (say < 85) I think it's better to just focus on the score, since thats how our submissions will be judged.


<a id="s019"></a>
## S019

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:3215243
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081#comment-3215243
- **thread_id:** 575081
- **comment_id:** 3215243
- **author_name:** Sergey Shnayder
- **author_role:** unknown
- **created_at:** 2025-06-01T21:20:42.443Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/16/text`

You can penalize low coverage by adding a penalty term to the Winkler score, ensuring intervals meet the 90% target


<a id="s020"></a>
## S020

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:3187682
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081#comment-3187682
- **thread_id:** 575081
- **comment_id:** 3187682
- **author_name:** Thomas Meißner
- **author_role:** unknown
- **created_at:** 2025-04-26T11:34:10.630Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/17/text`

[@carlmcbrideellis](https://www.kaggle.com/carlmcbrideellis) Will final submissions fail if the coverage is not 90%?


<a id="s021"></a>
## S021

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:3187840
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081#comment-3187840
- **thread_id:** 575081
- **comment_id:** 3187840
- **parent_comment_id:** 3187682
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-04-26T15:50:18.337Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/18/text`

Dear [@thomasmeiner](https://www.kaggle.com/thomasmeiner) 

Not this time; the Winkler score naturally punishes both under as well as over-coverage.

All the best,

carl


<a id="s022"></a>
## S022

- **source_id:** prediction-interval-competition-ii-house-price:thread:575081:3187580
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575081#comment-3187580
- **thread_id:** 575081
- **comment_id:** 3187580
- **author_name:** yunsuxiaozi
- **author_role:** unknown
- **created_at:** 2025-04-26T08:28:45.683Z
- **retrieved_at:** 2026-10-17T06:18:57.049791+00:00
- **Archive locator:** `/discussion/19/text`

[Here](https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/574842)

This is the general idea I have implemented, and my current CV is :`376226.55030169256, 0.9102314092563702`.


<a id="s023"></a>
## S023

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:opening
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452
- **thread_id:** 575452
- **comment_id:** opening
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-04-28T18:03:32.374Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/20/text`

Prizes for the Prediction interval competition II competition

The [Prediction interval competition II: House price competition](https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price) now has six digital books to be awarded to each of the top three winners*, as well as books for the best CatBoost, conformal prediction, and CatBoost + conformal prediction notebooks

- [Matt Harrison](https://store.metasnake.com/) has offered a digital book to each of the winners. The winners can choose from his books:

- [Effective XGBoost](https://store.metasnake.com/xgboost)

- [Effective Visualization](https://store.metasnake.com/effective-viz)

- [Effective Python Interviews](https://store.metasnake.com/effective-python-interviews-digital-book)

- [Effective Polars 1.0](https://store.metasnake.com/a5018258-063b-4802-b395-34e75b6eeb5e)

- [Intermediate Python Programming 2nd Edition](https://store.metasnake.com/intermediate-python-programming-2nd-edition)

- [Illustrated Guide to Python 3: Python 3.10 Version](https://store.metasnake.com/illustrated-guide-to-python-3-python-3-10-version)

- [Effective Pandas 2](https://store.metasnake.com/effective-pandas-book)

- [Giannis Tolios](https://giannis.io/) is providing three digital editions of his book [Simplifying Machine Learning with PyCaret](https://leanpub.com/pycaretbook)

- **Soledad Galli, PhD** of [Train in Data](https://www.trainindata.com/) is offering three copies of her ebook  [Feature Selection in Machine Learning with Python - 2nd Edition](https://www.trainindata.com/p/feature-selection-in-machine-learning-book)

- [Packt Publishing](https://www.packtpub.com/) is offering a choice between the following eBooks, one per winner:

- [Machine Learning with PyTorch and Scikit-Learn](https://www.amazon.com/Machine-Learning-PyTorch-Scikit-Learn-learning/dp/1801819319?link_from_packtlink=yes) by Sebastian Raschka, Yuxi (Hayden) Liu, and Vahid Mirjalili

- [In-Memory Analytics with Apache Arrow - 2nd Edition](https://www.amazon.com/Memory-Analytics-Apache-Arrow-hierarchical/dp/1835461220?link_from_packtlink=yes) by Matthew Topol

- [XGBoost for Regression Predictive Modeling and Time Series Analysis](https://www.amazon.com/XGBoost-Regression-Predictive-Modeling-Analysis/dp/180512305X?link_from_packtlink=yes) by Partha Pritam Deka and Joyce Weiner

- [Nick Desbarats](https://www.practicalreporting.com/about-nick-desbarats) is offering three copies of his ebook [Practical Charts: The Essential Guide to Creating Clear, Compelling Charts for Reports and Presentations](https://www.practicalreporting.com/practical-charts-book)

- [Valeriy Manokhin, PhD, MBA, CQF](https://www.linkedin.com/in/vmanokhin/) is offering the following prizes:

- For the highest scoring CatBoost-based solution without conformal prediction the book: ["Advanced Conformal Prediction: Reliable Uncertainty Quantification for Real-World ML"](https://valeman.gumroad.com/l/advancedconformalprediction)

- For the highest scoring conformal prediction solution without CatBoost the book ["Mastering CatBoost"](https://valeman.gumroad.com/l/MasteringCatboost)  

- For the best overall winning solution using both CatBoost and conformal prediction the following prize bundle

- Both of the books ["Mastering CatBoost"](https://valeman.gumroad.com/l/MasteringCatboost) and  ["Advanced Conformal Prediction: Reliable Uncertainty Quantification for Real-World ML"](https://valeman.gumroad.com/l/advancedconformalprediction)

- There are also three pdf's of my book [The Orange Book of Machine Learning - Green edition](https://leanpub.com/TOBoML2)

**Many, many thanks to Matt, Giannis, Soledad, Nick, Valeriy, and Packt for their generosity!**

* Notebooks will be reviewed by the hosts for suitability before the final three winners are announced and prizes awarded. 

The competition organizers are not directly responsible for the prizes.


<a id="s024"></a>
## S024

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:3235455
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452#comment-3235455
- **thread_id:** 575452
- **comment_id:** 3235455
- **author_name:** Kaustabh Ganguly
- **author_role:** unknown
- **created_at:** 2025-06-29T09:17:05.360Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/21/text`

[@predaddict](https://www.kaggle.com/predaddict) Do we need to "only" use catboost or we can use ensemble of catboost and others also to be eligible for your prize ?


<a id="s025"></a>
## S025

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:3238123
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452#comment-3238123
- **thread_id:** 575452
- **comment_id:** 3238123
- **parent_comment_id:** 3235455
- **author_name:** predict_addict
- **author_role:** unknown
- **created_at:** 2025-07-01T15:24:26.843Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/22/text`

Largely CatBoost base as in if used part of ensemble, the main part of ensemble.


<a id="s026"></a>
## S026

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:3215768
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452#comment-3215768
- **thread_id:** 575452
- **comment_id:** 3215768
- **author_name:** Muhammad Ibrahim
- **author_role:** unknown
- **created_at:** 2025-06-02T16:14:15.693Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/23/text`

Hi,

Most of the columns in the train dataset are self explanatory. However some of them are not like imp_val or wfnt


<a id="s027"></a>
## S027

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:3224751
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452#comment-3224751
- **thread_id:** 575452
- **comment_id:** 3224751
- **parent_comment_id:** 3224744
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-06-15T12:07:54.727Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/26/text`

Dear [@nina2025](https://www.kaggle.com/nina2025) 

  "WHO WILL CHECK the notebooks and FOR WHAT"

The three hosts of this competition will review the notebooks. Something that will be frowned upon are solutions that are simply blends of public notebooks, or have the appearance of incorporating the results from leaderboard probing.

All the best,

carl


<a id="s028"></a>
## S028

- **source_id:** prediction-interval-competition-ii-house-price:thread:575452:3224755
- **url:** https://www.kaggle.com/competitions/prediction-interval-competition-ii-house-price/discussion/575452#comment-3224755
- **thread_id:** 575452
- **comment_id:** 3224755
- **parent_comment_id:** 3224740
- **author_name:** Carl McBride Ellis
- **author_role:** unknown
- **created_at:** 2025-06-15T12:12:30.867Z
- **retrieved_at:** 2026-10-17T06:14:21.543679+00:00
- **Archive locator:** `/discussion/28/text`

Dear [@nina2025](https://www.kaggle.com/nina2025) 

  "there is an empty cup - what is this about?"

That is my personal Kaggle mug, and it is not part of the haul of prizes.

All the best,

carl

