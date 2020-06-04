# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
# In the column Gender, replace '-' with 'Agender' using "replace()" function

data['Gender'].replace('-','Agender', inplace= True)
gender_count = data['Gender'].value_counts()
print(gender_count)

#ploting a graph with proper labels.
plt.bar(gender_count.index,gender_count)
plt.show()

# Next check does good overpower evil or does evil overwhelm good?
# storing the value count of 'Aligment'

aligments = data.Alignment.value_counts()

# setting the figure size

plt.figure(figsize=(6,6))

#plotting the pie chart for 'Aligment'

plt.pie(aligments,labels=aligments.index,explode = (0.05,0.05,0.05),autopct = '%1.1f %%')

#setting the pie chart title

plt.title('character aligment')

#subsetting the data with columns

sc_df = data[['Strength','Combat']].copy()

#finding the covariance between 'strength' and 'combat'.

sc_covariance = sc_df.cov().iloc[0,1]

#finding the std dev of 'strength'

sc_strength = sc_df['Strength'].std()

#finding the std dev of 'combat'

sc_combat = sc_df['Combat'].std()


# calculating the pearson's correlaton between 'strength' and 'combat'

sc_pearson = sc_covariance/(sc_combat*sc_strength)

print('Pearson\'s correlation coefficient between strength and combat :', sc_pearson)


#subsetting the data with columns

ic_df = data[['Intelligence','Combat']].copy()

#finding the covariance between 'intelligence' and 'combat'.

ic_covariance = ic_df.cov().iloc[0,1]


#finding the std dev of 'intelligence'.

ic_intelligence = ic_df['Intelligence'].std()

#finding the std dev of 'combat'

ic_combat = ic_df['Combat'].std()

# calculating the pearson's correlaton between 'intelligence' and 'combat'

ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print('Pearson\'s correlation coefficient between intellignce and combat : ', ic_pearson)

# find the quantile = 0.99 for the 'Total' column .

total_high = data['Total'].quantile(q=0.99)

#subsetting the dataframe based on 'total_high'.

super_best =data[data['Total']>total_high]

# creating a list of 'Name' associated with the 'super_best' dataframe

super_best_names = list(super_best['Name'])

#printing the names
print(super_best_names)

#setting up the subplots

fig, (ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize=(20,8))

#plotting box plot

ax_1.boxplot(super_best['Intelligence'])

#setting the subplot axis title
ax_1.set(title='Intelligence')


#plotting box plot

ax_2.boxplot(super_best['Speed'])

#setting the subplot axis title
ax_2.set(title='Speed')

#plotting box plot

ax_3.boxplot(super_best['Power'])

#setting the subplot axis title
ax_3.set(title='Power')












