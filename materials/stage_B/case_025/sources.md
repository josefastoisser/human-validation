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
- [S008: multi-view-pig-posture-recognition:thread:667093:opening](#s008)
- [S009: multi-view-pig-posture-recognition:thread:667093:3438557](#s009)
- [S010: multi-view-pig-posture-recognition:thread:667093:3394289](#s010)
- [S011: multi-view-pig-posture-recognition:thread:667093:3399318](#s011)
- [S012: multi-view-pig-posture-recognition:thread:667093:3406223](#s012)
- [S013: multi-view-pig-posture-recognition:thread:667093:3414134](#s013)
- [S014: multi-view-pig-posture-recognition:thread:671741:opening](#s014)
- [S015: multi-view-pig-posture-recognition:thread:671741:3403225](#s015)
- [S016: multi-view-pig-posture-recognition:thread:671741:3404472](#s016)
- [S017: multi-view-pig-posture-recognition:thread:671741:3406224](#s017)
- [S018: multi-view-pig-posture-recognition:thread:671741:3414133](#s018)
- [S019: multi-view-pig-posture-recognition:thread:684661:opening](#s019)
- [S020: multi-view-pig-posture-recognition:thread:684661:3429617](#s020)
- [S021: multi-view-pig-posture-recognition:thread:685184:opening](#s021)
- [S022: multi-view-pig-posture-recognition:thread:685184:3438219](#s022)
- [S023: multi-view-pig-posture-recognition:thread:700153:opening](#s023)
- [S024: multi-view-pig-posture-recognition:thread:700153:3464702](#s024)
- [S025: multi-view-pig-posture-recognition:thread:700153:3466995](#s025)
- [S026: multi-view-pig-posture-recognition:thread:702242:opening](#s026)
- [S027: multi-view-pig-posture-recognition:thread:702242:3462217](#s027)
- [S028: multi-view-pig-posture-recognition:thread:702242:3467704](#s028)
- [S029: multi-view-pig-posture-recognition:thread:702401:opening](#s029)
- [S030: multi-view-pig-posture-recognition:thread:702401:3462511](#s030)

<a id="s001"></a>
## S001

- **source_id:** multi-view-pig-posture-recognition:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/data-description
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/0/text`

## Dataset Challenges: Generalization Across Cameras and Animals

This dataset is intentionally designed to evaluate **model generalization under realistic farm conditions**. The primary challenge arises from **distribution shifts** between training and testing data, including changes in **camera viewpoints, scene geometry, illumination, time period, and animal appearance**.

**Training Set 1 (T1)** represents the most challenging setting: models trained on T1 have **never seen the camera viewpoints or pig batches used in the test set**, requiring robust cross-view and cross-animal generalization.

**Training Set 2 (T2)** relaxes this constraint by adding a small number of images (**~4.5% of the test set size**) captured from the **same camera viewpoints as the test set**, while still ensuring that **no test-set pigs are included**. This provides limited **camera-view context** without introducing subject overlap, allowing models to better adapt to target scene geometry and perspective.

The performance gap between T1 and T2 highlights the difficulty of **viewpoint generalization** and emphasizes the importance of learning posture representations that are robust to camera-dependent variations rather than memorizing animal-specific cues.

## Dataset Folder and File Structure

The multiview_pig_posture_recognition directory has the following subfolder and file structure:

```
multiview_pig_posture_recognition/
├── train1_images/                 # Training set 1 images
│   ├── pen1_orb_cam1_20250108_085204.jpg
│   ├── pen1_orb_cam1_20250108_085209.jpg
│   └── ...
├── train2_images/                 # Training set 2 images
│   ├── pen1_orb_cam1_20250108_085204.jpg
│   ├── pen1_orb_cam1_20250108_085209.jpg
│   └── ...
├── test_images/                  # Test images
│   ├── pen1_tur_cam1_20250920_174649.jpg
│   ├── pen1_tur_cam1_20250921_050022.jpg
│   └── ...
├── train1.csv                     # Training set 1 annotations (bbox + posture labels)
├── train2.csv                     # Training set 2 annotations (bbox + posture labels)
├── test.csv                      # Test annotations (bbox only)
├── sample_submission.csv         # Example submission format
└── pig_posture_classes.txt       # Mapping of class IDs to posture names
```

---

## Training Annotations

Each row in the 'train1.csv' and 'train2.csv' files corresponds to **one pig instance** (one bounding box) of a train image.

### Columns

| Column            | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| row_id          | Unique identifier for each pig instance                      |
| image_id       | Image filename (e.g., pen1_orb_cam1_20250108_085204.jpg)                            |
| width, height | Original image dimensions (pixels)                           |
| bbox            | Bounding box in [xmin, ymin, w, h] format (absolute pixel units) |
| class_id        | Posture class ID (0–4)                                       |

### Example

```csv
row_id,image_id,width,height,bbox,class_id
train_pen1_orb_cam1_20250108_085204_0000,pen1_orb_cam1_20250108_085204.jpg,1920,1080,[967.5,331.5,463.0,447.0],3
```

## Filename Pattern 

Image filenames follow the pattern:

```
pen-number_camera-type_camera-number_date_time_instance-id.file-extension
```

**Example:**

```
pen1_orb_cam1_20250108_085204.jpg
```

### Filename Components

| Component        | Description                                     |
| ---------------- | ----------------------------------------------- |
| `pen-number`     | Pig pen identifier (e.g., `pen1`, `pen2`)       |
| `camera-type`    | Camera model (`orb` = Orbbec, `tur` = Turret)   |
| `camera-number`  | Camera index (e.g., `cam1`, `cam2`)             |
| `date_time`      | Capture timestamp in `YYYYMMDD_HHMMSS` format   |
| `file-extension` | Image file format (e.g., `.jpg`)                |

**Note:**
Bounding box coordinates are provided in **absolute pixel units** relative to the original image resolution and are **not normalized**.

---

## Test Set (`test.csv`)

All test images are provided in the `/test_images` directory.

The `test.csv` file contains **ground-truth bounding boxes only** (no posture labels).
Participants must **predict the posture class for each bounding box listed in `test.csv`**.

Ground-truth posture labels for the test set are **hidden** and used exclusively for leaderboard evaluation.

---

## Evaluation Metric

Submissions are evaluated using the **macro-averaged F1 score**, computed across the five posture classes.

A prediction is considered correct if:

* The predicted posture class matches the ground-truth label for the corresponding **pig instance (`row_id`)**

Macro-F1 assigns **equal importance to all posture classes**, making it suitable for class imbalance.

---

## Submission Format

A sample submission file, **sample_submission.csv**, is provided for reference. Each submission must be a **CSV file containing exactly two columns**, formatted as follows:

| Column     | Description                            |
| ---------- | -------------------------------------- |
| `row_id`   | Unique pig instance ID from `test.csv` |
| `class_id` | Predicted posture class (integer 0–4)  |

### Example

```csv
row_id,class_id
test_pen1_tur_cam1_20250920_174649_0000,0
test_pen1_tur_cam1_20250920_174649_0001,1
```

**Ensure that:**

   
- All row_id values exactly match those provided in test.csv.

    
- Each row_id appears once and only once in the submission file.

## Pig Posture Classes

The file pig_posture_classes.txt defines the mapping between **posture class IDs and their corresponding pig posture labels**.
Each line represents one posture class, with the **line index indicating the class ID**.

**Class Definitions:**

0 — Lateral_lying_left

1 — Lateral_lying_right

2 — Sitting

3 — Standing

4 — Sternal_lying

## Notes

* Bounding boxes are **axis-aligned** and provided for **both training and test sets**
* Multiple pigs may appear in a single image
* Participants **do not need to predict bounding boxes**
* The task focuses purely on **instance-level posture classification under real-world farm conditions**

---


<a id="s002"></a>
## S002

- **source_id:** multi-view-pig-posture-recognition:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/Description
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/1/text`

Accurate detection of pig posture in real farm environments remains a challenging problem in computer vision. Unlike controlled laboratory settings, commercial barns present cluttered backgrounds, frequent occlusions, variable lighting conditions, and diverse camera viewpoints. In addition, several pig postures exhibit subtle visual differences, making posture discrimination from 2D images particularly difficult.

This competition aims to advance pig posture recognition by encouraging the development and evaluation of deep learning models in multi-view scenes under realistic farm conditions.  It also addresses the difficulty in generalizing detections to different pigs and different cameras from those used in the training set.

All data were collected from two pig pens at the Swine Research Center, Michigan State University. Images were acquired using eight overhead cameras and include multiple pig breeds (Purebred Yorkshire, Exotic crossbred, and Meishan) across different production batches.

There are two training sets and one *Test Set*:

* **Training Set 1** contains 3,090 images captured from five camera views, with a total of 22,934 annotated posture instances. 
* **Training Set 2** adds 60 images from testing set camera views and so comprises 3,150 images with 23,450 posture instances.

<b>The camera array used in data collection</b>
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F29008476%2Fb2b6dc1d276b1698f1abb01a1c76ccec%2Fleaderboard_camera.png?generation=1767893280056824&alt=media)

<b>The training dataset statistics</b>
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F29008476%2F8b42bf6941e40f45c8686df5a1b61d3f%2Ftrain1_vs_train2_hist.png?generation=1767984424131922&alt=media)

Each pen contains 8 to 10 pigs per batch. For every pig instance, the dataset provides an axis-aligned bounding box (xmin, ymin, w, h) in both the training and test sets. However, posture labels are available only for the training set. Participants are required to predict the posture for each detected pig instance in the test set and submit their results using a standard submission CSV file, which will be automatically evaluated and ranked on the leaderboard.

The task is to classify the posture of each pig into one of the following five categories:

- Lateral_lying_left

- Lateral_lying_right

- Sitting

- Standing

- Sternal_lying


## Dataset Challenges: Generalization Across Cameras and Animals

> *“Generalization across unseen camera views and animals remains a core challenge in posture recognition.”*

This dataset is curated to evaluate **model generalization under realistic farm conditions**. The primary challenge arises from **distribution shifts** between training and testing data, including changes in **camera viewpoints, scene geometry, time period, and animal appearance**.

**Training Set 1 (T1)** represents the most challenging setting: models trained on T1 have **never seen the camera viewpoints or pig batches used in the test set**, requiring robust cross-view and cross-animal generalization.

**Training Set 2 (T2)** relaxes this constraint by adding a small number of images (**~4.5% of the test set size**) captured from the **same camera viewpoints as the test set**, while still ensuring that **no test-set pigs are included**. This provides limited **camera-view context** without introducing subject overlap, allowing models to better adapt to target scene geometry and perspective.

The performance gap between T1 and T2 highlights the difficulty of **viewpoint generalization** and emphasizes the importance of learning posture representations that are robust to camera-dependent variations rather than memorizing animal-specific cues.

By participating in this challenge, you will not only test your skills in instance-level image classification, representation learning, and model generalization between the camera views and pig batches, but also contribute to ongoing research in Precision Livestock Farming (PLF) an emerging interdisciplinary field where machine learning, sensor technology, and animal science converge to enable smarter, more sustainable livestock production systems.

The ultimate goal is to build a robust and generalizable posture recognition model that performs consistently across different camera devices, viewpoints, pig batches, pig populations, and environmental conditions.


<a id="s003"></a>
## S003

- **source_id:** multi-view-pig-posture-recognition:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/Evaluation
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/2/text`

Submissions are evaluated using the macro-averaged F1 score.
This metric computes the F1 score independently for each posture class and then averages the scores, giving equal weight to all classes regardless of their frequency. This makes it particularly suitable for imbalanced datasets.

F1 = 2 × (precision × recall) / (precision + recall)

Scores range from 0.0 to 1.0, where 1.0 indicates perfect classification performance, and 0.0 indicates no correct predictions.

The final competition ranking is based on the private leaderboard, which is evaluated using a Solution CSV file.

## Submission Format

Each submission must be a CSV file with **two columns**:

| Column     | Description                            |
| ---------- | -------------------------------------- |
| `row_id`   | Unique pig instance ID from `test.csv` |
| `class_id` | Predicted posture class (integer 0–4)  |

### Example

```csv
row_id,class_id
test_pen1_tur_cam1_20250920_174649_0000,0
test_pen1_tur_cam1_20250920_174649_0001,1
```

Must exactly match the row_id of test.csv.

- label

An integer value from 0 to 4, corresponding to the following posture classes:

  
    
      Class ID
      Posture Name
    

  
  
    0Lateral_lying left

    1Lateral_lying right

    2Sitting

    3Standing

    4Sternal_lying

  

## Submission Naming Requirement (Mandatory)

To clearly distinguish model performance across the two training sets, **all submissions must follow the naming convention specified below**.

### Required Submission Name Format

Participants must submit **two separate entries**, one for each training set, using the following prefixes:

* **`T1_`** — for models trained on **Training Set 1**
* **`T2_`** — for models trained on **Training Set 2**

The submission name **must begin exactly with the corresponding prefix**.

### Examples

* `T1_baseline_model`
* `T2_baseline_model`
* `T1_teamname_v03`
* `T2_teamname_v03`

Participants are strongly encouraged to use a **consistent identifier** (e.g., model name or version number) across the paired `T1_` and `T2_` submissions to facilitate comparison.

### Important Notes

* Submissions **not following this naming convention** may be excluded from prize eligibility.
* The leaderboard displays all submissions in a single list; however, submissions can be easily filtered using the `T1_` and `T2_` prefixes via the leaderboard search box.
* **Winner determination is based solely on the private leaderboard ranking of `T2_` submissions**, in accordance with the competition rules. However, the `T1_` submissions will also be highlighted and published.
* **Submissions with missing test images, incorrect labels, or formatting errors** may result in a submission failure.


<a id="s004"></a>
## S004

- **source_id:** multi-view-pig-posture-recognition:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/rules
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/3/text`

1. COMPETITION-SPECIFIC TERMS

1.1 Competition Title

Multi-view Pig Posture Recognition

1.2 Competition Organizer

Smart Sensing Lab, Michigan State University

Led by Dr. Daniel Morris

1.3 Competition Website

https://www.kaggle.com/competitions/multi-view-pig-posture-recognition

1.4 Prizes and Winner Selection

 1.4.1 Evaluation Metrics 

     

- To be eligible for prizes, participants must submit both their code and the model used to generate the final submission via a **Kaggle Notebook** on or before the prize deadline (**May 16, 2026, 12:00 AM GMT−5:00**).

- The challenge will remain active after winners have been finalized; however, any submissions made after the prize deadline will appear on the leaderboard for reference only and will **not** be considered for prize eligibility.

  
    
- All the ground truth labels on the test set are hidden.

    
- Submissions are evaluated using the **Macro F1 Score** on the test set.

    
- Participants must train models independently using each of the **two training sets**, evaluate their performance on the test set, and submit results for both training sets in accordance with the required submission format.

    
- Evaluation results from both training sets must be submitted and displayed.

    
- During the competition, the leaderboard will display results on 30% of the test set (public test set).

    
- When the competition closes, the leaderboard will display results from the remaining 70% of the test set (private test set).

    
- **Prize winners** will be determined based on the final private leaderboard rankings, computed using **70% of the test set**, for submissions trained on **Training Set 2**. Submissions trained on **Training Set 1** are not eligible for prizes; however, the top-performing Training Set 1 model will be highlighted in the associated publication..

 1.4.2 Prize Structures

The following cash prizes will be awarded
| Rank          | Prize        |
| ------------- | ------------ |
| **1st Place** | **$300 USD** |
| **2nd Place** | **$200 USD** |
| **3rd Place** | **$100 USD** |

 Winner Selection Criteria

    
- Prize eligibility and winner determination are based exclusively on the final **private leaderboard** ranking of   submissions trained using **Training Set 2**.

- Submissions on the private leaderboard are ranked in **descending order of Macro F1 score**.

- In the event of a tie on the private leaderboard among submissions trained on **Training Set 2**, the private leaderboard ranking of the corresponding submissions trained on **Training Set 1** will be used as the tie-breaking criterion.

- Only submissions that fully comply with all competition rules, requirements, and submission guidelines are eligible to receive prizes.

- Each individual participant or team may receive **no more than one prize**.

1.4.3 Tie-Breaking & Prize Sharing Policy

    
- If two or more participants achieve the same final ranking (equal private leaderboard Macro F1 scores up to Kaggle’s evaluation precision) for submissions trained on both training sets, the corresponding prize(s) will be shared equally among the tied participants.

    
- When a tie spans multiple prize ranks, the total prize money for those ranks will be pooled and split evenly among the tied participants.

**Examples:**

- Two-way tie for 1st place

→ ($300 + $200) ÷ 2 = $250 each

- Three-way tie for 2nd place

→ ($200 + $100) ÷ 3 ≈ $100 each

- Tie for 3rd place

→ $100 ÷ number of tied participants

1.4.4 Prize Distribution & Tax Responsibility 

- Winners will be contacted via their Kaggle account email after the competition ends.

- Prize payment details will be coordinated directly with the winners.

- All prizes are awarded as gross amounts.

- Winners are solely responsible for any and all taxes, fees, or other obligations arising from receiving a prize, in accordance with the laws and regulations of their country of residence.

- The organizers will not withhold or pay taxes on behalf of the winners.

1.4.5 Additional Notes

- Kaggle’s leaderboard ranking and score precision are considered final and binding.

- In the event of suspected rule violations or non-compliance, the organizers reserve the right to:

- Disqualify submissions

- Reassign or withhold prizes as appropriate

2. COMPETITION-SPECIFIC RULES

2.1 Team Limits

  
- Maximum team size: five (5) participants

  
- Team mergers are permitted through the Competition Website

  
- Combined submission counts must not exceed allowed limits

2.2 Submission Limits

  
- Maximum two (2) submissions per day

  
- Only one final submission may be selected

2.3 Competition Timeline

All important dates are listed under Overview > Timeline on the Competition Website.
Participants are responsible for monitoring updates.

2.4 Competition Data

a. Permitted Use

  
- Participation in this Competition

  
- Discussion on Kaggle competition forums

b. Data Security

Competition Data must not be shared outside registered participants.
Any suspected unauthorized access must be reported to Kaggle immediately.

2.5 External Data and Tools

  
- External data must be publicly available and free

  
- Automated ML tools may be used with appropriate licenses

2.6 Eligibility

  
- Open to students, researchers, and the Kaggle community

  
- Smart Sensing Lab affiliates may participate without preferential treatment

2.7 Submission Transparency

Top-performing participants may be asked to provide code and documentation
to ensure academic reproducibility.

2.8 Governing Law

These Rules are governed by the laws of the State of Michigan.
Any disputes will be handled exclusively in Ingham County, Michigan, USA.

3. KAGGLE FOUNDATIONAL RULES

This Competition is governed by Kaggle’s Foundational Competition Rules.
In case of conflict, Kaggle’s rules take precedence.

4. FINAL NOTES

This Competition encourages learning, collaboration, and ethical research.
Participants are expected to act in good faith and respect the academic nature of the challenge.

Questions should be posted in the Kaggle Discussion forum for this competition.


<a id="s005"></a>
## S005

- **source_id:** multi-view-pig-posture-recognition:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/abstract
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/4/text`

###🏆 About Challenge###

Pig posture recognition is a key task in Precision Livestock Farming, enabling automated monitoring of animal health and welfare. In this competition, participants develop computer vision models to classify pig postures from 2D images captured under realistic farm conditions, including occlusion, lighting variation, multiple camera views, and pig batches. Using the provided bounding boxes from multi-camera views, participants must predict the posture of each pig instance and submit their results in a standardized submission CSV file. 
Submissions are automatically evaluated, ranked against private leaderboard ground-truth labels, and published on the leaderboard.


<a id="s006"></a>
## S006

- **source_id:** multi-view-pig-posture-recognition:page:5:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/Prizes
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
- **Archive locator:** `/task_documents/5/text`

The following cash prizes will be awarded based on the final private leaderboard ranking.
Please refer to the Rules section for detailed winner selection criteria and prize distribution policies.

-  **First Prize: $300.00**

- **Second Prize: $200.00**

- **Third Prize: $100.00**


<a id="s007"></a>
## S007

- **source_id:** multi-view-pig-posture-recognition:page:6:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/overview/foundational-rules
- **retrieved_at:** 2026-10-13T13:51:08.737504+00:00
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

- **source_id:** multi-view-pig-posture-recognition:thread:667093:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093
- **thread_id:** 667093
- **comment_id:** opening
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-01-11T00:43:49.387Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/0/text`

Frequently Asked Questions

**📌 Pig Posture Recognition Competition — FAQ**

**1. How do I load the dataset and parse the bounding boxes?**

You can refer to the **multiview_dataset.py** provided in the Code section. It shows how to load images, parse bounding boxes, and extract crops.

**2. Are test images available?**

Yes. Test images are located at:

/kaggle/input/multi-view-pig-posture-recognition/multiview_pig_posture_recognition/test_images/

**3. What format should the submission file follow?**

Your submission must be a CSV with the following columns:

'''
row_id,class_id
row_id must match exactly with the IDs in test.csv
class_id must be an integer from 0 to 4
Refer to the Data tab for details and an example sample_submission.csv.
'''

**4. What evaluation metric is used?**

The competition uses the F1 Score, which is the harmonic mean of Precision and Recall.

**5. What is the public/private leaderboard split?**

Leaderboard split:

30% Public
70% Private
The public score is visible during the competition. Final rankings are determined by the private score.

**6. What happens if two participants tie?**

This competition follows the standard Kaggle tie-breaking and prize-sharing policy, as described in the Rules section.

**7. Are participants allowed to use external datasets?**

To be eligible for a prize:

- Only the provided pig_posture_recognition dataset may be used

- No external images or synthetic data are allowed

- Manual relabeling or extra annotations are not allowed

- Participants may use external data for non-prize submissions, but such entries are not eligible for awards.

**8. Is this a classification or detection task?**

This is a bounding-box guided classification task. Bounding boxes are already provided in both train.csv and test.csv. Your model only needs to classify the posture inside the given box. No object detection model is required.

**9. Is a baseline notebook provided?**

Yes. A full baseline is available in the Code section.

It demonstrates:

- Loading the dataset

- Parsing bounding boxes

- Generating posture crops

- Training a YOLO11 classification model

- Producing a valid submission.csv

Participants must share their code and model.


<a id="s009"></a>
## S009

- **source_id:** multi-view-pig-posture-recognition:thread:667093:3438557
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093#comment-3438557
- **thread_id:** 667093
- **comment_id:** 3438557
- **author_name:** Mazano 
- **author_role:** unknown
- **created_at:** 2026-04-09T10:33:47.597Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/1/text`

Hi [@cvchallenge](https://www.kaggle.com/cvchallenge) 

Can we use extra annotation and train on it if it is the output of a publicly available model. So like (Data with bound boxes) ->(feed to public model) -> new labels -> train a model to output the classes + output labels of public model used. Without the need for human labeling.


<a id="s010"></a>
## S010

- **source_id:** multi-view-pig-posture-recognition:thread:667093:3394289
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093#comment-3394289
- **thread_id:** 667093
- **comment_id:** 3394289
- **author_name:** Artyom Grishin
- **author_role:** unknown
- **created_at:** 2026-01-20T19:34:36.687Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/2/text`

Hello! You say that we can't use external datasets then what about pre-trained models? I'm sure we can't use them neither, but your baseline where you load weights of YOLO have confused me, can you clarify this moment? Thank you


<a id="s011"></a>
## S011

- **source_id:** multi-view-pig-posture-recognition:thread:667093:3399318
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093#comment-3399318
- **thread_id:** 667093
- **comment_id:** 3399318
- **parent_comment_id:** 3394289
- **author_name:** Spiritmilk
- **author_role:** unknown
- **created_at:** 2026-01-30T16:20:36.990Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/3/text`

I have the same question. Is using pre-trained weights allowed? [@cvchallenge](https://www.kaggle.com/cvchallenge)


<a id="s012"></a>
## S012

- **source_id:** multi-view-pig-posture-recognition:thread:667093:3406223
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093#comment-3406223
- **thread_id:** 667093
- **comment_id:** 3406223
- **parent_comment_id:** 3399318
- **author_name:** Alex Garayoa
- **author_role:** unknown
- **created_at:** 2026-02-15T03:38:26.763Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/4/text`

Same question here! [@cvchallenge](https://www.kaggle.com/cvchallenge)


<a id="s013"></a>
## S013

- **source_id:** multi-view-pig-posture-recognition:thread:667093:3414134
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/667093#comment-3414134
- **thread_id:** 667093
- **comment_id:** 3414134
- **parent_comment_id:** 3399318
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-02-26T02:42:01.507Z
- **retrieved_at:** 2026-10-13T13:52:31.435605+00:00
- **Archive locator:** `/discussion/5/text`

Hi everyone,
There is no restriction on using a pretrained model. The final training and testing should be solely on our dataset. I hope it cleared your confusion.


<a id="s014"></a>
## S014

- **source_id:** multi-view-pig-posture-recognition:thread:671741:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/671741
- **thread_id:** 671741
- **comment_id:** opening
- **author_name:** Marjan Anušić
- **author_role:** unknown
- **created_at:** 2026-02-03T19:03:47.490Z
- **retrieved_at:** 2026-10-13T13:52:25.916204+00:00
- **Archive locator:** `/discussion/6/text`

Mismatch Between Winner Rules

I have a question regarding a possible mismatch between the competition rules described on different pages.

Overview page

  Participants must submit **two separate entries**, one for each training set, using the following prefixes:

  **T1_** — for models trained on Training Set 1

  **T2_** — for models trained on Training Set 2  

  **Winner determination is based solely on the private leaderboard ranking of T1_ submissions**, in accordance with the competition rules. T2_ submissions are used for reference and tie-breaking only.

Rules page

  **Winner Selection Criteria**

  
  
- Prize eligibility and winner determination are based exclusively on the final **private leaderboard** ranking of submissions trained using **Training Set 2**.

  
- Submissions on the private leaderboard are ranked in **descending order of Macro F1 score**.

  
- In the event of a tie among submissions trained on **Training Set 2**, the ranking of the corresponding **Training Set 1** submissions will be used as the tie-breaker.

  

Could you please clarify which rule applies for winner determination?


<a id="s015"></a>
## S015

- **source_id:** multi-view-pig-posture-recognition:thread:671741:3403225
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/671741#comment-3403225
- **thread_id:** 671741
- **comment_id:** 3403225
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-02-08T00:35:11.353Z
- **retrieved_at:** 2026-10-13T13:52:25.916204+00:00
- **Archive locator:** `/discussion/7/text`

Hi Marjan,
Thank you for spotting that mismatch. I have corrected it. A winner will be selected based on the T2 submission. However, the top-ranked model on the T1 dataset will be highlighted during a paper publication, as it is a challenging dataset.


<a id="s016"></a>
## S016

- **source_id:** multi-view-pig-posture-recognition:thread:671741:3404472
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/671741#comment-3404472
- **thread_id:** 671741
- **comment_id:** 3404472
- **parent_comment_id:** 3403225
- **author_name:** Marjan Anušić
- **author_role:** unknown
- **created_at:** 2026-02-10T15:08:39.080Z
- **retrieved_at:** 2026-10-13T13:52:25.916204+00:00
- **Archive locator:** `/discussion/8/text`

Hi, Thank you for clarifying and fixing the inconsistency, I appreciate it.


<a id="s017"></a>
## S017

- **source_id:** multi-view-pig-posture-recognition:thread:671741:3406224
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/671741#comment-3406224
- **thread_id:** 671741
- **comment_id:** 3406224
- **parent_comment_id:** 3404472
- **author_name:** Alex Garayoa
- **author_role:** unknown
- **created_at:** 2026-02-15T03:43:10.810Z
- **retrieved_at:** 2026-10-13T13:52:25.916204+00:00
- **Archive locator:** `/discussion/9/text`

Hi [@cvchallenge](https://www.kaggle.com/cvchallenge) ,

Thank you for the clarification. I would like to confirm a couple of points about the submissions:

- Should participants submit two separate files, specifically named `T1_submission.csv` and `T2_submission.csv`, following the prefixes for each training set, or is a single `submission.csv` sufficient for prize eligibility?

2.To clarify, is it allowed to submit only the T2_ file to be eligible for the prize, while the T1_ submission is optional and only highlighted in the paper?

I appreciate your guidance.

Best regards!


<a id="s018"></a>
## S018

- **source_id:** multi-view-pig-posture-recognition:thread:671741:3414133
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/671741#comment-3414133
- **thread_id:** 671741
- **comment_id:** 3414133
- **parent_comment_id:** 3404472
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-02-26T02:33:40.290Z
- **retrieved_at:** 2026-10-13T13:52:25.916204+00:00
- **Archive locator:** `/discussion/10/text`

Hi Alex,
For prize eligibility, only T2_submission.csv is sufficient.


<a id="s019"></a>
## S019

- **source_id:** multi-view-pig-posture-recognition:thread:684661:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/684661
- **thread_id:** 684661
- **comment_id:** opening
- **author_name:** Yash Verdhan
- **author_role:** unknown
- **created_at:** 2026-03-25T18:42:05.487Z
- **retrieved_at:** 2026-10-13T13:52:09.370716+00:00
- **Archive locator:** `/discussion/11/text`

Regarding the T1/T2 training data and submission requirements

**Could you clarify the intended training constraints for each submission type? Specifically:**

- Is a T2_ submission required to be trained exclusively on Training Set 2, or is it permissible to use all available labeled data (T1 + T2 combined) and label the submission as T2_?

- Relatedly, is there any restriction on selectively using subsets of the provided training data - for example, up-weighting or exclusively training on a particular camera group within a training set?

We want to ensure our training strategy complies with the rules.
[@cvchallenge](https://www.kaggle.com/cvchallenge)


<a id="s020"></a>
## S020

- **source_id:** multi-view-pig-posture-recognition:thread:684661:3429617
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/684661#comment-3429617
- **thread_id:** 684661
- **comment_id:** 3429617
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-03-27T01:36:00.493Z
- **retrieved_at:** 2026-10-13T13:52:09.370716+00:00
- **Archive locator:** `/discussion/12/text`

Hi Yash,
Thank you for your interest in the challenge. There is no restriction on using the dataset. You can do any subsets or stratified sampling on the dataset that achieves a higher score on the test set. For your reference, the training set 2 has only 60 more images in addition to the training set 1 images.


<a id="s021"></a>
## S021

- **source_id:** multi-view-pig-posture-recognition:thread:685184:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/685184
- **thread_id:** 685184
- **comment_id:** opening
- **author_name:** Adarsh Kumar
- **author_role:** unknown
- **created_at:** 2026-03-27T07:13:02.746Z
- **retrieved_at:** 2026-10-13T13:52:03.880926+00:00
- **Archive locator:** `/discussion/13/text`

Do we have to select one T2 and one T1 for final submission

[@cvchallenge](https://www.kaggle.com/cvchallenge) First of all thanks for hosting this competition we are getting real world experience with this

I have a doubt we can only select 2 submission.csv for final check so do we need to select one best T1 and other best T2 or we can select 2 T2 only?

also while submitting can we zip both T1 and T2 together and upload the zip file or we need to submit both separately

and how will you evaluate the in private set like we are just giving csv not the pipeline where you can just change data and csv for it will be provided i think you know change comp to notebook based so that private set could be automatically tested just by changing dataset at same path as in other competition and by submitting just csv people could cheat by manually entering right option for test data


<a id="s022"></a>
## S022

- **source_id:** multi-view-pig-posture-recognition:thread:685184:3438219
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/685184#comment-3438219
- **thread_id:** 685184
- **comment_id:** 3438219
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-04-08T19:57:39.373Z
- **retrieved_at:** 2026-10-13T13:52:03.880926+00:00
- **Archive locator:** `/discussion/14/text`

Hi Adarsha,
Thank you for your active participation in the challenge. You may upload the best scores obtained from both the T1 and T2 trained models. However, for prize consideration, only your highest score will be taken into account.
Regarding dual submissions, you cannot upload a zipped file, as the Kaggle leaderboard will not be able to display your score. Instead, if you would like to submit results from both T1 and T2 models, please upload two separate submission files following the naming convention outlined in the Overview page (Submission Naming section).
Please note that you will be eligible for the prize even if you submit a score from the T2-trained model only. The final rankings based on the private test set will be displayed after the submission deadline.


<a id="s023"></a>
## S023

- **source_id:** multi-view-pig-posture-recognition:thread:700153:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/700153
- **thread_id:** 700153
- **comment_id:** opening
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-05-16T16:13:12.581Z
- **retrieved_at:** 2026-10-13T13:51:41.681104+00:00
- **Archive locator:** `/discussion/15/text`

🏆 Official Close and Next Steps

Hi everyone,

Thank you so much to all 251 teams for your enthusiastic participation in the Multi-view Pig Posture Recognition challenge! Seeing the community engage so deeply with this precision livestock farming problem has been incredibly motivating for our research team at the Swine Research Center.

Now that the deadline has passed, we wanted to outline the next steps regarding verification and the release of the final leaderboard.

🗓️ Timeline for Private Leaderboard Release
As a few of you have noticed, the private leaderboard is currently hidden while we conduct our standard validation process. We will verify the results and release the final private ranking on 23rd May.

🔍 Verification Process for Winners
To ensure the integrity of the results for our cash prizes ($300, $200, and $100), we will be reaching out to the top-ranking teams on the provisional leaderboard.

What we will request: We will ask the top teams to share their code (via a private Kaggle notebook or a GitHub repository).

What we are verifying: We will check that the code successfully reproduces the exact .csv files submitted and complies with all competition rules (e.g., no manual labeling of the test set, proper use of Training Set).

💡 Share Your Solutions!
Cross-view and cross-animal generalization under realistic farm conditions is a highly challenging problem in computer vision. Whether you finished near the top or just learned something new, we highly encourage you to create a post in the Discussion tab sharing your approach! We would love to hear about:

Your model architectures (EfficientNet, ViTs, etc.)

Your strategies for handling data imbalance or occlusion

How you approached the distribution shifts between T1 and T2

Thank you again for contributing to ongoing research in Precision Livestock Farming (PLF). We look forward to announcing the official winners next week!

Best regards,
The Competition Organizing Team


<a id="s024"></a>
## S024

- **source_id:** multi-view-pig-posture-recognition:thread:700153:3464702
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/700153#comment-3464702
- **thread_id:** 700153
- **comment_id:** 3464702
- **author_name:** suguuuuu
- **author_role:** unknown
- **created_at:** 2026-05-31T01:58:29.123Z
- **retrieved_at:** 2026-10-13T13:51:41.681104+00:00
- **Archive locator:** `/discussion/16/text`

Hi [@cvchallenge](https://www.kaggle.com/cvchallenge) ,

Now that the private leaderboard is finalized, I wanted to gently check in — I haven't received any contact about the prize verification yet, though I'm at the top of the leaderboard. 
Apologies if I've somehow missed a message on my end!

Thanks!


<a id="s025"></a>
## S025

- **source_id:** multi-view-pig-posture-recognition:thread:700153:3466995
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/700153#comment-3466995
- **thread_id:** 700153
- **comment_id:** 3466995
- **parent_comment_id:** 3464702
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-06-05T06:20:41.810Z
- **retrieved_at:** 2026-10-13T13:51:41.681104+00:00
- **Archive locator:** `/discussion/17/text`

Hi Sugu,

Congratulations on your well-deserved win! We have sent you a direct message on Kaggle. Please check your inbox and reply with your contact email address so we can get the prize process started with our finance team!

Best regards,
The Organizing Team


<a id="s026"></a>
## S026

- **source_id:** multi-view-pig-posture-recognition:thread:702242:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/702242
- **thread_id:** 702242
- **comment_id:** opening
- **author_name:** Ramazan Turan
- **author_role:** unknown
- **created_at:** 2026-05-21T21:27:11.581Z
- **retrieved_at:** 2026-10-13T13:51:30.734658+00:00
- **Archive locator:** `/discussion/18/text`

[Private LB 3rd 0.886] DINOv2 Giant (ViT-G/14), LLRD, K-Fold ensemble, TTA

Multi-view Pig Posture Recognition: 3rd Place Solution

Overview

The core of this solution is a DINOv2 Giant (ViT-G/14) trained from its default pretrained weights for 5-class pig posture classification. Predictions are made at the individual pig instance level: each bounding box is cropped from the full image, padded, and resized to 224×224.

Private score: **0.886** (T2), 3rd place.
Public score: **0.878** (T2), 4th place.

Model

`vit_giant_patch14_reg4_dinov2.lvd142m` via timm. I tried several architectures early on (SwinV2, ConvNeXt, DINOv2 variants) and DINOv2 outperformed everything else by a clear margin. Scaling up from DINOv2-S to B to L to G gave consistent gains each step, so I committed to the giant variant for all serious experiments.

Training

**K-Fold CV (3-fold).** The split is done at the image level, not the row level, so pigs from the same frame always end up in the same fold. Stratification is based on camera type (orb/tur) + dominant class per image. Test predictions are the weighted average of all three fold models, weighted by each fold's best validation F1. OOF macro F1 came out to **0.9508**.

Fold best val F1s: 0.9479 / 0.9486 / 0.9406

**Layer-wise LR Decay (LLRD).** The classification head gets the full learning rate (5e-5) and each transformer block gets 0.85× the rate of the block above it. This made a meaningful difference compared to a flat learning rate.

**Loss.** A custom `PairwisePenaltyLoss` wrapping Focal Loss (γ=2.5). Confusion matrix analysis showed that the hardest confusions were Sternal vs. Lateral (54+47 errors) and Sternal vs. Sitting. Penalty weights were set manually based on error counts to push the model harder on those pairs.

**Augmentation.** Class-specific augmentation policies rather than one-size-fits-all. Sternal_lying gets aggressive rotation (up to 180°) since orientation doesn't matter for that posture. Lateral_left/right get restricted rotation to preserve the directional cue. Sitting gets heavy perspective distortion because it's a small projection under overhead cameras. MixUp (α=0.2) is applied on top.

Other standard ingredients: WeightedRandomSampler (boosting Sternal and Lateral), Model EMA (decay=0.9999), AMP, cosine LR schedule with 3-epoch warmup, early stopping (patience=8).

**TTA (8×).** 4 rotations × 2 flips. Left/Right labels are swapped appropriately for horizontally flipped passes.

What Didn't Work

Non-DINOv2 architectures: SwinV2 and ConvNeXt fell significantly short of DINOv2, even when comparing similarly sized variants. The gap was large enough that I stopped pursuing them early.

Pseudo-labeling: I tried a two-stage approach where confident test predictions were added back as training data. It hurt performance and was removed entirely.

Every other addition was evaluated incrementally, and each contributed a measurable improvement to the validation F1: LLRD, class-specific augmentation, the custom penalty loss, and TTA were all additive.

What I'd Do Differently

I intentionally left K-Fold to the end, the plan was to finalize the model first and then run K-Fold on the best version since DINOv2-G training is slow. I got too focused on improving the model and by the time I remembered, there was little time left. The peak single-model score was 0.867 at epoch 28, and even with only 3 folds at 22 epochs due to the time constraint, K-Fold pushed the score up to 0.878 which is a really good improvement for this competition. With 4-5 folds at the full 28 epochs the result would likely be higher.

Environment & Hardware

Google Colab PRO, A100 40GB. Train code runs with 38GB VRAM, Inference requires lower VRAM.
3 folds with 22 epochs each and inference took about 12-14 hours.


<a id="s027"></a>
## S027

- **source_id:** multi-view-pig-posture-recognition:thread:702242:3462217
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/702242#comment-3462217
- **thread_id:** 702242
- **comment_id:** 3462217
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-05-22T14:40:47.410Z
- **retrieved_at:** 2026-10-13T13:51:30.734658+00:00
- **Archive locator:** `/discussion/19/text`

Hi Ramajan,
Thank you for submitting your solution.


<a id="s028"></a>
## S028

- **source_id:** multi-view-pig-posture-recognition:thread:702242:3467704
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/702242#comment-3467704
- **thread_id:** 702242
- **comment_id:** 3467704
- **parent_comment_id:** 3462217
- **author_name:** Ramazan Turan
- **author_role:** unknown
- **created_at:** 2026-06-07T05:36:47.253Z
- **retrieved_at:** 2026-10-13T13:51:30.734658+00:00
- **Archive locator:** `/discussion/20/text`

Hello [@cvchallenge](https://www.kaggle.com/cvchallenge). i saw your email about the prize. i replied to that email but i haven't received a response.

i also sent an email with a question 2-3 weeks ago and didn't receive a response to that one either.

i was just wondering whether my emails are reaching you and wanted to confirm that you're receiving them.

thank you.


<a id="s029"></a>
## S029

- **source_id:** multi-view-pig-posture-recognition:thread:702401:opening
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/702401
- **thread_id:** 702401
- **comment_id:** opening
- **author_name:** junicus
- **author_role:** unknown
- **created_at:** 2026-05-23T04:22:50.316Z
- **retrieved_at:** 2026-10-13T13:51:19.604010+00:00
- **Archive locator:** `/discussion/21/text`

Public 14th Solution - T2 v46/v49 Candidates, LB 0.854

Public 14th Solution - T2 v46/v49 Candidates, Public LB 0.854

Hi everyone,

I am sharing my public 14th place T2 solution notes for the Multi-view Pig Posture Recognition competition. My best public leaderboard score was 0.854, using the submitted file `T2_v46_final_02.csv`. I also selected `T2_v49_specv1_hgb_cap100.csv` as a second final candidate because it was more orthogonal to the main candidate and was designed as a private-leaderboard hedge.

Public code notebook:
[https://www.kaggle.com/code/junicus/t2-2final-candidates-v46-v49-lb0-854/notebook](https://www.kaggle.com/code/junicus/t2-2final-candidates-v46-v49-lb0-854/notebook)

Final selected submissions:

- `T2_v46_final_02.csv` - public LB 0.854

- `T2_v49_specv1_hgb_cap100.csv` - public LB 0.853

1. Overview

This competition was challenging mainly because of the domain shift between training and test data: different time periods, camera views, camera types, lighting conditions, and pig batches. In my experiments, the most difficult errors were around the lying classes, especially the boundary between:

- `Lateral_lying_left`

- `Lateral_lying_right`

- `Sternal_lying`

A large part of the work was not only training stronger classifiers, but also deciding which row-level corrections were reliable enough for the private leaderboard.

2. Base Pipeline

The solution was built around a strong SSL-based visual classifier and several later-stage candidate-generation scripts.

Main ingredients:

- Bounding-box guided classification only; no detector was trained.

- Crops were generated from the provided bounding boxes.

- The main anchor was a DINO/SSL-style image classifier trained on T2.

- Inference used test-time augmentation with correct left/right label handling for mirrored views.

- Multiple candidate submissions were generated by blending or selectively grafting row-level decisions.

The final public notebook does not rerun the full training pipeline because the heavy model checkpoints are large. Instead, it packages:

- final submitted CSV artifacts

- generation scripts

- validation/proxy reports

- checkpoint manifest

This mirrors the common Kaggle deliverable pattern where the notebook documents and reproduces final CSV artifacts from attached packages.

3. What Worked

3.1 Strong Anchor + Conservative Row-Level Grafting

Pure model ensembling saturated around the same public range for me. The biggest useful gains came from conservative row-level changes rather than aggressive retraining.

The best public candidate was:

- `T2_v46_final_02.csv`

- public LB: 0.854

This candidate used a stable anchor and grafted only a limited number of rows from another high-proxy candidate where the local validation/proxy evidence supported the change.

3.2 Shape / Lateral-Sternal Correction

The most useful post-processing family focused on the lateral-vs-sternal boundary. The goal was not to force the class distribution, but to correct low-confidence cases where bbox geometry and model disagreement suggested likely confusion.

Earlier variants in this direction produced the first small public improvement above the plateau.

3.3 Orthogonal Hedge Candidate

The second selected final submission was:

- `T2_v49_specv1_hgb_cap100.csv`

- public LB: 0.853

This candidate used a Sternal/Lateral specialist-style correction. Even though its public score was slightly lower than the main candidate, it disagreed with the main candidate on more rows than other near-identical shape variants. I selected it as a private-LB hedge because public differences of 0.001 were within noise, while diversity between final submissions mattered more.

4. What Did Not Work Well

Several directions did not give reliable improvement for my setup:

- aggressive pseudo-labeling

- broader context fine-tuning

- additional same-family ensembling after the anchor saturated

- large corrections to Sitting or Standing

- aggressive class distribution forcing

Most of these produced candidates around 0.851-0.853 public LB, so I treated that as a real plateau and stopped spending submissions on small unvalidated variants.

5. Validation / Selection Strategy

Because public LB represented only part of the test set, I did not choose final submissions purely by public score.

Final selection considered:

- public LB score

- candidate disagreement / orthogonality

- proxy validation reports

- class distribution sanity checks

- avoiding aggressive changes to rare or unstable classes

The final pair was chosen as:

- Main safe candidate:** `T2_v46_final_02.csv`

- Private hedge candidate:** `T2_v49_specv1_hgb_cap100.csv`

The idea was that the first candidate should preserve the strongest public score, while the second candidate should cover a different error pattern in case of private leaderboard shake-up.

6. Code Package

The public notebook is here:

[https://www.kaggle.com/code/junicus/t2-2final-candidates-v46-v49-lb0-854](https://www.kaggle.com/code/junicus/t2-2final-candidates-v46-v49-lb0-854)

It reproduces the two submitted final CSV artifacts from the attached package and writes:

- `/kaggle/working/T2_v46_final_02.csv`

- `/kaggle/working/T2_v49_specv1_hgb_cap100.csv`

- `/kaggle/working/submission.csv` as the primary v46 candidate

The package includes:

- final submissions

- candidate generation scripts

- validation/proxy reports

- checkpoint manifest

The original competition data is not redistributed; it is used only from the official Kaggle competition dataset.

7. Final Notes

This was a useful competition for learning how fragile public-LB probing can be when the remaining improvements are only a small number of rows. My final approach became more conservative near the end: trust robust candidates, avoid overfitting public noise, and keep the final submissions diverse enough to have a chance on private LB.

Thanks to the organizers for hosting the competition.


<a id="s030"></a>
## S030

- **source_id:** multi-view-pig-posture-recognition:thread:702401:3462511
- **url:** https://www.kaggle.com/competitions/multi-view-pig-posture-recognition/discussion/702401#comment-3462511
- **thread_id:** 702401
- **comment_id:** 3462511
- **author_name:** Smart Sensing Lab (SSL)
- **author_role:** unknown
- **created_at:** 2026-05-23T16:16:27.640Z
- **retrieved_at:** 2026-10-13T13:51:19.604010+00:00
- **Archive locator:** `/discussion/22/text`

Hi Junicus,
Thank you so much for submitting your solution.

