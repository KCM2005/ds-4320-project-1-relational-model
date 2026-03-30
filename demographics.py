import pandas as pd

df = pd.read_csv("cleaned_diabetic_data.csv")

#Age summary
age_summary = df['age'].describe()

#Gender distribution
gender_counts = df['gender'].value_counts()

#Race distribution
race_counts = df['race'].value_counts()

#Show summaries
print(age_summary)
print(gender_counts)
print(race_counts)
