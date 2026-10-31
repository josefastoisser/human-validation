# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation Metrics](#s003)
- [S004: rules](#s004)
- [S005: Competition Timeline](#s005)
- [S006: Organizing Team](#s006)

<a id="s001"></a>
## S001

- **source_id:** icdar-2025-ColiE_Task2:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/data-description
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/0/text`

##  Dataset description

The participants of this competition are provided with the BookSCE dataset. 

The dataset comprises around 11K book chunks accompanied by labels for subtasks 1.1 and 1.2. 


## Ground truth

To train the models, the participants are provided with training and validation sets consisting of books in the "txt" format and the corresponding ground truth files in the "csv" format. The ground truth includes the chunk IDs and the corresponding labels.



**Task 2.1: Identifying the century of origin for a given text (century_label)**

- 1  - 17th century
- 2 - 18th century
- 3 - 19th century
- 4 - 20th century
- 5 - 21st century

**Task 2.2: Pinpointing the specific decade within that century in which the text was composed (century_label)**

The decades in each century are encoded by one of ten labels:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Input and output formats
The classifier's input is a book chunk in text format, and its output is a single value (corresponding label). 
The training and validation sets are released at the beginning of the competition. The test set will be released (without labels) a week before the deadline.

The submission.csv file should have three columns:
`id` - unique identifier for each text chunk (e.g., "text10.txt", "text11.txt", etc.)
`century_label` - Century label prediction (one of five classes described in sub-task 2.1)
`decade_label` -  Label prediction for the decade within a century (one of the ten classes described in sub-task 2.2)

** *As an example of the submission format, we provide 'sample_submission.csv' file*.

## Ranking
The results will be evaluated and ranked based on *Mean Absolute Error (MAE)*, which is defined as follows:

$$
\text{Final Rank} = \frac{1}{N} \sum_{i=1}^{N} \left| (GT_{2.1}^{(i)} \cdot 10 + GT_{2.2}^{(i)}) - (Pred_{2.1}^{(i)} \cdot 10 + Pred_{2.2}^{(i)}) \right|
$$
where:
$$ GT_{2.1}^{(i)} \text{ is the ground truth century label for chunk } i $$
$$ GT_{2.2}^{(i)} \text{ is the ground truth decade label for chunk } i $$
$$ Pred_{2.1}^{(i)} \text{ is the predicted century label for chunk } i $$
$$ Pred_{2.2}^{(i)} \text{ is the predicted decade label for chunk } i $$
$$ N \text{ is the total number of chunks} $$ 

This metric directly measures the average temporal distance between ground truth and predictions on a linear timeline where each century spans 10 decades. For each chunk, we:

Calculate the ground truth position: $$ (GT_{2.1}^{(i)} \cdot 10 + GT_{2.2}^{(i)}) $$
Calculate the predicted position: $$ (Pred_{2.1}^{(i)} \cdot 10 + Pred_{2.2}^{(i)}) $$

The *final rank* is the arithmetic mean of these differences across all chunks, 

Lower scores indicate better performance, with 0 being the perfect prediction.
## Files

*   **train.zip** - the training set files 
*   **train.csv** - the training set labels
*   **valid.zip** - the validation set files
*   **valid.csv** - the validation set labels
*   **test.zip** - the test set files (to be released on April 1, 2025)
*   **sample_submission.csv** - a sample submission file in the correct format

**All the files are given in the form of 1000-word chunks.**

## Columns

*   **`id`** - id of a book
*   **`century_label`** -century label prediction ( `1`, `2`, `3`, `4`, `5`)
*   **`decade_label`** - label prediction for the decade within a century (`1`,  `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`,`10` )




<a id="s002"></a>
## S002

- **source_id:** icdar-2025-ColiE_Task2:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/Description
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/1/text`

This competition is organized in conjunction with the International Conference on Document Analysis and Recognition(ICDAR 2025).

The ICDAR 2025 Competition on Automatic Classification of Literary Epochs (CoLiE) [https://www.icdar2025.com] aims to advance the field of temporal text analysis by challenging participants to develop automated methods for dating literary texts, that is, automatically predicting the time in which the text was written.



###This competition presents two main tasks: **TASK 1: Literary Epochs Classification** and  **TASK 2: ChronoText Classification.** Each participant can participate in both or only one of them.  Here,  you are competing in TASK 2. To register and compete in [TASK 1](https://www.kaggle.com/competitions/icdar-2025-ColiE_Task1), follow this[ link](https://www.kaggle.com/competitions/icdar-2025-ColiE_Task1).

<mark><b style="font-size: 1.2em;">To join the competition, click the "Join Competition" button at the top right corner. In addition, please fill in the [registration form](https://forms.gle/TDJ9PHZYDo3mdQUJ9)</b></mark>.
________________________________________________________________________________________
###TASK 2 includes the following subtasks
**Sub-task 2.1:** Identifying the century of origin for a given text 1 (the 17th, 18th, 19th, 20th, and 21st centuries).
**Sub-task 2.2:** Pinpointing the specific decade within that century in which the text was composed.


We believe this shared task will help advance the field of information retrieval and natural language processing and contribute to a deeper understanding of literary history.

This competition is open to anyone passionate about information retrieval, machine learning, and natural language processing. Whether you are a seasoned expert or a newcomer to the field, we welcome you to participate and extend the boundaries of automated text analysis!



<a id="s003"></a>
## S003

- **source_id:** icdar-2025-ColiE_Task2:page:2:Evaluation Metrics
- **page_name:** Evaluation Metrics
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/Evaluation Metrics
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/2/text`

### The evaluation of TASK2 is based on *Mean Absolute Error (MAE)* which is defined as follows:

$$
MAE = \frac{1}{n} \sum_{i=1}^{n} \left| y_i - \hat{y}_i \right|, \text{where:} \newline \newline
n = \text{number of samples,} \newline
y_i = \text{True value,} \newline
\hat{y}_i = \text{Predicted value.}
$$

The *final rank* is calculated as a Harmonic Mean of normalized mean absolute errors across Sub-task 2.1 and Sub-task 2.2. :

$$
\text{Final Rank} = \frac{2 \cdot \hat{MAE_{2.1}} \cdot \hat{MAE_{2.2}}}{\hat{MAE_{2.1}} + \hat{MAE_{2.2}}},  \text{where}  \newline
\hat{MAE_{2.1}} =  \frac{MAE_{2.1}}{4} \text{is a normalized MAE for Sub-task 2.1}, \newline
\hat{MAE_{2.2}} = \frac{MAE_{2.2}}{9} \text{is a normalized MAE for Sub-task 2.2}. \newline
\text{*Normalization scales MAE values to the range [0, 1].}
 $$

**In addition, each participant is required to provide a short description of the method.**


## Input and output format specifications
The classifier's input is a chunk (an excerpt) of a book in text format, and its output is a single value (label).  Each chunk is provided as a separate text file with a unique identifier.
Further details are specified in the "Data" tab. 




<a id="s004"></a>
## S004

- **source_id:** icdar-2025-ColiE_Task2:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/rules
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/3/text`

### Participation
1. To join the competition, click the "Join Competition" button. **In addition, please fill in the**  [ registration form](https://forms.gle/TDJ9PHZYDo3mdQUJ9).

2.  Each participant is required to upload the ’solution.csv’ with labels predictions generated by their model.
2. To ensure the fairness of the competition,  the participants will be required to share their models so that the results can be verified. In addition, the participants will be required to generate confusion matrices and
provide a short description of their methods.
3. An article about this contest will be published in the [IСDAR'25](https://www.icdar2025.com/) proceedings.
4. The first- and second-place winners of this competition will be announced at a special session at the [ICDAR'25](https://www.icdar2025.com/) conference.

###  One account per participant
Participants cannot sign up to Kaggle from multiple accounts and, therefore, cannot submit from multiple accounts.

### Only automatic prediction methods are allowed to compete.  

### Merging input files is not allowed.

### No private sharing outside teams

Privately sharing code or data outside of teams is not permitted. It's okay to share code if made available to all participants on the forums.

### Team Limits
There is no maximum team size.

### Submission Limits
Participants may submit a maximum of 5 entries per day.

### The use of the competition data is not permitted for commercial purposes.
The use of the competition data is permitted for research purposes with the condition of properly citing the competition.










<a id="s005"></a>
## S005

- **source_id:** icdar-2025-ColiE_Task2:page:4:Competition Timeline
- **page_name:** Competition Timeline
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/Competition Timeline
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/4/text`

- December 17, 2024: Call for participation.
- December 17, 2024: The competition website is live and open to participants. Training and validation sets, together with their labels, are available. 
-  April 1, 2025: Test dataset available.
-  April 8, 2025: Deadline for competition participants.
-  April 20, 2025: Submission of methods descriptions.
-  June 30, 2025: Communicate winners to chairs.
-  September 17-21, 2025: Presentation of results at the special session at the ICDAR conference.


<a id="s006"></a>
## S006

- **source_id:** icdar-2025-ColiE_Task2:page:5:Organizing Team
- **page_name:** Organizing Team
- **url:** https://www.kaggle.com/competitions/icdar-2025-ColiE_Task2/overview/Organizing Team
- **retrieved_at:** 2026-10-20T08:00:52.259508+00:00
- **Archive locator:** `/task_documents/5/text`

The competition is organized by:
- **Marina Litvak** (marinal@ac.sce.ac.il),
Software Engineering Department,
Shamoon College of Engineering, Beer Sheva,
84100, Israel
-  **Irina Rabaev** (irinar@ac.sce.ac.il),
Software Engineering Department,
Shamoon College of Engineering, Beer Sheva,
84100, Israel
- **Ricardo Campos** (ricardo.campos@ipt.pt),
Ci2 - Smart Cities Research Center,  Polytechnic Institute of Tomar
INESC TEC, Porto
Porto, Portugal
- **Alípio Jorge** (amjorge@fc.up.pt)
University of Porto and INESC TEC
Porto, Portugal
- **Adam Jatowt** (adam.jatowt@uibk.ac.at)
University of Innsbruck, 
Innsbruck, Austria
- **Roza Bass** (rozzaba@ac.sce.ac.il),
Software Engineering Department,
Shamoon College of Engineering, Beer Sheva,
84100, Israel
- **Hugo Sousa** (hugo.sousa@fc.up.pt),
University of Porto and INESC TEC
Porto, Portugal

