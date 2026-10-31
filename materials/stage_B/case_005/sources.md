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
- [S007: Sponsors](#s007)
- [S008: Prizes](#s008)
- [S009: harmonizing-the-data-of-your-data:thread:670893:opening](#s009)
- [S010: harmonizing-the-data-of-your-data:thread:670893:3399261](#s010)
- [S011: harmonizing-the-data-of-your-data:thread:674908:opening](#s011)
- [S012: harmonizing-the-data-of-your-data:thread:674908:3431347](#s012)
- [S013: harmonizing-the-data-of-your-data:thread:674908:3431631](#s013)
- [S014: harmonizing-the-data-of-your-data:thread:674908:3431633](#s014)
- [S015: harmonizing-the-data-of-your-data:thread:674908:3409457](#s015)
- [S016: harmonizing-the-data-of-your-data:thread:674908:3413760](#s016)
- [S017: harmonizing-the-data-of-your-data:thread:680135:opening](#s017)
- [S018: harmonizing-the-data-of-your-data:thread:680135:3419753](#s018)
- [S019: harmonizing-the-data-of-your-data:thread:680135:3420378](#s019)
- [S020: harmonizing-the-data-of-your-data:thread:680135:3421589](#s020)
- [S021: harmonizing-the-data-of-your-data:thread:680135:3422259](#s021)
- [S022: harmonizing-the-data-of-your-data:thread:680135:3422260](#s022)
- [S023: harmonizing-the-data-of-your-data:thread:680135:3423038](#s023)
- [S024: harmonizing-the-data-of-your-data:thread:680135:3423327](#s024)
- [S025: harmonizing-the-data-of-your-data:thread:683992:opening](#s025)
- [S026: harmonizing-the-data-of-your-data:thread:683992:3429317](#s026)
- [S027: harmonizing-the-data-of-your-data:thread:683992:3429721](#s027)
- [S028: harmonizing-the-data-of-your-data:thread:686554:opening](#s028)
- [S029: harmonizing-the-data-of-your-data:thread:688827:opening](#s029)
- [S030: harmonizing-the-data-of-your-data:thread:694356:opening](#s030)

<a id="s001"></a>
## S001

- **source_id:** harmonizing-the-data-of-your-data:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/data-description
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/0/text`

### **Data Provided**  
We have provided the following datasets for Training:
1. The Open Access Publication text stored as .json files in `data/Training_PubText/`.  
2. The human annotated SDRFs for the Training set in `data/Training_SDRFs/`.  
3. The GPT annotated metadata using the `BaselinePrompt.txt` for the Training set in `data/Training_GPT_Extract/`.  

We have provided the following dataset for Testing and Leaderboard scoring: 
1. The Open Access Publication text stored as .json files in `data/Test_PubText/`.  

There is a `SampleSubmission.csv` file which contains a sample of how exactly you should format your solution to be scored within the confines of Kaggle's submission system. 

## Other Technical Information  
# Sample Data Relation File (SDRF) Generation
The SDRF-Proteomics format is a tab-delimited format that describes the sample characteristics and the relationships between samples and data files included in a dataset. The information in SDRF files is organized to follow the natural flow of a proteomics experiment.  

## Overall structure of an SDRF
An SDRF-Proteomics file is a single table where each row represents one sample–data file relationship. Columns can have the following headers:  
| Prefix                  | Indicates…                                                                |
| ----------------------- | ------------------------------------------------------------------------- |
| **Source Name**         | Unique ID for the *starting material* (e.g. organism)                     |
| **Characteristics\[…]** | Sample attributes (e.g. organism, tissue, disease)                        |
| **Factor Value\[…]**    | Study variables or experimental factors (e.g. treatment, time point)      |
| **Comment\[…]**         | Data-file or technical metadata (e.g. instrument, fraction, label)        |
| **Assay Name**          | Unique ID for the *assay* (i.e. the combination of sample + file)         |
| **Raw Data File**       | File name or path of the raw spectrum file                                |
| *(or)* **Data File**    | Processed output (e.g. mzML, mzTab)                                       |
  

### Characteristics — sample‐level metadata  
| Annotation Type                  | Definition                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Age**                          | Age of the donor or developmental stage of the organism (e.g. “45 years”, “E14.5 embryo”).        |             
| **AlkylationReagent**            | A chemical (like Iodoacetamide (IAA) or N-ethylmaleimide (NEM)) that irreversibly adds an alkyl group to the free sulfhydryl (-SH) of cysteine residues, blocking disulfide bonds and preventing protein re-folding.   |
| **AnatomicSiteTumor**            | Anatomical location from which a tumor sample was taken (e.g. “left lung lobe”).                  |
| **AncestryCategory**             | Donor ancestry or ethnicity category (e.g. “European”, “East Asian”).                             |
| **Bait**                         | The protein or molecule used as bait in an affinity‐purification experiment.                      |
| **BMI**                          | Body‐Mass Index of the donor (kg/m²).                                                             |
| **BiologicalReplicate**          | Identifier for biological replicates (e.g. “bioRep1”, “bioRep2”).                                 |
| **CellLine**                     | Name of the immortalized cell line (e.g. “HEK293T”, “U2OS”).                                      |
| **CellPart**                     | Subcellular compartment or fraction (e.g. “nucleus”, “mitochondria”).                             |
| **CellType**                     | Primary cell type or lineage (e.g. “neurons”, “fibroblasts”).                                     |
| **CleavageAgent**                | Protease or chemical used to digest proteins (e.g. “trypsin”, “chymotrypsin”).                    |
| **Compound**                     | Chemical or small molecule added to the sample (e.g. drug, inhibitor)                             |
| **ConcentrationOfCompound**      | Concentration of the Compound used (e.g. “10 µM”).                                                |
| **Depletion**                    | Method used to remove high‐abundance proteins (e.g. “albumin depletion kit”).                     |
| **DevelopmentalStage**           | Stage of development for the sample source (e.g. “adult”, “P7 pup”).                              |
| **Disease**                      | Disease state or diagnosis (e.g. “breast cancer”, “Type 2 diabetes”).                             |
| **DiseaseTreatment**             | Pre‐treatment applied to diseased samples (e.g. “chemotherapy”, “radiation”).                     |
| **GeneticModification**          | Any genetic alteration in the source organism/cells (e.g. “GFP‐tagged”, “knockout of gene X”).    |
| **Genotype**                     | Genotypic background (e.g. “C57BL/6J”, “BRCA1-mutant”).                                           |
| **GrowthRate**                   | Doubling time or growth rate of cell cultures (e.g. “24 h doubling”).                             |
| **Label**                        | Isobaric or metabolic label applied (e.g. “TMT-126”, “SILAC heavy”).                              |
| **MaterialType**                 | Broad class of material (e.g. “tissue”, “cell line”, “biofluid”).                                 |
| **Modification**                 | Post‐translational modification enrichment or tagging (e.g. “phosphorylation”, “ubiquitination”). |
| **NumberOfBiologicalReplicates**\* | Total number of biological replicates in the study.                                             |
| **NumberOfSamples**\*              | Total number of samples processed.                                                              |
| **NumberOfTechnicalReplicates**\*  | Total number of technical replicates per sample.                                                |
| **Organism**                     | Source species (NCBI Taxonomy ID and name, e.g. “9606 (Homo sapiens)”).                           |
| **OrganismPart**                 | Tissue or organ of origin (Uberon term, e.g. “UBERON:0002107 (liver)”).                           |
| **OriginSiteDisease**            | Anatomical site of disease origin (e.g. “colon”, “prostate”).                                     |
| **PooledSample**                 | Indicates if multiple samples were pooled (e.g. “pool1 of reps1–3”).                              |
| **ReductionReagent**             | Chemical used to reduce disulfide bonds (e.g. “DTT”, “TCEP”).                                     |
| **SamplingTime**                 | Time point of sample collection (e.g. “T0”, “24 h post‐treatment”).                               |
| **Sex**                          | Donor sex (e.g. “male”, “female”).                                                                |
| **Specimen**                     | Description of biological specimen (e.g. “biopsy”, “plasma”).                                     |
| **SpikedCompound**               | Exogenous standard or spike‐in added (e.g. “iRT peptides”).                                       |
| **Staining**                     | Any staining applied to the sample prior to mass spec that may still be present in the sample.    |
| **Strain**                       | Animal strain (e.g. “BALB/c”, “FVB/N”).                                                           |
| **SyntheticPeptide**             | Indicates a synthetic peptide sample (e.g. “synthetic phosphopeptide”).                           |
| **Temperature**                  | Growth temperature of the samples or perturbation temperature if a differential study.            |
| **Time**                         | Broad time parameter (e.g. “day 5”, “week 2”).                                                    |
| **Treatment**                    | Experimental treatment (e.g. “drug X 5 µM 24 h”).                                                 |
| **TumorCellularity**             | Percentage of tumor cells in the sample (e.g. “80%”).                                             |
| **TumorGrade**                   | Histological grade (e.g. “Grade II”).                                                             |
| **TumorSize**                    | Physical size of the tumor (e.g. “3 cm diameter”).                                                |
| **TumorSite**                    | Anatomical site of tumor (e.g. “breast”, “pancreas”).                                             |
| **TumorStage**                   | Clinical staging (e.g. “Stage III”).                                                              |
\* Not applicable on a per sample basis  

### Comment — data‐file and protocol parameters  
| Annotation Type             | Definition                                                                |
| --------------------------- | ------------------------------------------------------------------------- |
| **AcquisitionMethod**       | MS acquisition scheme (e.g. “DDA”, “DIA”, “PRM”).                         |
| **CollisionEnergy**         | Collision energy applied in MS/MS (e.g. “27 eV”).                         |
| **EnrichmentMethod**        | Peptide/enrichment protocol used (e.g. “TiO₂ phosphopeptide enrichment”). |
| **FlowRateChromatogram**    | LC flow rate (e.g. “300 nL/min”).                                         |
| **FractionationMethod**     | Any off-line method used to fraction bulk sample into the primary samples used in the MS or LC/MS.             |
| **FractionIdentifier**      | Numeric or text ID of each fraction (e.g. “F1”, “F2”).                    |
| **FragmentationMethod**     | Ion‐fragmentation technique (e.g. “HCD”, “CID”, “ETD”).                   |
| **FragmentMassTolerance**   | Mass tolerance for fragment matching (e.g. “0.02 Da”).                    |
| **GradientTime**            | Total LC gradient length (e.g. “120 min”).                                |
| **Instrument**              | Mass spec make/model (e.g. “Thermo Q-Exactive Plus”).                     |
| **IonizationType**          | Ionization source (e.g. “nanoESI”, “MALDI”).                              |
| **MS2MassAnalyzer**         | Analyzer used for MS2 (e.g. “orbitrap”, “ion trap”).                      |
| **NumberOfMissedCleavages** | Max missed cleavages allowed in database search (e.g. “2”).               |
| **NumberOfFractions**       | Total number of fractions generated from each sample.                     |
| **PrecursorMassTolerance**  | Mass tolerance for precursor matching (e.g. “10 ppm”).                    |
| **Separation**              | Any on-line method used to separate the samples into fractions right before MS.|

Note: Most of the sample characteristics and comments above are detailed in this .pdf file but not all. These are an expanded set of annotated tags we use to ensure we get as much metadata from the manuscript as possible and some many not be applicable on a per sample basis (such as NumberBiologicalReplicates).  
  

## References and Resources
[1] Perez-Riverol Y; European Bioinformatics Community for Mass Spectrometry. Toward a Sample Metadata Standard in Public Proteomics Repositories. J Proteome Res. 2020 Oct 2;19(10):3906-3909. doi: 10.1021/acs.jproteome.0c00376. Epub 2020 Sep 22. PMID: 32786688; PMCID: PMC7116434. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7116434/?utm_source=chatgpt.com)  
[2] [www.psidev.info/sdrf-sample-data-relationship-format](www.psidev.info/sdrf-sample-data-relationship-format)  
[3] [https://github.com/CompOmics](https://github.com/CompOmics)  
[4] [https://github.com/bigbio/proteomics-sample-metadata](https://github.com/bigbio/proteomics-sample-metadata)  
[5] Claeys, T., Van Den Bossche, T., Perez-Riverol, Y. et al. lesSDRF is more: maximizing the value of proteomics data through streamlined metadata annotation. Nat Commun 14, 6743 (2023). https://doi.org/10.1038/s41467-023-42543-5

Some more information on what exactly an SDRF is: https://drive.google.com/file/d/1O-LVFbR_hpvIeAnU3z2JV2uoDZ39qP29/view?usp=sharing


<a id="s002"></a>
## S002

- **source_id:** harmonizing-the-data-of-your-data:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/Description
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/1/text`

At the end of this competition, we will write a scientific article describing this event. If you would like to be considered as a co-author, please opt-in in this [form](https://docs.google.com/forms/d/e/1FAIpQLSeyqKmmTjHmTDPzkX2WBy7mUuUS68eO0ITkdC1Z5v5QiiRlpg/viewform?usp=publish-editor). The organizers reserve the right to select co-authors based on contribution merit.

# **Metadata Extraction from Mass Spetrometry Proteomics Publications**

## **Problem Statement**  
With computational power constantly accelerating, we find that bottlenecks for analyzing scientific data lie not in the availability of said power, but in the availability of the data for analysis. Scientific knowledge is disseminated through scientific articles, where data and metadata are described in natural language, rendering comparative analysis of experiments very difficult. Proteomics is the study of proteins and their functions. In proteomics, a data standard called Sample Data Relationship Format (SDRF) describes the characteristics of the samples used in the experiment and the relationships between samples in a standard, computationally tractable manner. However, many scientific articles do not provide full, computationally tractable SDRFs, and there are many older articles prior to the adoption of SDRF where sample data are sequestered. Therefore, it is urgent to develop a model that takes a scientific article as its input and provides a reliable SDRF as its output. Such a model will revolutionize our ability to perform large-scale scientific analyses of scientific articles by removing the barrier to accessing sample data.   

## **Authorship Call**
At the end of this competition, we will write a scientific article describing this event. If you would like to be considered as a co-author, please opt-in in this [form](https://docs.google.com/forms/d/e/1FAIpQLSeyqKmmTjHmTDPzkX2WBy7mUuUS68eO0ITkdC1Z5v5QiiRlpg/viewform?usp=publish-editor). The organizers reserve the right to select co-authors based on contribution merit.

# **Competition Overview**  

## **Core Task**
Create a model, prompt, or pipeline that converts paper text into a complete SDRF. You can use rule-based systems, LLM prompting, classical NLP, or fine-tuned models, anything that outputs a valid SDRF.
        
Your solution should match or outperform the benchmarks on a held-out test set of annotated SDRF files.

## **Data Provided**  
We have provided the following datasets for Training:
1. The Open Access Publication text stored as .json files in `data/Training_PubText/`.  
2. The human annotated SDRFs for the Training set in `data/Training_SDRFs/`.  
3. The GPT annotated metadata using the `BaselinePrompt.txt` for the Training set in `data/Training_GPT_Extract/`.  

We have provided the following dataset for Testing and Leaderboard scoring: 
1. The Open Access Publication text stored as .json files in `data/Test_PubText/`.  

There is a `SampleSubmission.csv` file which contains a sample of how exactly you should format your solution to be scored within the confines of Kaggle's submission system. 





<a id="s003"></a>
## S003

- **source_id:** harmonizing-the-data-of-your-data:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/Evaluation
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/2/text`

# Leader-board scores are computed with this [evaluation notebook](https://www.kaggle.com/code/iansitarik/sdrf-f1).  

## Leader-board Evaluation Metric Explanation

Your submission is compared to the ground-truth SDRF at the level of **unique annotation values per (PXD, column)** — not row-by-row sample alignment.

### Step 1 — Preprocessing

* Both solution and submission must contain a `PXD` column.
* Data are grouped by PXD.
* Within each PXD and column, **unique non-null values** are extracted.
* Columns containing only `"Not Applicable"` are excluded from scoring.

### Step 2 — String Harmonization

To allow minor wording differences, all unique values from solution and submission are combined and clustered using string similarity (≥ 0.80).
Values that are sufficiently similar are treated as the same entity.

### Step 3 — Set Comparison

For each (PXD, column), we compare the **set of harmonized entities**:

* **Precision** = fraction of predicted entities that are correct
* **Recall** = fraction of true entities that were recovered
* **F1** = harmonic mean of precision and recall

Duplicate entries do not increase weight — this is a **set-based comparison**, not count-based.

### Step 4 — Final Score

An F1 score is computed for each (PXD, column) pair.
The final leaderboard score is the **mean F1 across all evaluated pairs**.

### What This Means

* You are evaluated on recovering the correct **annotation entities**, not exact strings.
* Minor spelling or formatting differences are tolerated.
* Extra incorrect entities lower precision.
* Missing true entities lower recall.

Focus on accurately identifying the correct set of annotation values for each PXD and column.

---

# How to Submit

## Non-final submissions  
Your team can submit up to 5 submission files a day to be scored automatically for the leader board. These submission files should following the example `SampleSubmission.csv` located in the Data tab. 

## Final submission
Once you are ready for your final submission you use one of the following options to be eligible for winning:  

### Option 1: Submit via Kaggle (Zip File)

Submit your work directly to the Kaggle competition. This is the main submission method along with submitting a submission.csv for scoring on the leaderboard.

**Package your submission as a ZIP file containing:**

1. **`submission.csv`** - Your predicted SDRF following the SampleSubmission.csv format
2. **Minimal Working Example** - Code demonstrating your complete pipeline

**Structure:**
```
my_submission.zip
├── submission.csv
├── pipeline.py (or notebook)
├── requirements.txt
└── README.md (optional: explain your approach)
```

**Steps:**
1. Go to the [competition page](https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data)
2. Click "Make a Submission"
3. Upload your ZIP file
4. Your submission will be scored and ranked on the leaderboard

### Option 2: Contribute via Pull Request

**We strongly encourage sharing your complete pipeline with the community!** Contributing via pull request allows others to build upon your work, learn from your approach, and potentially improve the overall solution.  
https://github.com/NCEMS/Kaggle-Harmonizing-the-data-of-your-data  
  
#### Benefits of Contributing

✅ Share your solution with the broader community  
✅ Get credited for your approach  
✅ Help others improve their pipelines  
✅ Build a portfolio of open-source contributions  
✅ Potentially increase visibility for co-authorship consideration  

#### Step-by-Step Contribution Guide

##### Step 1: Fork the Repository

Click the "Fork" button on GitHub to create your own copy of the repository.

```bash
# Clone your fork locally
git clone https://github.com/YOUR-USERNAME/Kaggle-Harmonizing-the-data-of-your-data.git
cd Kaggle-Harmonizing-the-data-of-your-data
```

##### Step 2: Create a Feature Branch

Create a new branch for your contribution with a descriptive name:

```bash
git checkout -b feat/your-pipeline-name

# Example names:
# feat/gpt4-prompt-based-extraction
# feat/finetuned-bert-sdrf
# feat/rule-based-parser
# feat/ensemble-hybrid-approach
```

##### Step 3: Create Your Submission Folder

Each submission should be in a dedicated folder within `Submissions/`:

```bash
mkdir -p Submissions/your-team-or-name

# Create the following structure:
Submissions/your-team-or-name/
├── pipeline.py (or .ipynb - main implementation)
├── submission.csv (your best submission results)
├── requirements.txt (Python dependencies)
├── README.md (documentation of your approach)
└── data/ (optional: training data, models, etc.)
```

##### Step 4: Implement Your Solution

**`pipeline.py` (or Jupyter Notebook)**

Your main implementation should:
- Load the training and test data
- Implement your metadata extraction approach
- Generate the submission CSV
- Be executable as a minimal working example

```python
# Example structure:
import pandas as pd
from src.Scoring import score

def extract_sdrf(paper_text):
    """Your extraction logic here"""
    pass

def main():
    # Load data
    papers = load_papers()
    
    # Extract metadata
    predictions = [extract_sdrf(p) for p in papers]
    
    # Generate submission
    submission_df = pd.DataFrame(predictions)
    submission_df.to_csv('submission.csv', index=False)
    
    # (Optional) Score locally if you have test labels
    if has_test_labels():
        solution_df = pd.read_csv('test_solution.csv')
        eval_df, score = score(solution_df, submission_df, 'ID')
        print(f"Local F1 Score: {score:.6f}")

if __name__ == "__main__":
    main()
```

**`requirements.txt`**

List all Python dependencies:

```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
torch>=1.10.0
transformers>=4.0.0
# Add any other libraries your pipeline needs
```

**`README.md`**

Document your approach:

```markdown
# Your Solution Name

Brief description of your approach.

## Method

Explain your pipeline:
- Data preprocessing
- Feature extraction/engineering
- Model architecture or rules
- Post-processing
- Key hyperparameters

## Results

- Local F1 Score: X.XXX
- Kaggle Score: X.XXX
- Key findings

## Installation & Usage

```bash
pip install -r requirements.txt
python pipeline.py
```

## References

- Papers you cited
- Datasets you used
- Inspiration from other work
```

##### Step 5: Test Your Code

Ensure your minimal working example runs correctly:

```bash
# Install dependencies
pip install -r Submissions/your-team-or-name/requirements.txt

# Test your pipeline
python Submissions/your-team-or-name/pipeline.py

# (Optional) Test the scoring function
python src/Scoring.py \
  --solution test_data/solution.csv \
  --submission Submissions/your-team-or-name/submission.csv
```

##### Step 6: Commit and Push

Commit your changes with clear, descriptive messages:

```bash
# Stage your changes
git add Submissions/your-team-or-name/

# Commit with a descriptive message
git commit -m "feat: Add GPT-4 based SDRF extraction pipeline

- Implements few-shot prompting strategy
- Includes validation and error handling
- Local F1 score: 0.85"

# Push to your fork
git push origin feat/your-pipeline-name
```

##### Step 7: Create a Pull Request

1. Go to the original repository: https://github.com/[original-owner]/Kaggle-Harmonizing-the-data-of-your-data
2. Click "Pull Requests" → "New Pull Request"
3. Click "compare across forks"
4. Select your fork and branch
5. Click "Create Pull Request"

**PR Title:** Keep it concise
```
[Submission] Your Pipeline Name - Brief Description
```

**PR Description:** Provide context for reviewers

```markdown
## Description
Brief explanation of your approach

## Method
- Key techniques used
- Model/algorithm details
- Notable features

## Results
- Kaggle leaderboard score
- Local evaluation results
- Performance metrics

## Files Added
- `pipeline.py` - Main implementation
- `requirements.txt` - Dependencies
- `submission.csv` - Results file

## References
- Relevant papers
- Data sources
- Inspiration

## Checklist
- [ ] Code runs without errors
- [ ] Dependencies listed in requirements.txt
- [ ] README documents the approach
- [ ] Submission file is properly formatted
```

##### Step 8: Address Feedback

Maintainers may request changes:
- Make edits locally on the same branch
- Commit and push again
- The PR will automatically update

```bash
# Make updates to your code
git add .
git commit -m "fix: Improve preprocessing logic"
git push origin feat/your-pipeline-name
```

#### Submission Guidelines

**Do's:**
- ✅ Write clean, readable code with comments
- ✅ Include a working minimal example
- ✅ Document your approach clearly
- ✅ Test your code before submitting
- ✅ Include a realistic requirements.txt
- ✅ Add proper docstrings and type hints
- ✅ Consider edge cases and error handling

**Don'ts:**
- ❌ Large binary files (>10MB) - use .gitignore
- ❌ Training data or large models (reference external sources instead)
- ❌ Undocumented or hard-to-follow code
- ❌ Broken or incomplete pipelines
- ❌ Duplicate submissions (check existing ones first)

## Repository Structure

```
.
├── README.md                          # This file
├── LICENSE                            # Repository license
├── src/
│   └── Scoring.py                     # Competition scoring function
├── data/
│   ├── SampleSubmission.csv           # Template for submission format
│   ├── TrainingPubText/               # Training set publication texts (JSON)
│   ├── TrainingSDRFs/                 # Gold-standard SDRF annotations (CSV)
│   ├── TestPubText/                   # Test set publication texts (JSON)
│   └── detailed_evaluation_metrics.csv # Example evaluation output
├── detailed_evaluation_metrics.csv    # Example evaluation output
└── Submissions/                       # Community contributions
    ├── example-submission-1/
    │   ├── pipeline.py
    │   ├── submission.csv
    │   ├── requirements.txt
    │   └── README.md
    ├── example-submission-2/
    │   └── ...
    └── your-submission/
        └── ...
```


<a id="s004"></a>
## S004

- **source_id:** harmonizing-the-data-of-your-data:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/rules
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/3/text`

##ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.

**[See Section 3.18 for defined terms](rules#18.-terms)**

*The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions  must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules.*

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

1. COMPETITION-SPECIFIC TERMS

1. COMPETITION TITLE

 Metadata Extraction from Mass Spectrometry Proteomics Text
2. COMPETITION SPONSOR

  NSF - National synthesis Center for the Emergence of Molecular and Cellular Science
3. COMPETITION SPONSOR ADDRESS

 376 Science Dr, State College, PA 16801
4. COMPETITION WEBSITE

 https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data
5. TOTAL PRIZES AVAILABLE: $10,000

 
First Prize: $5,000 
Second Prize: $3,000 
Third Prize: $2,000 
Potential authorship.
6. WINNER LICENSE TYPE

 Open Source, MIT. For additional winner's obligations, see Section 8.4.
7. DATA ACCESS AND USE

 Competition Use and Non-Commercial & Academic Research

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

2. You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

b. Data Security. 

1. You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.

####5. WINNER LICENSE 

a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

2. Open Source: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org] (http://www.opensource.org)) that in no event limits commercial use of such code or model containing or depending on such code. 

3. For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the license in the preceding Section for that software. 

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.
 
####6. EXTERNAL DATA AND TOOLS

a. You may use data other than the Competition Data (“External Data”) to develop and test your Submissions. However, you will ensure the External Data is either publicly available and equally accessible to use by all Participants of the Competition for purposes of the competition at no cost to the other Participants, or satisfies the Reasonableness criteria as outlined in Section 2.6.b below. The ability to use External Data under this Section does not limit your other obligations under these Competition Rules, including but not limited to Section 2.8 (Winners Obligations). 

b. The use of external data and models is acceptable unless specifically prohibited by the Host. Because of the potential costs or restrictions (e.g., “geo restrictions”) associated with obtaining rights to use external data or certain software and associated tools, their use must be “reasonably accessible to all” and of “minimal cost”. Also, regardless of the cost challenges as they might affect all Participants during the course of the competition, the costs of potentially procuring a license for software used to generate a Submission, must also be considered. The Host will employ an assessment of whether or not the following criteria can exclude the use of the particular LLM, data set(s), or tool(s):

1. Are Participants being excluded from a competition because of the "excessive" costs for access to certain LLMs, external data, or tools that might be used by other Participants. The Host will assess the excessive cost concern by applying a “Reasonableness” standard (the “Reasonableness Standard”). The Reasonableness Standard will be determined and applied by the Host in light of things like cost thresholds and accessibility.

2. By way of example only, a small subscription charge to use additional elements of a large language model such as Gemini Advanced are acceptable if meeting the Reasonableness Standard of Sec. 8.2. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

c. Automated Machine Learning Tools (“AMLT”)

1. Individual Participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google toML, H2O Driverless AI, etc.) to create a Submission, provided that the Participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules. 

####7. ELIGIBILITY

a. Unless otherwise stated in the Competition-Specific Rules above or prohibited by internal policies of the Competition Entities, employees, interns, contractors, officers and directors of Competition Entities may enter and participate in the Competition, but are not eligible to win any Prizes. "Competition Entities" means the Competition Sponsor, Kaggle Inc., and their respective parent companies, subsidiaries and affiliates. If you are such a Participant from a Competition Entity, you are subject to all applicable internal policies of your employer with respect to your participation.

####8. WINNER’S OBLIGATIONS

a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:

1. Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. The delivered software must put forth a whole sale effort to solve the metadata harmonization problem at the core of this competition and not merely brute force an acceptable solution through an iterative processes. For avoidance of doubt, delivered software code should be as open sourced as possible and include training code, inference code, and a description of the required computational environment. A GitHub repo with documentation of the pipeline and all its code must be provided to the competition hosts to be eligible for prize money.  

a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).” 

b. Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules,

2. Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;

3. Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).

####9. GOVERNING LAW

a. Unless otherwise provided in the Competition Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.


<a id="s005"></a>
## S005

- **source_id:** harmonizing-the-data-of-your-data:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/abstract
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/4/text`

Scientific progress increasingly depends on our ability to turn published knowledge into structured, machine-readable data. While computational power continues to grow, the real bottleneck lies in the unstructured text of millions of scientific papers, where essential experimental details—sample types, conditions, and analytical methods—are buried in natural language.

Across the life sciences, these details are captured in a standardized metadata format called the Sample and Data Relationship Format (SDRF), which describes how samples are related to data files and experimental outcomes. SDRF has become a cornerstone for making datasets reusable across multiple omics domains, including genomics, transcriptomics, and proteomics. Yet, most published studies still lack complete or consistent SDRF annotations, preventing large-scale data integration and AI-driven discovery.

Proteins carry out most of the functions in cells, from catalyzing biochemical reactions to providing structure, signaling, and regulation. Understanding proteins reveals how biological systems work and enables advances in medicine, biotechnology, and our understanding of disease. The study of proteins and their functions is known as proteomics. In this competition you will build text mining systems that can read scientific papers and automatically generate accurate SDRF metadata. Using proteomics data as the primary use case, your models will extract structured experimental information from text, transforming narrative descriptions into standardized, computable data. A successful solution won’t just advance proteomics: it will create tools and methods with the potential to accelerate data reuse and knowledge synthesis across the entire life sciences ecosystem.

https://github.com/NCEMS/Kaggle-Harmonizing-the-data-of-your-data

## ** FINAL RANKING RELEASE **
Thank you for your patients. Here is the top 5 scoring teams from the competition along with an explanation of final scoring. 

| Team Name | Final Score | Final Rank |  
| --------- | ----------- | ---------- | 
| Jason Karpeles | 0.664699 | 1 | 
| prometio-group | 0.639313 | 2 | 
| Rohan_vinaik | 0.609268 | 3 | 
| DKMgroup | 0.578794 | 4 | 
| Automatica | 0.568274 | 5 |  
  
  
#### *Explanation of final scoring*   
- The top 10 candidates from the private leaderboard that made a final submission where eligable for the final re-scoring used to select the best performing pipelines. 
- The same scoring functions were used as during the competition but with two important modifications:
1. The fuzzy matching threshold for certain quantiative metadata categories was increased to 0.90 as we found during manual inspect a fair amount of false positives due to accepting 1000 uM as the same as 10 uM for example. 
    - `Comment[GradientTime]`
    - `Characteristics[Time]`
    - `Characteristics[Temperature]`
    - `Characteristics[SamplingTime]`
    - `Comment[PrecursorMassTolerance]`
    - `Comment[FragmentMassTolerance]`
    - `Comment[FlowRateChromatogram]`
2. The default fuzzy matching threshold for the rest of the categories was decreased to 0.5 to accomedate the more naturally variable categories and reduce some false negatives. 
3. After re-scoring using the adaptive threshold the results were manually inspected by an internal NCEMS staff scientist with 10 years of experience in the mass spectrometry proteomics field.
    - Both free text and ontology notation were accepted 


<a id="s006"></a>
## S006

- **source_id:** harmonizing-the-data-of-your-data:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/foundational-rules
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/5/text`

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

- **source_id:** harmonizing-the-data-of-your-data:page:6:Sponsors
- **page_name:** Sponsors
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/Sponsors
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/6/text`

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F19243414%2F3b1bf317f79f29fa40f950897a31438d%2FNCEMS%20Logo%201.svg?generation=1768577923940031&alt=media)  
NSF National Center for the Emergence of Molecular and Cellular Sciences (NSF-NCEMS) is catalyzing multidisciplinary scientific teams to leverage AI and data science to synthesize a myriad of publicly available data to answer the most fundamental questions in molecular and cellular biology, stimulating novel questions, answering long-standing mysteries, recruiting the best talent, and training the next-generation workforce of data savvy scientist, all while following gold standard science practices.
  
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F19243414%2Fff95910f039713b48a2e86fa9f939147%2FICDS%20preferred%20mark%20-%20for%20white%20or%20light%20colored%20background%20-%20PSU_CDS_RGB_2C%20(1).png?generation=1769823718725550&alt=media)
NCEMS would like to acknowledge support provided by the Penn State Institute for Computational and Data Sciences  (RRID:SCR_025154). As an interdisciplinary research institute, ICDS brings researchers together to develop and apply innovative, high performance computation methods. ICDS provides the Penn State research community with high performance computing infrastructure including the Roar supercomputer.
  
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F19243414%2F14debbcc306604440c43416d7eecab33%2Fhuck-logo.png?generation=1769175093078478&alt=media)  
NCEMS would like to acknowledge support provided by the The Huck Institutes of the Life Sciences which supports this competition through its commitment to advancing data-driven discovery in the life sciences.


<a id="s008"></a>
## S008

- **source_id:** harmonizing-the-data-of-your-data:page:7:Prizes
- **page_name:** Prizes
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/overview/Prizes
- **retrieved_at:** 2026-10-13T13:20:49.116518+00:00
- **Archive locator:** `/sources/7/text`

Total Prizes Available: $10,000
- **1st Place** - $5,000
- **2nd Place** - $3,000
- **3rd Place** - $2,000

Co-authorship on any papers results from the direct incorporation of a winning model or pipeline can be discussed. 


<a id="s009"></a>
## S009

- **source_id:** harmonizing-the-data-of-your-data:thread:670893:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/670893
- **thread_id:** 670893
- **comment_id:** opening
- **author_name:** Daniel Hernández Mota
- **author_role:** unknown
- **created_at:** 2026-01-30T04:14:26.434Z
- **retrieved_at:** 2026-10-13T13:22:10.680158+00:00
- **Archive locator:** `/sources/8/text`

Accessing information on the SDRF_Proteomics_Specification_v1.0.0.pdf 

Hello! I’m getting familiar with the project data and was looking for details on the specific annotation types. Unfortunately, the link provided doesn’t seem to be working.

Would someone be able to share the PDF or an updated link? Thanks!


<a id="s010"></a>
## S010

- **source_id:** harmonizing-the-data-of-your-data:thread:670893:3399261
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/670893#comment-3399261
- **thread_id:** 670893
- **comment_id:** 3399261
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-01-30T14:21:00.257Z
- **retrieved_at:** 2026-10-13T13:22:10.680158+00:00
- **Archive locator:** `/sources/9/text`

Hello, 

I will update the link later today. Apologies for the confusion. 

You can find that document here: [https://drive.google.com/file/d/1O-LVFbR_hpvIeAnU3z2JV2uoDZ39qP29/view?usp=sharing](https://drive.google.com/file/d/1O-LVFbR_hpvIeAnU3z2JV2uoDZ39qP29/view?usp=sharing)


<a id="s011"></a>
## S011

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908
- **thread_id:** 674908
- **comment_id:** opening
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-02-22T17:59:56.498Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/10/text`

Scoring Script Update (part 2)

We've identified and fixed a critical bug in our SDRF F1 scoring metric that was inflating contestant scores. All future submissions will be evaluated with the corrected metric.

What Has Changed.

Previous behavior:

Only evaluated metadata columns that appeared in both the solution and  submission files. Missing columns were silently ignored.

New behavior:

Evaluates all columns present in the solution, whether or not they appear in the submission. Missing columns in submissions are now correctly penalized.    

Re-scoring.

We have completed the re-scoring of the leader-board. If you believe there is an issue with your re-score please don't hesitate to reach out 😄


<a id="s012"></a>
## S012

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:3431347
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908#comment-3431347
- **thread_id:** 674908
- **comment_id:** 3431347
- **author_name:** akm4224
- **author_role:** unknown
- **created_at:** 2026-03-30T00:20:25.587Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/11/text`

Hi,

I would like to ask if it is allowed to use external LLM APIs (such as Claude, GPT, etc.) in this competition.
Also, does it matter whether the API is free or paid?

Thank you.


<a id="s013"></a>
## S013

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:3431631
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908#comment-3431631
- **thread_id:** 674908
- **comment_id:** 3431631
- **parent_comment_id:** 3431347
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-03-30T12:21:17.993Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/12/text`

You can use external LLM API calls! Paid or free does not matter in the final assessment, just what ever the best tool for the job is : )


<a id="s014"></a>
## S014

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:3431633
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908#comment-3431633
- **thread_id:** 674908
- **comment_id:** 3431633
- **parent_comment_id:** 3431631
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-03-30T12:23:35.940Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/13/text`

Please just make sure to specify which model you call, how you call it, and what prompts and parameters are used in detail.


<a id="s015"></a>
## S015

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:3409457
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908#comment-3409457
- **thread_id:** 674908
- **comment_id:** 3409457
- **author_name:** Yuyajk
- **author_role:** unknown
- **created_at:** 2026-02-23T01:19:41.673Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/14/text`

Hi, Thank you for holding such a great competition.

I have a question about re-scoring.
I submitted now the exact same file that was scored 0.17.. yesterday and it was scored 0.037… now.

My LB score is based on that file, so I guess My LB score should be more lower(sadly).

Is there any possibility some files weren't re-scored?

Thanks,


<a id="s016"></a>
## S016

- **source_id:** harmonizing-the-data-of-your-data:thread:674908:3413760
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/674908#comment-3413760
- **thread_id:** 674908
- **comment_id:** 3413760
- **parent_comment_id:** 3409457
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-02-25T05:59:01.343Z
- **retrieved_at:** 2026-10-13T13:21:16.366353+00:00
- **Archive locator:** `/sources/15/text`

Thanks for reaching out and apologies for the delayed response! 

I just tried re-scoring all of your submissions so give it 20 min and then check again. 

Also thank you for your participation and let me know if there is anything else I can help with.


<a id="s017"></a>
## S017

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135
- **thread_id:** 680135
- **comment_id:** opening
- **author_name:** Serge Panchenko
- **author_role:** unknown
- **created_at:** 2026-03-05T23:45:18.676Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/16/text`

Is there a format difference in test solution SDRFs?

Hello,

I am experiencing a significant gap between my tests local evaluation score (~0.47, computed against the training SDRFs) and my leaderboard score (~0.13). And I'm trying to understand whether this gap is caused by differences in the format/content of the test solution SDRFs compared to the training SDRFs.

Specifically, I would like to ask:

- Are the test solution SDRFs formatted in the same way as the training SDRFs provided in the competition data (i.e., using Characteristics[…] / Comment[…] column wrappers, lowercase organism names, AC=…;NT=… ontology terms for Instrument and CleavageAgent, etc.)?

- For columns like Comment[Instrument] and Characteristics[CleavageAgent], should submissions use full ontology terms (e.g. AC=MS:1001911;NT=Q Exactive) or plain text spans from the publication?

- Is there a sample row from the test solution (even a partially filled example) that i could use to verify my output format?

I suspect a format mismatch may be responsible for the low score..

Thank you very much for your time.

Best regards


<a id="s018"></a>
## S018

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3419753
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3419753
- **thread_id:** 680135
- **comment_id:** 3419753
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-03-11T16:18:54.763Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/17/text`

Hello Serge,

Apologies for the delayed response. I needed to get clarification from Kaggle on their competition closing policies.

**Are the test solution SDRFs formatted in the same way as the training SDRFs provided in the competition data (i.e., using Characteristics[…] / Comment[…] column wrappers, lowercase organism names, AC=…;NT=… ontology terms for Instrument and CleavageAgent, etc.)?**
No. The solutions are formatted in the same way as the SampleSubmission.csv. The training and test sets use the same controlled vocabulary. So all unique metadata categories present in the training set will be in the test set. But one set may have duplicate correct annotations for a given metadata category for a given sample and thus have columns like such:
Characteristic[Modification]
Characteristic[Modification].1
Characteristic[Modification].2

**For columns like Comment[Instrument] and Characteristics[CleavageAgent], should submissions use full ontology terms (e.g. AC=MS:1001911;NT=Q Exactive) or plain text spans from the publication?**
Use the text spans if found in (or inferred from) the publication or if you used an outside publicly available source (that meets the competition standards) to identify the ontology you can supply the NT= part of the ontology as that is what the scoring function will pull).

When the final scoring occurs after the competition ends we will make sure to accept both free text and or ontology terms. Keep in mind that some metadata will most likely need to be inferred from the text and may not be exactly matching what is in the text provided. 

You don't necessarily need to be in the top 3 ranks of the public leader board to be eligible to win once the competition closes. We will take those teams that have submitted their pipelines/models to the GitHub repo [Kaggle-Harmonizing-the-data-of-your-data](https://github.com/NCEMS/Kaggle-Harmonizing-the-data-of-your-data) and review and score their results internally before releaseing the final winners. 

**Is there a sample row from the test solution (even a partially filled example) that i could use to verify my output format?**
Unfortunately giving away one row will more than likely give away a whole publication as in most experiments many samples share the same metadata. Since we dealing with such a small set of papers in the hold out dataset I would prefer not to release it at this moment.


<a id="s019"></a>
## S019

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3420378
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3420378
- **thread_id:** 680135
- **comment_id:** 3420378
- **parent_comment_id:** 3419753
- **author_name:** cg
- **author_role:** unknown
- **created_at:** 2026-03-13T06:14:38.343Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/18/text`

Is it necessary to submit to github to be eligible for the reward? Also, can you share how to format values for each column?


<a id="s020"></a>
## S020

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3421589
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3421589
- **thread_id:** 680135
- **comment_id:** 3421589
- **parent_comment_id:** 3420378
- **author_name:** aggelos papadopoulos
- **author_role:** unknown
- **created_at:** 2026-03-15T21:56:39.180Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/19/text`

There is also Option 1: Submit via Kaggle (Zip File)


<a id="s021"></a>
## S021

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3422259
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3422259
- **thread_id:** 680135
- **comment_id:** 3422259
- **parent_comment_id:** 3420378
- **author_name:** Wout Bittremieux
- **author_role:** unknown
- **created_at:** 2026-03-17T10:28:16.153Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/20/text`

As Aggelos mentioned, you can also submit a zip file via Kaggle. Please check the instructions, directory layout, etc., on the Overview page.

Note that in order to be eligible for a prize, the final model's code must be submitted and results must be reproducible. See the rules, section 8. We will of course work together with the submitting teams to clarify any issues, in case of specific runtime or reproducibility challenges.


<a id="s022"></a>
## S022

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3422260
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3422260
- **thread_id:** 680135
- **comment_id:** 3422260
- **parent_comment_id:** 3420378
- **author_name:** Wout Bittremieux
- **author_role:** unknown
- **created_at:** 2026-03-17T10:30:02.260Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/21/text`

See above for how to format values for each column. Together with the competition data, this should provide the relevant information to correctly structure your submissions.


<a id="s023"></a>
## S023

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3423038
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3423038
- **thread_id:** 680135
- **comment_id:** 3423038
- **parent_comment_id:** 3420378
- **author_name:** cg
- **author_role:** unknown
- **created_at:** 2026-03-18T05:33:03.800Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/22/text`

Is the test dataset divided by pxds or columns? There are some columns that appear to be correct on manual check but the score does not seem to increase. The Instrument col is one such column.


<a id="s024"></a>
## S024

- **source_id:** harmonizing-the-data-of-your-data:thread:680135:3423327
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/680135#comment-3423327
- **thread_id:** 680135
- **comment_id:** 3423327
- **parent_comment_id:** 3420378
- **author_name:** Wout Bittremieux
- **author_role:** unknown
- **created_at:** 2026-03-18T12:41:39.147Z
- **retrieved_at:** 2026-10-13T13:21:43.410784+00:00
- **Archive locator:** `/sources/23/text`

The test data consists of unseen PXDs.


<a id="s025"></a>
## S025

- **source_id:** harmonizing-the-data-of-your-data:thread:683992:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/683992
- **thread_id:** 683992
- **comment_id:** opening
- **author_name:** Todd Gardiner
- **author_role:** unknown
- **created_at:** 2026-03-23T09:55:14.812Z
- **retrieved_at:** 2026-10-13T13:21:32.603474+00:00
- **Archive locator:** `/sources/24/text`

Two Expectation Asks + Deciphering Datasets Competitors Might Need

Some questions regarding output expectations have established during EDA:

- Is a proper attribution of the NT argument enough to be classified as correct by the scoring mechanism? Or would we need a correct Accession number attribution as well?

- When an abstract fails to give us a specific (i.e. age of 80years isn't mentioned in PXD010603 texts) are guesses of 70Y partially scored positively?

Bonus: Data Scientists outside the Proteomic Niche will need the following to have a chance matching words to the training data:

- [mzldentML](https://github.com/HUPO-PSI/mzIdentML/blob/2aacf89e164afc96f71dee7e433c055718d7db0d/specification_document-releases/specdoc1_3/mzIdentML1.3.0-release.pdf?raw=true) - AKA the key to the MS:####### items in the SDRFs.

- [PRIDE Ontology](https://github.com/PRIDE-Archive/pride-ontology/blob/master/pride_cv.obo) - AKA the key to the definitions of the PRIDE:####### items in the SDRFs.

- [UNIMOD](https://www.ebi.ac.uk/ols4/ontologies/unimod?viewMode=list&tab=classes) - AKA the key to the definitions of the UNIMOD:#### items in the SDRFs.

- AC = Accession Number (from 1, 2, & 3)

- NT = Name Tag (from 1, 2, & 3)

- SILAC = Stable Isotope Labeling by Amino Acids in Cell Culture  (example -> K:12C(6)14N(2) = lysine containing 6 carbon-12 atoms and 2 nitrogen-14 atoms)

Why did I write the bonus? To encourage more participants and ask the relevant experts to weigh in on the accuracy of what I've learned. Proteomics are outside of my intellectual comfort zone.


<a id="s026"></a>
## S026

- **source_id:** harmonizing-the-data-of-your-data:thread:683992:3429317
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/683992#comment-3429317
- **thread_id:** 683992
- **comment_id:** 3429317
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-03-26T15:58:16.917Z
- **retrieved_at:** 2026-10-13T13:21:32.603474+00:00
- **Archive locator:** `/sources/25/text`

Hi Todd,

Here are some answers to your questions.

**Is a proper attribution of the NT argument enough to be classified as correct by the scoring mechanism? Or would we need a correct Accession number attribution as well?**

Yes the proper attribution of NT is enough. 
After the competition closes the top leader-board contenders will be re-scored by both the traditional fuzzy matching scheme present in this competition and then followed up by review with our in-house proteomics experts. We hope this will give non-experts who may have a novel approach to this problem more incentive to submit. It will also allow for both free-text and ontological annotations to count for a specific field.

**When an abstract fails to give us a specific (i.e. age of 80years isn't mentioned in PXD010603 texts) are guesses of 70Y partially scored positively?**

In short there is no partial scoring in this context. 

Thanks for the bonus!


<a id="s027"></a>
## S027

- **source_id:** harmonizing-the-data-of-your-data:thread:683992:3429721
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/683992#comment-3429721
- **thread_id:** 683992
- **comment_id:** 3429721
- **parent_comment_id:** 3429317
- **author_name:** Todd Gardiner
- **author_role:** unknown
- **created_at:** 2026-03-27T06:38:57.590Z
- **retrieved_at:** 2026-10-13T13:21:32.603474+00:00
- **Archive locator:** `/sources/26/text`

Thank you for the clarification.


<a id="s028"></a>
## S028

- **source_id:** harmonizing-the-data-of-your-data:thread:686554:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/686554
- **thread_id:** 686554
- **comment_id:** opening
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-03-31T17:49:50.243Z
- **retrieved_at:** 2026-10-13T13:21:10.746511+00:00
- **Archive locator:** `/sources/27/text`

IMPORTANT - FINAL SUBMISSION INFORMATION

As the competition comes to a close please remember to visit the How to Submit sections on the Overview page to learn how to submit your final submission package via either the Kaggle portal or a GitHub pull request.

In accordance with Kaggle rules we will release the 3 finalist winners after we verify the solutions and approach of each participants final submission package. 

Please make sure you are familiar with the Winner's Obligation section of the Rules page. 

`8. WINNER’S OBLIGATIONS  
a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:  

    Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. The delivered software must put forth a whole sale effort to solve the metadata harmonization problem at the core of this competition and not merely brute force an acceptable solution through an iterative processes. For avoidance of doubt, delivered software code should be as open sourced as possible and include training code, inference code, and a description of the required computational environment. A GitHub repo with documentation of the pipeline and all its code must be provided to the competition hosts to be eligible for prize money.  

a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).”  

b. Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules,  

    Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;  

    Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).
`


<a id="s029"></a>
## S029

- **source_id:** harmonizing-the-data-of-your-data:thread:688827:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/688827
- **thread_id:** 688827
- **comment_id:** opening
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-04-07T02:17:46.514Z
- **retrieved_at:** 2026-10-13T13:21:05.307643+00:00
- **Archive locator:** `/sources/28/text`

IMPORTANT ANNOUNCEMENT REGARDING FINAL RANKING RELEASE

Thank you to all participants for your contributions to the Harmonizing the Data of your Data competition.

Due to the complexity of the evaluation process and the need to verify submissions against the competition rules and scoring criteria, final adjudication is still in progress.

Please note that any automated emails from Kaggle reflect preliminary leaderboard standings and do not constitute final winner selection.

**The final winners have been contacted via the Kaggle email system**

Once all winners have responded to the email and verified their eligibility we will release their team names here.


<a id="s030"></a>
## S030

- **source_id:** harmonizing-the-data-of-your-data:thread:694356:opening
- **url:** https://www.kaggle.com/competitions/harmonizing-the-data-of-your-data/discussion/694356
- **thread_id:** 694356
- **comment_id:** opening
- **author_name:** Ian Sitarik
- **author_role:** unknown
- **created_at:** 2026-04-24T13:35:48.560Z
- **retrieved_at:** 2026-10-13T13:20:59.796194+00:00
- **Archive locator:** `/sources/29/text`

FINAL RANKING RELEASE

Thank you for your patients. Here is the top 5 scoring teams from the competition along with an explanation of final scoring. 

Team Name
Final Score
Final Rank

Jason Karpeles
0.664699
1

prometio-group
0.639313
2

Rohan_vinaik
0.609268
3

DKMgroup
0.578794
4

Automatica
0.568274
5

Explanation of final scoring

- The top 10 candidates from the private leaderboard that made a final submission where eligable for the final re-scoring used to select the best performing pipelines. 

- The same scoring functions were used as during the competition but with two important modifications:

- The fuzzy matching threshold for certain quantiative metadata categories was increased to 0.90 as we found during manual inspect a fair amount of false positives due to accepting 1000 uM as the same as 10 uM for example. 

- `Comment[GradientTime]`

- `Characteristics[Time]`

- `Characteristics[Temperature]`

- `Characteristics[SamplingTime]`

- `Comment[PrecursorMassTolerance]`

- `Comment[FragmentMassTolerance]`

- `Comment[FlowRateChromatogram]`

- The default fuzzy matching threshold for the rest of the categories was decreased to 0.5 to accomedate the more naturally variable categories and reduce some false negatives. 

- After re-scoring using the adaptive threshold the results were manually inspected by an internal NCEMS staff scientist with 10 years of experience in the mass spectrometry proteomics field.

- Both free text and ontology notation were accepted

