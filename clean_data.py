import pandas as pd

df = pd.read_csv("diabetic_data.csv")

cols_to_drop = [
    'weight',
    'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide',
    'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
    'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone',
    'tolazamide', 'examide', 'citoglipton', 'glyburide-metformin',
    'glipizide-metformin', 'glimepiride-pioglitazone', 'metformin-rosiglitazone',
    'metformin-pioglitazone',
    'max_glu_serum'
]

df.drop(columns=cols_to_drop, inplace=True)
df.reset_index(drop=True, inplace=True)

df.to_csv("cleaned_diabetic_data.csv", index=False)
