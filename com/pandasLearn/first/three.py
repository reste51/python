'''
How do I select a subset of a DataFrame?
How do I select specific columns from a DataFrame?

'''

import  pandas as pd

titanic = pd.read_csv('../../../data/titanic.csv')
print(titanic.head()) # default 5

# I’m interested in the age of the Titanic passengers.
age_series = titanic[['Age','Sex']]
head_age_series = age_series.head()
# A pandas Series is 1-dimensional and only the number of rows is returned.
print(head_age_series, age_series.shape)

# To select multiple columns, use a list of column names within the selection brackets [].
age_sex = titanic[['Age','Sex']]
print(age_sex.head())

print('*'* 100)

# <class 'pandas.core.frame.DataFrame'>
print( type(age_sex))

# The selection returned a DataFrame with 891 rows and 2 columns.
# Remember, a DataFrame is 2-dimensional with both a row and column dimension.
print( age_sex.shape)


# How do I filter specific rows from a DataFrame?

# I’m interested in the passengers older than 35 years.
above_35 = titanic[titanic['Age'] > 35]
print(above_35.head())
print(above_35.shape)

# in 条件的使用
class_23 = titanic[titanic['Pclass'].isin([2,3])]
print(class_23)
print(class_23.shape)

# 逻辑运算:  and /or  &/ |
class_23 = titanic[(titanic['Pclass']==2) | (titanic['Pclass']==3)]
print(class_23)
print(class_23.shape)


#  each row the values are not an Null value
age_no_na = titanic[titanic['Age'].notna()]
print(age_no_na.shape)

# slice -> I’m interested in rows 10 till 25 and columns 3 to 5.
splice_result = titanic.iloc[10:26, 2:5]
print(splice_result)



