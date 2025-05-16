import pandas as pd

df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\file2 - placement.csv")
print(df.head())

# typeconversion 
df['cgpa'] = df['cgpa'].astype(int)
print(df)


# DataFrames are mutable implies we can apply operations on it
df['cgpa'] = df['cgpa'].add(4)
print(df)


# DataFrame ke har column ke non-null (NaN nahi) values ka count deta hai.
print(df.count())
# for rows
print(df.count(axis=1))


# har column ka maximum value return karta hai (sirf numeric ya comparable data types ke liye), for rows(axis=1)
print(df.max())


# har column ka minimum value return karta hai
print(df.min())


# each column ka mean calculate krta hai
print(df.mean())

# specifically bhi apply kr skte hai
print(df['cgpa'].mean())


# calculating median 
print(df['resume_score'].median())


# har column ke values ka total (sum) return karta hai, specific column ke liye bhi kr skte hai, and rows ke liye axis=1
print(df.sum())


# items=[] sirf columns by default select karta hai.
print(df.filter(items = ['resume_score']))

# second method for filtering, 2D
print(df[['cgpa', 'placed']])

# for rows
print(df.filter(items=[2, 6], axis=0))  # 2nd & 6th row


# saves DataFrame in Dictionary format
print(df.to_dict())


# saves DataFrame in String format
print(df.to_string())


# print(df.to_csv("path location")) - DataFrame ko ek CSV file banakar save karta hai


# df.columns ek Index object return karta hai jisme DataFrame ke saare column names hote hain, isse list ki tarah access kar sakte hain
new_df=df.columns
print(new_df)
# Output - Index(['cgpa', 'resume_score', 'placed'], dtype='object')


# particular column access karne ke liye
label = df.columns[2]
print(label)
# Output - placed


# list of column labels - returns a python list
print(df.columns.tolist())
# Output - ['cgpa', 'resume_score', 'placed']


# returns NumPyarray
print(df.columns.values)
# Output - ['cgpa' 'resume_score' 'placed']


# used to rename the col_name (multiple columns bhi rename kar skte hai)
print(df.rename(columns = {'cgpa': 'grades'}))


# kisi column ko remove karne ke liye
# print(df.drop(columns = ['grades']))



df['New'] = df['cgpa'].where(df['cgpa']>10, other=0)
print(df.sample())
# where(condition, other=0):Agar condition True ho → original value df['cgpa'] rakhta hai
# Agar condition False ho → value ko 0 bana deta hai (as specified by other=0)
# df['New'] = ...: Isse ek naya column 'New' DataFrame mein add ho jata hai.
# also used for multiple conditions
# condition = (df['cgpa'] > 10) & (df['cgpa'] < 11)
# df['New'] = df['cgpa'].where(condition, other='Invalid')



# merge() function is designed to merge two DataFrames based on one or more columns with matching values or index
# pd.merge(df1, df2, on='column_name', how='type_of_join')
 
#  Student info
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

# CGPA info
df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'cgpa': [9.0, 8.5, 7.0]
})

#  Inner Join (only common id values):
# Left Join (all from df1, matched from df2)
# Right Join (all from df2, matched from df1)
# Outer Join (all from both, unmatched filled with NaN(missing values))

new_df=pd.merge(df1, df2, on='id', how='right')
print(new_df)   



# Concatenationfunction - used to combine DataFrames either vertically (rows-wise) or horizontally (columns-wise).

df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

df4 = pd.DataFrame({
    'Name': ['Charlie', 'David'],
    'Age': [22, 28]
})

# Vertical Concatenation (default axis=0)
print(pd.concat([df3, df4], ignore_index = True))

# Horizontal Concatenation (axis=1)
print(pd.concat([df3, df4], axis=1))









