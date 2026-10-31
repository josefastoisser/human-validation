# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Announcements](#s002)
- [S003: Important Dates](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: foundational-rules](#s006)
- [S007: Final Submission](#s007)
- [S008: Description](#s008)
- [S009: Evaluation](#s009)
- [S010: Self Evaluation](#s010)
- [S011: Leaderboard Ranking](#s011)
- [S012: Submission File](#s012)
- [S013: Prizes](#s013)
- [S014: Open-Access Policy](#s014)
- [S015: Organizers](#s015)
- [S016: Sponsor](#s016)
- [S017: Acknowledgment](#s017)
- [S018: filament-segmentation-2026:thread:728062:opening](#s018)
- [S019: filament-segmentation-2026:thread:728062:3507555](#s019)
- [S020: filament-segmentation-2026:thread:728062:3501408](#s020)
- [S021: filament-segmentation-2026:thread:728062:3501343](#s021)
- [S022: filament-segmentation-2026:thread:728062:3501351](#s022)
- [S023: filament-segmentation-2026:thread:728062:3507227](#s023)
- [S024: filament-segmentation-2026:thread:728062:3508024](#s024)
- [S025: filament-segmentation-2026:thread:729396:opening](#s025)
- [S026: filament-segmentation-2026:thread:729396:3514996](#s026)
- [S027: filament-segmentation-2026:thread:729396:3504225](#s027)
- [S028: filament-segmentation-2026:thread:729487:opening](#s028)
- [S029: filament-segmentation-2026:thread:735256:opening](#s029)
- [S030: filament-segmentation-2026:thread:735256:3512956](#s030)
- [S031: filament-segmentation-2026:thread:736543:opening](#s031)
- [S032: filament-segmentation-2026:thread:736543:3515337](#s032)
- [S033: filament-segmentation-2026:thread:740400:opening](#s033)
- [S034: filament-segmentation-2026:thread:740400:3522678](#s034)
- [S035: filament-segmentation-2026:thread:740400:3525175](#s035)
- [S036: filament-segmentation-2026:thread:740400:3525344](#s036)
- [S037: filament-segmentation-2026:thread:740400:3525565](#s037)
- [S038: filament-segmentation-2026:thread:740400:3525685](#s038)

<a id="s001"></a>
## S001

- **source_id:** filament-segmentation-2026:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/data-description
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/0/text`

For this competition, you will need (1) images and (2) ground-truth annotations. Both of these items can be downloaded in this page. Below, click on the "Download All" button, and then choose "Download as zip". When the download is complete, unzip the downloaded file. The content of the unzipped file is shown below:

```text
MAGFiLO_1.0_Kaggle_2026/
|-- train/
|   |-- train_images/
|   |-- MAGFiLO_1.0_Annotations_kaggle2026_train.json
|-- test/
    |-- test_images/
```

### Images and Annotations
The goal is to identify solar filaments from solar images. Solar filaments are best visible in H-Alpha images. Therefore, we use the observations (images) captured by H-Alpha instruments of Global Oscillations Network Group ([GONG](https://en.wikipedia.org/wiki/Global_Oscillations_Network_Group)). These are the same images used for creating the manual annotation of solar filaments available in MAGFiLO.

These H-Alpha observations are images of size `2048 x 2048` pixels, which, for the sake of this competition, have been converted from their original FITS format to the standard 8-bit JPEG format. Contestants should note that these images are grayscale and should not be processed as color images (e.g., RGB images).

Each observation's capture time and instrument are encoded in its file name as follows: `YYYYMMDDHHMMSSII`. For example, `20260901165702Bh.jpeg` corresponds to the capture time of September 1, 2026, at 16:57:02, using the Big Bear (Bh) Solar Observatory. 

The H-alpha observations in MAGFiLO often contain multiple filaments. Further, all filaments present within one image may be annotated multiple times by different annotators, independently. As an example, the image with `file_name` as `20260901165702Bh.jpeg` may have two sets of annotations, e.g., `010101-20260901165702Bh` and `010102-20260901165702Bh` (note that they are different by only one digit). You may treat those images simply as "different" images.

For this competition, the ground-truth data are the filament **segmentations**. For storage efficiency, instead of binary masks, we store segmentations as polygons in [RLE](https://en.wikipedia.org/wiki/Run-length_encoding) format. The conversion (RLE <-> Binary Masks) are lossless. 

The annotations are structured into the [COCO-style data format](https://cocodataset.org/#format-data). That means, you can take advantage of many common operations using the `pycocotools` python package (see [https://github.com/ppwwyyxx/cocoapi](https://github.com/ppwwyyxx/cocoapi)). 

### More Info about JSON File

```json
{
"info": info,
"images": [image],
"annotations": [annotation],
"licenses": [license],
"categories": [category],
}

info{
"year": int,
"version": str,
"description": str,
"contributor": str,
"url": str,
"date_created": datetime,
}

license{
"id": int,
"name": str,
"url": str,
}

categories[
{
   "id": int,
   "name": str,
   "supercategory": str,
}]

annotation{
"id": str,
"image_id": int,
"category_id": int,
"segmentation": [[]],
"area": float,
"spine": [],
"bbox": [x, y, width, height],
"iscrowd": 0 or 1,
}

image{
"id": str,
"width": int,
"height": int,
"file_name": str,
"license": int,
"date_captured": datetime,
}
```

- **info:** corresponds to a dictionary containing metadata description of the dataset.
- **images:** corresponds to a list of image dictionaries.
- **annotations:** corresponds to a list of annotation dictionaries.
- **licenses:** corresponds to a dictionary containing the license information of the GONG H-Alpha images.
- **categories:** corresponds to a list of category dictionaries. 
- **image:** corresponds to a dictionary containing information  about an annotated image, including its name and downloadable URL.
- **annotation:** corresponds to a dictionary containing information about an annotated filament, including its segmentation and bounding box.
- **license:** corresponds to a dictionary describing the license of an image.
- **category:** corresponds to a dictionary containing the category information that each filament may be described with. 

#### More Information on Annotations

- A bounding box in `annotation["bbox"]` is represented with a list of 4 values,  `[x, y, width, height]` , where `x,y` corresponds to the top-left corner of the box. All values are in pixels unit.
- A segmentation in `annotation["segmentation"]` is a list of floats representing a closed path. Each path forms a polygon capturing a filament's shape. A polygon made with n points is represented as `[x_0, y_0, x_1, y_1, ..., x_(n-1), y_(n-1)]` where `x_0 = x_(n-1)` and `y_0 = y_(n-1)`.
- The area in  `annotation["area"]` is the segmentation area (not the bbox area). This is computed using pycocoapi package, by first converting the polygon into RLE.
- A spine in `annotation["spine"]` is a list of floats representing a path. Each path captures a filament's spine. Disconnected line segments are not allowed. A spine with `n` points is represented as `[x_0, y_0, x_1, y_1, ..., x_(n-1), y_(n-1)]`.
- The tag `annotation["iscrowd"]` is always zero indicating that each segmentation corresponds to a single filaments (i.e., no group of filaments is annotated together).
- Although `annotation["segmentation"]` is a list, it only contains one polygon. That is, each filament is annotated using a single-piece polygon.
- The class labels listed in `category["name"]` are: "Left" (id = 1), "Right", (id = 2), "Unidentifiable" (id = 3), and "Ambiguous" (id = 4).
- The image ids in `image["id"]`  is a string that shows the annotator's batch name, as well as the  name (together, unique). For example, id `010401-20160920230134Lh` indicates that the image with name `20160920230134Lh.jpg` is annotated by the annotator `010401`, and it might have also been annotated by two other annotators, `010402` and `010403`, in the same group.
- The annotation ids in `annotation["id"]` is a string (e.g., `a7639f8a-c76d-43a7-b392-e75842262b75`) generated by the annotation platform, which is unique for filaments. 


<a id="s002"></a>
## S002

- **source_id:** filament-segmentation-2026:page:1:Announcements
- **page_name:** Announcements
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Announcements
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/1/text`

- **[Sep 20, 2026]** Reminder: The SABID workshop of IEEE BigData Conference is interested in the topic of this challenge. Please consider submitting your reports to this workshop: https://sites.google.com/view/sabid2026/home .   
- **[Aug 20, 2026]** Looking at some submissions, it is clear to us that some participants are spending their time and energy on hacking the system rather tackling the actual problem. We encourage honest participants to continue their work without comparing their scores with others. Any PQ score of greater than 0.35 is of great value to us.  
- **[Aug 12, 2026]** Our leaderboard is now re-scored. 
- **[Aug 9, 2026]** We added a self-evaluation notebook for participants. Please see the "Self Evaluation" section.
- **[Aug 7, 2026]** We are going to update our evaluation methodology to address the raised issues. The details are explained below. The new scoring metric will be in effect soon; all previous submissions will be updated as well. The exact time the leaderboard is to be updated depends on when Kaggle resets the scoring mechanism.


<a id="s003"></a>
## S003

- **source_id:** filament-segmentation-2026:page:2:Important Dates
- **page_name:** Important Dates
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Important Dates
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/2/text`

- July 10, 2026: Competition is launched. Contestants can start working on the challenge.
- Nov 15, 2026: Deadline for contest teams to submit final reports and solutions.
- Nov 30, 2026: The winning teams will be announced.
- Dec 14-17, 2026: (Optional) IEEE BigData conference will take place at Phoenix, AZ. The winners of this BigDataCup competition (as well as all other BigDataCups) will be announced


<a id="s004"></a>
## S004

- **source_id:** filament-segmentation-2026:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/rules
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/3/text`

##ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**[See Section 3.18 for defined terms](rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions  must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

 Solar Filament Segmentation Challenge 2026
2. COMPETITION SPONSOR

 The U.S. National Science Foundation (NSF) National Solar Observatory (NSO)
3. COMPETITION SPONSOR ADDRESS

National Solar Observatory
3665 Discovery Drive
Boulder
CO 80303
4. COMPETITION WEBSITE

 https://www.kaggle.com/competitions/filament-segmentation-2026/
5. TOTAL PRIZES AVAILABLE: $3,000

 
First Prize: (Dynamic)
Second Prize: (Dynamic)
Third Prize: (Dynamic)

###2. COMPETITION-SPECIFIC RULES 
In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

####1. TEAM LIMITS
a. The maximum Team size is five (5).

b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the competition has been running.

####2. SUBMISSION LIMITS
a. You may submit a maximum of five (5) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

####3. COMPETITION TIMELINE
a. Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s Overview > Timeline page.

####4. COMPETITION DATA

a. Data Access and Use.

*Competition Use and Non-Commercial & Academic Research is checked*: You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

####5. WINNER LICENSE

a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

*Open Source: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org] (http://www.opensource.org)) that in no event limits commercial use of such code or model containing or depending on such code. 

For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the license in the preceding Section for that software. 

In the event that input data or pretrained models with an incompatible license are used to generate your winning solution, you do not need to grant an open source license in the preceding Section for that data and/or model(s). 

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.
 
####6. EXTERNAL DATA AND TOOLS

a. You may use data other than the Competition Data (“External Data”) to develop and test your Submissions. However, you will ensure the External Data is either publicly available and equally accessible to use by all Participants of the Competition for purposes of the competition at no cost to the other Participants, or satisfies the Reasonableness criteria as outlined in Section 2.6.b below. The ability to use External Data under this Section does not limit your other obligations under these Competition Rules, including but not limited to Section 2.8 (Winners Obligations). 

b. The use of external data and models is acceptable unless specifically prohibited by the Host. Because of the potential costs or restrictions (e.g., “geo restrictions”) associated with obtaining rights to use external data or certain software and associated tools, their use must be “reasonably accessible to all” and of “minimal cost”. Also, regardless of the cost challenges as they might affect all Participants during the course of the competition, the costs of potentially procuring a license for software used to generate a Submission, must also be considered. The Host will employ an assessment of whether or not the following criteria can exclude the use of the particular LLM, data set(s), or tool(s):

1. Are Participants being excluded from a competition because of the "excessive" costs for access to certain LLMs, external data, or tools that might be used by other Participants. The Host will assess the excessive cost concern by applying a “Reasonableness” standard (the “Reasonableness Standard”). The Reasonableness Standard will be determined and applied by the Host in light of things like cost thresholds and accessibility.

2. By way of example only, a small subscription charge to use additional elements of a large language model such as Gemini Advanced are acceptable if meeting the Reasonableness Standard of Sec. 8.2. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

c. Automated Machine Learning Tools (“AMLT”)

1. Individual Participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google toML, H2O Driverless AI, etc.) to create a Submission, provided that the Participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules. 

####7. ELIGIBILITY

a. Unless otherwise stated in the Competition-Specific Rules above, any individual may participate in the Competition. However, individuals who are supervised, advised, or directly mentored by a member of the organizing committee, or who are otherwise subject to a conflict of interest as determined by the organizing committee, are not eligible to receive prizes. Such participants may submit entries, appear on the leaderboard, and participate fully in the Competition, but will not be considered for prize awards. If a prize-eligible position is achieved by an ineligible participant, the prize will instead be awarded to the next highest-ranked eligible participant.

####8. WINNER’S OBLIGATIONS

a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:

1. Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code should follow [these documentation guidelines][5], must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. For avoidance of doubt, delivered software code should include training code, inference code, and a description of the required computational environment. 

a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).” 

b. Individual Participants and Teams may use artificial intelligence or automated machine learning tools (including AutoML systems and large language models) in the development of their Submissions and remain eligible to win a Prize. However, to be eligible for a Prize, the potential winner must demonstrate a thorough understanding of the submitted solution and be able to explain, justify, and reproduce all major components of the methodology. Submissions that rely substantially on AI-generated code or content without the participant's ability to understand and defend the underlying methods may, at the sole discretion of the organizing committee, be deemed ineligible for prize consideration. All Submissions must otherwise comply with these Rules,

2. Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;

3. Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).

####9. GOVERNING LAW

a. Unless otherwise provided in the Competition Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.


<a id="s005"></a>
## S005

- **source_id:** filament-segmentation-2026:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/abstract
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/4/text`

*(See the Announcement section below for updates.)*

# TASK  
Participants are invited to develop algorithms for the automated segmentation of solar filaments. Any computational approach may be employed, including traditional image-processing techniques, machine learning methods, and state-of-the-art deep neural network architectures.

The objective of this challenge is to develop an algorithm---whether novel or existing---that generates accurate segmentation masks for individual solar filaments. For each filament, the predicted mask should capture the complete extent of the filament, including its fine-scale structures, while minimizing the inclusion of non-filament regions. The challenge emphasizes robust and precise delineation of filament morphology across a diverse set of solar observations.

# GOAL
**(Updated: Aug 7, 2026)**
  
This competition focuses on the pixel-level precision of filament segmentation masks. ~~The primary evaluation criterion is the Dice score, which quantifies the degree of overlap between the predicted and ground-truth segmentation masks (see [torchmetrics.segmentation.DiceScore](https://lightning.ai/docs/torchmetrics/stable/segmentation/dice.html))~~ **The primary evaluation criteria is the Panoptic Quality metric ([10.1109/CVPR.2019.00963](https://ieeexplore.ieee.org/abstract/document/8953237)).** In addition to segmentation accuracy, the evaluation framework incorporates penalties related to fragmentation and over-merging (e.g., one-to-many and many-to-one correspondences between predicted and ground-truth filament structures), as well as the end-to-end computational efficiency of the proposed method.


<a id="s006"></a>
## S006

- **source_id:** filament-segmentation-2026:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/foundational-rules
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/5/text`

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


<a id="s007"></a>
## S007

- **source_id:** filament-segmentation-2026:page:6:Final Submission
- **page_name:** Final Submission
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Final Submission
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/6/text`

**(Added: Aug 7, 2026)**  

When ready, prepare the following items and submit them through [this google form](https://docs.google.com/forms/d/e/1FAIpQLSfyrM4dhc8QzxR90PtF6fb018KPf0S0Cbf5hPqMuUognmzQsA/viewform?usp=dialog). The items are:
 - **A technical report**: A 4-page technical report is required. Please use [this Overleaf template](https://www.overleaf.com/read/vjztpvrnbrdh#43fbbe) for your report. More details about the content of this report are provided in the template. The final report should be submitted as a single pdf file.
 - **Code Repository**: A publicly accessible link to a Git-based repository such as GitHub, GitLab, or Bitbucket, is required. The organizing committee should access your source code without requiring additional access permissions or approval. Within this repository, a file named `requirements.txt` must include all utilized packages and their corresponding versions. Also, a jupyter notebook should illustrate the entire pipeline. The committee should not require any additional file to reproduce the submitted predictions.

All participants who wish to be considered for the final evaluation must complete the Google form. Please ensure that all information provided is accurate and complete. Any errors or omissions that prevent the judging committee from accessing the required materials or contacting the participant may result in the submission being deemed ineligible for final evaluation.


<a id="s008"></a>
## S008

- **source_id:** filament-segmentation-2026:page:7:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Description
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/7/text`

#### What Are Solar Filaments?

Filaments (as shown below) are dense "clouds" of solar material suspended by magnetic field lines above photospheric neutral lines. The significance of filaments for space weather research lies in the fact that they are at the core of solar eruptions, including Coronal Mass Ejections (CMEs), solar flares, and Solar Energetic Particle (SEP) storms. An Earth-directed CME can cause enormous damage to the electric power grid, disrupt GPS systems, create radiation hazards for passengers and crew on polar flights, and be lethal to astronauts traveling outside the protective bubble provided by the Earth's magnetosphere. This is why solar filaments are a critical event type in space weather research and forecasting operations.

<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3070992%2F77fe20a042912564b30d941836d26f70%2Ffilament_GONG_20240103224642Ch.png?generation=1779296142924487&alt=media" alt="an example of a solar filament" style="width:60%; height:auto;"/>

#### What Is MAGFiLO?
MAGFiLO, short for *Manually Annotated GONG Filaments from H-Alpha Observations*, is the ground-truth data of filaments' segmentation mask ([10.1038/s41597-024-03876-y](https://doi.org/10.1038/s41597-024-03876-y)). It is created for training and evaluation of machine-learning algorithms, and for evaluation of traditional computer-vision algorithms.

The illustration below shows an H-Alpha observation of the Sun, in which solar filaments have been identified by expert human annotators. Although the dataset includes additional annotations, such as bounding boxes, filament spines, and class labels, this competition focuses exclusively on the segmentation masks of solar filaments.

MAGFiLO is the testbed for all participants' models.

See the Data tab for more details.

<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3070992%2F7b19d336400715aa6b69a895f6cee0ed%2Fmagfilo_segmentation_examples.png?generation=1779302394935245&alt=media" alt="an example of a MAGFiLO instances" style="width:100%; height:auto;">

#### What Are the Main Challenges?
Although recent advances in object segmentation have led to remarkable performance across many domains, solar filament segmentation remains a challenging task for several reasons:  
- **Fine-scale structures.** Accurately capturing fine filament structures, such as barbs, remains difficult. Barbs are thin, thread-like features that extend from the main body of a filament along a characteristic orientation. Their orientation relative to the filament spine carries important information about the filament's underlying magnetic field configuration.  
- **Background noise and image quality.** Distinguishing filament material (dark regions) from background structures and noise is nontrivial. Since the observations used in this competition originate from ground-based observatories, they are affected by various sources of noise and imaging artifacts. Accurately identifying small-scale filament structures while suppressing background noise remains a significant challenge.  
- **Structural continuity.** Existing segmentation algorithms often struggle to identify solar filaments as contiguous physical structures. Instead, they may produce fragmented segmentations or segment clusters of nearby dark regions ("islands"), resulting in incomplete or physically inconsistent representations of the filament morphology.


<a id="s009"></a>
## S009

- **source_id:** filament-segmentation-2026:page:8:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Evaluation
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/8/text`

**(Updated: Aug 7, 2026)**  

Although participants may use other external data sources, please note that: (1) for inference of ML models, only the H-alpha images provided in the test directory will be used; and (2) the models may not use any other ground-truth metadata for training.

All submissions are judged based on the following rubric:

- Quantitative Comparison (70%):
  - ~~Mean Dice score (using [torchmetrics.segmentation.DiceScore](https://lightning.ai/docs/torchmetrics/stable/segmentation/dice.html))~~ **Panoptic Quality metric (see the Leaderboard Ranking section below for more details.)**
  - Distribution of Dice scores
  - Distribution of IoU scores
  - Distribution of one-to-many and many-to-one relations between the ground-truth and predicted segmentations.
- Qualitative Comparison (30%):
  - Detailed description of the entire pipeline (from preprocessing to final prediction, including the architecture of the utilized algorithm).
  - The apparent morphology of predicted segmentations on H-Alpha images.
  - The quality of code (modularity and documentation)

**Note:** The evaluation of the above criteria is contingent upon the availability of the source code. Please refer to the Open-Access Policy section below.


<a id="s010"></a>
## S010

- **source_id:** filament-segmentation-2026:page:9:Self Evaluation
- **page_name:** Self Evaluation
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Self Evaluation
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/9/text`

**(Added: Aug 7, 2026)**  

A self-evaluation notebook containing a few scores and plots is now available. Participants can use this notebook to have a better understanding of the effectiveness of their segmentation algorithms.

- Notebook: [https://www.kaggle.com/code/azimahmadzadeh/self-evaluation-notebook](https://www.kaggle.com/code/azimahmadzadeh/self-evaluation-notebook)


<a id="s011"></a>
## S011

- **source_id:** filament-segmentation-2026:page:10:Leaderboard Ranking
- **page_name:** Leaderboard Ranking
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Leaderboard Ranking
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/10/text`

**(Added: Aug 7, 2026)**  

The ranking on the leaderboard is one of the considerations in our evaluation (see above rubric.)

The submissions will be evaluated against the ground-truth data (MAGFiLO) using the **Panoptic Quality** metric which is defined as follows:

$$
\text{PQ}(Y, \hat{Y}) = \frac{\sum_{(\mathbf{y}, \hat{\mathbf{y}}) \in TP} \text{IoU}(\mathbf{y}, \hat{\mathbf{y}})}{|TP| + 0.5 |FP| + 0.5 |FN|}
$$

where
 - Y is a set of all ground-truth segments y,
 - Y-hat is a set of all predicted segments y-hat,
 - IoU computes the Intersection-over-Union as shown below,
 - TP, FP, and FN denote sets of all true-positive, false-positive, and false-negative cases, respectively, and
 - |.| is the set cardinality operation.

Intersection-over-Union is measured as follows:
$$
\text{IoU}(\mathbf{y}, \hat{\mathbf{y}}) = \text{IoU}(\mathbf{y}, \hat{\mathbf{y}}) = \frac{\cap(\mathbf{y}, \hat{\mathbf{y}})}{\cup{(\mathbf{y}, \hat{\mathbf{y}})}} 
                = \frac{\sum {(\mathbf{y} \odot \hat{\mathbf{y}}})}{\sum ({\mathbf{y} \oplus \hat{\mathbf{y}} \ominus \mathbf{y} \odot \hat{\mathbf{y}})}}
$$


For more information about Panoptic Quality metric, see the original paper ([10.1109/CVPR.2019.00963](https://ieeexplore.ieee.org/abstract/document/8953237)).

**Note:** There are further verification strategies addressing certain edge cases. Appropriate messages will be shown after a submission is uploaded, when/if such cases are identified.


<a id="s012"></a>
## S012

- **source_id:** filament-segmentation-2026:page:11:Submission File
- **page_name:** Submission File
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Submission File
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/11/text`

We expect the participants to upload a single CSV file for the entire test set, where each row corresponds to one predicted filament, as shown below.

```text
filament_id        | segmentation_rle   |
-------------------|--------------------|
20150125172714Mh_1 | "f8uSDds ... VQNC" |
20150125172714Mh_2 | "KHT%$HD ... 9>km" |
20150125172714Mh_3 | "YQNEgn1 ... BH6^" |
...                | ...                |
20170501024112Bh_1 | "HBy4d6D ... 97*D" | 
```

 - Column `filament_id` contains unique ids for each filament, e.g., `20150125172714Mh_2`.
 - Column `segmentation_rle` contains RLE counts each encoding the mask corresponding to one filament, e.g., ```^Vj02jo16I5O2O1`PNA]o1c0N19G1N11O3L01O4JYamT3```. Do not include quotations (`'` or `"`).

**Note:** You only need to store RLE Counts; no need to store RLE Size. The Size is fixed for all images: 2048 X 2048 pixels.

To convert your output (e.g., masks, polygons, etc.) to the expected format (RLE Counts), please use [the `pycocotools` Python package](https://pypi.org/project/pycocotools), specifically, the methods `annToMask`, `decodeMask`, and `encodeMask`. For more details, see [coco.py](https://github.com/ppwwyyxx/cocoapi/blob/master/PythonAPI/pycocotools/coco.py).


**Note:** The tail strings in the `filament_id` column (e.g., `_2`) is only to make the rows unique. For example, if your algorithm identifies 3 filaments in a given image with id `20150125172714Mh`, your should generate 3 rows with the following keys: `20150125172714Mh_1`, `20150125172714Mh_2`, and `20150125172714Mh_3`. As long as the tail strings render the rows unique , and the image id remains unchanged, your filament id is acceptable.  
**Note:** The number of ground-truth segmentations may also be different from the number of predicted ones. So, the evaluation method matches the predicted and ground-truth segmentations based on their actual overlap, not their index. 

The scoreboard will show to the contestants the mean Dice score for ~50% of images in the test set. The results on the remaining images will be only visible to the organizers of the competition. For a fair evaluation pipeline, the two scores should be fairly close.


<a id="s013"></a>
## S013

- **source_id:** filament-segmentation-2026:page:12:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Prizes
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/12/text`

All submissions will be evaluated according to the criteria described above. The organizing committee will review the submitted solutions and determine scores for the top-3 teams. Awards will be granted across the first-, second-, and third-place categories. A total prize pool of up-to $3,000 will be distributed among the winning teams, proportional to their scores which is assigned based on the Evaluation rubric).

The winners of this competition will be announced in the IEEE BigData 2026 in December 14-17, 2026 at Phoenix, AZ.

The exact prize calculation method is shown below:
```Python
def compute_prizes(scores, total_prize=3000, temperature=2.0):
    scores = np.asarray(scores, dtype=float)
    weights = np.power(scores, temperature)
    weights = weights / np.sum(weights)
    prizes = total_prize * weights

    return prizes
```

Upon determining the winners and their exact prizes, AURA/NSO will contact the winners requesting bank information.

**Note:** Prizes will be split equally among all verified team members listed on the winning submission.

### Requirements:
- **Banking Info Requirement.** All prize recipients must provide valid banking and payment information to AURA and complete any required vendor onboarding process in accordance with AURA policies. Prize payments will be issued by AURA/NSO via direct bank transfer. Prize disbursement is contingent upon the recipient being able to receive payments from U.S. financial institutions. Failure to complete the required vendor setup or provide valid payment information will result in forfeiture of the prize.
- **Source Code Release Requirement.** Acceptance of a prize is contingent upon the winning teams providing the organizing committee with the complete source code, scripts, configuration files, and any other materials necessary to reproduce the submitted results. The submitted code must successfully reproduce the competition results using the instructions provided by the team.

By accepting a prize, the winning team grants the organizers a perpetual, worldwide, non-exclusive, royalty-free license to use, execute, reproduce, modify, and analyze the submitted code for research, educational, benchmarking, and archival purposes. This includes, but is not limited to, reproducing the reported results, evaluating and comparing submitted methods, and preparing scientific publications (e.g., survey or benchmark papers) describing the competition and the approaches submitted. The organizers will provide appropriate attribution to the authors when the submitted methods or code are discussed or referenced in such publications. 

- **Technical Report Requirement.** Acceptance of a prize is contingent upon the winning team submitting a concise technical report describing its solution. The report must document the complete data processing pipeline, including data preprocessing, feature engineering (if applicable), model architecture, training procedure, post-processing steps, and any other components necessary to understand and reproduce the submitted results. The report should be sufficiently detailed to enable the organizing committee to evaluate the methodology and independently reproduce the reported performance.  


**Note:** The organizing committee will not claim authorship of, or take credit for, any submitted code or methods. All intellectual contributions will remain attributed to their original authors, and appropriate credit will be given in any resulting publications or other uses of the submitted materials.  


<a id="s014"></a>
## S014

- **source_id:** filament-segmentation-2026:page:13:Open-Access Policy
- **page_name:** Open-Access Policy
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Open-Access Policy
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/13/text`

All participants wishing to be considered for the final evaluation must maintain a Git repository containing the source code of their solution. The repository must be made publicly accessible immediately upon the close of the competition and must remain publicly accessible at least until when the winners are announced. Please refer to the competition end date and time for the submission deadline.

The quality of the submitted code—including its modularity, reproducibility, and documentation—will be considered as part of the final evaluation and may affect a team's overall score. Please refer to the Evaluation section for additional details.



<a id="s015"></a>
## S015

- **source_id:** filament-segmentation-2026:page:14:Organizers
- **page_name:** Organizers
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Organizers
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/14/text`

- Azim Ahmadzadeh, Ph.D., University of Missouri–St. Louis ([www.azim-a.com/](https://www.azim-a.com/))
- Dustin J. Kempton, Ph.D., Georgia State University
- Qin Li, Ph.D., New Jersey Institute of Technology
- Alexei A. Pevtsov, Ph.D., National Solar Observatory


<a id="s016"></a>
## S016

- **source_id:** filament-segmentation-2026:page:15:Sponsor
- **page_name:** Sponsor
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Sponsor
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/15/text`

This competition is sponsored by the U.S. National Science Foundation (NSF) National Solar Observatory (NSO). The NSO is the United States' national center for ground-based solar physics and advances research, education, and public outreach in solar science. The NSO is operated by the Association of Universities for Research in Astronomy (AURA) under a cooperative agreement with the NSF Division of Astronomical Sciences.

For more information about the National Solar Observatory, please visit [www.nso.edu](https://nso.edu/).

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3070992%2F92e6fcb0cff5365b607c6b6057ee6544%2Fnso-aura_logos.png?generation=1783377127838047&alt=media)

The organization of the Filament Segmentation Challenge 2026 is partially supported by the U.S. National Science Foundation (NSF) under Grant No. 2209912 and 2433781, directorate for Computer and Information Science and Engineering (CSE), and Office of Advanced Cyberinfrastructure (OAC), and Grant No. 2511630, AST Division Of Astronomical Sciences and MPS Directorate for Mathematical and Physical Sciences.


<a id="s017"></a>
## S017

- **source_id:** filament-segmentation-2026:page:16:Acknowledgment
- **page_name:** Acknowledgment
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/overview/Acknowledgment
- **retrieved_at:** 2026-10-07T15:14:31.875079+00:00
- **Archive locator:** `/original_sources/16/text`

This work utilizes GONG data obtained by the NSO Integrated Synoptic Program, managed by the National Solar Observatory, which is operated by the Association of Universities for Research in Astronomy (AURA), Inc. under a cooperative agreement with the National Science Foundation and with contribution from the National Oceanic and Atmospheric Administration. The GONG network of instruments is hosted by the Big Bear Solar Observatory, High Altitude Observatory, Learmonth Solar Observatory, Udaipur Solar Observatory, Instituto de Astrofísica de Canarias, and Cerro Tololo Interamerican Observatory.


<a id="s018"></a>
## S018

- **source_id:** filament-segmentation-2026:thread:728062:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062
- **thread_id:** 728062
- **comment_id:** opening
- **author_name:** JAB100
- **author_role:** unknown
- **created_at:** 2026-07-21T21:02:31.394Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/17/text`

Test set overlap with public dataset

Summary

139 of the 180 images (77.2%) in the competition's private test set are
byte-identical to images distributed in the publicly available MAGFiLO 1.0
dataset, which ships with full ground-truth segmentation annotations for
every one of those images. This allows a participant to obtain substantially
inflated leaderboard scores without any real modeling, and likely explains
how the current top scores (~0.9) are reached.

Did a submission replacing my real models predictions with annotations from MAGFiLO 1.0 and it gave a 0.73->0.82 bump, so while the annotations used in the real test set may differ it makes the leaderboard a significantly less reliable metric for finding good models/approaches


<a id="s019"></a>
## S019

- **source_id:** filament-segmentation-2026:thread:728062:3507555
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3507555
- **thread_id:** 728062
- **comment_id:** 3507555
- **author_name:** Aurora wy
- **author_role:** unknown
- **created_at:** 2026-08-02T08:30:07.357Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/18/text`

I think the same as you..🫡


<a id="s020"></a>
## S020

- **source_id:** filament-segmentation-2026:thread:728062:3501408
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3501408
- **thread_id:** 728062
- **comment_id:** 3501408
- **author_name:** Raffi Ardhi Naufal
- **author_role:** unknown
- **created_at:** 2026-07-21T23:49:46.697Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/19/text`

I verified this at the metadata level, all 180 test filenames appear with annotations in the public MAGFiLO v1.0 release. Note that since the overlap covers the full test set, the public/private split alone won't separate leak-based submissions from real models (both halves are equally exposed). 

So the reliable differentiators left are exactly what the hosts emphasize (reproducibility and documented methodology). I also support the suggestion that review order should prioritize submissions whose scores are reproducible from their code, rather than raw leaderboard position.


<a id="s021"></a>
## S021

- **source_id:** filament-segmentation-2026:thread:728062:3501343
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3501343
- **thread_id:** 728062
- **comment_id:** 3501343
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-07-21T21:27:23.343Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/20/text`

Thanks for your comment.

Please note that our evaluation is not based on the scores shown in the leaderboard. That's only a preliminary way of filtering some submissions out.

Please take a look at the Evaluation section of our competition where we presented our evaluation rubric. It consists of two parts: a quantitative and a qualitative method. Submissions without a decent strategy will NOT be rewarded in any ways.

I strongly encourage all participants to focus on the quality of their segmentations. That's what matters, and that's what differentiates winning submissions from the rest.

Good luck!


<a id="s022"></a>
## S022

- **source_id:** filament-segmentation-2026:thread:728062:3501351
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3501351
- **thread_id:** 728062
- **comment_id:** 3501351
- **parent_comment_id:** 3501343
- **author_name:** JAB100
- **author_role:** unknown
- **created_at:** 2026-07-21T21:51:33.657Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/21/text`

Exactly why I note "significantly less reliable metric for finding good models/approaches". The preliminary filter is now misleading, a potentially good model could be hidden under many leaky submissions, how far does one keep going down top score interviews until finally finding something that didn't make use of public data. 

If a technique exists to determine "decent strategy", and "quality of segmentations" it ought to be the filter, surely this makes life easier for both the hosts and the participants


<a id="s023"></a>
## S023

- **source_id:** filament-segmentation-2026:thread:728062:3507227
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3507227
- **thread_id:** 728062
- **comment_id:** 3507227
- **parent_comment_id:** 3501343
- **author_name:** Peng Wang
- **author_role:** unknown
- **created_at:** 2026-08-01T16:43:33.420Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/22/text`

Can I ask for Qualitative Comparison section (I just start this game), how people submit it? Save the paper in the Git Hub? Or? As looks like that part is not submit in Kaggle


<a id="s024"></a>
## S024

- **source_id:** filament-segmentation-2026:thread:728062:3508024
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/728062#comment-3508024
- **thread_id:** 728062
- **comment_id:** 3508024
- **parent_comment_id:** 3507227
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-08-03T14:03:55.597Z
- **retrieved_at:** 2026-10-07T15:15:18.760300+00:00
- **Archive locator:** `/original_sources/23/text`

Please stay tuned. We will let everyone know about that soon.


<a id="s025"></a>
## S025

- **source_id:** filament-segmentation-2026:thread:729396:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/729396
- **thread_id:** 729396
- **comment_id:** opening
- **author_name:** Valentin Haase
- **author_role:** unknown
- **created_at:** 2026-07-25T15:20:39.147Z
- **retrieved_at:** 2026-10-07T15:15:14.474158+00:00
- **Archive locator:** `/original_sources/24/text`

Clarification requested: public MAGFiLO release overlaps the competition test set

Hello, and thanks to the organizers for putting this dataset and competition together.

While reading the MAGFiLO paper (Scientific Data, doi:10.1038/s41597-024-03876-y) I looked up the published dataset itself, which is openly available at Harvard Dataverse (doi:10.7910/DVN/J6JNVK) under CC BY-NC-ND 4.0. Comparing it against the competition data, the picture is:

The public release contains 1,593 image records and 10,244 annotations.
The competition training set corresponds to that release with the test observations removed (8,199 annotations, matching annotation IDs).
The remaining ~2,045 annotations in the public release belong to the 180 observations used as the competition test set.
In other words, ground-truth annotations for the test observations are publicly downloadable, and the file names make them straightforward to identify.

Rule Section 6 permits external data that is publicly available and free to all participants, which the MAGFiLO release is. So I wanted to ask for explicit guidance rather than assume:

Should participants avoid using the public MAGFiLO release altogether?
Or is it acceptable to use it provided the competition test observations are excluded?
Will this be checked at the source-code review stage for prize-eligible teams, and is there anything you would like us to document about data provenance in our submissions?
I am not using the public release in my pipeline. After the comparison above it turned out to contain no additional labelled training data beyond what the competition already provides, so there is nothing to gain from it either way. I am raising it because the overlap is easy to run into unintentionally (downloading "all of MAGFiLO" is a natural first step), and a clear statement from the organizers would help everyone train on a level footing.

Thanks very much.


<a id="s026"></a>
## S026

- **source_id:** filament-segmentation-2026:thread:729396:3514996
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/729396#comment-3514996
- **thread_id:** 729396
- **comment_id:** 3514996
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-08-20T15:17:16.643Z
- **retrieved_at:** 2026-10-07T15:15:14.474158+00:00
- **Archive locator:** `/original_sources/25/text`

Also, please see the updated content (marked with strikethrough) in **Overview**.


<a id="s027"></a>
## S027

- **source_id:** filament-segmentation-2026:thread:729396:3504225
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/729396#comment-3504225
- **thread_id:** 729396
- **comment_id:** 3504225
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-07-27T14:53:40.840Z
- **retrieved_at:** 2026-10-07T15:15:14.474158+00:00
- **Archive locator:** `/original_sources/26/text`

Thanks for bringing this up. Let me clarify this.

All participants can use external data sources (e.g., GONG's magnetograms, SDO's AIA images, etc.) to obtain more information for segmentation, but for the final test, inference takes place solely on the H-Alpha images shared with the participants. Further, the ground-truth data (i.e., annotations in MAGFiLO) should be limited to what is provided through this competition. Otherwise, the submissions will be disregarded.


<a id="s028"></a>
## S028

- **source_id:** filament-segmentation-2026:thread:729487:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/729487
- **thread_id:** 729487
- **comment_id:** opening
- **author_name:** Felipe KNBIS
- **author_role:** unknown
- **created_at:** 2026-07-25T18:26:06.883Z
- **retrieved_at:** 2026-10-07T15:15:11.536503+00:00
- **Archive locator:** `/original_sources/27/text`

Clarification: how is the test-set ground truth constructed when an image has multiple annotators?

Hi organizers,

Thank you for the detailed rubric and for the clarifications already posted in this forum.

In the training annotations, the same physical image can appear under multiple image_id values, each corresponding to an independent annotator (e.g. 010101-… and 010102-…), as described in the Data Description. For the test set, however, the submission format uses a single image id per image (_1, _2, …), so each image has exactly one predicted set of filaments.

Could you clarify how the ground-truth segmentations for the test set are derived for images annotated by more than one annotator? Specifically:

(1) Is the ground truth a single merged mask per image, or are the per-annotator sets kept separate with the score averaged over them?

(2) If merged, are the annotations combined by union, or is a consensus/agreement rule applied?

We are building our offline validation from the training annotations, and how multiple annotators are combined changes the target our models are evaluated against. Knowing this would let us align our local evaluation with yours.

Thank you!


<a id="s029"></a>
## S029

- **source_id:** filament-segmentation-2026:thread:735256:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/735256
- **thread_id:** 735256
- **comment_id:** opening
- **author_name:** Viacheslav Popika
- **author_role:** unknown
- **created_at:** 2026-08-14T19:10:47.393Z
- **retrieved_at:** 2026-10-07T15:15:05.811263+00:00
- **Archive locator:** `/original_sources/28/text`

Some visible filaments are missing from the annotations

Hello. I noticed that some visible filaments are missing from the annotations. If I build an algorithm that detects every real filament, those extra correct detections may be treated as false positives if the test annotations also omit them.

Should we try to match the dataset annotations exactly, including missed filaments, or should the goal be to detect every real filament visible in the image?


<a id="s030"></a>
## S030

- **source_id:** filament-segmentation-2026:thread:735256:3512956
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/735256#comment-3512956
- **thread_id:** 735256
- **comment_id:** 3512956
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-08-14T20:35:34.883Z
- **retrieved_at:** 2026-10-07T15:15:05.811263+00:00
- **Archive locator:** `/original_sources/29/text`

Great question. We are interested in algorithms which detect all filaments whether they were annotated by human or not. In doing so, note that an algorithm may aggressively detect many tiny filaments. Such filaments may not be too interesting as they lack morphological details, or may not even be filaments---they may be background noise or sunspots. If needed, a post-processing step can clean out the predictions.

You are right that such cases of false-positives will be penalized when measuring Panoptic Quality, however, the judging committee will also look at the distribution of many-to-many relations (among several factors). Our "Self Evaluation" notebook generates a plot that shows the many-to-many relations. Please use that to find ways to improve on your algorithm.


<a id="s031"></a>
## S031

- **source_id:** filament-segmentation-2026:thread:736543:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/736543
- **thread_id:** 736543
- **comment_id:** opening
- **author_name:** Jamshid Ganiev
- **author_role:** unknown
- **created_at:** 2026-08-21T12:20:16.655Z
- **retrieved_at:** 2026-10-07T15:15:02.899761+00:00
- **Archive locator:** `/original_sources/30/text`

Clarification on Using Additional MAGFiLO Annotations for Training

The competition description states:

  “Although the dataset includes additional annotations, such as bounding boxes, filament spines, and class labels, this competition focuses exclusively on the segmentation masks of solar filaments.”

It also states:

  “the models may not use any other ground-truth metadata for training.”

Could you please clarify whether this means that **only the provided `segmentation` annotations may be used as training supervision**?

Specifically, would using the provided `spine` annotation as an auxiliary supervision target be prohibited, even if the model's final output and submission contain only instance segmentation masks?

Also, are auxiliary targets derived directly from the segmentation masks—such as skeletons/medial axes, boundaries, distance transforms, bounding boxes, or areas—allowed?

I would appreciate some clarificaiton on this by the organizers.

Thank you,


<a id="s032"></a>
## S032

- **source_id:** filament-segmentation-2026:thread:736543:3515337
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/736543#comment-3515337
- **thread_id:** 736543
- **comment_id:** 3515337
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-08-21T14:23:55.067Z
- **retrieved_at:** 2026-10-07T15:15:02.899761+00:00
- **Archive locator:** `/original_sources/31/text`

Good question!

  Could you please clarify whether this means that only the provided segmentation annotations may be used as training supervision?

You can use other meta data available in the dataset (i.e., `spine`, `bbox`, `area`, and `category_id`). What you cannot use is any piece of information that you may obtain from external sources leaking the ground-truth data of the test set into your final submission. 

  Also, are auxiliary targets derived directly from the segmentation masks—such as skeletons/medial axes, boundaries, distance transforms, bounding boxes, or areas—allowed?

`spine` and `category_id` data are manually annotated, whereas `bbox` and `area` data are inferred from the segmentations. For more information, please see the Data Description section in [Data tab](https://www.kaggle.com/competitions/filament-segmentation-2026/data).


<a id="s033"></a>
## S033

- **source_id:** filament-segmentation-2026:thread:740400:opening
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400
- **thread_id:** 740400
- **comment_id:** opening
- **author_name:** Rahul S.
- **author_role:** unknown
- **created_at:** 2026-09-09T14:01:45.879Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/32/text`

We're not fighting a filament-detection problem, we're fighting a scoring convention.

The metric requires matching a loose, multiple-annotated consensus, not finding the filament. Many annotated masks are looser and fuzzier than the physical filament. So a mask that's physically correct can still be counted as a FP. Detecting a real but a low-agreement filament is a net-negative.


<a id="s034"></a>
## S034

- **source_id:** filament-segmentation-2026:thread:740400:3522678
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400#comment-3522678
- **thread_id:** 740400
- **comment_id:** 3522678
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-09-09T14:31:33.300Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/33/text`

Hi [@rsiyanwal](/rsiyanwal) ! Thanks for your comment.

Your observation is partially correct, but your statement is not.

- Of thousands of filaments manually annotated, some segmentations are better than others. You are right! But this is how you know you are dealing with a real-world problem, not an overly-processed dataset which serves no value beyond serving a competition. You may enjoy reading [the published paper on how this dataset was created](https://www.nature.com/articles/s41597-024-03876-y)

- The variance you are observing is rooted in the reality of what we study. Solar filaments are fluid "objects" and marking their "boundary" from observations capturing such phenomena from 150 million km away is what makes this an interesting problem.

- Because of this variance, no single-value evaluation measure will be adequate to reflect the "true" performance of any model. This is why, as the rubric of this challenge indicates, we do not rely solely on any single-value measure. Our judging committee will look at individual predictions, as well as the logic of the algorithm.

So, again, we encourage all participants to focus on the quality of their predictions instead of their score. Anything beyond 3.5 PQ is of great interest to us.

I hope you still can enjoy and appreciate the imperfection of this real-world problem.


<a id="s035"></a>
## S035

- **source_id:** filament-segmentation-2026:thread:740400:3525175
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400#comment-3525175
- **thread_id:** 740400
- **comment_id:** 3525175
- **parent_comment_id:** 3522678
- **author_name:** harikrishnacs
- **author_role:** unknown
- **created_at:** 2026-09-17T03:08:18.380Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/34/text`

How many of those 0.55 score on leaderboard legit ?? 
You can find a notebook that dumped values and got .55 and a lot of training decoration all around 
Am i missing anything ? 
Or am I wrong ?


<a id="s036"></a>
## S036

- **source_id:** filament-segmentation-2026:thread:740400:3525344
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400#comment-3525344
- **thread_id:** 740400
- **comment_id:** 3525344
- **parent_comment_id:** 3525175
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-09-17T15:08:06.273Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/35/text`

You are not wrong. Please do not let random scores discourage you. We are only interested in real solutions, and we can easily weed out the fake ones.


<a id="s037"></a>
## S037

- **source_id:** filament-segmentation-2026:thread:740400:3525565
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400#comment-3525565
- **thread_id:** 740400
- **comment_id:** 3525565
- **parent_comment_id:** 3525175
- **author_name:** Maxim
- **author_role:** unknown
- **created_at:** 2026-09-18T07:09:15.447Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/36/text`

Will the leaderboard be cleaned up at some point, so that the final placement shown on our Kaggle profiles reflects only legitimate submissions?


<a id="s038"></a>
## S038

- **source_id:** filament-segmentation-2026:thread:740400:3525685
- **url:** https://www.kaggle.com/competitions/filament-segmentation-2026/discussion/740400#comment-3525685
- **thread_id:** 740400
- **comment_id:** 3525685
- **parent_comment_id:** 3525175
- **author_name:** Azim Ahmadzadeh
- **author_role:** unknown
- **created_at:** 2026-09-18T16:33:00.383Z
- **retrieved_at:** 2026-10-07T15:14:55.190862+00:00
- **Archive locator:** `/original_sources/37/text`

Yes. At this point, I cannot share more details.

