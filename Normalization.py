# Normalization is a technique used in data preprocessing to rescale data so that it fits within a specific range, typically [0, 1]. 
# It ensures that all features (variables) contribute equally to the analysis or model, especially when the features are on different scales.
# Example
# If we have two features:
# Age: [20, 25, 30, 35]
# Salary: [30,000, 50,000, 70,000, 90,000]
# Without normalization, the model might consider salary more important just because of its scale. Normalization brings both features to a similar range, e.g., [0, 1].

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

df=pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file2 - placement.csv")
print(df.head())

x = df.drop(columns = ['placed'])
y = df['placed']

x_train , x_test , y_train  , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Initialize the scaler
mn = MinMaxScaler()

# Fit and transform the data
x_train_mn = mn.fit_transform(x_train)

# Convert back to a DataFrame
x_train_new = pd.DataFrame(x_train_mn , columns = x_train.columns)

print(x_train_new)

print(np.round(x_train_new.describe() , 2))