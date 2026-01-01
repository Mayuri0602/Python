import numpy as np

import pandas as pd

# Part 1 : Basic Operations
# 1. Load the dataset using Pandas.
df = pd.read_csv('C:\\Users\\lenovo\\OneDrive\\Desktop\\Python 3.0\\Students_data.csv')
print(df)
# 2. Display the first 5 rows of the dataset.
print(df.head(5))
# 3. Display the last 5 rows of the dataset.
df.tail(5)
# 4. Check the shape, size, and ndim attributes of the DataFrame.
df.shape     
df.size
df.ndim
# 5. Display the column names.
df.columns
# 6. Check the data types of all columns.
df.dtypes
# 7. Check for any missing values in the dataset.
df.isnull().sum()
# 8. Select and display only the math score and reading score columns.
df[['math score', 'reading score']]
# 9. Find the number of male and female students (count of each gender).
df['gender'].value_counts()
# 10. Find the unique values present in the lunch column.
df['lunch'].unique()


# Part 2: Filtering Questions
# 1. Find and display the records of students who scored more than 80 in math score.
df[df['math score'] > 80]
# 2. Find and display the records of students who scored less than 50 in writing score.
df[df['writing score'] < 50]
# 3. Filter and display the students who completed the test preparation course.
df[df['test preparation course'] == 'completed']
# 4. Find and display the records of female students with a reading score greater than 70.
df[(df['gender'] == 'female') & (df['reading score'] > 70)]
# 5. Find and display the records of students who got free/reduced lunch.
df[df['lunch'] == 'free/reduced']


# Part 3: Basic Aggregation
# 1. Find the average of the math score.
df['math score'].mean()
# 2. Find the maximum and minimum values in the reading score column.
df['reading score'].max()
df['reading score'].min()
# 3. Count the number of students grouped by race/ethnicity.
df.groupby('race/ethnicity').size()
df['race/ethnicity'].value_counts()
# 4. Find the average writing score grouped by gender.
df.groupby('gender')['writing score'].mean()
# 5.  Sort the students by math score in descending order and display the top 10.
df.sort_values(by='math score', ascending=False).head(10)


# Part 4: Beginner Friendly Tasks
# 1. Create a new column named total_score, which is the sum of math score, reading score, and writing score.
df['total_score'] = (df['math score'] + df['reading score'] + df['writing score'])
# 2. Create a new column named average_score (total score divided by 3).
df['average_score'] = df['total_score'] / 3
# 3. Add a column named result. A student passes if their average_score is 60 or above; otherwise, they fail. (Hint: Use a conditional function or lambda expression).
df['result'] = df['average_score'].apply(
    lambda x: 'Pass' if x >= 60 else 'Fail')
df
# 4. Find the top 5 students based on their total_score.
df.sort_values(by='total_score', ascending=False).head(5)
# 5. Find the bottom 5 students based on their math score.
df.sort_values(by='math score', ascending=True).head(5)


