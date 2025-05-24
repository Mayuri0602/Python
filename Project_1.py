# Employee attrition analysis is a type of behavioural analysis where we study the behaviour
# and characteristics of the employees who left the organization and compare their characteristics
# with the current employees to find the employees who may leave the organization soon.

import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\Python\\Attrition - Attrition.csv")
print(df)

print(df.head())

import plotly.graph_objects as go
import plotly.io as pio 

print(df.isnull().sum())

# Filter the data to show only "Yes" values in the "Attrition" column

attr_df = df[df['Attrition']=='Yes']
print(attr_df)

# Calculate the attrition by department

attrition_by_dpt = attr_df.groupby(['Department']).size().reset_index(name = "count")
attrition_by_dpt

# create a donut chart
fig = go.Figure(data=[go.Pie(
    labels=attrition_by_dpt['Department'],
    values=attrition_by_dpt['count'],
    hole=0.4,
    marker=dict(colors=['red','green']),
    textposition='inside'
)])

# update the layout
fig.update_layout(title='Attrition by Department')

# show the chart
fig.show()

attrition_by = attr_df.groupby(['EducationField']).size().reset_index(name='Count')
attrition_by

# create a donut chart
fig = go.Figure(data=[go.Pie(
    labels=attrition_by['EducationField'],
    values=attrition_by['Count'],
    hole=0.4,
    marker=dict(colors=['blue','pink']),
    textposition='inside'
)])

# update the layout 
fig.update_layout(title='Attrition by Education Field')
# show the chart
fig.show()


attrition_by = attr_df.groupby(['YearsAtCompany']).size().reset_index(name='Count')
attrition_by

# We can see that most of the employees leave the organization after completing a year.

attrition_by = attr_df.groupby(['YearsSinceLastPromotion']).size().reset_index(name='Count')
attrition_by

attrition_by = attr_df.groupby(['Gender']).size().reset_index(name='count')
attrition_by

# Create a donut chart
fig = go.Figure(data=[go.Pie(
    labels=attrition_by['Gender'],
    values=attrition_by['count'],
    hole=0.4,
    marker=dict(colors=['#3CAEA3', '#F6D55C']),
    textposition='inside'
)])

# Update the layout
fig.update_layout(title='Attrition by Gender')
# Show the chart
fig.show()

import plotly.express as px

fig = px.scatter(df, x="Age", y="MonthlyIncome", color="Attrition", 
                 trendline="ols")
fig.update_layout(title="Age vs. Monthly Income by Attrition")
fig.show()