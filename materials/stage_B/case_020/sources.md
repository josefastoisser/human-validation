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
- [S007: Competition Information](#s007)
- [S008: Timeline](#s008)
- [S009: Acknowledgements](#s009)
- [S010: CVPR 2025](#s010)
- [S011: Citation](#s011)
- [S012: fathomnet-2025:thread:566403:opening](#s012)
- [S013: fathomnet-2025:thread:566403:3141564](#s013)
- [S014: fathomnet-2025:thread:566403:3141572](#s014)
- [S015: fathomnet-2025:thread:566403:3141186](#s015)
- [S016: fathomnet-2025:thread:566403:3142661](#s016)
- [S017: fathomnet-2025:thread:566403:3142773](#s017)
- [S018: fathomnet-2025:thread:566403:3142779](#s018)
- [S019: fathomnet-2025:thread:580144:opening](#s019)
- [S020: fathomnet-2025:thread:580144:3207460](#s020)
- [S021: fathomnet-2025:thread:580144:3207423](#s021)

<a id="s001"></a>
## S001

- **source_id:** fathomnet-2025:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/data-description
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/0/text`

## Data Format
The datasets are formatted to adhere to the [COCO Object Detection](https://cocodataset.org/#format-data) standard. Every training image contains at least one annotation corresponding to a category from 1 to 79.

We are not able to provide images as a single downloadable archive due to FathomNet Database's Terms of Use. Images should be downloaded using the indicated coco_url field in each of the annotation files. Participants can either use the provided download.py python script or write their own. The download script will save two folders: an image and a region of interest (ROI) folder. The ROI folder contains cropped images that are saved with the following file format <image_id>_<annoation_id>.png while the image folder contains files saved as <image_id>.png, where the ids are specified in the dataset.json file provided to download.py. 

## Files
- dataset_train.json - the training images, annotations, and categories in COCO formatted json
- dataset_test.json - the evaluation images in COCO formatted json
- sample_submission.csv - a sample submission file in the correct format
- download.py - python script to download imagery from FathomNet

## Terms of Use
By downloading and using this dataset you are agreeing to FathomNet's data use policy. In particular:
The annotations are licensed under a Creative Commons Attribution-No Derivatives 4.0 International License.
The images are licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 International License. Notwithstanding the foregoing, all of the images may be used for training and development of machine learning algorithms for commercial, academic, and government purposes.
Images and annotations are provided by the copyright holders and contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed.
Please acknowledge FathomNet and MBARI when using images for publication or communication purposes regarding this competition. For all other uses of the images, users should contact the original copyright holder.
For more details please see the FathomNet Database [Terms of Use](https://database.fathomnet.org/fathomnet/#/license).

## Download

Images are made available for download by the unique URLs in the COCO-formatted object detection annotation files. The download script can be run from the command line. To install the requirements, run the following with Python >= 3.8:

```bash
pip install -r requirements.txt
```

To download the images, run the script from the command line:

```bash
python download.py path/to/dataset.json path/to/output_dir [-n NUM_DOWNLOADS]
```

The optional `-n`/`--num-downloads` parameter can be used to specify the maximum number of concurrent downloads. Setting this to a value >1 can speed up the total time it takes to download the images.

>💡 Tip
> If you've cloned this repository, the COCO dataset file is available at `dataset/dataset.json`:
> ```bash
> python download.py dataset/dataset.json dataset/
> ```



<a id="s002"></a>
## S002

- **source_id:** fathomnet-2025:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Description
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/1/text`

For this competition, we have curated data from the broader [FathomNet Database](https://database.fathomnet.org/fathomnet/#/) image set to tackle hierarchical classification. The training set contains 79 categories of marine animals of varying taxonomic ranks (e.g., family, genus, species), wherein 300 example instances of each category are provided for training. The test set contains the same 79 categories, where roughly 10 example instances of each category are provided for evaluation. The challenge is to develop a model that can accurately classify these taxa and ideally leverage their taxonomic information to do so. Developing these solutions for ocean research will enable scientists to process and explore ocean data more efficiently
Participants should not use other image sets to train their models outside of the Kaggle competition data and the FathomNet Database [website](https://database.fathomnet.org/fathomnet/#/), however they can leverage other types of outside data sources for other aspects of the competition. Pre-trained models can be used for initialization of training (e.g. [BioCLIP](https://imageomics.github.io/bioclip/), [ImageNet](https://www.image-net.org/), or [COCO](https://cocodataset.org/#home) classification or detection models provided by many deep learning packages). Teams should plan on specifying additional data sources and/or pre-trained models used when uploading results.


<a id="s003"></a>
## S003

- **source_id:** fathomnet-2025:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Evaluation
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/2/text`

The final test score is the mean of the hierarchical distances calculated across the test set, where the best average score is 0 and the worst is 12. Read below to see how the hierarchical distance is calculated. 

## Submission Format
Submission format should resemble the following:

| annotation_id | concept_name |
| --- | --- |
| 1 | Ophiuroidea |

Where an annotation_id is provided alongside a classification, or concept_name, for each ROI. 

Submissions can be any of the following taxonomic ranks: kingdom, phylum, class, order, family,  genus, and species. These ranks are part of a taxonomic tree, which organizes living things into a branching structure, starting with broad groups and narrowing down to specific species. A visual representation of this can be seen below for a specific animal Abyssocucumis abyssorum,

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F23590972%2Fdc76332649aee257aaf5051e04cfd338%2Ftaxonomic_tree_example.png?generation=1738879903021487&alt=media)

Submissions will be evaluated on taxonomic distance from the ground truth answer. To do so we use the [FathomNet WoRMS Module](https://fathomnet-py.readthedocs.io/en/latest/api.html#module-fathomnet.api.worms) to populate the full taxonomic name and a reference library of these taxonomic names is stored in the evaluation script. This reference library only considered the 79 categories within the dataset. Each submission mush correspond to one of the original 79 categories to be considered. For example, if the submission concept name is Abyssocucumis abyssorum, the score function will populate a tree like what can be seen in the visual above.

This submission is compared with the ground truth taxonomic name, and a score is given corresponding to the distance between the submission and the ground truth answer along the taxonomic tree. Example scores and visual representations are provided below.

In the following example a score of one is given, and is represented visually via the bolded line. In this case, the submission is Asteronyx of genus rank while the ground truth is Asteronyx loveni, which is at the species rank. The distance between the rank of the ground truth and the submission is 1, so the resulting score is 1. 

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F23590972%2Fd11b659dae9f99834b04f6aa0e4fea29%2Fsame%20line_example.png?generation=1738879926734632&alt=media)

In the following example a score of six is given, and visually this can be seen in the bolded line. In this case the submission taxon is Ophiacanthidae of family rank while the ground truth is Asteronyx loveni, which is of the species rank. The distance between the rank of the ground truth and the submission is 6, so the resulting score is 6. 

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F23590972%2Fb1696618c501b7e779278e29cccb7b76%2Fdifferent_rank_example.png?generation=1738879941390101&alt=media)]

## Notes:
- Each submission must be one of the 79 categories that encompasses the dataset. If a submission name is not discoverable within the map of taxonomic names referenced in the evaluation metric, then a maximum score of 12 is assigned. This includes null submissions and misspellings.
- Some classifications have more complex taxonomic ranks such as suborders and infraclasses. For this task, we will only consider the 7 taxonomic rankings: kingdom, phylum, class, order, family, genus, and species.
- The ground truth categories vary in taxonomic rank.
- An important note on the test set: the images in the test set are on average smaller than those in the training. For more context on this please review [this](https://www.kaggle.com/competitions/fathomnet-2025/discussion/573371) discussion.


<a id="s004"></a>
## S004

- **source_id:** fathomnet-2025:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/rules
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/3/text`

##ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**[See Section 3.18 for defined terms](rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions  must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

 FathomNet 2025 @ FathomNet & CVPR-FGVC
2. COMPETITION SPONSOR

  Monterey Bay Aquarium Research Institute ([MBARI](https://www.mbari.org/)), [FGVC12](https://sites.google.com/view/fgvc12), and [FathomNet](https://www.fathomnet.org/)
3. COMPETITION SPONSOR ADDRESS

 7700 Sandholdt Rd, Moss Landing, CA 95039
4. COMPETITION WEBSITE

 https://www.kaggle.com/competitions/fathomnet-2025/rules
5. TOTAL PRIZES AVAILABLE:

 Kudos
6. WINNER LICENSE TYPE:

 Open Source
7. DATA ACCESS AND USE:

 Images [CC BY-NC-ND 4.0] Annotations [CC BY-ND 4.0] for more detail see [here](https://database.fathomnet.org/fathomnet/#/license)
8. COMPETITION ACKNOWLEDGEMENTS:

  
Laura Chrobak ([MBARI](https://www.mbari.org/)), Kevin Barnard ([MBARI](https://www.mbari.org/)), Kakani Katija ([MBARI](https://www.mbari.org/))

###2. COMPETITION-SPECIFIC RULES 
In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

####1. TEAM LIMITS
a. The maximum Team size is ten (10).

b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the competition has been running.

####2. SUBMISSION LIMITS
a. You may submit a maximum of ten (10) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

####3. COMPETITION TIMELINE
a. Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s Overview > Timeline page.

####4. COMPETITION DATA

a. Data Access and Use. 

1. Competition Use and Non-Commercial & Academic Research: You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

Please acknowledge FathomNet and MBARI when using images for publication or communication purposes. For more details please see the full [FathomNet Use Policy](https://database.fathomnet.org/fathomnet/#/license).

b. Data Security. 

1. You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.

####5. WINNER LICENSE 

a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

1. Open Source: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org] (http://www.opensource.org)) that in no event limits commercial use of such code or model containing or depending on such code. 

2. For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the license in the preceding Section for that software. 

3. In the event that input data or pretrained models with an incompatible license are used to generate your winning solution, you do not need to grant an open source license in the preceding Section for that data and/or model(s). 

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.
 
####6. EXTERNAL DATA AND TOOLS

a. The general rule is that participants should only use the provided training and validation data for training models to classify the test images. We do not want participants crawling the web in search of additional data. Pretrained models may be used to construct the algorithms from publicly available academic datasets (e.g., ImageNet, iNaturalist). Please specify (openly in [Discussion](https://www.kaggle.com/competitions/fathomnet-2025/discussion?sort=hotness) section) any and all external data and/or models used for training before uploading results. 

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

  [1]: https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx
  [2]: http://www.kaggle.com/terms
  [3]: http://www.opensource.org
  [4]: http://www.opensource.org
  [5]: https://www.kaggle.com/WinningModelDocumentationGuidelines
  [6]: http://www.kaggle.com/privacy
  [7]: http://www.kaggle.com/contact


<a id="s005"></a>
## S005

- **source_id:** fathomnet-2025:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/abstract
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/4/text`

Consider marine wildlife monitoring in coastal waters near California. Daily video footage analyzed by a standard ML model shows 2 octopuses, 1 shark, and 10 jellyfish - broad taxonomic categories. But species-level identification could reveal crucial details. Is that an Octopus rubescens, commonly found in this area, or is it an Octopus cyanea usually only observed in warm, tropical waters near Hawai’i? Accurate species classification is essential for understanding ocean ecosystems. 

Hierarchical classification—architectures that structure data to capture relationships across taxonomic ranks (e.g., from broad categories like families to specific species)—can significantly improve classification accuracy, as demonstrated by [recent advances](https://imageomics.github.io/bioclip/) in machine learning. In the field of marine ecology, accurate taxonomic classification is essential for addressing fundamental questions: What species exist in a particular place? What is the ecosystem biodiversity and how does it change over time? Questions like these motivate the focus of our 2025 FathomNet Competition, aiming to push the boundaries of taxonomic accuracy and inspire innovative solutions in this space.


<a id="s006"></a>
## S006

- **source_id:** fathomnet-2025:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/foundational-rules
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
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

- **source_id:** fathomnet-2025:page:6:Competition Information
- **page_name:** Competition Information
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Competition Information
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/6/text`

This competition is presented as part of the 12th Fine-Grained Visual Categorization (FGVC12) workshop at CVPR 2025 in Nashville, Tennessee.
Please feel free to open an issue on the competition [git repo](https://github.com/fathomnet/fgvc-comp-2025) if you have a question, comment, or problem. We will also respond to threads opened on the competition discussion board here on Kaggle.


<a id="s008"></a>
## S008

- **source_id:** fathomnet-2025:page:7:Timeline
- **page_name:** Timeline
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Timeline
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/7/text`

* **March 3, 2025** - Start Date. 
* **May 26, 2025** - Final Submission Deadline. 

All deadlines are at 5:00 PM PST on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.


<a id="s009"></a>
## S009

- **source_id:** fathomnet-2025:page:8:Acknowledgements
- **page_name:** Acknowledgements
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Acknowledgements
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/8/text`

The images for this competition have been generously provided by [MBARI](https://www.mbari.org/). Annotations were made possible through the support of [FathomNet](https://fathomnet.org/) and experts from the [MBARI Video Lab](https://doi.org/10.1109/OCEANS.2006.306879). Special acknowledgment is given to Marine Biologist Linda Kuhnz for her invaluable expertise in generating a substantial portion of the groundtruth dataset.


<a id="s010"></a>
## S010

- **source_id:** fathomnet-2025:page:9:CVPR 2025
- **page_name:** CVPR 2025
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/CVPR 2025
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/9/text`

This competition is part of the Fine-Grained Visual Categorization [FGVC12](https://sites.google.com/view/fgvc12) workshop at the Computer Vision and Pattern Recognition (CVPR)  [Conference](https://cvpr.thecvf.com/Conferences/2024). A panel will review the top submissions for the competition based on the description of the methods provided. From this, a subset of participants may be invited to present their results at the workshop, as a poster presentation. We highly encourage teams to share a public repository with their submission to aid the community in learning from one another’s approach. Attending the workshop is not required to participate in the competition, however only teams that are attending the workshop will be considered to present their work.
There is no cash prize for this competition. PLEASE NOTE: CVPR frequently sells out early, and we cannot guarantee CVPR registration after the competition's end. If you are interested in attending CVPR, please plan ahead.
You can see a list of all FGVC12 competitions [here](https://sites.google.com/view/fgvc12/competitions?authuser=0).


<a id="s011"></a>
## S011

- **source_id:** fathomnet-2025:page:10:Citation
- **page_name:** Citation
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/overview/Citation
- **retrieved_at:** 2026-10-17T10:05:55.663844+00:00
- **Archive locator:** `/task_documents/10/text`

Laura Chrobak and Kevin Barnard. FathomNet2025. https://kaggle.com/competitions/fathomnet-2025, 2025. Kaggle.


<a id="s012"></a>
## S012

- **source_id:** fathomnet-2025:thread:566403:opening
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403
- **thread_id:** 566403
- **comment_id:** opening
- **author_name:** Laura
- **author_role:** unknown
- **created_at:** 2025-03-05T09:45:59.544Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/0/text`

broken links

Hi, there are some broken links in your description :( I also cannot access the git repo: [https://github.com/fathomnet/fgvc-comp-2025](https://github.com/fathomnet/fgvc-comp-2025)


<a id="s013"></a>
## S013

- **source_id:** fathomnet-2025:thread:566403:3141564
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3141564
- **thread_id:** 566403
- **comment_id:** 3141564
- **author_name:** Laura Chrobak
- **author_role:** unknown
- **created_at:** 2025-03-05T17:56:17.433Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/1/text`

Hi [@laura1](https://www.kaggle.com/laura1) Thanks for flagging this- we had some recent updates to the FathomNet urls which caused the urls to break. The links in the description should be fixed now and we will update the image urls in the data shortly. Really appreciate you bringing this to our attention!


<a id="s014"></a>
## S014

- **source_id:** fathomnet-2025:thread:566403:3141572
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3141572
- **thread_id:** 566403
- **comment_id:** 3141572
- **parent_comment_id:** 3141564
- **author_name:** Laura Chrobak
- **author_role:** unknown
- **created_at:** 2025-03-05T18:04:37.993Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/2/text`

The dataset paths are updated :)


<a id="s015"></a>
## S015

- **source_id:** fathomnet-2025:thread:566403:3141186
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3141186
- **thread_id:** 566403
- **comment_id:** 3141186
- **author_name:** Laura
- **author_role:** unknown
- **created_at:** 2025-03-05T09:54:41.180Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/3/text`

I also cannot download the data… "RuntimeError: Cannot send a request, as the client has been closed."


<a id="s016"></a>
## S016

- **source_id:** fathomnet-2025:thread:566403:3142661
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3142661
- **thread_id:** 566403
- **comment_id:** 3142661
- **parent_comment_id:** 3141186
- **author_name:** Laura
- **author_role:** unknown
- **created_at:** 2025-03-06T15:19:29.070Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/4/text`

Hi [@lauravchrobak](https://www.kaggle.com/lauravchrobak), thanks for getting back to me! sadly I still cannot download the data (I still get the same runtime error), any ideas?


<a id="s017"></a>
## S017

- **source_id:** fathomnet-2025:thread:566403:3142773
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3142773
- **thread_id:** 566403
- **comment_id:** 3142773
- **parent_comment_id:** 3142661
- **author_name:** Laura Chrobak
- **author_role:** unknown
- **created_at:** 2025-03-06T16:48:18.900Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/5/text`

Hi [@laura1](https://www.kaggle.com/laura1), how are you trying to download the data? I ask because there are several methods so it will help me to understand where you are running into the problem specifically.


<a id="s018"></a>
## S018

- **source_id:** fathomnet-2025:thread:566403:3142779
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/566403#comment-3142779
- **thread_id:** 566403
- **comment_id:** 3142779
- **parent_comment_id:** 3142661
- **author_name:** Brian Schlining
- **author_role:** unknown
- **created_at:** 2025-03-06T16:55:06.720Z
- **retrieved_at:** 2026-10-17T21:40:08.676538+00:00
- **Archive locator:** `/discussion/6/text`

[@laura1](https://www.kaggle.com/laura1) 

Here's the steps I've done to start a download and it seems to be working well. Note that I'm on a very fast fiber connection. I'm not sure if your connection speed is the source of the troubles.

`git clone git@github.:fathomnet/fgvc--.git
 fgvc--
conda create --name fgvc-- =
conda activate fgvc--
pip install -r requirements.txt
 - ./temp/data/train
# Download All from https://www.kaggle./competitions/fathomnet-/data
#   in ./temp/fathomnet-
 download. temp/fathomnet-/dataset_train.json temp/data/train/
`


<a id="s019"></a>
## S019

- **source_id:** fathomnet-2025:thread:580144:opening
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/580144
- **thread_id:** 580144
- **comment_id:** opening
- **author_name:** Bodhisatta Maiti
- **author_role:** unknown
- **created_at:** 2025-05-22T17:34:51.823Z
- **retrieved_at:** 2026-10-17T21:40:16.525731+00:00
- **Archive locator:** `/discussion/7/text`

Queries regarding taxonomy

Hi [@lauravchrobak](https://www.kaggle.com/lauravchrobak) ,

I was going through the taxonomy hierarchy information gathered from fathomnet-worms. For certain labels/categories i observed that they are not listed anywhere within the 7 taxonomic rankings. I wanted to recheck if this information retrieved from the worms module is correct:

label Tunicata

{'kingdom': 'Animalia', 'phylum': 'Chordata'}

label Caridea

{'kingdom': 'Animalia', 'phylum': 'Arthropoda', 'class': 'Malacostraca', 'order': 'Decapoda'}

label Actinopterygii

{'kingdom': 'Animalia', 'phylum': 'Chordata'}

label Acanthascinae

{'kingdom': 'Animalia', 'phylum': 'Porifera', 'class': 'Hexactinellida', 'order': 'Lyssacinosida', 'family': 'Rossellidae'}

My next question is with respect to the submissions. In the competition overview tab, this is mentioned: Each submission must be one of the 79 categories that encompasses the dataset.

for example, the label Octopus rubescens has this taxonomy hierarchy:

{'kingdom': 'Animalia', 'phylum': 'Mollusca', 'class': 'Cephalopoda', 'order': 'Octopoda', 'family': 'Octopodidae', 'genus': 'Octopus', 'species': 'Octopus rubescens'}

for example, 'Octopus rubescens' exists in the list of 79 categories. If the model predicts correctly at the genus level 'Octopus', but 'Octopus' doesn't exist in the list of 79 categories, would the evaluation algorithm still award a score?

Please let me know.

Thanks.

With Regards,

Bodhisatta


<a id="s020"></a>
## S020

- **source_id:** fathomnet-2025:thread:580144:3207460
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/580144#comment-3207460
- **thread_id:** 580144
- **comment_id:** 3207460
- **author_name:** Laura Chrobak
- **author_role:** unknown
- **created_at:** 2025-05-22T18:50:48.183Z
- **retrieved_at:** 2026-10-17T21:40:16.525731+00:00
- **Archive locator:** `/discussion/8/text`

Hi [@bodhisattamaiti](https://www.kaggle.com/bodhisattamaiti), thank you for your questions!

As [@sumit08](https://www.kaggle.com/sumit08) pointed out, the concepts in this dataset vary in their taxonomic rank, so not every label will have all seven taxonomic levels represented - this variation is expected.

Regarding your question about the evaluation metric (link [here](https://www.kaggle.com/code/lauravchrobak/taxonomic-hierarchical-distance)): the evaluation currently only accepts predictions that match one of the 79 lowest-level concept names in the dictionary. So in the case you described, if the model predicts "Octopus" (a genus), but the correct label is "Octopus rubescens" (a species) and only the latter exists in the dictionary key, the prediction would receive the maximum penalty score of 12..

You're absolutely right to flag this as an area of improvement -  it's a known limitation of the current evaluation metric. A more ideal evaluation might account for hierarchical proximity (e.g., rewarding predictions that are close in taxonomy even if not exact matches), but we constrained the evaluation to the 79 target concepts in order to keep the problem scope manageable in the evaluation code.

Developing useful and fair evaluation methods for hierarchical classifiers remains an active area of research. In fact, one of our hopes for this competition is that it highlights the need for further work in this space.


<a id="s021"></a>
## S021

- **source_id:** fathomnet-2025:thread:580144:3207423
- **url:** https://www.kaggle.com/competitions/fathomnet-2025/discussion/580144#comment-3207423
- **thread_id:** 580144
- **comment_id:** 3207423
- **author_name:** Sumit_08
- **author_role:** unknown
- **created_at:** 2025-05-22T17:38:19.353Z
- **retrieved_at:** 2026-10-17T21:40:16.525731+00:00
- **Archive locator:** `/discussion/9/text`

You're absolutely right in noting that some of the labels (such as Tunicata or Actinopterygii) retrieved from the fathomnet-worms module are missing certain taxonomic ranks. This is expected in some cases, particularly for higher-level taxa or clades that are not always broken down into all seven Linnaean ranks in WoRMS. For example, Tunicata is a subphylum within Chordata, and Actinopterygii is a class-level clade that may not always have complete downstream hierarchy listed if the specific lineage isn't resolved.

