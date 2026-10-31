# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Prizes](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: Evaluation](#s006)

<a id="s001"></a>
## S001

- **source_id:** financial-performance-prediction:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/data-description
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/0/text`

Dataset contains financial data points for 2030 publicly traded companies based on financial reports submitted to [SEC](https://www.sec.gov/dera/data/financial-statement-data-sets) authority EDGAR database over the course of 11 consecutive quarters starting from Q3-2023 (latest quarter indicated by Q0 prefix) and finishing with Q1-2021 (furthest quarter indicated by Q10 prefix).

### The ordering is as follows:
Columns starting with Q0 contain the companys' financial indicators from the latest reported quarter, it is the closest in time statistics reported by companies.
Q1 - is the quarter which went before Q0
Q10 - represents the furthest statistics in time

Each quarter (except for Q0) contains 17 indicators, please refer to the **data_dictionary.txt** for details.

There are 9 targets which represent the latest financial data points for each company. Kagglers need to train model(s) which will map the historical financial performance of the companies’ to their latest financial indicators.

## Files

- **train.csv** - the training set
- **test.csv** - the test set
- **sample_submission.csv** - a sample submission file in the correct format
- **data_dictionary.txt** - detailed data points description

**Please refer to data_dictionary.txt for detailed columns description**



<a id="s002"></a>
## S002

- **source_id:** financial-performance-prediction:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/Description
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/1/text`

**Financial Performance Prediction** task is highly creative and can be solved as a traditional ML problem with training models on features to predict targets. The dataset is contains a lot of static metadata characterizing the companies, along with dinamics of change of key financial data points across 11 consecutive quarters. 

Alternatively contestants may use a time series approach based on target variables’ values recorded in the previous quarters. 

One may also enrich the training/testing with macroeconomic statistics based on time frames present in the datasets - refer to data_dictionary.txt for mapping of quarters indicators in the dataset (Q0 - Q10) to the actual dates.

**Important**: Synnax has developed a novel approach to predicting the probability of default for private companies working in the `web3` domain leveraging the distributed ML effort provided by many individual contributors independently. This competition is a prequel to the production phase. It shares the type of data individual contributors shall be working with and grows the community - **Synnax will invite all the top performing Kagglers to take part in the production pipeline with monthly profit sharing**.


<a id="s003"></a>
## S003

- **source_id:** financial-performance-prediction:page:2:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/Prizes
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/2/text`

Kagglers shall be evaluated and rewarded along two scales:

## Absolute best

 - 1st place - 20,000 SYNAI Tokens airdrop
 - 2nd place - 10,000 SYNAI Tokens airdrop
 - 3rd place - 5,000 SYNAI Tokens airdrop


SYNAI Airdrop: SYNAI tokens listing is expected to occur at the beginning of 2024 third quarter of the year. Prior to listing the SYNAI tokens, the utility token that is going to power up the Synnax Protocol, will be minted and distributed via an airdrop to the winners blockchain addresses on Ethereum. Important: when submitting your results for the competition, please include your email and ethereum wallet address in the description field.

## Top 25 in the final Leaderboard

The first 25 Kagglers in the final leaderboard of the competition  will be guaranteed a spot in all the upcoming highly incentivized production phase competitions to predict companies’ financial indicators and invited to join the Synnax Lab as Founding Masters. 

# Synnax Lab

Synnax mission is to become the best place in the world where DS interested in challenging their AI skills and applying them in the field of Financial Credit can come together as a community tackling the biggest problems that so far restrained the healthy growth of the private credit market that still functions on a structure and models created in the 70s. Synnax Lab will be the perfect place for DS to learn, improve and do research on the field on Synnax Testnet environment and through regular highly rewarded challenges. Those that will raise up the ranks of Synnax Lab and graduate as Synnax Scientists will be then eligible to put their skills and model at work in Synnax mainnet where they will be eligible to share ⅓ of the revenues of the whole protocol as a payout for their contributions. The best performers that will achieve the rank of Synnax Masters will be eligible to directly contribute to the development of the Synanx Protocol and Synnax product becoming eligible for special revenue shares.


<a id="s004"></a>
## S004

- **source_id:** financial-performance-prediction:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/rules
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/3/text`

1. **Eligibility**: The competition is open to participants of all skill levels and backgrounds. Participants must adhere to Kaggle's terms of service.
2. **Data Usage**: Participants are allowed to use the provided dataset for training their models and making predictions.
3. **Task Description**: Participants are tasked with predicting the financial data indicators for the last reported quarter (Q0) for the given companies.
5. **Modeling Approaches**: Participants can use traditional machine learning approaches or time series methods to predict the target variables.
Enriching training/testing with macroeconomic statistics based on the time frames present in the dataset is allowed.
6. **Submission Guidelines**: Participants must submit their predictions for the target variables of the last reported quarter (Q0).
Submissions should be in CSV format, with the same structure as the provided sample_submission.csv.
7. **Evaluation Criteria**: Submissions will be evaluated based on the mean absolute percentage error (MAPE) between the predicted and actual values of the target variables.
8. **Code and Model Sharing**: Participants are encouraged to share their code and models with the community on the competition discussion board.
Code sharing should comply with Kaggle's terms and conditions.
9. **Communication**: Participants are encouraged to actively engage in the competition discussion board to share insights, ask questions, and collaborate with others.
Respectful and constructive communication is expected.
11. **Compliance**: Participants must comply with all competition rules to be eligible for prizes.
Any violation of the rules or inappropriate behaviour may result in disqualification.
12. **Prize Distribution**: Prizes will be awarded based on the performance of participants as determined by the evaluation criteria.
13. **Code of Conduct**: Participants are expected to conduct themselves in a professional and respectful manner.
Any form of cheating, plagiarism, or unethical behavior will result in immediate disqualification.
14. **Acknowledgment**: Synnax reserves the right to use participants' solutions for research and development purposes, with proper acknowledgment.
By participating in this competition, participants agree to abide by these rules and any updates or clarifications posted on the competition platform. Synnax and Kaggle reserve the right to modify the rules if necessary and will communicate any changes promptly.


<a id="s005"></a>
## S005

- **source_id:** financial-performance-prediction:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/abstract
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/4/text`

**Synnax** is proud to present a carefully crafted dataset containing real financial indicators of 2030 publicly traded companies over 11 consecutive quarters. A lot of effort has been put into compiling these statistics and we believe this data can serve as a basis for a wide range of financial analytics tasks, including budget forecasting, financial health, loan default prediction, etc.

In this competition **Synnax** is challenging Kagglers to predict the companies’ financial data points for the last (closest to today) reported quarter. Each quarter in the dataset is represented by 9 financial data points such as `TOTAL_ASSETS`, `TOTAL_LIABILITIES`, `EBITDA`, etc. and the quarter indicator is the prefix (Q0, Q1, … Q10) where the “0” indicates the most recent quarter in the dataset . The target variables are indicated with `Q0` prefix and are only present in the `train.csv`.

## ! IMPORTANT
Please add your contact details and an Ethereum wallet address to your winning submission for collecting your prize. Please refer to this discussion [thread](https://www.kaggle.com/competitions/financial-performance-prediction/discussion/478828) for explanation.


<a id="s006"></a>
## S006

- **source_id:** financial-performance-prediction:page:5:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/financial-performance-prediction/overview/Evaluation
- **retrieved_at:** 2026-10-20T18:34:56.244338+00:00
- **Archive locator:** `/task_documents/5/text`

Submissions are evaluated on the [R2 score](https://en.wikipedia.org/wiki/Coefficient_of_determination) (coefficient of determination) between their predicted financial indicators and the actual data. R2 score shall be calculated separately for each of the 9 predicted financial data points then averaged.


## Submission File
For each `Id` in the test set, you must predict 9 financial data points. The file should contain a header and have the following format:

    Id,Q0_TOTAL_ASSETS,Q0_TOTAL_LIABILITIES,Q0_TOTAL_STOCKHOLDERS_EQUITY,Q0_GROSS_PROFIT,Q0_COST_OF_REVENUES,Q0_REVENUES,Q0_OPERATING_INCOME,Q0_OPERATING_EXPENSES,Q0_EBITDA
    2,0,0,0,0,0,0,0,0,0
    5,0,0,0,0,0,0,0,0,0
    6,0,0,0,0,0,0,0,0,0
    etc.

Please check the sample_submission.csv for reference.

