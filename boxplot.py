import numpy as np
import pandas as pd


df = pd. read_csv("newplacementdata - newplacementdata.csv")
print(df)

print(df.head())

# even  = ((n/2)+ ((n/2)+1))/2 
# odd = ((n/2)+1)

import matplotlib.pyplot as plt
import seaborn as sns

print(df['placement_exam_marks'].describe())


sns.boxplot(x = df['placement_exam_marks'])

# finding the IRQ

percentile25 = df['placement_exam_marks'].quantile(0.25)
percentile75 = df['placement_exam_marks'].quantile(0.75)

print(percentile25)
print(percentile75)

IQR = percentile75 - percentile25
print(IQR)

upper_limit = percentile75 + 1.5*IQR
print(upper_limit)

lower_limit = percentile25 - 1.5*IQR
print(lower_limit)


# Finding our Outliers

print(df[df['placement_exam_marks'] > upper_limit])

print(df[df['placement_exam_marks'] < lower_limit])

# Trimming  ---> 4(lower).....1 , upper(25).....(50) ---> here 1,50 are outliers ---> 
# lower(4) <----> upper(25) mid data . 

# Capping ---->  4(lower).....1 , upper(25).....(50) ---> capping lower point lowest point(1)
# upper point upper point(50)  ---> Range expand ---> outliers remove . 

# Trimming (Outlier Removing technique 1) 

newdf = df[df['placement_exam_marks'] < upper_limit] 
print(newdf)

# newdf
# comparison

plt.figure(figsize = (15,5)) 


plt.subplot(222) 
sns.boxplot(x = df['placement_exam_marks']) 


plt.subplot(224)
sns.boxplot(x = newdf['placement_exam_marks']) 
plt.show() 

# Capping(Outlier Removing technique 2)

new_df_cap = df.copy() 
print(new_df_cap)

# min = 5  , max 15 

# min 4 , 3 , 1 
# max = 20 , 30 , 50 

# updated_min_value = 1 
# updated_max_value = 50 

new_df_cap['placement_exam_marks'] = np.where(
    
    new_df_cap['placement_exam_marks'] > upper_limit , 
    upper_limit , 
    
    np.where(
    new_df_cap['placement_exam_marks'] < lower_limit , 
    lower_limit , 
    new_df_cap['placement_exam_marks']))

print(new_df_cap)
print(new_df_cap.shape)

# comparison

plt.figure(figsize = (15,8)) 


plt.subplot(222) 
sns.boxplot(x=df['placement_exam_marks'])


plt.subplot(224)
sns.boxplot(x=new_df_cap['placement_exam_marks'])
plt.show()