import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("cleaned_diabetic_data.csv")

#Convert target to binary 
df['readmitted_binary'] = df['readmitted'].apply(lambda x: 1 if x == '<30' else 0)

#Features
X = df[['time_in_hospital', 'num_lab_procedures', 'num_medications']]
y = df['readmitted_binary']

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Apply Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

#Summaries
print(df.groupby('age')['insulin'].describe())
print(df.groupby('readmitted')['insulin'].describe())
