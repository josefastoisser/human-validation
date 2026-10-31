# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: Join the Community](#s006)
- [S007: Timeline](#s007)
- [S008: Prizes](#s008)
- [S009: Teams](#s009)
- [S010: Citation](#s010)
- [S011: 2024-flame-ai-challenge:thread:539685:opening](#s011)
- [S012: 2024-flame-ai-challenge:thread:539685:3013699](#s012)
- [S013: 2024-flame-ai-challenge:thread:539685:3013706](#s013)
- [S014: 2024-flame-ai-challenge:thread:539685:3013897](#s014)
- [S015: 2024-flame-ai-challenge:thread:539685:3014141](#s015)
- [S016: 2024-flame-ai-challenge:thread:539685:3013939](#s016)
- [S017: 2024-flame-ai-challenge:thread:539685:3013989](#s017)
- [S018: 2024-flame-ai-challenge:thread:539685:3013992](#s018)
- [S019: 2024-flame-ai-challenge:thread:539685:3013655](#s019)
- [S020: 2024-flame-ai-challenge:thread:539685:3013661](#s020)
- [S021: 2024-flame-ai-challenge:thread:539685:3013674](#s021)
- [S022: 2024-flame-ai-challenge:thread:539685:3013676](#s022)
- [S023: 2024-flame-ai-challenge:thread:539685:3013686](#s023)
- [S024: 2024-flame-ai-challenge:thread:539685:3013672](#s024)
- [S025: 2024-flame-ai-challenge:thread:539685:3013679](#s025)
- [S026: 2024-flame-ai-challenge:thread:539685:3013949](#s026)
- [S027: 2024-flame-ai-challenge:thread:539685:3013993](#s027)
- [S028: 2024-flame-ai-challenge:thread:539685:3014001](#s028)
- [S029: 2024-flame-ai-challenge:thread:539685:3014038](#s029)
- [S030: 2024-flame-ai-challenge:thread:539685:3013673](#s030)
- [S031: 2024-flame-ai-challenge:thread:539685:3013684](#s031)
- [S032: 2024-flame-ai-challenge:thread:539685:3013885](#s032)
- [S033: 2024-flame-ai-challenge:thread:539685:3013931](#s033)
- [S034: 2024-flame-ai-challenge:thread:539685:3013964](#s034)
- [S035: 2024-flame-ai-challenge:thread:539685:3013969](#s035)
- [S036: 2024-flame-ai-challenge:thread:539685:3020102](#s036)
- [S037: 2024-flame-ai-challenge:thread:539685:3020646](#s037)
- [S038: 2024-flame-ai-challenge:thread:538410:opening](#s038)
- [S039: 2024-flame-ai-challenge:thread:538410:3010211](#s039)
- [S040: 2024-flame-ai-challenge:thread:538410:3012249](#s040)
- [S041: 2024-flame-ai-challenge:thread:538410:3012472](#s041)
- [S042: 2024-flame-ai-challenge:thread:538410:3012485](#s042)
- [S043: 2024-flame-ai-challenge:thread:538410:3012512](#s043)
- [S044: 2024-flame-ai-challenge:thread:538410:3012521](#s044)
- [S045: 2024-flame-ai-challenge:thread:538410:3012522](#s045)
- [S046: 2024-flame-ai-challenge:thread:538410:3012533](#s046)
- [S047: 2024-flame-ai-challenge:thread:538410:3012537](#s047)
- [S048: 2024-flame-ai-challenge:thread:538410:3012540](#s048)
- [S049: 2024-flame-ai-challenge:thread:538410:3013074](#s049)
- [S050: 2024-flame-ai-challenge:thread:538410:3013131](#s050)
- [S051: 2024-flame-ai-challenge:thread:538410:3013147](#s051)
- [S052: 2024-flame-ai-challenge:thread:543873:opening](#s052)

<a id="s001"></a>
## S001

- **source_id:** 2024-flame-ai-challenge:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/data-description
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/0/text`

## Files

*   **train.csv** - contains training set info
*   **test.csv** - contains test set info
*   **sample_submission.csv** - a sample submission file in the correct format generated via linear interpolation. See `generate_submission.ipynb` for how this is generated in the `Code` tab.
*   **data**  - See `Starter_Notebook` in the `Code`tab  on how to load the data and visualize it.


## Columns
*   `id` - file id 
*   `u` - wind speed
*   `alpha` - terrain slope
*   `Nt` - number of available snapshots (temporally correlated)
*   `Nx`, `Ny` - number of pixels in height and width.
*   `ustar_filename` - Filename for ustar velocity
*   `theta_filename` - Filename for potential temperature
*   `xi_filename` - Filename for fire location 


## Columns in sample_submission
*   `id` - file id 
*  `0,1,...` - flattened array from fire location predictions
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F7329892%2Fd463685965e51e7bb515b704c62f2b7f%2Fflameai-fig-2.png?generation=1726962366515635&alt=media)


<a id="s002"></a>
## S002

- **source_id:** 2024-flame-ai-challenge:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Description
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/1/text`

Participants in this Kaggle challenge will be provided with a high-fidelity dataset containing 2D wildfire flowfield data of wind speed (*ustar*), temperature (*theta*), and fire-line location (xi). To describe each case globally, we are also providing information about the slope (*alpha*) and mean wind speed (*u10*) -- both being scalar values, and are commonly used in the wildfire community to parameterize wildfire-spread behavior.

Your task is to develop a state-of-the-art spatio-temporal ML model that can accurately forecast the 2D fire propagation as a function of time. The challenge consists in capturing the complex dynamics of wildfire spread that is affected by factors such as wind speed, terrain, and atmospheric turbulence. Your model should not only predict the instantaneous fire-line but also account for temporal variations, ensuring that forecasts remain robust and reliable over extended time periods. This will be critical for enhancing wildfire management and fire prevention strategies. To add interpretability, we encourage you to consider infusing physical information into your ML model. 

# Challenge

We are hosting seminars concurrently with the challenge. For more information, see our website https://flame-ai-workshop.github.io/

There are invited talks and seminars with experts in AI, ML, and physical flows. Join us to participate in them and ask questions. There is also a Slack channel with support to facilitate this challenge and encourage collaboration!

Register at https://events.humanitix.com/stanford-flame-ai-workshop-2024

# Dataset
The dataset provided for this challenge contains high-fidelity 2D flowfield sequences of wildfire propagation that are extracted from 3D ensemble simulations. The sequences of flowfield data are represented as n channels (wind field, potential temperature, fire-line location, 2D grid, slope, and mean wind speed). The dataset will be divided into training and validation sets, and a separate test set will be used for evaluation. *This contains all the data available for this ML challenge, and you're **not** allow to use other data (we will retrain model submissions for verification).* 

## Key Features of the Dataset:

1. **Spatial Resolution**: Each flowfield is represented as a 2D grid of data points, where each point contains information about key parameters such as velocity, potential temperature, wind speed, and fire location. The grid resolution captures both large-scale fire movements and finer details associated with turbulence, and fire-atmospheric coupling. Note that the fire-line location is binarized with 1 indicating the fire and 0 indicating no fire.

2. **Temporal Data**: The dataset is temporal in nature, consisting of multiple sequential snapshots of fire propagation that are separated by equidistant intervals. Each sequence represents the evolution of a fire over time, allowing participants to model the time-dependent nature of the system.

3. **Multiple Scenarios**: The dataset includes wildfire simulations under various conditions:
- *Wind Conditions*: Simulations capture different mean wind speed, which significantly influence the fire-spread behavior. 
- *Terrain*: Data accounts for diverse terrains, from flat surfaces to high-slope conditions, affecting the fire-propagation speed.

4. **Training and Testing Splits**: The dataset is pre-split into training and testing sets:
- *Training Set*: Contains annotated flowfields with both input data (initial conditions, wind profiles, fire location).
- *Testing Set*: Consists of input flowfields without corresponding fire spread labels. Participants will be required to predict fire propagation for these cases.

5. **Data Format**: The dataset is provided in a standardized format, with each flowfield stored as a time-indexed sequence of 2D arrays in binary data format '.dat'. Accompanying metadata contain information about environmental conditions, including mean wind speed and terrain slope.

# ML Task
The objective is to develop an auto-regressive ML model that predicts the fire-line location (xi) at a time t+1, using 2D information of wind field, potential temperature, and fire line at previous and current time ≤ t. While the primary evaluation focuses on your model’s predictions for the fire-line location, you are encouraged to leverage all the provided information for improved accuracy. For the leaderboard, your model will be evaluated based on its ability to forecast 20 timesteps on the testing dataset, starting from the end of the initial 5 steps provided.

# Submission Requirements

1. Use Kaggle's `Submit Predictions` to evaluate your generated predictions on the public leaderboard with MSE.
2. Share a google drive: your final code [After Oct 17] using this google form: 
https://forms.gle/1v2SM9wPUoeXYxi87
3. Share on google drive: trained weights and code for loading weights [After Oct. 17] using the same google form.

# Getting Started

To get started, please review the provided dataset and the sample code provided in the Code subsection. You are encouraged to explore various deep learning architectures, data augmentation techniques, and pre-processing methods to achieve the best results. Please contact flame.ai.workshop@gmail.com for further information. 


<a id="s003"></a>
## S003

- **source_id:** 2024-flame-ai-challenge:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Evaluation
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/2/text`

As a primary metric for model evaluation, we'll be using MSE(Ground Truth, Prediction) of the fire-line location to evaluate pixel-wise accuracy for the public leaderboard. The top-10 model submissions for invitation to join a journal submission will be reproduced and tested with additional evaluation metrics (SSIM, PSNR, error accumulation over time, robustness for long term prediction). [updated 10/9 -- blastnet] 

## Submission File
For each ID in the test set, you must predict a flattened (C-order) 113x32 fire line location. The file should contain a header and have the following format:

    id,0,1,2,...,72319
    1,0,0,0,...,0
    2,0,0,0,...,0
    5,0,0,0,...,0
    6,0,0,0,...,0
    etc.


<a id="s004"></a>
## S004

- **source_id:** 2024-flame-ai-challenge:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/rules
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/3/text`

1. Only use training data provided here.
2. Open-source Pretrained Models are allowed.
3. We will be checking and reproducing top code submissions at the end of the competition.
4. Feel free to take the data offline and use your own platforms
5. Be polite and Inclusive during discussions!
6. code and solutions must be your own or your team’s work. Plagiarism, or presenting another’s work as your own, will lead to disqualification. 


<a id="s005"></a>
## S005

- **source_id:** 2024-flame-ai-challenge:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/abstract
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/4/text`

**Welcome to the FLAME AI 2024 Challenge!**
The propagation of wildfires is a complex, dynamic process that is influenced by various factors, such as fuel, wind, terrain, and other environmental conditions. Accurately and reliably predicting the rate-of-spread of wildfires is of critical importance for fire management, rapid fire response, and fire mitigation.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F22578283%2F7e09b4a232ef2e70caec6b402336df3c%2Ffire_3d_u6s15Public.png?generation=1726969390383946&alt=media)

In this competition, you’ll have the opportunity to develop a spatio-temporal ML model to accurately forecast the fire propagation, considering effects of terrain, atmospheric flow conditions, and environmental interactions. The underlying data is extracted from a series of high-fidelity ensemble simulations that are the basis of the [Google FireBench](https://sites.research.google/gr/wildfires/firebench/) dataset, which consists of an ensemble of high-resolution large-eddy simulations that capture the three-dimensional wildfire-spread behavior and coupling with the atmospheric environment. 

By considering a reduced data-set that was extracted from FireBench, your task is to create an autoregressive ML model that learns from these intricate flowfield conditions and generalizes to predict fire propagation in unseen conditions.



<a id="s006"></a>
## S006

- **source_id:** 2024-flame-ai-challenge:page:5:Join the Community
- **page_name:** Join the Community
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Join the Community
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/5/text`

We encourage participants to join the Kaggle and Slack (please register under https://flame-ai-workshop.github.io to be added to the slack channel) discussion forums for this challenge, where you can collaborate with other data scientists, ask questions, and share insights. 

Reminder: There is a prize associated with collaborative activities!


<a id="s007"></a>
## S007

- **source_id:** 2024-flame-ai-challenge:page:6:Timeline
- **page_name:** Timeline
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Timeline
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/6/text`

1. Launching the Competition Page [Sept 23, after FLAMEAI launch event]
2. Start of Challenge [9.30 am PDT, Sept 24]
3. Python/ML Recap [9.30 am PDT, Sept 24]
4. Kaggle Competitions Platform Tutorial [11.00 am PDT, Sept 24]
5. Team Registration  [11.59 pm, ~~Sept 30~~ Oct 11]
6. Results Final Submission [11.59 pm PDT, Oct 17]
7. Code Submission [11.59 pm PDT, ~~Oct 20~~ Oct 25]
8. Prize Announcements [11.59 pm PDT, ~~Oct 24~~ Nov 1]


<a id="s008"></a>
## S008

- **source_id:** 2024-flame-ai-challenge:page:7:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Prizes
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/7/text`

We are offering exciting prizes for:
* 1st prize - $2500 per team
* 2nd prize - $1500 per team
* 3rd prize - $1000 per team





<a id="s009"></a>
## S009

- **source_id:** 2024-flame-ai-challenge:page:8:Teams
- **page_name:** Teams
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Teams
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/8/text`

1. Max of 2 people per team
2. Can choose teammate from registered participants (Use Slack DM’s, #networking channel)
3. Ask your friends if they’re interested (we can add them to slack channel)
4. To form a team, we will provide a google forms link: https://forms.gle/pW3MSzdn2k1ptMWY6
5. Deadline for team registration: Fri Sept 30, 11.59 pm PDT
6. You may find the `Teams` tab convenient for team mergers for Kaggle team functionalities. 


<a id="s010"></a>
## S010

- **source_id:** 2024-flame-ai-challenge:page:9:Citation
- **page_name:** Citation
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/overview/Citation
- **retrieved_at:** 2026-10-20T09:50:55.742922+00:00
- **Archive locator:** `/task_documents/9/text`

Matthias Ihme, Jen Zen Ho, Bassem Akoush, Wai Tong Chung. (2024). 2024 FLAME AI Challenge. Kaggle. https://kaggle.com/competitions/2024-flame-ai-challenge



<a id="s011"></a>
## S011

- **source_id:** 2024-flame-ai-challenge:thread:539685:opening
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685
- **thread_id:** 539685
- **comment_id:** opening
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T09:39:12.652Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/0/text`

Winner determination metric

I understand that the main metric is MSE for winner determination. What is the purpose of additional evaluation metrics (SSIM, PSNR, error accumulation over time, robustness for long term prediction)? Is it only for host's usage?


<a id="s012"></a>
## S012

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013699
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013699
- **thread_id:** 539685
- **comment_id:** 3013699
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T12:32:21.760Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/1/text`

I offer four solutions for the sponsor's reference:

- Participants need to provide code and weight files, advantages: can be a comprehensive test, disadvantages: everyone runs the program in different environments, so it takes a lot of time to configure the environment, download the model weight takes a lot of time (especially for the integration of multiple models of the solution), which is out of the Kaggle scoring environment, so the fairness is difficult to guarantee. 【 High complexity, low fairness 】

- The organizer will provide an extra test set or predict a longer time step in the current test set, and allow the top ten contestants to submit on the Kaggle platform. The organizer will test these submissions and calculate a scoring formula as the final ranking [in complexity, in fairness].

- The organizer will test other indicators according to the existing submissions, and use a scoring formula as the final ranking [low complexity, high fairness].

- The final ranking is based on ranking only [no complexity, high fairness]


<a id="s013"></a>
## S013

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013706
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013706
- **thread_id:** 539685
- **comment_id:** 3013706
- **parent_comment_id:** 3013699
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T12:46:56.210Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/2/text`

I think hosts consider the challenge as a academic communication more than a pure competition, and they need seminar after the submission deadline to learn more from kagglers. They may have more subjective thoughts, because different metrics are applicable to different situations.

By the way, I think FLAME AI challenge as a community competition is better than many recent reward competitions.


<a id="s014"></a>
## S014

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013897
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013897
- **thread_id:** 539685
- **comment_id:** 3013897
- **parent_comment_id:** 3013699
- **author_name:** Bassem Akoush
- **author_role:** unknown
- **created_at:** 2024-10-10T16:57:26.843Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/3/text`

Hi [@zhuoqun](https://www.kaggle.com/zhuoqun), 

I would like to elaborate more on retraining and reproducibility of models performance. There's no problem for the environment configuration in python. If you are using any older versions of Python packages, it’s essential to export your environment to a .yml or .txt file. This allows us to replicate your environment settings, which is a common practice in public GitHub repos. Depending on the software you’re using, you should check the documentation for instructions on how to export the environment correctly. Additionally, submitting your model weights is a requirement to ensure fairness in the evaluation process. This rule helps verify that models can be retrained and perform consistently on our end as well.


<a id="s015"></a>
## S015

- **source_id:** 2024-flame-ai-challenge:thread:539685:3014141
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3014141
- **thread_id:** 539685
- **comment_id:** 3014141
- **parent_comment_id:** 3013897
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-11T01:29:47.980Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/4/text`

[@bassemakoush](https://www.kaggle.com/bassemakoush) Thank you for your reply, the submission of the weight file is important to ensure fairness


<a id="s016"></a>
## S016

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013939
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013939
- **thread_id:** 539685
- **comment_id:** 3013939
- **parent_comment_id:** 3013699
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T17:55:09.897Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/5/text`

4th proposition leads to extreme overfitting to test dataset and is good for you :)  [no complexity, mid fairness, no real application]


<a id="s017"></a>
## S017

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013989
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013989
- **thread_id:** 539685
- **comment_id:** 3013989
- **parent_comment_id:** 3013939
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T18:50:47.277Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/6/text`

[@jankowalski2000](https://www.kaggle.com/jankowalski2000) No, my solution is just more robust, not overfitting. I can accept any plan. Let's look forward to the test. Best wishes.


<a id="s018"></a>
## S018

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013992
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013992
- **thread_id:** 539685
- **comment_id:** 3013992
- **parent_comment_id:** 3013939
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T18:55:04.760Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/7/text`

I don't say your solution is overfitted, I say only about 4th proposition…


<a id="s019"></a>
## S019

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013655
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013655
- **thread_id:** 539685
- **comment_id:** 3013655
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T11:44:53.920Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/8/text`

As a primary metric for model evaluation, we'll be using MSE(Ground Truth, Prediction) of the fire-line location to evaluate pixel-wise accuracy for the public leaderboard. The top-10 model submissions for invitation to join a journal submission will be reproduced and tested with additional evaluation metrics (SSIM, PSNR, error accumulation over time, robustness for long term prediction). [updated 10/9 -- blastnet]

In my understanding, hosts will contact top 10 teams using auto-regressive ML model in the public leaderboard  (based on MSE), then hosts determine the winner among these 10 teams with additional evaluation metrics. Shortly, qualified by MSE, finalized by more evaluation metrics. Public leaderboard is just qualification.


<a id="s020"></a>
## S020

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013661
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013661
- **thread_id:** 539685
- **comment_id:** 3013661
- **parent_comment_id:** 3013655
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T11:49:35.140Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/9/text`

Besides, top 10 teams will be tested with longer term


<a id="s021"></a>
## S021

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013674
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013674
- **thread_id:** 539685
- **comment_id:** 3013674
- **parent_comment_id:** 3013661
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-10T12:02:17.253Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/10/text`

Yeah, but does being placed 1st and 10th on leaderboard make any difference at all? I think hosts should share a clear formula for how to determine the winners like `0.5 * leaderboard score + 0.5 * other evaluations`. People dedicating hours to this competition and we have to know those things beforehand.


<a id="s022"></a>
## S022

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013676
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013676
- **thread_id:** 539685
- **comment_id:** 3013676
- **parent_comment_id:** 3013661
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T12:04:50.747Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/11/text`

Agreed, this requires a clear formula and is based on a reliable evaluation criterion


<a id="s023"></a>
## S023

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013686
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013686
- **thread_id:** 539685
- **comment_id:** 3013686
- **parent_comment_id:** 3013661
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T12:14:40.113Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/12/text`

Hosts may reveal that after Oct 17.


<a id="s024"></a>
## S024

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013672
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013672
- **thread_id:** 539685
- **comment_id:** 3013672
- **parent_comment_id:** 3013655
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T12:00:57.293Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/13/text`

I think the 10/9 update will only be evaluated based on MSE's prediction of 20 time steps, that is, based on leaderboard results only. In addition, they will invite the models of the top 10 contestants to participate in the rest of the test of their article. This is my understanding and needs clarification from the organizer.


<a id="s025"></a>
## S025

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013679
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013679
- **thread_id:** 539685
- **comment_id:** 3013679
- **parent_comment_id:** 3013672
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T12:11:09.840Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/14/text`

That's what I was thinking.


<a id="s026"></a>
## S026

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013949
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013949
- **thread_id:** 539685
- **comment_id:** 3013949
- **parent_comment_id:** 3013672
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T18:01:57.333Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/15/text`

May I ask you [@ucas0v0zhuoqunli](https://www.kaggle.com/ucas0v0zhuoqunli) why are you looking for a teammate being first?


<a id="s027"></a>
## S027

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013993
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013993
- **thread_id:** 539685
- **comment_id:** 3013993
- **parent_comment_id:** 3013672
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T18:55:42.250Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/16/text`

Sorry, I didn't understand your question.


<a id="s028"></a>
## S028

- **source_id:** 2024-flame-ai-challenge:thread:539685:3014001
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3014001
- **thread_id:** 539685
- **comment_id:** 3014001
- **parent_comment_id:** 3013672
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T19:06:52.243Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/17/text`

You have active status looking for teammates. I just considered to offer a join proposition.


<a id="s029"></a>
## S029

- **source_id:** 2024-flame-ai-challenge:thread:539685:3014038
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3014038
- **thread_id:** 539685
- **comment_id:** 3014038
- **parent_comment_id:** 3013672
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-10T19:54:27.903Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/18/text`

[@jankowalski2000](https://www.kaggle.com/jankowalski2000) If you have made a decision, you are welcome at any time. Learning from others and improving myself is the main purpose of my participation in the competition.Although rewards are also very important. haha


<a id="s030"></a>
## S030

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013673
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013673
- **thread_id:** 539685
- **comment_id:** 3013673
- **parent_comment_id:** 3013655
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T12:01:50.610Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/19/text`

I think about a method of winner determination. The hosts will calculate these extra metrics and what then? Will they create a rating per each metric and take a mean?


<a id="s031"></a>
## S031

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013684
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013684
- **thread_id:** 539685
- **comment_id:** 3013684
- **parent_comment_id:** 3013673
- **author_name:** Timmy Juicehouse
- **author_role:** unknown
- **created_at:** 2024-10-10T12:13:37.427Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/20/text`

Yeah, It's possible that they are still considering this issue as well, lol


<a id="s032"></a>
## S032

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013885
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013885
- **thread_id:** 539685
- **comment_id:** 3013885
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-10T16:37:18.010Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/21/text`

Hi everyone, thanks for your questions, here are some clarifications:

- The winners will only be based on MSE. The other metrics are purely for analysis for the publication and may be important for you if you were interested in joining us in the joint publication.

- The MSE score on the leaderboard will be verified by retraining the top models. Bassem is writing up how that procedure will be conducted and will respond to zhuoqun's comment.

We will also be hosting a meeting tomorrow at 10 AM PDT if you have any questions about this you can ask it during that meeting. I'll post up the Zoom link on a new Discussion board soon.

Hope this helps!


<a id="s033"></a>
## S033

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013931
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013931
- **thread_id:** 539685
- **comment_id:** 3013931
- **parent_comment_id:** 3013885
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-10T17:45:11.537Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/22/text`

To sum up, solutions will be verified on unknown time steps (different than in leaderboard time steps 5-26)? [@bassemakoush](https://www.kaggle.com/bassemakoush) said two days ago 'No, the top performing models will be evaluated on their ability to forecast the fire propagation beyond the 20 time steps' Is it the final statement?


<a id="s034"></a>
## S034

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013964
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013964
- **thread_id:** 539685
- **comment_id:** 3013964
- **parent_comment_id:** 3013931
- **author_name:** Bassem Akoush
- **author_role:** unknown
- **created_at:** 2024-10-10T18:13:38.637Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/23/text`

Hi Rafal, 

Thanks for bringing this up! The long-term prediction beyond 20 steps won’t impact the leaderboard or the winner announcement; it’s primarily for those will be invited to the paper (top performing models).


<a id="s035"></a>
## S035

- **source_id:** 2024-flame-ai-challenge:thread:539685:3013969
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3013969
- **thread_id:** 539685
- **comment_id:** 3013969
- **parent_comment_id:** 3013885
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-10T18:19:53.857Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/24/text`

Another clarification - the MSE will be based only on 20 timesteps into the future and on the testing data that we have given to you. No other cases will be considered for the prizes. 

The only thing here is that we will be retrieving everyone's source code to 1) ensure that the model is autoregressive and 2) retrain the models to ensure that the models can actually achieve the stated leaderboard MSE. 

To ensure your model is fully reproducible, please think about the reproducibility of your training. I.e. set your random seeds whenever you use random processes and use deterministic algorithms in torch/tensorflow/keras. We will use the settings your source code has to retrain your model.


<a id="s036"></a>
## S036

- **source_id:** 2024-flame-ai-challenge:thread:539685:3020102
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3020102
- **thread_id:** 539685
- **comment_id:** 3020102
- **author_name:** Giacomo Baldan
- **author_role:** unknown
- **created_at:** 2024-10-17T06:53:48.527Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/25/text`

Just a clarification, can the submission file contain only binary values, i.e. 0 and 1, or arbitrary floats like 0.5?


<a id="s037"></a>
## S037

- **source_id:** 2024-flame-ai-challenge:thread:539685:3020646
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/539685#comment-3020646
- **thread_id:** 539685
- **comment_id:** 3020646
- **parent_comment_id:** 3020102
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-17T18:18:34.270Z
- **retrieved_at:** 2026-10-20T09:53:54.207702+00:00
- **Archive locator:** `/discussion/26/text`

Hi Giacomo, your submission can be floats or binary values. It is up to you. Good luck!


<a id="s038"></a>
## S038

- **source_id:** 2024-flame-ai-challenge:thread:538410:opening
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410
- **thread_id:** 538410
- **comment_id:** opening
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-08T18:51:57.277Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/0/text`

robustness for long term prediction

I would like to ask about time window size for long term prediction. Is it 20 too?


<a id="s039"></a>
## S039

- **source_id:** 2024-flame-ai-challenge:thread:538410:3010211
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3010211
- **thread_id:** 538410
- **comment_id:** 3010211
- **author_name:** Bassem Akoush
- **author_role:** unknown
- **created_at:** 2024-10-08T19:07:14.533Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/1/text`

No, the top performing models will be evaluated on their ability to forecast the fire propagation beyond the 20 time steps.  In real-world applications, such as wildfire mitigation, users need predictions of fire spread not just for the next 10 or 20 steps, but also for 100 or more steps—even indefinitely—to inform critical decisions like evacuation planning. For this challenge, there is no fixed sequence length, so it’s important to tune your model to minimize the error accumulation over time.


<a id="s040"></a>
## S040

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012249
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012249
- **thread_id:** 538410
- **comment_id:** 3012249
- **parent_comment_id:** 3010211
- **author_name:** Rafał Pawłowski
- **author_role:** unknown
- **created_at:** 2024-10-08T19:46:41.233Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/2/text`

My current solution is limited to 145 next time steps. Is is valid?


<a id="s041"></a>
## S041

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012472
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012472
- **thread_id:** 538410
- **comment_id:** 3012472
- **parent_comment_id:** 3012249
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-09T04:49:09.927Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/3/text`

If I understood correctly, that benchmark is beyond the scope of this competition. We are only responsible for predicting next 20 timesteps here.


<a id="s042"></a>
## S042

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012485
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012485
- **thread_id:** 538410
- **comment_id:** 3012485
- **parent_comment_id:** 3012249
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-09T05:10:36.837Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/4/text`

Hi Rafał, thanks for your question. One of the rules is that model must be autoregressive and be able to predict any arbitrarily large n_predictions, where n_predictions is an integer.

More precisely, the model should be able to predict the indicator, xi, at any sequence t in the future, where t is an integer - so if a firefighter or wildfire management team were to ask 'where will the fire be at 40 time units into the future?', the model will still be able to give a prediction on that (even if it's not technically being scored as part of the MSE).

Hope this helps!


<a id="s043"></a>
## S043

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012512
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012512
- **thread_id:** 538410
- **comment_id:** 3012512
- **parent_comment_id:** 3012249
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-09T05:56:43.990Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/6/text`

no, we're going to develop an infinite autoregressive model, You should not limit the prediction step size to a fixed constant.


<a id="s044"></a>
## S044

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012521
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012521
- **thread_id:** 538410
- **comment_id:** 3012521
- **parent_comment_id:** 3012249
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-09T06:12:35.967Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/7/text`

[@gunesevitan](https://www.kaggle.com/gunesevitan) The organizers state in the Evaluation section that the score on the leaderboard is the primary metric, but they also test other metrics in addition


<a id="s045"></a>
## S045

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012522
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012522
- **thread_id:** 538410
- **comment_id:** 3012522
- **parent_comment_id:** 3012249
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-09T06:14:08.610Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/8/text`

Thanks for the clarification [@jenzenho](https://www.kaggle.com/jenzenho), but any model can be autoregressive as long as you feed outputs of previous timesteps as inputs in a loop. I haven't extended my models to that yet since I'm focusing on improving my overall score. Is it okay to implement that part after the competition ends and how are you going to experiment with those models exactly? I'm currently ensembling more than a single model.


<a id="s046"></a>
## S046

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012533
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012533
- **thread_id:** 538410
- **comment_id:** 3012533
- **parent_comment_id:** 3012249
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-09T06:29:24.600Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/9/text`

I think there are some gray areas that should be clarified.

  One of the rules is that model must be autoregressive and be able to predict any arbitrarily large n_predictions, where n_predictions is an integer.

For me, spatio-temporal models on OpenSTL work better. They take 5 steps as inputs and they predict the next 20 steps in a single forward pass which isn't autoregressive. I can still implement an autoregression wrapper that would make my model able to predict any number of time steps. My approach isn't autoregressive on leaderboard, but it can be on further evaluations. Does that make me price eligible?


<a id="s047"></a>
## S047

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012537
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012537
- **thread_id:** 538410
- **comment_id:** 3012537
- **parent_comment_id:** 3012249
- **author_name:** Zhuoqun Li
- **author_role:** unknown
- **created_at:** 2024-10-09T06:33:19.583Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/10/text`

I think that's acceptable


<a id="s048"></a>
## S048

- **source_id:** 2024-flame-ai-challenge:thread:538410:3012540
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3012540
- **thread_id:** 538410
- **comment_id:** 3012540
- **parent_comment_id:** 3012249
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-09T06:40:45.763Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/11/text`

Then it becomes like as I said. Autoregression and predicting arbitrary number of timesteps is beyond the scope of this Kaggle competition.


<a id="s049"></a>
## S049

- **source_id:** 2024-flame-ai-challenge:thread:538410:3013074
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3013074
- **thread_id:** 538410
- **comment_id:** 3013074
- **parent_comment_id:** 3012249
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-09T16:27:04.057Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/12/text`

Hi Gunes, you're right that lots of models can be infinitely autoregressive as long as you put a wrapper around it to feed the output back, and that OpenSTL contains many of these models. However, some other models may not be infinitely autoregressive - an example of an ineligible model may take in ustar, theta, and xi, and then output only xi for the next 20 timesteps. Since it does not predict ustar or theta, its outputs cannot be fed back into the inputs and hence cannot be considered an autoregressive model.

As long as the inputs of the model are predicted and are then fed back into the model until n_prediction timesteps are reached, the model can be considered autoregressive. In terms of how to implement it in the competition, in the generate_submission notebook, there is a FireSpreadModel which takes in n_predictions. We envisioned that competitors would swap the FireSpreadModel in this notebook with your own autoregressive model, where n_predictions should be any arbitrary number and your FireSpreadModel class should be able to have the wrapper that autoregressively feeds the outputs of your ML model back into its input until n_predictions is reached.

Let me know if this helps!


<a id="s050"></a>
## S050

- **source_id:** 2024-flame-ai-challenge:thread:538410:3013131
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3013131
- **thread_id:** 538410
- **comment_id:** 3013131
- **parent_comment_id:** 3012249
- **author_name:** Gunes Evitan
- **author_role:** unknown
- **created_at:** 2024-10-09T17:11:10.257Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/13/text`

Thanks for the reply. I assume that it's fine to predict next 20 timesteps in a single forward pass while submitting, but you want this model to be able to predict infinite timesteps in later phases if it qualifies to price.


<a id="s051"></a>
## S051

- **source_id:** 2024-flame-ai-challenge:thread:538410:3013147
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/538410#comment-3013147
- **thread_id:** 538410
- **comment_id:** 3013147
- **parent_comment_id:** 3012249
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-10-09T17:28:09.020Z
- **retrieved_at:** 2026-10-20T09:54:30.697028+00:00
- **Archive locator:** `/discussion/14/text`

Hi Gunes, yes exactly! The idea is that we can then compare the performance of these models at any arbitrary time in the future and use these learnings to help wildfire management, which is why the rule for an autoregressive model that can keep predicting far into the future is there.


<a id="s052"></a>
## S052

- **source_id:** 2024-flame-ai-challenge:thread:543873:opening
- **url:** https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/543873
- **thread_id:** 543873
- **comment_id:** opening
- **author_name:** Jen Zen Ho
- **author_role:** unknown
- **created_at:** 2024-11-01T23:54:39.491Z
- **retrieved_at:** 2026-10-20T09:51:51.867846+00:00
- **Archive locator:** `/discussion/42/text`

Congratulations to the winners of FLAME AI 2024!!

Congratulations to the winners of this year’s FLAME AI Challenge! Their creativity and skill at generating spatiotemporal models is extremely impressive, and will be a great contribution to improving existing wildfire models!

First place, $2,500 prize: Ajay Asaithambi

[https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541397](https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541397)

Second place, $1,500 prize: Jobayer Hossain

[https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541458](https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541458)

Third place, $1,000 prize: Rafał Pawłowski

[https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541383](https://www.kaggle.com/competitions/2024-flame-ai-challenge/discussion/541383)

Most collaborative person, $100 Google cloud platform credits: Thomas Dubail for his well-liked nifty animation code shared early on in the competition

[https://www.kaggle.com/code/thomasdubail/flame-2024-animation](https://www.kaggle.com/code/thomasdubail/flame-2024-animation)

Congratulations once again and we will be in touch regarding prizes.

In addition to the prizes, the top 10 competitors will be contacted regarding the joint publication! If you are not in the top 10 but are still interested in joining us for the joint publication, you can still submit your model for consideration via [https://docs.google.com/forms/d/e/1FAIpQLSdvkGKWsgJcYZ39PYK1HYAauKbLQDqWDcR4TuDbCVGs7EDjcQ/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdvkGKWsgJcYZ39PYK1HYAauKbLQDqWDcR4TuDbCVGs7EDjcQ/viewform)

