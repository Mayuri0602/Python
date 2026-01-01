# Make a series of 1 to 10 numbers
import pandas as pd

df = pd.Series(range(1, 11))
print(df)


# Add a cond to filter even entries of the series
new_df = df [df % 2 == 0]
print(new_df)


# Make a series of 10 to 100 no.s. and filter out odd no.s. and add 5 to each element
s = pd.Series(range(10,101))
print(s)

p = s[s % 2 == 1]
print(p)

new_df = p + 5
print(new_df)

# Create a DataFrame from a dictionary of lists
data = {
       'Name' : ['Alice', 'Bablu', 'Chetna'],
       'Age' : [23, 21, 20],
       'City' : ['Sikar', 'Jaipur', 'Kuchaman'],
       'Gender' : ['F', 'M', 'F']
}

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd'] )
print(df)

# Mean calculation of Age
print(df['Age'].mean())

# Mode on 'Gender' col
print(df['Gender'].mode()[0])

# Median calculation
df['Age'].median()



