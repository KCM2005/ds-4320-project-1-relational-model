# Headline
Insulin Management Insights: Analysis Reveals Link Between Insulin Usage and 30-day Readmissions

## Hook
Is Your Insulin Usage Plan Working? New analysis uncovers the key to reducing hospital readmissions.

## Problem Statement
Hospital readmissions are a persistent challenge for adult American diabetic patients, often signaling that critical aspects of their care need refinement (Ostling et al, 2017). While many factors contribute to these readmissions, insulin usage often holds the key to preventing 30-day risk hospital readmissions (American Diabetes Association, 2018). When insulin usage and management are not optimized, blood sugar levels can become unstable, leading to a cascade of complications that necessitate hospital readmissions within 30 days or more. Therefore, the specific problem statement “Analyzing the 30-day risk of hospital readmission for adult American diabetic patients based on their insulin usage patterns” can help identify high-risk patients, enabling targeted interventions and improved outcomes.

References: 
Ostling S, Wyckoff J, Ciarkowski SL, Pai CW, Choe HM, Bahl V, et al. (2017). The relationship between diabetes mellitus and 30-day readmission rates.  Clinical Diabetes and Endocrinology, Vol 3, Issue 3. https://link.springer.com/content/pdf/10.1186/s40842-016-0040-x.pdf. Accessed 12 March, 2026.

American Diabetes Association (ADA). (2018). Economic Costs of Diabetes.Diabetes Care, 41(5), 917-928. https://pubmed.ncbi.nlm.nih.gov/29567642/. Accessed 12 Mar, 2026.


## Solution Description
This analysis examined a dataset of 101,766 diabetic patients from 130 US hospitals to assess the relationship between 30-day hospital readmission risk and insulin use patterns (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008). At a high level, the analysis was conducted by comparing proportions of 30-day hospital readmissions across different categories of insulin usage (Down, No, Steady, Up), which were then visualized on a bar chart as shown in Figure 1. The following are the key findings and potential insights into the relationship between insulin usage and the 30-day hospital readmission for diabetic patients: (a) The "Down" Insulin Usage patients have the lowest 30-day readmission rate (4.5%). This could indicate that patients are perhaps stabilizing, or their diabetes is in a less severe phase, or that they have different care pathways or discharge instructions. (b) The "No" Insulin Usage patients have a higher 30-day readmission risk (12.6%). This could mean that patients have poorly controlled diabetes where insulin therapy is either not yet prescribed or they are non-compliant with prescribed insulin, thus increasing their risk of hospital readmission within the critical 30-day period. (c) The "Steady" Insulin Usage patients have a moderate within 30-day readmission rate (7.4%). This could suggest that while their diabetes is being managed with a consistent insulin dose, there are still factors contributing to readmissions, such as comorbidities, lifestyle, or other aspects of their treatment not captured in this specific data. (d) To the contrary, the "Up" Insulin Usage patients have an equal and striking distribution (33%) for readmission within 30 days, after 30 days, and those not readmitted. This striking outcome could imply that patients may be in a more advanced stage of their disease or developing other complications that require more intensive management, warranting readmissions both within and beyond 30 days, as well as survival without readmission. 

## Chart
Visualization is linked in data folder of the repository
