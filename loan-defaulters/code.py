# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

# probability p(A)for the event that fico credit score is greater than 700.

p_a = df[df['fico'].astype(float) > 700].shape[0]/df.shape[0]
print(p_a)

# probability p(B)for the event that purpose == 'debt_consolidation'.

p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# create new dataframe for condition purpose == 'debt_consolidation'.
df1=df[df['purpose'] == 'debt_consolidation']

# calculate p(B|A).
 
p_a_b = df1[df1['fico'].astype(float) > 700].shape[0]/df1.shape[0]
print(p_a_b)

result = (p_a == p_a_b)
print(result)

# bayes theorem

# calculate paid.back.loan
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
print(prob_lp)

# calculate credit.policy
 
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
print(prob_cs)

# new dataframe

new_df = df[df['paid.back.loan'] == 'Yes']

# Calculate the probablityp(B|A)

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]

print(prob_pd_cs)

# bayes theorem

bayes = (prob_pd_cs*prob_lp)/prob_cs

print(bayes)

# code start here

#create a bar plot for purpose

df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title('probablity distribution of purpose')
plt.ylabel('probability')
plt.xlabel('number of purpose')
plt.show()

# create a new dataframe

df1 = df[df['paid.back.loan'] == 'No']

#  plot the bar graph for the purpose where paid.back.loan == No

df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title('probablity distribution of purpose')
plt.ylabel('probability')
plt.xlabel('number of purpose')
plt.show()

# calculate median

inst_median = df.installment.median()
inst_mean = df.installment.mean()

# histogram for installment

df['installment'].hist(normed = True,bins = 50)
plt.axvline(x=inst_median, color = 'r')
plt.axvline(x= inst_mean,color = 'g')
plt.show()

# histogram for log annual income
df['log.annual.inc'].hist(normed = True,bins = 50)
plt.show()









