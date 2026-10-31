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

- **source_id:** copy-of-flares-identification:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/copy-of-flares-identification/overview/data-description
- **retrieved_at:** 2026-10-20T18:35:30.160242+00:00
- **Archive locator:** `/task_documents/0/text`

The dataset contains a total of 570 news items annotated with the journalistic   technique 5W1H, obtaining approximately 19,322 annotations. The dataset has been splitted into a proportion of 70% (13,526) for training, 10% (1,932) for development, and 20% (3,864) for testing. The corpus contains text in Spanish manually annotated with an extraction technique known as 5W1H, which is a journalistic technique consisting of annotating all the entities present in a text related to the questions What, Who, Where, When, Why and How. It was annotated by three expert annotators (2 linguistics and 1 sociologist), all three specialized in NLP and with knowledge in the annotation guideline created for this purpose.
The language chosen is Spanish because, although it is the fourth most widely spoken language in the world and the second mother tongue in the world in terms of number of speakers, there are few corpora built in Spanish to address the automatic reliability detection task in NLP. 

With regard to the domain, the topics covered in this dataset include economy, sports, science, education, health, society, entertainment, politics and security.

Regarding the collection procedure, 170 news was collected manually and via web crawling, while the other 400 news was collected from an existing corpus --- named The Spanish Fake News Corpus (SFN). News was collected from digital newspapers such as ABC, BBC News, CNN Spanish, El Espectador, El Financiero, El Mundo, El País, Huffpost, Marca, La Jornada, El Diestro, Eje21, Periodista Digital, Ok Diario, 20 Minutos, la Vanguardia, among others. For the construction of the dataset, news that did not follow the language, format, extension, or other semantic characteristics desired in the corpus was filtered out.

## Files

*   **5w1h_subtask_1_train.csv** - the training set 1
*   **5w1h_subtask_1_test.json** - the test set


<a id="s002"></a>
## S002

- **source_id:** copy-of-flares-identification:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/copy-of-flares-identification/overview/Description
- **retrieved_at:** 2026-10-20T18:35:30.160242+00:00
- **Archive locator:** `/task_documents/1/text`

Target community: 
Targeting researchers, media professionals, journalists, and policymakers, since the initiative offers tools to enhance content quality and accuracy.

**Subtask 1: 5W1Hs identification** (approx 19k annotations): Participants will be provided with a text, and they will have to determine the essential content of it by annotating the answers to the 5W1H questions of the document.


The RUN-AS annotation guideline enables the detection of the essential parts of a news item together with the reliability of its semantic elements, as well as other linguistic elements of interest that allow to find linguistic patterns of reliability in text, without using external knowledge. The goal of this annotation proposal is to analyze content on the basis of a purely  linguistic analysis to find out whether the way in which a news item is structured or written influences its reliability. To find out whether a news item presents objective information and follows journalistic standards, this proposal enables a three-level annotation: Structure (Inverted Pyramid hypothesis), Content (5W1H technique) and Elements of Interest (key expressions, orthotypography, quotes, etc.). For the present task, only the second level will be used, that is the use of the 5W1H, to detect the most important information in a text along with its reliability. 
The labels proposed for annotating this task are WHAT (fact), WHO (subject), WHEN (time), WHERE (place), WHY (cause) and HOW (manner). 

Using the 5W1H technique, we can break down the sentence “The arrest of the Italian scientist took place by force yesterday in Milan for selling an unauthorized vaccine” as follows:

     - What: The arrest 
     - Who: Italian scientist 
     - How: by force
     - When: yesterday
     - Where:  in Milan
     - Why: for selling an unauthorized vaccine

---------
Schedule:
- February 5, 2024: Call for Participation and participant's subscription
- March 20, 2024: Training Set Available
- May 3, 2024: Testing Set Available
- May 17, 2024: Submission of Run
- May 24, 2024: Notification of Results
- June 10, 2024: Submission of Working Notes by Participants
- June 28, 2024: Reviews to Participants
- July 11, 2024: Camera-ready Submissions Due

----------
Participant's subscription:
 
To participate and receive notifications fill the following Google form ([FLARES Registration](https://docs.google.com/forms/d/e/1FAIpQLSeDE8tPqJtEJI4zM4wVFK06oZ8HYnHNVnj0k1A-74DRrIHQgw/viewform))




<a id="s003"></a>
## S003

- **source_id:** copy-of-flares-identification:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/copy-of-flares-identification/overview/Evaluation
- **retrieved_at:** 2026-10-20T18:35:30.160242+00:00
- **Archive locator:** `/task_documents/2/text`

**For Subtask 1**, we will use the metrics proposed by Piad-Morffis et al. (2020). This work defines correct, partial, missing, incorrect, and spurious matches to be applied in the span classification task. 
- Correct matches are reported when a text in the predicted file matches exactly with a corresponding text span in the gold file for start and end index, and also the 5W1H label. Only one correct match per entry in the gold file can be matched. 
- Incorrect matches are reported when the start and end index match, but not the type.
- Partial matches are reported when two intervals [start, end] have a non-empty intersection, such as the case of “scientists” and “scientists specialised in biophysics” in the previous example (and matching the 5W1H label). Notice that a partial phrase will only be matched against a single correct phrase. For example, “researchers from the GPLSI Group” could be a partial match for both “researchers” and “the GPLSI Group”, but it is only counted once as a partial match with the word “researchers”. The words “the GPLSI Group” are counted then as Missing. This aims to discourage a few large text spans that cover most of the document from getting a very high score. 
- Missing matches are those that appear in the gold file but not in the predicted file. 
- Spurious matches are those that appear in the predicted file but not in the gold file.
From these definitions, we compute precision, recall, and a standard F1-Score as follows: 

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3216324%2F7eee21e2e17591ddef569c4adcdb468d%2FScreenshot%202024-02-05%20at%2019.07.10.png?generation=1707210587317872&alt=media)

**Submission File**
You have to create a CSV file where each row represents an example. For each line in the test set, you must add an array where each element contains the "TAGS" 5W1H labels and its start and end index. Below we show three lines examples:

ID,TEXT,TAGS
1,Input text 1,"[{'start': 0, 'end': 5, 'tag': 'What'}, {'start': 6, 'end': 10, 'tag': 'How'}]"
2,Input text 2,"[{'start': 0, 'end': 5, 'tag': 'What'}, {'start': 6, 'end': 10, 'tag': 'Who'}]"
3,Input text 3,"[{'start': 6, 'end': 10, 'tag': 'When'}]"


<a id="s004"></a>
## S004

- **source_id:** copy-of-flares-identification:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/copy-of-flares-identification/overview/rules
- **retrieved_at:** 2026-10-20T18:35:30.160242+00:00
- **Archive locator:** `/task_documents/3/text`

It is allowed to use any algorithm, model, etc, as well as external data.


<a id="s005"></a>
## S005

- **source_id:** copy-of-flares-identification:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/copy-of-flares-identification/overview/abstract
- **retrieved_at:** 2026-10-20T18:35:30.160242+00:00
- **Archive locator:** `/task_documents/4/text`

FLARES: Fine-Grained Language-based Reliability Detection in Spanish News

Description of the task:

Assessing the reliability of the language used in news writing is becoming increasingly crucial in today's digital media landscape. Identifying specific segments of a news article to gauge the linguistic credibility offers a more nuanced understanding of the message's truthfulness. This approach not only enhances our grasp of information presentation but also paves the way for the development of more effective techniques in spotting fake or misleading news.

Recent studies have delved into this approach, highlighting the importance of analyzing language style, tone, and structure in identifying deceptive content. Style and language are features that have proven valuable in distinguishing between fake and true articles, and specific linguistic features have proven valuable in indicating potential biases or misrepresentations in online content. These studies underscore the emerging significance of leveraging linguistic analysis to discern trustworthy news in the digital age.

In this context, we propose harnessing the “5W1H” technique commonly employed by journalists to clearly present the key information of a news item in an explicit way. This method focuses on identifying the What, Who, Why, When, Where, and How elements within a text. By applying this technique, we can systematically evaluate the reliability of the language across these dimensions. Analyzing the presence of these fundamental journalistic questions offers a structured approach to gauge the linguistic integrity and potential biases within the content. Moreover, our challenge will utilize texts in Spanish, aiming to advance techniques of this nature specifically tailored for this language. This integration of journalistic methodology with linguistic analysis not only provides a comprehensive framework but also could pave the way for enhancing the authenticity and trustworthiness of information in the Spanish digital media landscape.


## Additional original source extracts

These files preserve original published code or saved web-source extracts. Web extracts may be partial; inspect their stated URLs and coverage. They are historical source material, not the local private grader.

- [evaluation_metric_template_kaggle_subtask_1.py](supplement_01.py)
