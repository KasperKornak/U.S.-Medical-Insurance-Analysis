import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv ('insurance.csv')

#parents with 1 and 2 children
parents = df.loc[(df['children'] == 1) | (df['children'] == 2)]
sns.set_theme(style="whitegrid", palette="pastel")
sns.boxplot(x="children", y="charges",
            hue="sex", palette=["m", "g"],
            data=parents)
sns.despine(offset=10, trim=True)
plt.title('Distribution of charges between 1 and 2 children parents')
plt.show()
plt.close()

maleparents = parents.loc[parents['sex'] == 'male']
sns.boxplot(x="children", y="charges",
            hue="smoker", palette=["m", "g"],
            data=maleparents)
sns.despine(offset=10, trim=True)
plt.title('Distribution of charges between male parents')
plt.show()
plt.close()

non_smoking_males = maleparents.loc[maleparents['smoker'] == 'no']
smoking_males = maleparents.loc[maleparents['smoker'] == 'yes']

print('Non-smoking counts:')
print(non_smoking_males['children'].value_counts())
print('Smoking counts:')
print(smoking_males['children'].value_counts())

#is dad bod related to age or children status?
malefathes_zero = df.loc[(df['children'] == 0) & (df['sex'] == 'male')]
malefathes_more = df.loc[(df['children'] != 0) & (df['sex'] == 'male')]
males_young = df.loc[(df['age'] < 35) & (df['sex'] == 'male')]
males_middle = df.loc[(df['age'] >= 35) & (df['age'] < 50) & (df['sex'] == 'male')]

data = [['Young Males',males_young['bmi'].mean(),'Age Group'],['Middle-Aged Males',males_middle['bmi'].mean(),'Age Group'],['Childrenless Males',malefathes_zero['bmi'].mean(),'Children-count Group'],["Fathers",malefathes_more['bmi'].mean(),'Children-count Group']]
toplot = pd.DataFrame(data,columns=['Who','Average BMI','Group'])

ax = sns.barplot(x="Group",y = "Average BMI", hue="Who", data=toplot)
plt.ylim(ymin=30)
plt.title('Average BMI in two groups of males')
plt.show()
plt.close()

#corelation heatmap
ax = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
plt.title('Correlation heatmap')
plt.show()
plt.close()