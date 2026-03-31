import matplotlib.pyplot as plt
#Get predicted probabilities for the positive class (<30 readmission)
y_prob = model.predict_proba(X_test)[:, 1]

#Sort probabilities for a clean line plot
y_prob_sorted = sorted(y_prob)

#Add predicted probabilities to test set
test_df = X_test.copy()
test_df['readmitted_binary'] = y_test
test_df['predicted_prob'] = model.predict_proba(X_test)[:, 1]

#Include age and insulin from original dataframe
test_df['age'] = df.loc[test_df.index, 'age']
test_df['insulin'] = df.loc[test_df.index, 'insulin']

#Aggregate mean predicted probability by age and insulin usage
agg_df = test_df.groupby(['age', 'insulin'])['predicted_prob'].mean().reset_index()

plt.figure(figsize=(12,6))

#Plot 
for insulin_type in agg_df['insulin'].unique():
    subset = agg_df[agg_df['insulin'] == insulin_type]
    plt.plot(subset['age'], subset['predicted_prob'], marker='o', linestyle='-', label=insulin_type)

plt.title(f"Predicted 30-Day Readmission Probability by Age and Insulin Usage\nModel Accuracy: {accuracy:.3f}", fontsize=14, fontweight='bold')
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Mean Predicted Probability of Readmission", fontsize=12)
plt.legend(title='Insulin Usage')
plt.tight_layout()
plt.show()
