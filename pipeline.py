# Data ==> seperate (categorical, numerical)
# Categorical data ==> SimpleImputer fill ===> Encode
# Numerical data ==> SimpleImputer fill ===> 

import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file1.csv")
print(df.head())

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

