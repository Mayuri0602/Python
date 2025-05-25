# Data division is the process of splitting your dataset into separate parts for different purposes, typically to train and evaluate machine learning models.

# Training Set:- trained our model from input to target data relation
# Validation Set:-
# Test Set:- after training, we test the model on new, unseen data


import pandas as pd

df=pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file2 - placement.csv")
print(df.head())

print(df.shape)

# Input data
x = df.drop(columns = ['placed'])
# Target data
y = df['placed']

from sklearn.model_selection import train_test_split

# 80% training, 20% test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Total data shape:", df.shape)
print("Input data shape:", x.shape)
print("Input data shape:", x_train.shape)
print("Input data shape:", x_test.shape)

print("Target data shape:", y.shape)
print("Target data shape:", y_train.shape)
print("Target data shape:", y_test.shape)

# df(100,3) = x(100,2) + y(100,1)
# x(100,2) = x_train(80,2) + x_test(20,2)
# y(100,1) = y_train(100,1) + y_test(20,1)


df=pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file1.csv")
print(df.head(3))

print(df['gender'].value_counts())
print(df['cough'].value_counts())
print(df['city'].value_counts())
print(df['has_covid'].value_counts())

# .map() is used to transform or map values in a column by applying:
# Example: Convert "Yes"/"No" to 1/0
# Using a Function to Modify Values
#  Using map() for Category Encoding

df['gender'] = df['gender'].map({"Female":0, "Male":1})
df['cough'] = df['cough'].map({"Mild":0, "Strong":1})
print(df.sample(4))

# Input data
x = df.drop(columns = ['has_covid'])
# Target data
y = df['has_covid']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Total data shape:", df.shape)
print("Input data shape:", x.shape)
print("Input data shape:", x_train.shape)
print("Input data shape:", x_test.shape)

print("Target data shape:", y.shape)
print("Target data shape:", y_train.shape)
print("Target data shape:", y_test.shape)