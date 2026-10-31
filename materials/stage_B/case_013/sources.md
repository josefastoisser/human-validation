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
- [S008: aeroclub-recsys-2025:thread:585898:opening](#s008)
- [S009: aeroclub-recsys-2025:thread:585898:3233134](#s009)
- [S010: aeroclub-recsys-2025:thread:585898:3231457](#s010)
- [S011: aeroclub-recsys-2025:thread:585898:3231465](#s011)
- [S012: aeroclub-recsys-2025:thread:585898:3231186](#s012)
- [S013: aeroclub-recsys-2025:thread:588131:opening](#s013)
- [S014: aeroclub-recsys-2025:thread:591217:opening](#s014)
- [S015: aeroclub-recsys-2025:thread:591217:3266076](#s015)
- [S016: aeroclub-recsys-2025:thread:591217:3259448](#s016)
- [S017: aeroclub-recsys-2025:thread:591217:3262524](#s017)
- [S018: aeroclub-recsys-2025:thread:591217:3262734](#s018)
- [S019: aeroclub-recsys-2025:thread:591217:3262773](#s019)
- [S020: aeroclub-recsys-2025:thread:591217:3262861](#s020)
- [S021: aeroclub-recsys-2025:thread:591217:3262867](#s021)
- [S022: aeroclub-recsys-2025:thread:591217:3262875](#s022)
- [S023: aeroclub-recsys-2025:thread:591217:3262919](#s023)
- [S024: aeroclub-recsys-2025:thread:591217:3254375](#s024)
- [S025: aeroclub-recsys-2025:thread:591217:3254376](#s025)
- [S026: aeroclub-recsys-2025:thread:591217:3254489](#s026)
- [S027: aeroclub-recsys-2025:thread:591217:3254491](#s027)
- [S028: aeroclub-recsys-2025:thread:591217:3254492](#s028)
- [S029: aeroclub-recsys-2025:thread:591217:3254521](#s029)
- [S030: aeroclub-recsys-2025:thread:591217:3254583](#s030)
- [S031: aeroclub-recsys-2025:thread:591217:3254560](#s031)
- [S032: aeroclub-recsys-2025:thread:591217:3254721](#s032)
- [S033: aeroclub-recsys-2025:thread:591217:3254804](#s033)
- [S034: aeroclub-recsys-2025:thread:591217:3254651](#s034)
- [S035: aeroclub-recsys-2025:thread:591217:3254774](#s035)
- [S036: aeroclub-recsys-2025:thread:591217:3254817](#s036)
- [S037: aeroclub-recsys-2025:thread:596975:opening](#s037)
- [S038: aeroclub-recsys-2025:thread:596975:3265509](#s038)
- [S039: aeroclub-recsys-2025:thread:598515:opening](#s039)
- [S040: aeroclub-recsys-2025:thread:598515:3267533](#s040)
- [S041: aeroclub-recsys-2025:thread:598515:3267544](#s041)
- [S042: aeroclub-recsys-2025:thread:599666:opening](#s042)
- [S043: aeroclub-recsys-2025:thread:599666:3276565](#s043)
- [S044: aeroclub-recsys-2025:thread:599666:3273518](#s044)
- [S045: aeroclub-recsys-2025:thread:599666:3272919](#s045)
- [S046: aeroclub-recsys-2025:thread:599666:3271644](#s046)
- [S047: aeroclub-recsys-2025:thread:599666:3271431](#s047)
- [S048: aeroclub-recsys-2025:thread:599666:3271452](#s048)
- [S049: aeroclub-recsys-2025:thread:599666:3274842](#s049)
- [S050: aeroclub-recsys-2025:thread:599666:3273531](#s050)
- [S051: aeroclub-recsys-2025:thread:599666:3271434](#s051)
- [S052: aeroclub-recsys-2025:thread:599666:3271169](#s052)
- [S053: aeroclub-recsys-2025:thread:599687:opening](#s053)
- [S054: aeroclub-recsys-2025:thread:599687:3272114](#s054)
- [S055: aeroclub-recsys-2025:thread:600069:opening](#s055)

<a id="s001"></a>
## S001

- **source_id:** aeroclub-recsys-2025:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/data-description
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/0/text`

# Data Description

## Overview

This dataset contains flight booking options for business travelers along with user preferences and company policies. The task is to predict user flight selection preferences.

## Data Structure

The dataset is organized around flight search sessions, where each session (identified by `ranker_id`) contains multiple flight options that users can choose from.


**Main Data**
- 'train.parquet' - train data
- 'test.parquet' - test data
- 'sample_submission.parquet' - submission example

**JSONs Raw Additional Data**
- 'jsons_raw.tar.kaggle'* - Archived raw data in JSONs files (150K files, ~50gb). To use the file as a regular .gz archive you should manually change extension to '.gz'. Example jsons_raw.tar.**kaggle** -> jsons_raw.tar.**gz**
- 'jsons_structure.md' - JSONs raw data structure description

## Column Descriptions

### Identifiers and Metadata

- `Id` - Unique identifier for each flight option
- `ranker_id` - Group identifier for each search session (key grouping variable for ranking)
- `profileId` - User identifier
- `companyID` - Company identifier

### User Information

- `sex` - User gender
- `nationality` - User nationality/citizenship
- `frequentFlyer` - Frequent flyer program status
- `isVip` - VIP status indicator
- `bySelf` - Whether user books flights independently
- `isAccess3D` - Binary marker for internal feature

### Company Information

- `corporateTariffCode` - Corporate tariff code for business travel policies

### Search and Route Information

- `searchRoute` - Flight route: single direction without "/" or round trip with "/"
- `requestDate` - Date and time when search was performed

### Pricing Information

- `totalPrice` - Total ticket price
- `taxes` - Taxes and fees component

### Flight Timing and Duration

- `legs0_departureAt` - Departure time for outbound flight
- `legs0_arrivalAt` - Arrival time for outbound flight  
- `legs0_duration` - Duration of outbound flight
- `legs1_departureAt` - Departure time for return flight
- `legs1_arrivalAt` - Arrival time for return flight
- `legs1_duration` - Duration of return flight

### Flight Segments

Each flight leg (legs0/legs1) can consist of multiple segments (segments0-3) when there are connections. Each segment contains:

#### Geography and Route
- `legs*_segments*_departureFrom_airport_iata` - Departure airport code
- `legs*_segments*_arrivalTo_airport_iata` - Arrival airport code  
- `legs*_segments*_arrivalTo_airport_city_iata` - Arrival city code

#### Airline and Flight Details
- `legs*_segments*_marketingCarrier_code` - Marketing airline code
- `legs*_segments*_operatingCarrier_code` - Operating airline code (actual carrier)
- `legs*_segments*_aircraft_code` - Aircraft type code
- `legs*_segments*_flightNumber` - Flight number
- `legs*_segments*_duration` - Segment duration

#### Service Characteristics
- `legs*_segments*_baggageAllowance_quantity` - Baggage allowance: small numbers indicate piece count, large numbers indicate weight in kg
- `legs*_segments*_baggageAllowance_weightMeasurementType` - Type of baggage measurement
- `legs*_segments*_cabinClass` - Service class: 1.0 = economy, 2.0 = business, 4.0 = premium
- `legs*_segments*_seatsAvailable` - Number of available seats

### Cancellation and Exchange Rules

#### Rule 0 (Cancellation)
- `miniRules0_monetaryAmount` - Monetary penalty for cancellation
- `miniRules0_percentage` - Percentage penalty for cancellation
- `miniRules0_statusInfos` - Cancellation rule status (0 = no cancellation allowed)

#### Rule 1 (Exchange)
- `miniRules1_monetaryAmount` - Monetary penalty for exchange
- `miniRules1_percentage` - Percentage penalty for exchange
- `miniRules1_statusInfos` - Exchange rule status

### Pricing Policy Information

- `pricingInfo_isAccessTP` - Compliance with corporate Travel Policy
- `pricingInfo_passengerCount` - Number of passengers

### Target Variable

- `selected` - In training data: binary variable (0 = not selected, 1 = selected). In submission: ranks within ranker_id groups

## Important Notes

- Each `ranker_id` group represents one search session with multiple flight options
- In training data, exactly one flight option per `ranker_id` has `selected = 1`
- The prediction task requires ranking flight options within each search session
- Segment numbering goes from 0 to 3, with segment 0 always present and higher numbers representing additional connections

### JSONs Raw Data Archive

The competition includes a json_raw_tar.gz archive containing the original raw data from which the train and test datasets were extracted. This archive contains **150,770 JSON files**, where **each filename corresponds to a ranker_id group**. Participants are allowed to use this raw data for feature enrichment and engineering, but it is not obligatory and only an option. 

Warning: The uncompressed archive requires more than **50GB** of disk space.

- 'jsons_raw.tar.kaggle'* - Compressed JSONs raw data  (150K files, ~50gb). To use the file as a regular .gz archive you should manually change extension to '.gz'. Example jsons_raw.tar.**kaggle** -> jsons_raw.tar.**gz**
- 'jsons_structure.md' - JSONs raw data structure description

-------------------

## Submission Format

### Training Data Target
In the training data, the `selected` column is **binary**:
- `1` = This flight was chosen by the traveler
- `0` = This flight was not chosen

**Important:** There is exactly one row with `selected=1` per user search request (`ranker_id`). Each row within a `ranker_id` group represents a different flight option returned by the search system for that specific route and date.

**Training data example:**
```
Id,ranker_id,selected
100,abc123,0     # Flight option 1 - not chosen
101,abc123,0     # Flight option 2 - not chosen  
102,abc123,1,    # Flight option 3 - SELECTED by user
103,abc123,0     # Flight option 4 - not chosen
```

### Submission Format
Your submission must contain **ranks** (not probabilities) for each flight option:

```
Id,ranker_id,selected
100,abc123,4
101,abc123,2
102,abc123,1
103,abc123,3
```

Where:
- `Id` matches the row identifier from the test set
- `ranker_id` is the search session identifier (same as in test.csv)
- `selected` is the **rank** you assign (1 = best option, 2 = second best, etc.)

**Important:** Maintain the exact same row order as in `test.csv`

In this example, your model predicts that:
- Row 102 (Id=102) is the best option → Rank 1
- Row 101 (Id=101) is second best → Rank 2  
- Row 103 (Id=103) is third best → Rank 3
- Row 100 (Id=100) is the worst option → Rank 4


## Submission Requirements

1. **Preserve row order:** Maintain the exact same row order as in `test.csv`
2. **Complete rankings:** For each user search request, you must rank ALL flight options returned by the search system
3. **Valid permutation:** Ranks within each `ranker_id` must be a valid permutation (1, 2, 3, ..., N) where N is the number of rows in that group
4. **No duplicate ranks:** Each row within a `ranker_id` group must have a unique rank
5. **Integer values:** All ranks must be integers ≥ 1

### Example for one user search request:
```
Training data shows:
ranker_id: abc123 → Row 102 was chosen (selected=1)

Your submission:
ranker_id: abc123
├── Row 100 → Rank 4 (worst option)
├── Row 101 → Rank 2 (second best)
├── Row 102 → Rank 1 (best - correctly predicted!)
└── Row 103 → Rank 3 (third best)

```

## Validation

Your submission will be validated for:
- Correct number of rows
- Integer rank values
- Valid rank permutations within each group
- No duplicate ranks per search session
- Basic anti-cheating measures

**Note:** The evaluation system expects you to transform your model's output (scores/probabilities) into ranks before submission. Higher model scores should correspond to lower rank numbers (1 = best).


<a id="s002"></a>
## S002

- **source_id:** aeroclub-recsys-2025:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/Description
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/1/text`

Business travel presents unique challenges for recommendation systems. Unlike leisure travelers who prioritize cost or vacation preferences, business travelers must balance multiple competing factors: corporate travel policies, meeting schedules, expense compliance, and personal convenience. This creates complex decision patterns that are difficult to predict.

This competition challenges participants to solve a **group-wise ranking problem** where your models must rank flight options within each user search session.  Each search session (ranker_id) represents a real user query with multiple flight alternatives, but only one chosen option. Your task is to build a model that can rank these options and identify the most likely selection.

### The Challenge
The dataset contains real flight search sessions with various attributes including pricing, timing, route information, user features and booking policies. The key technical challenge lies in ranking flight options to identify the most suitable choices for each business traveler on their specific route and circumstances. This becomes particularly complex as the number of available options can vary dramatically - from a handful of alternatives on smaller routes to thousands of possibilities on major trunk routes. Your model must effectively rank this entire spectrum of options to enhance the user experience by accurately identifying which flights best match traveler preferences.

### Why This Matters
Flight recommendation systems power major travel platforms serving millions of business travelers. Accurate ranking models can significantly improve user experience by surfacing relevant options faster, ultimately leading to higher conversion rates and customer satisfaction.

Your model will be evaluated based on ranking quality - how well it places the actually selected flight at the top of each search session's ranked list.


<a id="s003"></a>
## S003

- **source_id:** aeroclub-recsys-2025:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/Evaluation
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/2/text`

## HitRate@3

Competition metric HitRate@3 measures the fraction of search sessions where the correct flight appears in your top-3 predictions.

$$HitRate@3 = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \mathbf{1}(rank_i \leq 3)$$

Where:
- `|Q|` is the number of search queries (unique `ranker_id` values)
- `rank_i` is the rank position you assigned to the correct flight in query `i`
- `𝟙(rank_i ≤ 3)` is 1 if the correct flight is in top-3, 0 otherwise

**Example:** If the correct flight is ranked 1st, 2nd, or 3rd, you get 1.0 points. Otherwise, you get 0 points.

**Score range:** 0 to 1, where 1 means the correct flight is always in top-3

### Important Note on Group Size Filtering
The metric evaluation will only consider groups (`ranker_id`) with **more than 10 flight options**. Groups with 10 or fewer options are excluded from the final score calculation to focus on more challenging ranking scenarios where distinguishing between options is meaningful.

However, we have intentionally kept these smaller groups in both the training and test datasets because:

- They represent real-world search scenarios
- They provide additional training signal for your models
- They help capture the full diversity of user behavior patterns

## Submission Format

### Training Data Target
In the training data, the `selected` column is **binary**:
- `1` = This flight was chosen by the traveler
- `0` = This flight was not chosen

**Important:** There is exactly one row with `selected=1` per user search request (`ranker_id`). Each row within a `ranker_id` group represents a different flight option returned by the search system for that specific route and date.

**Training data example:**
```
Id,ranker_id,selected
100,abc123,0     # Flight option 1 - not chosen
101,abc123,0     # Flight option 2 - not chosen  
102,abc123,1,    # Flight option 3 - SELECTED by user
103,abc123,0     # Flight option 4 - not chosen
```

### Submission Format
Your submission must contain **ranks** (not probabilities) for each flight option:

```
Id,ranker_id,selected
100,abc123,4
101,abc123,2
102,abc123,1
103,abc123,3
```

Where:
- `Id` matches the row identifier from the test set
- `ranker_id` is the search session identifier (same as in test.csv)
- `selected` is the **rank** you assign (1 = best option, 2 = second best, etc.)

**Important:** Maintain the exact same row order as in `test.csv`

In this example, your model predicts that:
- Row 102 (Id=102) is the best option → Rank 1
- Row 101 (Id=101) is second best → Rank 2  
- Row 103 (Id=103) is third best → Rank 3
- Row 100 (Id=100) is the worst option → Rank 4

## Submission Requirements

1. **Preserve row order:** Maintain the exact same row order as in `test.csv`
2. **Complete rankings:** For each user search request, you must rank ALL flight options returned by the search system
3. **Valid permutation:** Ranks within each `ranker_id` must be a valid permutation (1, 2, 3, ..., N) where N is the number of rows in that group
4. **No duplicate ranks:** Each row within a `ranker_id` group must have a unique rank
5. **Integer values:** All ranks must be integers ≥ 1

### Example for one user search request:
```
Training data shows:
ranker_id: abc123 → Row 102 was chosen (selected=1)

Your submission:
ranker_id: abc123
├── Row 100 → Rank 4 (worst option)
├── Row 101 → Rank 2 (second best)
├── Row 102 → Rank 1 (best - correctly predicted!)
└── Row 103 → Rank 3 (third best)

```

## Validation

Your submission will be validated for:
- Correct number of rows
- Integer rank values
- Valid rank permutations within each group
- No duplicate ranks per search session
- Basic anti-cheating measures

**Note:** The evaluation system expects you to transform your model's output (scores/probabilities) into ranks before submission. Higher model scores should correspond to lower rank numbers (1 = best).


<a id="s004"></a>
## S004

- **source_id:** aeroclub-recsys-2025:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/rules
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/3/text`

##ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions  must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*


# COMPETITION RULES

**TOTAL PRIZE FUND: $10,000**

- 1st Place: $2,500 or $5,000 (with bonus)
- 2nd Place: $1,750 or $3,500 (with bonus)  
- 3rd Place: $750 or $1,500 (with bonus)

## Bonus - Performance Threshold:

Winners who achieve **HitRate@3 ≥ 0.7** receive double their prize amount.

## Technical Requirements

**Inference Limitations**: Final solutions must not use GPU for predictions (GPU usage for training is allowed).

## Winner Selection

**Additional Verification**: Private leaderboard metrics are not final. Organizers will request code from top-10 participants for final evaluation.

**New Data Testing**: Organizers reserve the right to test candidate solutions on unpublished 2025 data.

## 1. COMPETITION-SPECIFIC TERMS

### Competition Name
FlightRank 2025: Aeroclub RecSys Challenge

### Competition Sponsor
AEROCLUB LTD

### Competition Sponsor Address
Republic of Kazakhstan, Almaty, st. Varlamova 27a, 050005

### Competition Website
https://www.kaggle.com/competitions/aeroclub-recsys-2025

### Winner License Type
Non-Exclusive License (see section 3.3)

### Data Access and Use
Competition Use Only (see section 3.1)

## 2.SPECIFIC RULES

### 2.1 Team Limits
a. The maximum team size is five (5).
b. Team mergers are allowed and can be performed by the team leader. In order to merge, the combined team must have a total submission count less than or equal to the maximum allowed as of the team merger deadline.

### 2.2 Submission Limits
a. You may submit a maximum of five (5) submissions per day.
b. You may select up to two (2) final submissions for judging.

### 2.3 Competition Timeline
Competition timeline dates (including entry deadline, final submission deadline, start date, and team merger deadline) are reflected on the competition's Overview > Timeline page.

### 3. Competition Data

**3.1 Data Access and Use**

You may access and use the competition data only for participating in the competition and on Kaggle.com forums. The competition sponsor reserves the right to disqualify any participant who uses the competition data other than as permitted by the competition website and these rules.

**3.2 Data Security**

You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these rules from gaining access to the competition data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the competition data to any party not participating in the competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the competition data.

### 3.3 Winner License

As a condition to being awarded a prize, you hereby grant the competition sponsor the following license with respect to your submission if you are a competition winner:

**Non-Exclusive License**: You hereby grant and will grant to competition sponsor and its designees a worldwide, non-exclusive, sub-licensable, transferable, fully paid-up, royalty-free, perpetual, irrevocable right to use, reproduce, distribute, create derivative works of, publicly perform, publicly display, digitally perform, make, have made, sell, offer for sale and import your winning submission and the source code used to generate the submission, in any media now known or developed in the future, for any purpose whatsoever, commercial or otherwise, without further approval by or payment to you.

For generally commercially available software that you used to generate your submission that is not owned by you, but that can be procured by the competition sponsor without undue expense, you do not need to grant the license for that software.

### 4 External Data and Tools

**4.1 External Data**
You may use data other than the competition data ("external data") to develop and test your submissions. However, you will ensure the external data is either publicly available and equally accessible to use by all participants of the competition at no cost to the other participants.

**4.2 Reasonableness Criteria**
The use of external data and models is acceptable unless their use must be "reasonably accessible to all" and of "minimal cost". A small subscription charge to use additional elements of large language models is acceptable. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

### 5. Eligibility

Unless otherwise stated in the competition-specific rules above, employees, interns, contractors, officers and directors of the competition sponsor, Kaggle Inc., and their respective parent companies, subsidiaries and affiliates may enter and participate in the competition, but are not eligible to win any prizes.

### 6. Winner's Obligations

**a. Delivery & Documentation**
Final model must be implemented as an Estimator with a `predict(X)` method. As a condition of receipt of the prize, the prize winner must deliver the final model's software code as used to generate the winning submission and associated documentation (consistent with the winning model documentation template available on the Kaggle wiki at [https://www.kaggle.com/WinningModelDocumentationGuidelines](https://www.kaggle.com/WinningModelDocumentationGuidelines)) to the competition sponsor. The delivered software code must be capable of generating the winning submission and contain a description of resources required to build and/or run the executable code successfully.

**b. Detailed Description**
You may be required to provide a detailed description of how the winning submission was generated. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.


<a id="s005"></a>
## S005

- **source_id:** aeroclub-recsys-2025:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/abstract
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/4/text`

Welcome aboard! ✈️  

Imagine you're a business traveler searching for flights. You see dozens or even thousands of options with different prices, airlines, departure times, and durations. What makes you click "Book Now" on one specific flight? This competition challenges you to decode those preferences and build a recommendation system that can predict business traveler choices.

### Competition Goal
Build an intelligent flights ranking model that predicts which flight option a business traveler will choose from search results.


<a id="s006"></a>
## S006

- **source_id:** aeroclub-recsys-2025:page:5:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/Prizes
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
- **Archive locator:** `/task_documents/5/text`

**TOTAL PRIZE FUND: $10,000**

**Leaderboard Prizes:**
* 1st Place: $2,500 or $5,000 (with bonus)
* 2nd Place: $1,750 or $3,500 (with bonus)  
* 3rd Place: $750 or $1,500 (with bonus)

**Bonus Performance Threshold:**
* Winners who achieve **HitRate@3 ≥ 0.7** receive Bonus - double their prize amount.


<a id="s007"></a>
## S007

- **source_id:** aeroclub-recsys-2025:page:6:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/overview/foundational-rules
- **retrieved_at:** 2026-10-17T02:59:01.380232+00:00
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

- **source_id:** aeroclub-recsys-2025:thread:585898:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585898
- **thread_id:** 585898
- **comment_id:** opening
- **author_name:** kakuteki
- **author_role:** unknown
- **created_at:** 2025-06-24T03:11:09.960Z
- **retrieved_at:** 2026-10-17T03:10:58.917885+00:00
- **Archive locator:** `/discussion/0/text`

CV vs LB Scores

Let’s discuss CV and LB Scores here.

To start with, My scores.

CV
LB

0.3886
0.3995

0.3886
0.39922

0.3217
0.33091

0.4446
0.43512

0.4490
0.42732

0.4110
0.41832


<a id="s009"></a>
## S009

- **source_id:** aeroclub-recsys-2025:thread:585898:3233134
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585898#comment-3233134
- **thread_id:** 585898
- **comment_id:** 3233134
- **author_name:** Sergey Qt2024
- **author_role:** unknown
- **created_at:** 2025-06-26T13:51:18.073Z
- **retrieved_at:** 2026-10-17T03:10:58.917885+00:00
- **Archive locator:** `/discussion/1/text`

cv0.51 -> lb0.49


<a id="s010"></a>
## S010

- **source_id:** aeroclub-recsys-2025:thread:585898:3231457
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585898#comment-3231457
- **thread_id:** 585898
- **comment_id:** 3231457
- **author_name:** yunsuxiaozi
- **author_role:** unknown
- **created_at:** 2025-06-24T11:39:01.970Z
- **retrieved_at:** 2026-10-17T03:10:58.917885+00:00
- **Archive locator:** `/discussion/2/text`

Seeing that the CV and LB of this competition are almost identical, we can optimize our model offline without submitting it on the leaderboard until the last day.


<a id="s011"></a>
## S011

- **source_id:** aeroclub-recsys-2025:thread:585898:3231465
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585898#comment-3231465
- **thread_id:** 585898
- **comment_id:** 3231465
- **parent_comment_id:** 3231457
- **author_name:** kakuteki
- **author_role:** unknown
- **created_at:** 2025-06-24T11:55:35.217Z
- **retrieved_at:** 2026-10-17T03:10:58.917885+00:00
- **Archive locator:** `/discussion/3/text`

Thank you for your comment. I think so too.


<a id="s012"></a>
## S012

- **source_id:** aeroclub-recsys-2025:thread:585898:3231186
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585898#comment-3231186
- **thread_id:** 585898
- **comment_id:** 3231186
- **author_name:** kakuteki
- **author_role:** unknown
- **created_at:** 2025-06-24T03:49:12.450Z
- **retrieved_at:** 2026-10-17T03:10:58.917885+00:00
- **Archive locator:** `/discussion/4/text`




<a id="s013"></a>
## S013

- **source_id:** aeroclub-recsys-2025:thread:588131:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/588131
- **thread_id:** 588131
- **comment_id:** opening
- **author_name:** 林炯基
- **author_role:** unknown
- **created_at:** 2025-07-04T15:16:52.552Z
- **retrieved_at:** 2026-10-17T03:08:23.774115+00:00
- **Archive locator:** `/discussion/5/text`

How to reduce the group_size


<a id="s014"></a>
## S014

- **source_id:** aeroclub-recsys-2025:thread:591217:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217
- **thread_id:** 591217
- **comment_id:** opening
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-07-26T08:24:32.801Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/6/text`

No reliable CV?

I tried various CV methods (groupkfold, time-wise) but none seems quite as robust in my opinion. only one that somewhat works is groupkfold CV, but I am not 100% confident in that either. 

Has anyone figured out a better way to construct robust validation?


<a id="s015"></a>
## S015

- **source_id:** aeroclub-recsys-2025:thread:591217:3266076
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3266076
- **thread_id:** 591217
- **comment_id:** 3266076
- **author_name:** Cyrus
- **author_role:** unknown
- **created_at:** 2025-08-08T11:11:59.373Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/7/text`

You can easily achieve very strong CV scores using hyperparameter optimization (HPO) with higher tree depths and group-based cross-validation (without leakage). However, the fact that such high scores are possible strongly suggests there's inherent leakage, regardless of the CV strategy used.

This seems to be the kind of competition where it's safer to stick with a highly regularized, small-sized model to avoid overfitting to the private test set. I expect we'll see a leaderboard reshuffle.

My approach is to focus purely on achieving the best CV performance using group-fold CV and a compact model, while completely ignoring the private leaderboard. There’s really no other safe option here.


<a id="s016"></a>
## S016

- **source_id:** aeroclub-recsys-2025:thread:591217:3259448
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3259448
- **thread_id:** 591217
- **comment_id:** 3259448
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2025-08-01T13:29:21.307Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/8/text`

CV | LB

42.1 | 42.0

46.2 | 46.1

56.6 | 48.0

60.4 | 49.2


<a id="s017"></a>
## S017

- **source_id:** aeroclub-recsys-2025:thread:591217:3262524
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262524
- **thread_id:** 591217
- **comment_id:** 3262524
- **parent_comment_id:** 3259448
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-08-03T19:23:49.450Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/9/text`

your correlation seems quite nice, what's your CV scheme?


<a id="s018"></a>
## S018

- **source_id:** aeroclub-recsys-2025:thread:591217:3262734
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262734
- **thread_id:** 591217
- **comment_id:** 3262734
- **parent_comment_id:** 3262524
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2025-08-04T07:44:31.373Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/10/text`

Group 10 folds


<a id="s019"></a>
## S019

- **source_id:** aeroclub-recsys-2025:thread:591217:3262773
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262773
- **thread_id:** 591217
- **comment_id:** 3262773
- **parent_comment_id:** 3262524
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2025-08-04T08:52:08.293Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/11/text`

I will ensemble 10 models and I am done. 0.51+ is out of my reach.


<a id="s020"></a>
## S020

- **source_id:** aeroclub-recsys-2025:thread:591217:3262861
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262861
- **thread_id:** 591217
- **comment_id:** 3262861
- **parent_comment_id:** 3262524
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-08-04T11:34:13.343Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/12/text`

woah! 10 gkf on entire data? How long does it take to train?


<a id="s021"></a>
## S021

- **source_id:** aeroclub-recsys-2025:thread:591217:3262867
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262867
- **thread_id:** 591217
- **comment_id:** 3262867
- **parent_comment_id:** 3262524
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2025-08-04T11:48:07.167Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/13/text`

10 days if not parallel. Now, I use a sample to train, but validate on full.


<a id="s022"></a>
## S022

- **source_id:** aeroclub-recsys-2025:thread:591217:3262875
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262875
- **thread_id:** 591217
- **comment_id:** 3262875
- **parent_comment_id:** 3262524
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2025-08-04T12:03:50.037Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/14/text`

Do you use JSONs Raw Additional Data? I don't.


<a id="s023"></a>
## S023

- **source_id:** aeroclub-recsys-2025:thread:591217:3262919
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3262919
- **thread_id:** 591217
- **comment_id:** 3262919
- **parent_comment_id:** 3262524
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-08-04T13:25:32.040Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/15/text`

Very little json data, i am not sure if too many things can be extracted and successfully merged with the training data.


<a id="s024"></a>
## S024

- **source_id:** aeroclub-recsys-2025:thread:591217:3254375
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254375
- **thread_id:** 591217
- **comment_id:** 3254375
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-26T11:45:33.923Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/16/text`

Same here. May local CV could achieve 0.6 without data leakage, but only get 0.51 in test.


<a id="s025"></a>
## S025

- **source_id:** aeroclub-recsys-2025:thread:591217:3254376
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254376
- **thread_id:** 591217
- **comment_id:** 3254376
- **parent_comment_id:** 3254375
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-26T11:46:37.437Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/17/text`

But I haven't tried k-fold or other model ensemble things yet, not sure would it affect.


<a id="s026"></a>
## S026

- **source_id:** aeroclub-recsys-2025:thread:591217:3254489
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254489
- **thread_id:** 591217
- **comment_id:** 3254489
- **parent_comment_id:** 3254376
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-07-26T16:00:07.007Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/18/text`

Thanks. Whats your CV scheme BTW?


<a id="s027"></a>
## S027

- **source_id:** aeroclub-recsys-2025:thread:591217:3254491
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254491
- **thread_id:** 591217
- **comment_id:** 3254491
- **parent_comment_id:** 3254376
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-26T16:08:43.803Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/19/text`

not sure. but maybe normal 5-fold. Other than that, It will take too long to train the proper model.


<a id="s028"></a>
## S028

- **source_id:** aeroclub-recsys-2025:thread:591217:3254492
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254492
- **thread_id:** 591217
- **comment_id:** 3254492
- **parent_comment_id:** 3254376
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-26T16:09:48.447Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/20/text`

how about you? BTW how did your CV compare to test?


<a id="s029"></a>
## S029

- **source_id:** aeroclub-recsys-2025:thread:591217:3254521
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254521
- **thread_id:** 591217
- **comment_id:** 3254521
- **parent_comment_id:** 3254376
- **author_name:** Phaedrus
- **author_role:** unknown
- **created_at:** 2025-07-26T17:01:55.590Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/21/text`

Group kfold, cv 0.6 lb 0.52


<a id="s030"></a>
## S030

- **source_id:** aeroclub-recsys-2025:thread:591217:3254583
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254583
- **thread_id:** 591217
- **comment_id:** 3254583
- **parent_comment_id:** 3254376
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-26T19:54:03.727Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/22/text`

Thanks for answering!


<a id="s031"></a>
## S031

- **source_id:** aeroclub-recsys-2025:thread:591217:3254560
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254560
- **thread_id:** 591217
- **comment_id:** 3254560
- **parent_comment_id:** 3254375
- **author_name:** Sergey Qt2024
- **author_role:** unknown
- **created_at:** 2025-07-26T18:36:39.883Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/23/text`

Same here. 0.599 and 0.5 in test. Thank you for sharing, because I spend 2 days searching for leakage. And sure no leak.  I think it is because ticket offer changed after summer has gone. (Just few train test split, not k fold)


<a id="s032"></a>
## S032

- **source_id:** aeroclub-recsys-2025:thread:591217:3254721
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254721
- **thread_id:** 591217
- **comment_id:** 3254721
- **parent_comment_id:** 3254560
- **author_name:** Mikhail Golubchik
- **author_role:** unknown
- **created_at:** 2025-07-27T05:21:23.760Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/24/text`

Yes, it's possible that the proportion of larger groups has increased, for example. However, my local validation was showing 0.511–0.514 with lb 0.512 until recently. Then the validation rose to 0.520 while the lb was 0.513.


<a id="s033"></a>
## S033

- **source_id:** aeroclub-recsys-2025:thread:591217:3254804
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254804
- **thread_id:** 591217
- **comment_id:** 3254804
- **parent_comment_id:** 3254560
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-27T09:04:46.117Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/25/text`

Interesting! Anyway, thanks for sharing!


<a id="s034"></a>
## S034

- **source_id:** aeroclub-recsys-2025:thread:591217:3254651
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254651
- **thread_id:** 591217
- **comment_id:** 3254651
- **parent_comment_id:** 3254375
- **author_name:** mango
- **author_role:** unknown
- **created_at:** 2025-07-27T00:20:50.333Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/26/text`

do you exclude group with size <= 10 when calculating hitrate@3?


<a id="s035"></a>
## S035

- **source_id:** aeroclub-recsys-2025:thread:591217:3254774
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254774
- **thread_id:** 591217
- **comment_id:** 3254774
- **parent_comment_id:** 3254651
- **author_name:** Ding Yang Wang
- **author_role:** unknown
- **created_at:** 2025-07-27T07:58:22.157Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/27/text`

Yes

` ():
    
    
    val_df = pl.DataFrame({
        : groups_np,
        : labels_np,
        : preds_np
    })

    
    val_df = val_df.sort([, ], descending=[, ])

    
    val_df = val_df.with_columns([
        pl.col().rank(method=, descending=).over().alias()
    ])

    
    group_size_df = (
        val_df.group_by()
              .agg(pl.().alias())
    )

    
    hit_df = (
        val_df.(pl.col() == )
              .join(group_size_df, on=)
              .with_columns([
                  (pl.col() <=top).cast(pl.Int8).alias()
              ])
    )

    
    cond = pl.col() > min_group_size
     max_group_size   :
        cond = cond & (pl.col() <= max_group_size)
    hit_filtered = hit_df.(cond)

    
    num_groups = hit_filtered.height
    num_hits = hit_filtered[].()
     num_groups > :
        hitrate = num_hits / num_groups
    :
        hitrate = 

    
    ()

     hitrate
`


<a id="s036"></a>
## S036

- **source_id:** aeroclub-recsys-2025:thread:591217:3254817
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/591217#comment-3254817
- **thread_id:** 591217
- **comment_id:** 3254817
- **parent_comment_id:** 3254651
- **author_name:** mango
- **author_role:** unknown
- **created_at:** 2025-07-27T09:39:50.863Z
- **retrieved_at:** 2026-10-17T03:07:27.452076+00:00
- **Archive locator:** `/discussion/28/text`

The function looks fine. Did you by any chance use information from the validation set when constructing your features?


<a id="s037"></a>
## S037

- **source_id:** aeroclub-recsys-2025:thread:596975:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/596975
- **thread_id:** 596975
- **comment_id:** opening
- **author_name:** just another tuesday
- **author_role:** unknown
- **created_at:** 2025-08-05T23:24:38.659Z
- **retrieved_at:** 2026-10-17T03:05:21.071068+00:00
- **Archive locator:** `/discussion/29/text`

dealing with large group sizes

has anyone been able to share some insights on how to deal with the large group sizes? looking at the hitrate@3 from the example notebooks it has been dismal. ive tried negative sampling and mining and running a pre-classifier to downsample the group sizes to the ranker but the performance seems to be worse than if i just feed the entire dataset to the ltr ranker


<a id="s038"></a>
## S038

- **source_id:** aeroclub-recsys-2025:thread:596975:3265509
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/596975#comment-3265509
- **thread_id:** 596975
- **comment_id:** 3265509
- **author_name:** Samvel Kocharyan
- **author_role:** unknown
- **created_at:** 2025-08-07T15:43:50.880Z
- **retrieved_at:** 2026-10-17T03:05:21.071068+00:00
- **Archive locator:** `/discussion/30/text`

That is one of the most interesting question in the competition. Hope we'll continue to discover it very soon 😊


<a id="s039"></a>
## S039

- **source_id:** aeroclub-recsys-2025:thread:598515:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/598515
- **thread_id:** 598515
- **comment_id:** opening
- **author_name:** Ionut Visan
- **author_role:** unknown
- **created_at:** 2025-08-11T12:02:35.968Z
- **retrieved_at:** 2026-10-17T03:04:52.949381+00:00
- **Archive locator:** `/discussion/31/text`

Documentation and Solutions

[@samvelkoch](https://www.kaggle.com/samvelkoch) 

In case of ranking in the top 3 or qualifying for bonus prizes, what is the deadline for delivering the documentation and solutions?


<a id="s040"></a>
## S040

- **source_id:** aeroclub-recsys-2025:thread:598515:3267533
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/598515#comment-3267533
- **thread_id:** 598515
- **comment_id:** 3267533
- **author_name:** Samvel Kocharyan
- **author_role:** unknown
- **created_at:** 2025-08-11T12:26:12.493Z
- **retrieved_at:** 2026-10-17T03:04:52.949381+00:00
- **Archive locator:** `/discussion/32/text`

[@ionutvisan](https://www.kaggle.com/ionutvisan) open for suggestions. What will be optimal for your team for example? Usually it is 7-14 days.


<a id="s041"></a>
## S041

- **source_id:** aeroclub-recsys-2025:thread:598515:3267544
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/598515#comment-3267544
- **thread_id:** 598515
- **comment_id:** 3267544
- **parent_comment_id:** 3267533
- **author_name:** Ionut Visan
- **author_role:** unknown
- **created_at:** 2025-08-11T12:42:09.613Z
- **retrieved_at:** 2026-10-17T03:04:52.949381+00:00
- **Archive locator:** `/discussion/33/text`

Thanks [@samvelkoch](https://www.kaggle.com/samvelkoch) for the answer. Anything between 10 to 14 days should be fine.


<a id="s042"></a>
## S042

- **source_id:** aeroclub-recsys-2025:thread:599666:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666
- **thread_id:** 599666
- **comment_id:** opening
- **author_name:** gezi
- **author_role:** unknown
- **created_at:** 2025-08-18T03:45:09.739Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/34/text`

1st solution using count-based features (Single model PB 0.54942)

First, I want to express my sincere gratitude to the organizers for providing such a large-scale, real-world dataset. It offered a rare opportunity to dive deep into practical challenges and learn from them.

I also want to thank the authors of several outstanding notebooks that guided my journey:

- I began with [XGBoost Ranker with Polars](https://www.kaggle.com/code/ka1242/xgboost-ranker-with-polars) a clean and efficient starting point that helped me grasp the essentials of ranking models. Thank you [@ka1242](https://www.kaggle.com/ka1242)!

- The most creative idea, in my opinion, came from [reranking approach](https://www.kaggle.com/code/mango789/xgboost-ranker-rule-based-rerank) . The rule-based reranking worked like a charm, and without that notebook, I wouldn’t have realized how crucial `flight_hash` is to the final performance. Huge thanks to [@mango789](https://www.kaggle.com/mango789) !

Approach overview and note on test data usage

My main single-model solution initially leveraged a leak-like feature: I included the test data from the very beginning of the competition. Count-based categorical encoding built on the full dataset noticeably improved both local validation and the public leaderboard.

I recall a discussion where the host mentioned that using the test set was acceptable because it contains no labels. While some recommendation competitions forbid using the test data, I didn’t find such a restriction here. Still, in real scenarios we cannot rely on future data, and we usually predict day by day using only past labels. A streaming setup would better reflect production.

Below I share results for the same single model trained without the test data (i.e., I removed the test set from the count-based encodings and training input).

Results without using test data

model
valid
LB
PB

best single model
0.504745
0.54062
0.54156

best single model without testdata
0.478704
0.51978
0.52692

This is an ongoing write-up; I may refine it or add more data stats later.

Key components

Validation strategy

- **Temporal split:** This is a recommendation task, so datetime order matters. The dataset spans `requestDate` from 2024-05-17 03:03:08 to 2024-12-31 18:54:00, which I index as days 1–229.

- **Fold design:** I used a single temporal fold: train on days 1–103, validate on days 104–166, and test on days 167–229.

- **Rationale:** Validation and test windows have similar lengths, and local validation generally matched the LB, especially for larger improvements. When there was a mismatch, I trusted local validation. One exception was the final Optuna weight tuning for ensembles, which can overfit to the validation set.

Count-based categorical encoding

- **XGBoost / LightGBM:** I applied count-based encoding to all categorical features, then treated all columns as numerical — no categorical indices were passed into training.

- **CatBoost:** I also experimented with exactly the same count-based encoding here, converting everything to numerical features. However, in my tests, all variations yielded very similar results, with no meaningful gain over the baseline.

Time features

- **Importance:** Time-derived features gave the largest lift compared to using only the provided CSV fields.

- **Cyclical encoding:** I added sine/cosine transforms so the model can capture wrap-around (e.g., hours 23 and 0 are adjacent).

Duration and distance features

- **Accurate duration:** I converted local times to UTC to compute true elapsed durations.

- **Distance-based signals:** I computed airport distances from lat/lon and derived related features such as `direct_price_per_km`.

Simple rank-based features on important base features

- **Motivation:** Ranking proxies (per group) for price, duration, and itinerary complexity helped the ranker focus on relative ordering within a user/query.

Ranking features code (Polars)

` polars  pl

rank_order = {
    : ,
    : ,
    : ,
    : ,
    : ,
    : ,
    : ,
    : ,
    : ,
}

 () :
    exprs = []
     col, order  rank_order.items():
         col  df.columns:
            exprs.append(
                pl.col(col)
                  .rank(method=, descending=(order == ))
                  .over(group_col)
                  .alias()
            )
     df.with_columns(exprs)
`

There are more experiments to be done, for example adding  'miniRules0_statusInfos': 'desc',  'miniRules1_statusInfos': 'desc' will further improve local valid and online PB, unfortunately LB drop:)    

model
valid
LB
PB

best single model
0.504745
0.54062
0.54156

adding more rank feats like  miniRules*_statusInfos
0.506949
0.53557
0.54284

Additonal ranking features based on (ranker_id, flight_hash)

As we fould rule based on flight_hash could improve local and online, we could add them to our feats so tree models could learn more.    

So in additon to add_ranking_feats(df, 'ranker_id')  I also added add_ranking_feats(df, (ranker_id, flight_hash))

`COLS_TO_COMPARE = [
    ,
    ,
    ,
    ,
    ,
    
]

df = df.with_columns(
    pl.concat_str(
        [pl.col(c).cast().fill_null()  c  COLS_TO_COMPARE]
    ).alias()
)

df = add_ranking_feats(df, )
df = add_ranking_feats(df, [, ])
`

Couting of important base features groupby profileId and compayID

`
 ():
  exprs = []
   col  rank_order.keys():
     col  df.columns:
      exprs.extend([
        pl.col(col).mean().over(group_col).alias(),
        pl.col(col).().over(group_col).alias(),
        pl.col(col).().over(group_col).alias(),
        pl.col(col).std().over(group_col).alias(),
        pl.col(col).median().over(group_col).alias(),
      ])
  df = df.with_columns(exprs)
  exprs = []
   col  rank_order.keys():
     col  df.columns:
      exprs.extend([
        ((pl.col(col) - pl.col()) / (pl.col() + )).alias(),
        ((pl.col(col) - pl.col()) / (pl.col() - pl.col() + )).alias(),
        (pl.col(col) / (pl.col() + )).alias(),
      ])

  df = df.with_columns(exprs)
   df

df = add_stats_feats(df, )
df = add_stats_feats(df, )
`

Ensembel

During the competition, I trained 41 models and tuned their weights with Optuna, but none beat a simple ensemble of my top five single models. For simplicity, I report that 5‑model ensemble result (late submission) here: all models use the same features but differ by learner and objective. XGBoost consistently performed best, with LightGBM adding useful diversity; CatBoost underperformed. The ensemble includes five models—XGBoost with rank:ndcg, rank:map, and rank:pairwise objectives, an XGBoost binary classifier, and LightGBM with LambdaRank (LightGBM’s xendcg performed much worse). The best setup uses equal weights across the five models. 

model
valid
LB
PB

5 top single models
0.5101
0.54053
0.54725

Further improments

I intentionally avoided using any stat features derived from labels or selected outcomes, as including them could lead the model to "see" future labels during training, resulting in overfitting and poor generalization on unseen data. 

However, one promising workaround is to construct **windowed features**—that is, using only historical statistics available prior to each instance's timestamp. This technique is effectively demonstrated in [Mikhail Golubchik’s XGBoost notebook](https://www.kaggle.com/code/mikhailgolubchik/sm-xgboost-single). Thanks to [@mikhailgolubchik](https://www.kaggle.com/mikhailgolubchik) for the inspiration!

I haven’t implemented this yet, mainly because it’s time-consuming and I was concerned about a potential mismatch between training and test data: for training, you can use stats up to the instance time, but for test data, you're limited to stats from earlier days only. Still, this approach is definitely worth exploring further.

I merged the code from [@mikhailgolubchik](https://www.kaggle.com/mikhailgolubchik)'s notebook and changed the feats to be used(source_cols) a bit , notice you could investigate more feats.  

` FLAGS.history_avg:
  test = util.get_test(df)

  df = util.get_nontest(df)
  train = util.get_train(df)

    FLAGS.online:
    valid = util.get_valid(df)
    test = pl.concat([valid, test], =)

  source_cols = [
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
      ,
  ]

  train, df_stats_pr = make_history_avg(train,
                                      =source_cols,
                                      =,
                                      =)
  train, df_stats_co = make_history_avg(train,
                                      =source_cols,
                                      =,
                                      =)

  test = test.join(df_stats_pr, =, =)
  test = test.join(df_stats_co, =, =)

  df = gz.align_and_concat([train, test])
`

model
valid
LB
PB

add selected/pos history avg feats
0.5120
0.54889
0.54942

4 history avg feats xgb ensemble

0.55201
0.55291

Well such great improvment, PB up about 0.008, so personally I think we might have over 0.6 score on PB but > 0.7 might be a bit too hard but not mission impossible:) For this dataset about 50% profileId in test exists in the train dataset, I did not investiage for each profileId how many ranker_ids exits, if there are many then may be we can also use more user history book info.  Another finding is with model perform better we do not need rerank anymore.  

Opensource the solution

[https://www.kaggle.com/code/goldenlock/aeroclub-recsys-2025-1st-solution](https://www.kaggle.com/code/goldenlock/aeroclub-recsys-2025-1st-solution)  

Notice aeroclub-recsys-2025-model2 has the 4 xgb models which ensemble with PB 55291 and the submission.parquet.   

Please refer to the notebook and its README.


<a id="s043"></a>
## S043

- **source_id:** aeroclub-recsys-2025:thread:599666:3276565
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3276565
- **thread_id:** 599666
- **comment_id:** 3276565
- **author_name:** sanjana kumari
- **author_role:** unknown
- **created_at:** 2025-08-26T18:00:30.603Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/35/text`

Nice and interesting


<a id="s044"></a>
## S044

- **source_id:** aeroclub-recsys-2025:thread:599666:3273518
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3273518
- **thread_id:** 599666
- **comment_id:** 3273518
- **author_name:** Irakoze Ntawigenga Kelly
- **author_role:** unknown
- **created_at:** 2025-08-22T20:11:23.677Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/36/text`

Thank you for sharing this it will help while learning!


<a id="s045"></a>
## S045

- **source_id:** aeroclub-recsys-2025:thread:599666:3272919
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3272919
- **thread_id:** 599666
- **comment_id:** 3272919
- **author_name:** Naqi Naqvi
- **author_role:** unknown
- **created_at:** 2025-08-21T18:48:29.943Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/37/text`

Nice, really interesting to see you approached this and to learn from it. Thanks for sharing! Congrats on winning!!


<a id="s046"></a>
## S046

- **source_id:** aeroclub-recsys-2025:thread:599666:3271644
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3271644
- **thread_id:** 599666
- **comment_id:** 3271644
- **author_name:** 267-khyati
- **author_role:** unknown
- **created_at:** 2025-08-19T10:24:16.363Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/38/text`

good work this is my first comment


<a id="s047"></a>
## S047

- **source_id:** aeroclub-recsys-2025:thread:599666:3271431
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3271431
- **thread_id:** 599666
- **comment_id:** 3271431
- **author_name:** Samvel Kocharyan
- **author_role:** unknown
- **created_at:** 2025-08-18T21:36:06.557Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/39/text`

Still, in real scenarios we cannot rely on future data, and we usually predict day by day using only past labels. A streaming setup would better reflect production.

Why your approach could work in real scenario in this specific case? In flight search, count-based encoding is realistic because flight schedules, route frequencies, and large volumes of daily requests are all available and some features can be pre-computed.


<a id="s048"></a>
## S048

- **source_id:** aeroclub-recsys-2025:thread:599666:3271452
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3271452
- **thread_id:** 599666
- **comment_id:** 3271452
- **parent_comment_id:** 3271431
- **author_name:** gezi
- **author_role:** unknown
- **created_at:** 2025-08-19T00:05:57.150Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/40/text`

Yeah you are correct, we could have real time counting, but for my approach here the problem is I used counting of like day 100 to predict on day 99, however the total pipline could still work if I use test dataset but still if I count based only on instance history (not look ahead), so using just  previous window/history feature could be fine either counting on all expousure data or selected data.


<a id="s049"></a>
## S049

- **source_id:** aeroclub-recsys-2025:thread:599666:3274842
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3274842
- **thread_id:** 599666
- **comment_id:** 3274842
- **author_name:** Sarah Arshad
- **author_role:** unknown
- **created_at:** 2025-08-25T14:02:30.667Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/41/text`

Thanks for sharing…it helps alot!


<a id="s050"></a>
## S050

- **source_id:** aeroclub-recsys-2025:thread:599666:3273531
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3273531
- **thread_id:** 599666
- **comment_id:** 3273531
- **author_name:** ABDELHAK OUANZOUGUI
- **author_role:** unknown
- **created_at:** 2025-08-22T20:33:35.343Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/42/text`

Super cool work !! thank you !!


<a id="s051"></a>
## S051

- **source_id:** aeroclub-recsys-2025:thread:599666:3271434
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3271434
- **thread_id:** 599666
- **comment_id:** 3271434
- **author_name:** Irakoze Ntawigenga Kelly
- **author_role:** unknown
- **created_at:** 2025-08-18T21:47:02.087Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/43/text`

Thanks for sharing this!


<a id="s052"></a>
## S052

- **source_id:** aeroclub-recsys-2025:thread:599666:3271169
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599666#comment-3271169
- **thread_id:** 599666
- **comment_id:** 3271169
- **author_name:** Sergey Qt2024
- **author_role:** unknown
- **created_at:** 2025-08-18T08:09:03.440Z
- **retrieved_at:** 2026-10-17T03:02:17.439184+00:00
- **Archive locator:** `/discussion/44/text`

您好。 Congratulation！


<a id="s053"></a>
## S053

- **source_id:** aeroclub-recsys-2025:thread:599687:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599687
- **thread_id:** 599687
- **comment_id:** opening
- **author_name:** mango
- **author_role:** unknown
- **created_at:** 2025-08-18T07:35:54.485Z
- **retrieved_at:** 2026-10-17T03:02:03.100967+00:00
- **Archive locator:** `/discussion/45/text`

4th solution: XGBoost at the Core of Flight Recommendation

First of all, I’d like to thank the organizers for hosting this recommendation competition. As a newcomer to both Kaggle and recommendation systems, I feel honored to work with a real-world industrial dataset and to develop and refine algorithms on it.

I used [@ka1242’s notebook](https://www.kaggle.com/code/ka1242/xgboost-ranker-with-polars) as my starting point, and my entire pipeline is built upon it. Many thanks to [@ka1242](https://www.kaggle.com/ka1242) for sharing this solid foundation, which allowed me to focus on further improvements and model refinement.

**You can find the source code for training our best xgboost model in this repo** [https://github.com/mango7789/FlightRank-2025-Aeroclub-RecSys-Cup-4th-Solution](https://github.com/mango7789/FlightRank-2025-Aeroclub-RecSys-Cup-4th-Solution)

Data Split and Validation

Since the order of occurrence can influence recommendation performance, I followed the train–validation split strategy used in the starter notebook. Specifically, the last ~10% of the training data is held out for validation.

Feature Engineering

I constructed a wide range of features for this task. Broadly, they can be grouped into the following categories: **segments, time, rank, price, cabin class, company, carrier, frequent flyer, profile, airport, corporateTariffCode, group, label, option, and route.** Most of these are relatively straightforward and intuitive to design, so here I will highlight a few representative ones:

- **Rank**: derived from the within-query ranks of price and duration, each normalized separately, and further combined through interaction features.  

- **Cabin class**: added a feature indicating whether all segments belong to the same (economic) class.  

- **Company**: occurrence counts, average price, and proportion of direct flights — this category provided notable improvement.  

- **Carrier**: selection frequency and ratio.  

- **Profile**: only counted occurrences, as additional statistics were not effective due to sparsity.  

- **Airport**: enriched with external data from [this discussion](https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/585877), including indicators such as whether the flight is international and whether it crosses time zones. I also experimented with haversine distance and “same departure–return airport” as a proxy for convenience.  

- **CorporateTariffCode**: usage frequency.  

- **Route**: aggregated statistics such as average price, average duration, direct-flight ratio, and corporate-code ratio.  

- **Group**: aggregated stats for each `ranker_id`.  

The **label** and **option** features are derived from insights in the raw json files. Each json file contains additional information, such as a label for each flight combination. These labels likely correspond to the information displayed on the flight page during ticket purchase and may influence user choice. I extracted these labels from the json files; however, as noted in [this discussion](https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/590264#3253916), a perfect match to the parquet data is not possible. Instead, I applied a coarse-grained row-order alignment, which introduces roughly 10% mismatches. Despite this noise, including these features still led to some model improvement.  

Upon inspecting the raw json, I observed that a single **flight option** can have multiple **pricings**, likely due to different promotional policies. In the parquet data, multiple records may correspond to the same option with different pricings, which are **mutually exclusive** since a user can select only one flight and one pricing at a time. Therefore, it is important to construct features grouped by option, such as maximum, minimum, average, or rank within the option. As with labels, perfect alignment between the parquet and json files is infeasible, so I used the `flight_hash` as a surrogate to approximate the option.

Originally, the `flight_hash` was used in reranking as a penalty for flights within the same option ([example here](https://www.kaggle.com/code/mango789/xgboost-ranker-rule-based-rerank)). After confirming its usefulness in reranking, I extended its use to create additional groupby features for the model.

I also extracted `searchType` and `age` from the json files, but for reasons I do not fully understand, these features did not improve model performance.

Other Notes

Most of my work in this competition focused on feature engineering, training XGBoost and LGBM models, tuning parameters, and experimenting with objectives such as `rank:pairwise`, `rank:ndcg`, and `lambdarank`. For data transformations, I noticed that price and duration follow a long-tail distribution, so I applied log transformations.  

I also explored other ideas, such as pseudo-labeling and adding weights to each group, but these approaches did not improve performance on my side.  

Additionally, I considered training a rerank deep learning model to fine-tune scores after the coarse-grained GBDT predictions, as I observed a hitrate@20 above 0.8 in local CV. However, due to time constraints, this was not implemented.

Regarding the `bySelf` column, all tickets in the training data are booked `bySelf`, while in the test data there are about 200,000 rows that are not `bySelf`. I believe results could improve if we had non-`bySelf` tickets in the training data. It might also be beneficial to create some human-crafted rules for non-`bySelf` ticket selection based on empirical company choices.

Other external data, such as more informative airport data, flight number (for delay statistics) and aircraft code (to distinguish low-cost, standard, and premium flights), may also help improve performance, I think.

To be honest, my best model was trained three weeks ago, and further attempts at feature engineering or adjustments did not yield improvement. This may be due to the sparsity in users' historical behavior, suggesting that the practical limit for GBDT methods on this dataset is around 0.53–0.54.

Deep Learning Ranker

To explore ways of enhancing the module's capabilities, I tested several architectures with different configurations. The most effective one turned out to be a hybrid neural ranking architecture that combines:

Linear terms:

- One-hot style embeddings for categorical features (dimension = 1).

- A linear projection of numeric features.

Embeddings for categorical features:

- Each categorical feature is mapped to a dense embedding (shared size = 64).

- These embeddings are concatenated with normalized numeric features.

Deep MLP tower:

- Several fully connected layers (512 → 256 → 128 → 64) with BatchNorm, ReLU, and Dropout.

- Produces nonlinear interactions between categorical and numeric features.

Output layer:

- Final linear unit outputs a single relevance score per item.

- Scores are trained with a pairwise ranking loss (xRankNet variant).

The deep learning model showed relatively weak performance (0.48–0.495), emphasizing that deeper architectures are not always more effective than traditional methods. In many cases, it is more reliable to rely on well-established models such as XGBoost, LightGBM, and similar approaches.

I also experimented with other architectures incorporating ideas such as SENet with normalization and dropout, bilinear interactions, self-attention layers, and transformer-based encoders for categorical and numerical features. However, in most cases, the results were not optimal or showed only minor variations in individual performance.

Ensemble

To further enhance performance and boost the overall score, I explored several ensemble strategies that combine the three previously trained models: XGBoost, LightGBM, and DL, with the most effective one being:

First, the confidence score is computed by combining two signals: a base score that decreases linearly from 1 for the top item to 0 for the last item within each group, and an RRF score that gives higher weight to top-ranked items; the final confidence is a weighted mix of these two, balancing group position and reciprocal rank.

Next, load multiple confidence files, aligning them, and then computing weights for each model based on two factors — uniqueness (how different it is from others, using PCA + Spearman residuals) and informativeness (entropy of its confidence distribution); these weights are combined to produce a final weighted confidence score, which is then ranked per group to generate the ensemble submission.

This method achieved solid performance (0.536–0.537), but it required tremendous effort for only a marginal improvement over the standalone XGBoost model (0.53552).


<a id="s054"></a>
## S054

- **source_id:** aeroclub-recsys-2025:thread:599687:3272114
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599687#comment-3272114
- **thread_id:** 599687
- **comment_id:** 3272114
- **author_name:** mango
- **author_role:** unknown
- **created_at:** 2025-08-20T09:20:31.347Z
- **retrieved_at:** 2026-10-17T03:02:03.100967+00:00
- **Archive locator:** `/discussion/46/text`

Feel free to check out the source code repository: [FlightRank 2025 – 4th Solution](https://github.com/mango7789/FlightRank-2025-Aeroclub-RecSys-Cup-4th-Solution)😘


<a id="s055"></a>
## S055

- **source_id:** aeroclub-recsys-2025:thread:600069:opening
- **url:** https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/600069
- **thread_id:** 600069
- **comment_id:** opening
- **author_name:** Mikhail Golubchik
- **author_role:** unknown
- **created_at:** 2025-08-20T18:12:55.624Z
- **retrieved_at:** 2026-10-17T03:01:20.659184+00:00
- **Archive locator:** `/discussion/47/text`

8-th place solution

Before diving into the solution description itself, I would first like to thank the competition organizers for an interesting task and for providing real, authentic data.

Solution Description

**Baseline**. I began with the solution by Kirill Khoruzhii (@ka1242): 'AeroClub RecSys 2025 - XGBoost Ranking Baseline' ([https://www.kaggle.com/code/ka1242/xgboost-ranker-with-polars)](https://www.kaggle.com/code/ka1242/xgboost-ranker-with-polars)). I would like to thank him for an excellent set of features.

**Models Used.** I also experimented with using LightGBM both as a replacement for and in addition to XGBoost. However, it yielded roughly the same results, so I eventually discontinued its use by the end of the competition.

**Important Features.** As expected, the most important features turned out to be ticket prices and their derivatives. This includes metrics like the ratio to the median price within a group, among others. Features related to flight duration and the number of connections were also significant. Additionally, features indicating the possibility of ticket cancellation or exchange, as well as the ticket class, proved to be substantial contributors.

**Feature Selection:** Features were selected primarily based on intuition, driven by what we expected to be important for a person when choosing a flight ticket. This initial selection was then validated, and if the assumption about a feature's usefulness was confirmed, it was kept for the final model.

In several cases, however, adding certain features—particularly categorical ones related to the customers' past choice history—led to severe overfitting. Although using such features seemed intuitively beneficial, they proved to be impractical in practice.

For example, a factor like the price at which a customer/company previously booked a ticket turned out to be useful. Conversely, trying to incorporate the type of aircraft or the airline carrier a customer/company preferred in the past led to overfitting.

**Overfitting:** Features based on customer choice history led to overfitting. In fact, the first-place competition winner, [@goldenlock](https://www.kaggle.com/goldenlock), stated in his solution [https://www.kaggle.com/competitions/aeroclub-recsys-2025/writeups/1st-solution-using-count-based-features](url) that he avoided using them entirely until the competition ended. However, after the competition concluded, he tested the approach I proposed for utilizing a subset of these features and managed to significantly improve the score of his final solution.

**Mitigating Overfitting:** The approach was based on a windowed method for generating customer history features. Specifically, for each group, features were constructed using data only from groups where a ticket was purchased by the same customers prior to the current ticket selection group

**Historical Window Features:** For the features used to calculate the history of option selection within a group, a specific company, or a user, the following metrics were generated: mean, median, and the number of groups in which a choice was previously made and this feature was present. The 25% and 75% quantiles were also generated. The historical features were based on the following features:

- 'legs0_departureAt_hour', 'legs1_departureAt_hour', 'legs0_arrivalAt_hour', 'legs1_arrivalAt_hour' 

- 'price_rank', 'price_from_median', 'duration_rank', 'duration_from_median', 

- 'avg_cabin_class', 'baggage_total', 'l0_seg', 

- 'legs0_segments0_seatsAvailable', 'legs0_segments0_baggageAllowance_quantity', 'legs0_segments0_cabinClass', 

- 'miniRules1_statusInfos', 'miniRules0_statusInfos' 

Training of Models

**Validation:** When selecting features, the data was split into a training and test part, which was then combined with validation. As I now understand, this was probably a mistake, and validation and test should have been separated.

At the same time, the score obtained on validation was almost the same as the one on the Public and Private Leaderboards. Moreover, improvements in local validation usually correlated with improvements on the LB.

Local validation yielded about 0.535. For local validation, the last month of training data was used.

**Training:** Training was performed on the full training dataset without any use of test data. This included not using the test set for computing statistics or encoding categorical features.

**Handling New Data in Test:** To prevent the model from being significantly distorted by the appearance of new categories in categorical features, about 1% of categorical values in the training data were randomly replaced with missing values. If the proportion of such missing values was less than 1%, additional ones were added. Then, in the test set, unknown categories in categorical features were also marked as missing values (-1) during categorical encoding.

**Reducing Group Size**: While considering ways to preselect the most promising candidates for the final choice of the three most likely options a client would choose, I tried simply randomly reducing all groups to a maximum of 50 options. This involved downsampling negative examples (those not chosen by the client). Unexpectedly, this improved the score. I hypothesized that ranking became easier for the models, and the class imbalance was reduced. This is because the probability of correctly guessing the user's choice in a large group was low anyway. However, without reducing group size, models might have struggled more to learn anything useful from such a large group.

A beneficial side effect was the reduction in memory usage during training and an increase in training speed. This, in turn, allowed for the use of more features. It's important to note that the group size reduction was performed after all features were calculated and statistics were collected. That is, the features were generated using the full groups. Reducing the group size before feature engineering led to worse model performance.

Possible Improvements

It would be beneficial to find a way to train the model without overfitting, not only on numerical data but also on historical categorical data. This was not achieved within the scope of this solution.

Approaches that generate additional features using language models, or other transformers seem very promising. The idea is to use an attention mechanism to extract meaningful information from the full description of the offered options. [@sergeyqt20244](https://www.kaggle.com/sergeyqt20244) mentioned attempts to apply Bert2rec, though so far without significant results: [https://www.kaggle.com/competitions/aeroclub-recsys-2025/discussion/599559#3271192](url)

Below is a notebook with my single model solution:

[https://www.kaggle.com/code/mikhailgolubchik/sm-xgboost-single](url)

