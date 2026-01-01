# EDA stands for Exploratory Data Analysis where we explore datasets to summarize their main characteristics, visualize data using graphs and plots,
#  identify patterns, trends, outliers, and check assumptions and data quality (e.g., missing values, data types, distributions)

# Main parts of EDA:
# 1. Understanding the Dataset

# Check data structure: How many rows and columns?
# Data types: Are the columns numerical, categorical, datetime, etc.?
# Preview the data: Use head() to view the first few rows.

#  2. Data Cleaning

# Missing values: Identify and handle null or missing entries.
# Duplicates: Detect and remove duplicate rows.
# Inconsistencies: Fix inconsistent formats or entries (e.g., "yes", "Yes", "Y").
# Outliers: Detect values that deviate significantly from the rest.

# 3. Univariate Analysis (One variable at a time)

# Numerical: Use histograms, box plots, mean, median, standard deviation.
# Categorical: Use bar charts, value counts, and frequency tables.

# 4. Bivariate/Multivariate Analysis (Two or more variables)

# Numerical vs. Numerical: Scatter plots, correlation heatmaps.
# Categorical vs. Numerical: Box plots, grouped bar charts.
# Categorical vs. Categorical: Crosstabs, stacked bar charts.

# 5. Feature Engineering & Transformation

# Creating new variables from existing data.
# Encoding categorical variables (Label Encoding, One-Hot Encoding).
# Scaling/normalizing data.
# Date/time extraction (e.g., extracting month or weekday from a date).

# 6. Correlation Analysis

# Identify relationships between numerical features using:
# Correlation coefficients (Pearson, Spearman)
# Heatmaps for visualization

# 7. Outlier Detection

# Using box plots, Z-score, or IQR method to find abnormal values.

# 8. Data Visualization

# Use tools like matplotlib, seaborn, or plotly to:
# Summarize distributions
# Reveal patterns and trends
# Support insights for decision making


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load and Preview the Data
df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\titanic - titanic.csv")
print(df.head())

# 2. Understand the Structure
print(df.shape)  # Rows and columns
print(df.info())  # Data types and non-null values
print(df.describe())  # Summary statistics

# 3. Check for Missing Values & Duplicates
print(df.isnull().sum())  # Missing values per column
print(df.duplicated().sum())  # Count duplicates

# 4. Univariate Analysis

# If we want to calculate actual values then we use value_counts
print(df['Survived'].value_counts())              
#  categorical data
sns.countplot(x=df['Survived'])
plt.title("Count of Survived Passengers")
plt.show()
# # If we want to find out the percentage then we use piechart
print(df['Survived'].value_counts().plot(kind = 'pie', autopct='%.2f')) 
sns.countplot(x=df['Survived'])
plt.title("Count of Survived & Died Passengers")
plt.show()

# numerical data
plt.hist(x=df['Age'])
plt.title("Distribution of Age")
plt.show()


# Boxplot(only for numerical data) - to find outliers(that particular point in data which fluctuates the mean)
# lower fence(min. non-utlier value), (Q1)25% data, Median(Q2-50%), (Q3)75% data, upper fence(max.-non-outlier value),
# IQR stands for Interquartile Range(Q3-Q1)-middle 50% of data, 
# outliers (dots) - Outliers are values that fall below Q1 - 1.5×IQR or above Q3 + 1.5×IQR.
# Example to understand what outlier is - 
# x = 1,2,3,4,5
# mean = (1+2+3+4+5)/5 = 3
#  x = 1,2,3,4,5,100
# mean = (1+2+3+4+5+100)/6 = 115/6 = 19.1


            # Outliers
            #    |
    #   whisker     whisker
        #  |          |
        #  ─────────────  ← Maximum
        #  |          |
    #  ┌────────────┐ ← Q3 (75%)
    #  |            |
    #  |   Median   | ← Q2 (50%)
    #  |            |
    #  └────────────┘ ← Q1 (25%)
        #  |          |
        #  ─────────────  ← Minimum

sns.boxplot(x=df['Age'])
plt.title("Boxplot for Age")
plt.show()