# DS 4320 Project 1: Predicting Hospital Readmission Risk
Repository for DS 4320 Project 1

# Executive Summary
Hospital readmissions represent a significant challenge in the care of American diabetic patients, often indicating gaps in treatment and management. This analysis delves into the critical role of insulin usage patterns in predicting 30-day hospital readmissions among this population. The analysis reveals insights into insulin usage and 30-day hospital readmission risk for diabetic patients. Patients with decreasing ("Down") insulin usage have the lowest readmission rate (4.5%), suggesting stable diabetes management. Those with "No" insulin usage have a higher risk (12.6%), potentially indicating poor control or non-compliance. Patients with "Steady" insulin usage have a moderate risk (7.4%), implying managed diabetes, but with other contributing factors like comorbidities. Patients with increasing ("Up") insulin usage show a complex profile, with equal likelihood of readmission within 30 days, after 30 days, or no readmission, suggesting advanced disease or complications. The key takeaways are: "Down" insulin usage is linked to lower risk, "No" insulin to higher risk, "Steady" insulin to moderate risk, and "Up" insulin usage to complex patient profiles.

# Name
Kalenga Mumba

# NetID
kew6jk

# DOI
[Project 1 - DOI](https://doi.org/10.5281/zenodo.19323230)

# Press release
[Press release](https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/Press_Release.md)

# Data
[Data folder](https://github.com/KCM2005/ds-4320-project-1-relational-model/tree/main/data)

# Pipeline
[Pipeline files](https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/readmission_risk.py)

# License
MIT License
https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/LICENSE

## Problem Definition
Initial General Problem: Predicting hospital readmission risk

Refined Specific Problem: Analyzing the 30-day risk of hospital readmission for American diabetic patients based on their insulin usage patterns.

## Rationale for refinement
The refined problem statement is highly relevant because it addresses a significant healthcare challenge with a focused approach. Diabetic patients, regardless of age, are a demographic known to have a higher risk of hospital readmissions due to the chronic nature of diabetes and its associated complications. Focusing on the critical 30-day readmission risk allows for timely interventions and aligns with key healthcare quality metrics. By analyzing insulin usage patterns, a fundamental aspect of diabetes management, the problem enables the development of precise predictive models. This specificity is crucial for implementing targeted interventions and improving patient care, ultimately aiming to reduce costly hospital readmissions across a broad patient population.

## Motivation
The motivation for this refined problem stems from the significant burden of diabetes on individuals and the healthcare system, coupled with the high rates of hospital readmissions among diabetic patients. Diabetes is a chronic condition often complicated by comorbidities like cardiovascular disease, kidney disease, and obesity, leading to hospitalizations. Reducing these readmissions is not only a matter of improving patient outcomes and quality of life by preventing complications and ensuring continuity of care, but also a significant economic imperative. Therefore, developing a precise model to identify diabetic patients at high risk of readmission can drive the implementation of proactive care management, patient education, and post-discharge support, leading to better health outcomes and a more efficient healthcare system.

## Headline of Press Release and link to press release
Headline: "Insulin Management Insights: Analysis Reveals Link Between Insulin Usage and 30-day Readmissions."
Link: https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/Press_Release.md


## Terminology of KPIs
| **Term / KPI**           | **Description**                                               | **Relevance to Domain**                                                     |
| ------------------------ | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| encounter_id             | Unique identifier for a hospital encounter or visit           | Helps track individual patient visits and link to outcomes like readmission |
| patient_nbr              | Unique identifier for each patient                            | Allows tracking patient history and longitudinal analysis                   |
| race                     | Patient’s self-reported race                                  | Important for studying disparities in care and outcomes                     |
| gender                   | Patient’s gender                                              | Used to analyze demographic differences in treatment and outcomes           |
| age                      | Patient age group                                             | Age is a major factor in diabetes management and risk of complications      |
| admission_type_id        | Type of admission (e.g., emergency, elective)                 | Indicates urgency and can correlate with length of stay or readmission risk |
| discharge_disposition_id | Type of discharge (e.g., home, transferred, deceased)         | Relevant for post-hospitalization planning and outcomes                     |
| admission_source_id      | Where the patient came from before admission                  | Helps understand care pathways and referral patterns                        |
| time_in_hospital         | Number of days spent in hospital during encounter             | KPI for resource utilization and severity of condition                      |
| payer_code               | Insurance payer code                                          | Used to study financial aspects and disparities in access to care           |
| medical_specialty        | Specialty of the admitting physician                          | May affect treatment plans and patient outcomes                             |
| num_lab_procedures       | Number of lab tests performed                                 | Reflects intensity of monitoring and care                                   |
| num_procedures           | Number of procedures performed                                | Reflects complexity of care                                                 |
| num_medications          | Number of medications prescribed                              | High counts can indicate multimorbidity or complex treatment                |
| number_outpatient        | Number of outpatient visits in past year                      | Indicates chronic care usage and disease management                         |
| number_emergency         | Number of emergency visits in past year                       | High counts can signal poor disease control or lack of access               |
| number_inpatient         | Number of prior inpatient stays                               | Predictor of readmission risk and healthcare burden                         |
| diag_1                   | Primary diagnosis code for encounter                          | Identifies main reason for admission, used in outcome modeling              |
| diag_2                   | Secondary diagnosis code                                      | Captures comorbidities influencing care complexity                          |
| diag_3                   | Tertiary diagnosis code                                       | Further captures comorbidities and risk factors                             |
| number_diagnoses         | Total number of diagnoses for encounter                       | KPI for patient complexity and multimorbidity                               |
| insulin                  | Whether patient is on insulin therapy                         | Indicator of diabetes severity and treatment type                           |
| change                   | Whether diabetes medication was changed during stay           | Reflects treatment adjustment and clinical decision-making                  |
| diabetesMed              | Whether patient is on any diabetes medication                 | Captures overall treatment status                                           |
| A1Cresult                | Most recent A1C test result category (e.g., normal, >7%, >8%) | Key indicator of blood sugar control, used to monitor diabetes management   |
| readmitted               | Whether patient was readmitted within 30 days              | Key outcome KPI for quality of care and hospital performance                |

## Paragraph explaining the domain
This project lives in the domain of healthcare analytics, specifically predicting readmission risk for diabetic patients. It leverages Electronic Health Record (EHR) data and machine learning to analyze patient demographics (age, gender, race), and analyzes how they relate to hospital admission rates across a number of key performance indicators such as time/days spent in hospital (to capture severity of condition), number of diagnoses (relevant to capture patient complexity and multimorbidity), and readmission occurring within 30 days (relevant to capture quality of care and hospital performance). By identifying patterns in these data, the project aims to predict 30-day readmission risk, enabling targeted interventions like telehealth monitoring to improve patient outcomes.

## Background readings
Folder is in the repo

## Table showing summary of readings
| Title | Brief Description | Link |
|------|------------------|------|
| Economic Costs of Diabetes | The American Diabetes Association (ADA) (2018) estimates the economic burden of diabetes in the United States, including healthcare costs and lost productivity. | https://pubmed.ncbi.nlm.nih.gov/29567642/ |
| Health and Economic Benefits of Diabetes Interventions | The Center for Disease Control (CDC) (2024) highlights the health and economic benefits of diabetes interventions. <br> It emphasizes the importance of prevention and management strategies to reduce the burden of diabetes. | https://www.cdc.gov/nccdphp/priorities/diabetes-interventions.html |
| Economic Costs of Diabetes in the U.S. in 2022 | Parker et al. (2024) estimate the economic costs of diabetes in the U.S. in 2022. <br> The study provides insights into the financial impact of diabetes on the healthcare system. | https://pubmed.ncbi.nlm.nih.gov/37909353/ |
| The Relationship Between Diabetes Mellitus and 30-Day Readmission Rates | Ostling et al. (2017) explore the relationship between diabetes mellitus and 30-day readmission rates. <br> The study highlights the challenges of managing diabetes and preventing hospital readmissions. | https://link.springer.com/content/pdf/10.1186/s40842-016-0040-x.pdf |
| Predicting 30-Day Hospital Readmission in Patients With Diabetes Using Machine Learning on Electronic Health Record Data | Emi-Johnson et al. (2025) use machine learning to predict 30-day hospital readmissions in patients with diabetes. <br> The study leverages electronic health record data to identify high-risk patients. | https://www.cureus.com/articles/358756-predicting-30-day-hospital-readmission-in-patients-with-diabetes-using-machine-learning-on-electronic-health-record-data#!/ |
| Predicting and Validating 30-Day Hospital Readmission in Adults With Diabetes Whose Index Admission Is Diabetes-related | Soh et al. (2022) develop and validate a model to predict 30-day hospital readmission in adults with diabetes. <br> The study focuses on diabetes-related index admissions. | https://pmc.ncbi.nlm.nih.gov/articles/PMC9516045/ |

## Raw data acquisition process (provenance)
The dataset originated from the University of California at Irvine (UCI) Machine Learning Repository website (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008), which contains de-identified data from 130 U.S. hospitals (1999-2008) on diabetic patients, including demographics, diagnoses, medications, and 30-day readmission outcomes. The dataset was formatted into a CSV file, comprising 101, 766 patient encounters.

My refined specific problem for Project 1 is: Predicting the 30-day risk of hospital readmission for American diabetic patients based on their insulin usage patterns. As such, the raw data acquisition process (provenance) involved the following steps. First, I went to the UCI Machine Learning Repository website (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008). Second, I searched for “diabetes” in the search box, and selected “Diabetes130-US Hospitals for Years 1999-2008”. Third, I clicked on the “download” button, and downloaded the dataset consisting of 101,766 records (rows) in CSV format. 

## Code data table
| File / Step                   | Description                                                     | Link / Source     |
| ----------------------------- | --------------------------------------------------------------- | ----------------- |
| diabetics_data.csv          | Original dataset downloaded from online source                  | https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008 |
| clean_data.py               | Cleans missing values, removes duplicates, standardizes columns | https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/clean_data.py               |             |
| demographics.py     | Extracts age, gender, and race for patients                     | https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/demographics.py               |
| readmission_risk.py | Identifies patients at risk of readmission within 30 days       | https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/readmission_risk.py               |
| insulin_usage.py    | Extracts information about patients’ insulin usage              | https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/insulin_usage.py               |
| save_secondary_dataset.py   | Combines all processed data and saves as secondary dataset      | https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/save_secondary_dataset.py              |

## Bias Identification
- Selection bias: Data only includes hospitalized diabetic patients (1999-2008), excluding outpatient cases or those not seeking care.

- Geographic bias: Data is from U.S. hospitals, and may not represent global diabetes patient demographics.

- Time period bias: Data is outdated (from 1999-2008), which may not reflect current diabetes treatment/management practices or patient demographics.

- Measurement bias: Variations in hospital data collection/recording practices across the 130 hospitals may affect data consistency.

- Socioeconomic bias: Limited representation of uninsured or underinsured patients may skew results.

- Data Quality Bias: Missing values and potential errors in data extraction (e.g., during the de-identification process may have removed relevant information) may both impact analysis.

## Bias Mitigation
Selection Bias:
- Weighting: Apply weights to match national diabetes prevalence rates.

Geographic Bias:
- Stratification: Given the 130 hospitals, could be analyzed by location of hospitals or hospital type or hospital size.
   
Time Period Bias:
- Data Augmentation: Incorporate more recent data.

Measurement Bias:
- Data Harmonization: Standardize variables across the 130 hospitals if possible.
- Stratification: Analyze by hospital or data collection practices.

Socioeconomic Bias:
- Weighting: Adjust for insurance status.
- Stratification: Analyze subgroups by socioeconomic factors.

Data Quality Bias:
- Data Validation: Check for inconsistencies and outliers.
- Imputation: Handle missing values appropriately (e.g., multiple imputation).
- Sensitivity Analysis: Assess the impact of missing/de-identified data.

## Rationale 
- Data Inclusion Criteria:

1. Decision: Include all diabetic patients (1999-2008) from all U.S. hospitals.
2. Uncertainty: Excluding some patients (e.g., non-hospitalized) may introduce bias.
3. Mitigation: Apply weighting or data augmentation.

- Variable Selection:

1. Decision: Focus on demographics, insulin usage, time in hospital, and readmission risk.
2. Uncertainty: Omitting relevant variables (e.g., socioeconomic status, insurance) may introduce bias.
3. Mitigation: Include relevant variables if available.

- Handling Missing Data:

1. Decision: Impute missing values.
2. Uncertainty: Imputation methods can introduce uncertainty.
3. Mitigation: Use multiple imputation methods and compare results.

- Modeling Approach:

1. Decision: Choose a model (e.g., logistic regression, random forest).
2. Uncertainty: Model choice can impact results.
3. Mitigation: Compare multiple models and use ensemble methods.

- Generalizability:

1. Decision: Apply model to broader populations.
2. Uncertainty: Geographic and time period biases may limit generalizability.
3. Mitigation: Validate model on external datasets and use data augmentation.

## Schema
[![ER Diagram](ER_Diagram.png)](https://github.com/KCM2005/ds-4320-project-1-relational-model/blob/main/data/figures/ER_Diagram.png)

## Data Table
| File / Step    | Description                                                                   | Link / Source                                                                                                                                                                    |
| -------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| patients.csv   | Contains patient demographic information such as age, gender, and race        | [https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/patients.csv](https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/patients.csv)     |
| encounters.csv | Records of hospital visits, including admission and discharge dates           | [https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/encounters.csv](https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/encounters.csv) |
| treatments.csv | Details of treatments provided during hospital stays, including insulin usage | [https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/treatments.csv](https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/treatments.csv) |
| outcomes.csv   | Tracks patient outcomes, including readmission within 30 or 90 days           | [https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/outcomes.csv](https://github.com/KCM2005/ds-4023-project-1-relational-model/blob/main/outcomes.csv)     |


## Data Dictionary
| Feature Name       | Data Type   | Description                              | Example     |
|--------------------|------------|------------------------------------------|-------------|
| encounter_id       | int        | Unique encounter ID                      | 12345       |
| patient_nbr        | int        | Unique Patient ID                        | 22305       |
| age                | int        | Patient age                              | 30          |
| gender             | string| Patient gender                           | Female      |
| race               | string| Patient race                             | Caucasian   |
| admission_type_id  | int        | Admission Type ID                        | 1           |
| time_in_hospital   | int        | Length of stay (days)                    | 10          |
| insulin            | string| Insulin usage level                      | up          |
| readmitted         | string| Readmission risk (<30, >30, no)          | <30         |

## Data Dictionary - Numerical Features
| Feature Name        | Measure of Uncertainty | Description                              |
|--------------------|-----------------------|------------------------------------------|
| age                | Standard Deviation    | How much patient ages vary from average  |
| time_in_hospital   | Standard Deviation    | How much hospital stay length varies     |
| encounter_id       | N/A                   | A unique identifier that remains constant and does not change within the dataset                      |
| patient_nbr        | N/A                   | A unique identifier that remains constant and does not change within the dataset                        |
| admission_type_id  | N/A                   | A unique identifier that is remains constant and does not change within the dataset                |
