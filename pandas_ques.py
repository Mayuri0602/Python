import pandas as pd

df = pd.read_csv("file1.csv")
# print(df)

# head - provides top 5 data
# print(df.head())

# # tail - provides data(5) from bottom 
# print(df.tail())

# # sample - gives data randomly
# print(df.sample(6))

# # describe - statically view of data
# print(df.describe())

# # info - data type information
# print(df.info())

# # iloc - [row_index,column_index]  (integer positions)
# print(df.iloc[6,4])

# # loc - [row_label,column_label]    (labels(names))
# print(df.loc[3,'gender'])

# gives info about type of data in dataframe
# print(df.dtypes)

# It returns True if there is any missing data in dataframe otherwise returns False
# print(df.empty)

# isnull() only shows "True" for missing values otherwise False
# isnull().sum() counts missing values in each column and gives "number" of missing values in each column
# sum() column - wise sum, skipping missing values(NaNs)
# print(df.isnull().sum())

# used to remove missing values (i.e., rows or columns that contain NaNs(missing values)).
# print(df.dropna())

# no. of rows, no. of columns i.e. 100,6
# print(df.shape)

# row count * column count i.e. 100*6
# print(df.size)

# returns the underlying data of a DataFrame as a NumPy array, it removes row and column labels, the result is a NumPy ndarray.
# print(df.values)

# creates a copy that does not affect the original DataFrame.
# print(df.copy())

# df.sort_values(by = 'column_name')  -  used to sort a DataFrame by the values in one or more columns.
# print(df.sort_values(by = 'age'))

# used to sort a DataFrame by its index (row labels) instead of the data in the columns.
# r = df.sort_index
# print(r)

# 
print(df['fever'].astype(int))