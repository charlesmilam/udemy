# import pandas
import pandas as pd

# read Salaries.csv as a dataframe called sal
csv_file = 'Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Salaries.csv'
sal_df = pd.read_csv(csv_file)

# head of dataframe
print(sal_df.head().to_string())
print()

# use .info to get number of entries
print(sal_df.info())
print()

# what is the average base pay
print('average base pay: ', sal_df['BasePay'].mean())
print()

# what is the highest overtime pay
print('highest overtime pay: ', sal_df['OvertimePay'].max())
print()

# what is the job title of joseph driscoll
print('joseph driscoll job title: ', sal_df[sal_df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print()

# highest paid person
print('person with greatest total benefits: ', sal_df[sal_df['TotalPayBenefits'] == sal_df['TotalPayBenefits'].max()][['EmployeeName', 'TotalPayBenefits']])
print()
# alt highest paid person
print(sal_df.groupby(['EmployeeName'])['TotalPayBenefits'].max())
print()

# lowest paid person
print('person with least total benefits: ', sal_df[sal_df['TotalPayBenefits'] == sal_df['TotalPayBenefits'].min()][['EmployeeName', 'TotalPayBenefits']])
print()
# alt lowest paid
# stuff goes here

# average base pay by year
print('avg base pay by year: ', sal_df.groupby('Year')['BasePay'].mean())
print()

# number of unique job tites
print('num unique job titles: ', sal_df['JobTitle'].nunique())
print()

# top 5 common jobs
print('top 5 common jobs:\n', sal_df['JobTitle'].value_counts().head())
print()

# job titles wih only 1 person in 2013
# print('2013 single person job titles:', sal_df[(sal_df[sal_df['Year'] == 2013]['JobTitle']) & (sal_df[sal_df['JobTitle'].value_counts() == 1])])
print()

# how many job titles with chief in title
sal_df['has_chief'] = sal_df['JobTitle'].apply(lambda x: 'chief' in x.lower())
print(sal_df[sal_df['has_chief'] == True]['JobTitle'].to_string())
print('number of jobs with Chief in title: ', len(sal_df[sal_df['has_chief'] == True]))

# bonus => correlation between job title len and TotalPayBenefits
# add column of job title lengths
sal_df['title_len'] = sal_df['JobTitle'].apply(lambda x: len(x))
# determine correlation of title_len and TotalPayBenefits
titlelen_totalcomp_corr = sal_df['title_len'].corr(sal_df['TotalPayBenefits'])
print('Correlation between Job Title Length and Total Pay Benefits')
print(titlelen_totalcomp_corr)
# apply correlation to entire dataframe
print()
print('Table - Correlation between Job Title Length and Total Pay Benefits')
print(sal_df[['title_len', 'TotalPayBenefits']].corr())
print()
