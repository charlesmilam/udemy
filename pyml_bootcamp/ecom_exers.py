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
# solution answer
print('ecom_df info:\n{}'.format(ecom_df.info()))
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
# solution  uses .value_counts().head() much cleaner
print('top 5 common job titles:')
print(ecom_df.groupby('Job')['Job'].count().sort_values(ascending=False).head())
print()

# purchase price for given lot number
msg = 'purchase price for lot: {}: '.format(ecom_df[ecom_df['Lot'] == '90 WT']['Purchase Price'])
print(msg)
print()

# email for given cc number
cc_num = 4926535242672853
cc_email = ecom_df[ecom_df['Credit Card'] == cc_num]['Email']
msg = 'email for cc num {}: {}'.format(cc_num, cc_email)
print(msg)
print()

# number amex users with purchase > $95
amex_count = (ecom_df[ecom_df['CC Provider'] == 'American Express']['Purchase Price'] > 95).count()
msg = 'num of amex users, purchase > $95: {}'.format(amex_count)
print(msg)
print()
# solution
amex_count = ecom_df[(ecom_df['CC Provider'] == 'American Express') & (ecom_df['Purchase Price'] > 95)].count()
print('amex solution:\n{}'.format(amex_count))
print()

# number of users with cc expire in 2025
num_exp_2025 = [x[3:] == '25' for x in ecom_df['CC Exp Date']].count(True)
print('num of users with cc exp in 2025: {}'.format(num_exp_2025))
print()

# top 5 email providers
ecom_df['email_domain'] = ecom_df['Email'].apply(lambda x: x.split('@')[1])
print('top 5 email domains:\n{}'.format(ecom_df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head()))
