# Apply label encoding, standardization and how to handle missing data on attrition dataset. 

# handling missing data

import pandas as pd

df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\Attrition - Attrition.csv")
print(df.head())

print(df.info())

print(df.dropna())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Gender'] = df['Gender'].fillna('Unknown')
print(df.sample())


# label encoding

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Gender_encoded'] = le.fit_transform(df['Gender'])
print(df[['Gender', 'Gender_encoded']])


# standardization


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


x = df.drop(columns=["MaritalStatus"])  
y = df["MaritalStatus"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
sc = StandardScaler()

x_train_numeric = x_train.select_dtypes(include=np.number)

x_train_sc = sc.fit_transform(x_train_numeric)

x_train_new = pd.DataFrame(x_train_sc, columns=x_train_numeric.columns)
print(np.round(x_train_new.describe(), 3))
