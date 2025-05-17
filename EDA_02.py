# Exploratory Data Analysis(EDA) - Bivariate Analysis

# Bivariate / Multivariate Analysis (Two or more than two variables or columns)

# Numerical vs. Numerical: Scatter plots, correlation heatmaps.
# Categorical vs. Numerical: Box plots, grouped bar charts.
# Categorical vs. Categorical: Crosstabs, stacked bar charts.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tips dataset comes built-in with the Seaborn library — it's one of several sample datasets that Seaborn provides 
# for practice, testing, and data visualization.

tips = sns.load_dataset('tips')
print(tips)

# 1. Load and Preview the Data
# print(df.head())
# 2. Understand the Structure
# print(df.shape)  # Rows and columns
# print(df.info())  # Data types and non-null values
# print(df.describe())  # Summary statistics
# 3. Check for Missing Values & Duplicates
# print(df.isnull().sum())  # Missing values per column
# print(df.duplicated().sum())  # Count duplicates


# Tips dataset comes built-in with the Seaborn library — it's one of several sample datasets that Seaborn provides 
# for practice, testing, and data visualization.


# Bivariate analysis (Num. vs Num.)
# sns.scatterplot(x = tips['total_bill'],
#                 y = tips['tip'])
# plt.title("Total_bill vs Tip")
# plt.show()


# Multivariate analysis
sns.scatterplot(x = "total_bill",
                y = "tip", data = tips, 
                hue = tips['sex'], style = tips['smoker'])
plt.show() 