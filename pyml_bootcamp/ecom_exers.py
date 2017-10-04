import numpy as np
import pandas as pd

csv_file = 'Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases'

ecom_df = pd.read_csv(csv_file)

# check head of dataframe
print(ecom_df.head())
print()

# basic stats on df
print('ecom_df made of {} rows and {} cols.'.format(ecom_df.shape[0], ecom_df.shape[1]))
print()
print('ecom_df described:')
print(ecom_df.describe())
print()
print('ecom_df size:')
print(ecom_df.size)
print()

# average purchase price
msg = 'average purchase price: {:.2f}'.format(ecom_df['Purchase Price'].mean())
print(msg)
print()

# what are the highest and lowest purchase prices
high_msg = 'highest purchase price: {:.2f}'.format(ecom_df['Purchase Price'].max())
low_msg = 'lowest purchase price: {:.2f}'.format(ecom_df['Purchase Price'].min())

print(high_msg)
print(low_msg)
print()

# number of customers with english as chosen language
msg = 'number of custs with "en" as language: {}'.format(ecom_df[ecom_df['Language'] == 'en']['Language'].count())
print(msg)
print()

# number of customers with job title 'lawyer'
msg = 'number of custs with lawyer title: {}'.format(ecom_df[ecom_df['Job'] == 'Lawyer']['Job'].count())
print(msg)
print()

# number of custs AM/PM purchase
msg = 'AM vs PM purchases:'
print(msg)
print(ecom_df['AM or PM'].value_counts())
print()

# top 5 common job titles
print('top 5 common job titles:')
print(ecom_df.groupby('Job')['Job'].count().sort_values(ascending=False).head())
print()
