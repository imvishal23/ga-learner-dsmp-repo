# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
# finding the confidence interval
#sampling the dataframe

data_sample = data.sample(n=sample_size, random_state=0)

#finding the mean of the sample
sample_mean = data_sample['installment'].mean()

# finding the standard deviation of  the sample

sample_std = data_sample['installment'].std()

# finding the margin of error

margin_of_error = z_critical*(sample_std/math.sqrt(sample_size))

# finding the confidence interval

confidence_interval = (sample_mean - margin_of_error,sample_mean + margin_of_error)

print('confidence interval:', confidence_interval)

# finding the true mean

true_mean = data['installment'].mean()

print('true mean: {}',format(true_mean))

# Central Limit Theorem for installment

# different sample sizes to take
sample_size = np.array([20,50,100])

# creating different subplot
fig,axes = plt.subplots(3,1, figsize=(10,20))

# runnin loop to iterate through rows
for i in range(len(sample_size)):
    # initializeing list
    m=[]
    # loop to implement the no. of samples
    for j in range(1000):
        # find the mean of the random sample
        mean = data['installment'].sample(sample_size[i]).mean()

        # appending the mean to the list

        m.append(mean)

    # converting the list to the series

    mean_series = pd.Series(m)

    #plotting the histogram for the series
    axes[i].hist(mean_series,normed= True)

# display the plot
plt.show()

# Small Business Interests

# removing the last character from the values in column
data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])

#dividing the column value by 100
data['int.rate']=data['int.rate'].astype(float)/100

# applying the ztest for the hypothesis

z_statistic_1 , p_value_1 = ztest(x1=data[data['purpose']=='small_business']['int.rate'], value=data['int.rate'].mean(), alternative='larger')

print('z_statistic is: {}'.format(z_statistic_1))
print('p-value is: {}'.format(p_value_1))

# Installment vs Loan Defaulting

# applying ztest for the hypothesis

z_statistic_2, p_value_2 = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])

print(('z_statistic is: {}'.format(z_statistic_2)))
print(('p-value is: {}'.format(p_value_2)))

# Purpose vs Loan Defaulting

# subsetting the dataframe

yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()

# concating yes or no in a single dataframe

observed = pd.concat([yes.transpose(),no.transpose()],1,keys=['Yes','No'])

print(observed)

chi2, p ,dof , ex = chi2_contingency(observed)

print('critical value')
print(critical_value)














































