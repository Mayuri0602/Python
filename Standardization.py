# Standardization (also called Z-score normalization) transforms the data to have a mean of 0 and a standard deviation of 1.
# Used to scale features in our dataset - If features are on different scales (e.g., salary in thousands vs. age in years), the model might give more weight to larger-scaled features — even if they're not more important.

#  Split our data into training and test sets.
# Fit the scaler only on the training data (to avoid data leakage).
# Transform both the training and test sets using the scaler.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file2 - placement.csv")
print(df.head())

# Step 1: Split features and target
X = df.drop(columns = ['placed'])
y = df['placed']

# Step 2: Split into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 3: Apply StandardScaler
scaler = StandardScaler()

# Fit on training data only
x_train_scaled = scaler.fit_transform(x_train)

# Transform test data using the same scaler
x_test_scaled = scaler.transform(x_test)

# (Optional) Convert back to DataFrame for readability
x_train_scaled_df = pd.DataFrame(x_train_scaled, columns=x_train.columns)
x_test_scaled_df = pd.DataFrame(x_test_scaled, columns=x_test.columns)

print("Standardized training data:\n", x_train_scaled_df.round(2))
print("\nStandardized test data:\n", x_test_scaled_df.round(2))



# SimpleImputer is a preprocessing tool that fills in missing values in a DataFrame or NumPy array using a specified strategy like: mean,median,most frequent common values...
# Missing data can break your machine learning model or lead to errors when training. Instead of removing rows or columns, imputing keeps more data and improves model performance.



df=pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file1.csv")
print(df.head())

df['gender'] = df['gender'].map({"Male":0 , "Female":1})
df['cough'] = df['cough'].map({"Mild":0 , "Strong":1}) 
df['city'] = df['city'].map({"Kolkata":0 , "Bangalore":1 , "Delhi":2 , "Mumbai":3}) 
df['has_covid'] = df['has_covid'].map({'Yes':0 , 'No':1})
print(df.sample())

from sklearn.impute import SimpleImputer

# seperate features and target
x = df.drop(columns = ['has_covid'])  ## Input data 
y = df['has_covid']   ### Target data

# Split into training and test sets 
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2 , random_state = 42)

# Step 3: Handle missing values with SimpleImputer
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent', 'constant'

# Fit on training data only
x_train_imputed = imputer.fit_transform(x_train)

# Use the same imputer on test data
x_test_imputed = imputer.transform(x_test)

# Step 4: Scale the data
scaler = StandardScaler()  

x_train_scaled = scaler.fit_transform(x_train_imputed)
x_test_scaled = scaler.transform(x_test_imputed)

# (Optional) Convert back to DataFrames
x_train_scaled_df = pd.DataFrame(x_train_scaled, columns=x.columns)
x_test_scaled_df = pd.DataFrame(x_test_scaled, columns=x.columns)

print("Cleaned & Scaled Training Data:\n", x_train_scaled_df.round(2))
print("\nCleaned & Scaled Test Data:\n", x_test_scaled_df.round(2))
