ds-4023-project-1-relational-model/
│
├─ data/
│   ├─ patients.csv        #raw patient demographics
│   ├─ encounters.csv      #raw hospital visit records
│   ├─ treatments.csv      #raw treatment records, including insulin
│   └─ outcomes.csv        #raw patient outcomes
│
├─ scripts/
│   ├─ clean_data.py       #cleans missing values, standardizes columns
│   ├─ demographics.py     #extracts age, gender, race features
│   ├─ insulin_usage.py    #extracts insulin usage info
│   ├─ readmission_risk.py #calculates 30-day readmission risk
│   └─ save_secondary_dataset.py  #merges all processed data into a final dataset
│
├─ output/
│   └─ cleaned_diabetics_data.csv   #the combined, cleaned dataset ready for analysis
│
└─ README.md              #explains the whole project process
