# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)

<a id="s001"></a>
## S001

- **source_id:** event-based-eye-tracking-ais2024:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/overview/data-description
- **retrieved_at:** 2026-10-20T18:49:04.553085+00:00
- **Archive locator:** `/task_documents/0/text`

## Dataset Description
There are 13 subjects in total, each having 2-6 recording sessions. The subjects are required to perform 5 classes of activities: random, saccades, read text, smooth pursuit, and blinks. Figure 2 visualizes one real recording sample by making the raw events into event frames. The total data volume is approximately 1 GB in the compressed .h5 form. Depending on your method, you may have very different data representations and processing pipelines based on the raw events. We provide an event [voxel-grid-based](https://tonic.readthedocs.io/en/latest/auto_examples/representations/plot_tovoxelgrid.html#sphx-glr-auto-examples-representations-plot-tovoxelgrid-py) data loading pipeline in the GitHub repository. It will automatically slice the raw event recordings into subsequences. For more details please refer to the GitHub repository.

#### Labeling
The ground truth is labeled at 100Hz and consists of two parts for each label (x, y, close) with 

* labeling of the pupil center coordinates (x,y).
* a binary value 'close' indicating whether the eye blinks or not (0 for opening, 1 for closing). 

Labels (x,y, close) for the train split are provided at a frequency of 100Hz. The user is free to decide if they would like to downsample this frequency and whether to use the close label or not. In the training sample pipeline we provided, the labels are downsampled to 20Hz and we do not use the close label by default. For the test set, we will evaluate the prediction at **20Hz** only. If you would like to alter the data loading pipeline, please be aware of this downsampling.

#### Dataset splitting
We use 12 recordings for testing (test_files.txt) and the remaining recordings are for the user to train (dataset/train_files.txt ) and validate (dataset/val_files.txt) their methods. The users are free to re-divide the training and validation sets in train_files.txt and val_files.txt.



<a id="s002"></a>
## S002

- **source_id:** event-based-eye-tracking-ais2024:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/overview/Description
- **retrieved_at:** 2026-10-20T18:49:04.553085+00:00
- **Archive locator:** `/task_documents/1/text`

For the full coding pipeline and tutorial please refer to the GitHub repository: https://github.com/EETChallenge/challenge_demo_code

## Training Pipeline Description
The default training pipeline is very handy to use. Simply run the following command with the code in the GitHub repository:
```python
python3 train.py --config sliced_baseline.json
```
This should give a baseline result for a basic CNN+GRU model trained on voxel-grid event representation. The training progress, checkpoints and metrics are all logged with the mlflow library. See the repo for more details.

![Eye movement recorded with event camera](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F18771626%2Fe78190165f02d967a7bd8bc992e5ca64%2Fevent-based-eye-movement.gif?generation=1706607242333944&alt=media)


<a id="s003"></a>
## S003

- **source_id:** event-based-eye-tracking-ais2024:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/overview/Evaluation
- **retrieved_at:** 2026-10-20T18:49:04.553085+00:00
- **Archive locator:** `/task_documents/2/text`

#### scoring functions
There are two evaluation metrics for the challenge:
**p10 accuracy** and **mean euclidean distances**.

The p10 accuracy is defined as the percentage of the predictions that are within 10 pixels of the ground truths (in the downsampled 80x60 spatial space). The mean Euclidean distance is defined as the average Euclidean distance between the predictions and the ground truths. 


## Submission File
Please reference the test.py to load your model checkpoint and generate the submission csv file. The file should contain a header (already included in the script) and have the following format:

    x, y
    35.20940399169922,22.15359878540039
    34.5449104309082,25.2341251373291
    40.37540817260742,21.507827758789062
    37.30218505859375,23.70339012145996
    etc.


<a id="s004"></a>
## S004

- **source_id:** event-based-eye-tracking-ais2024:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/overview/rules
- **retrieved_at:** 2026-10-20T18:49:04.553085+00:00
- **Archive locator:** `/task_documents/3/text`

If you join this challenge, you accept the [terms and conditions of NTIRE and AIS Workshop Challenges 2024.](https://ai4streaming-workshop.github.io/terms.txt)

If you have any question regarding this challenge, please contact Zuowen Wang (zuowen [at] ini [dot] uzh [dot] ch) or Qinyu Chen (q.chen [at] liacs [dot] leidenuniv [dot] nl)

For general workshop questions please contact the workshop organizers: Marcos Conde (Marcos.Conde[at]uni-wuerzburg.de) or Zongwei Wu  (Zongwei.Wu[at]uni-wuerzburg.de)


<a id="s005"></a>
## S005

- **source_id:** event-based-eye-tracking-ais2024:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/overview/abstract
- **retrieved_at:** 2026-10-20T18:49:04.553085+00:00
- **Archive locator:** `/task_documents/4/text`

## [New] IMPORTANT ANNOUNCEMENT
Please check this [news post](https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/discussion/484138) for understanding the submission of code and factsheet (deadline March 25, 2024 (!!)) and challenge paper submission (deadline April 5, 2024(!!)).

## [ AIS: Vision, Graphics and AI for Streaming Workshop at CVPR 2024 ](https://ai4streaming-workshop.github.io/)

This challenge aims to develop an event-based eye-tracking system for precise tracking of rapid eye movements to produce lighter and more comfortable devices for a better user experience.
The task is to predict the eye center position (x,y) given the event camera inputs. The event recordings are captured with an Inivation DVXplorer Mini event camera. See the youtube video below using event-based eye-tracking system for playing a simple video game!

**Official Challenge Site** [https://eetchallenge.github.io/EET.github.io/](https://eetchallenge.github.io/EET.github.io/)

**Official GitHub Demo Code Repository** [https://github.com/EETChallenge/challenge_demo_code](https://github.com/EETChallenge/challenge_demo_code)

![event-based eye-tracking video game](https://www.youtube.com/watch?v=aRB5mDNfrHM)


## Additional original source extracts

These files preserve original published code or saved web-source extracts. Web extracts may be partial; inspect their stated URLs and coverage. They are historical source material, not the local private grader.

- [web_sources_10.txt](supplement_01.md)
- [web_sources_2.txt](supplement_02.md)
- [web_sources_3.txt](supplement_03.md)
- [web_sources_4.txt](supplement_04.md)
- [web_sources_5.txt](supplement_05.md)
- [web_sources_6.txt](supplement_06.md)
- [web_sources_7.txt](supplement_07.md)
- [web_sources_8.txt](supplement_08.md)
- [web_sources_9.txt](supplement_09.md)
