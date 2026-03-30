import matplotlib.pyplot as plt

#Create a cross-tabulation of insulin usage vs readmission status
#normalize='index' converts counts to proportions (row-wise)
insulin_readmit = pd.crosstab(df['insulin'], df['readmitted'], normalize='index')

#Plot a bar chart of readmission proportions by insulin usage
ax = insulin_readmit.plot(kind='bar', rot=1, figsize=(10,6))

#Set chart title
plt.title("The 30-day risk readmission of insulin usage among American diabetic patients")

#Set y-axis label
plt.ylabel("Proportion of Readmissions")

#Set x-axis label
plt.xlabel("Insulin Usage")

#Add legend with title
plt.legend(title="Readmitted")

#Add percentage labels above each bar
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0:
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                height + 0.01,                   
                f"{height*100:.1f}%",             
                ha='center',                     
                va='bottom',                      
                fontsize=8                     
            )

#Show bar chart
plt.show()
