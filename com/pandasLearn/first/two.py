'''
    进一步学习pandas

    How do I read and write tabular data?
    Whereas "read_*" functions are used to read data to pandas, the "to_*" methods are used to store data.

    如： read_csv / to_excel

REMEMBER
    Getting data in to pandas from many different file formats or data sources is supported by read_* functions.
    Exporting data out of pandas is provided by different to_*methods.
    The head/tail/info methods and the dtypes attribute are convenient for a first check.


'''

import pandas as pd
# 使用相对路径 读取文件
titanic = pd.read_csv('../../../data/titanic.csv')
print(titanic)

# I want to see the first 8 rows of a pandas DataFrame.
print(titanic.head(8))

# will return the last 10 rows of the DataFrame.
print(titanic.tail(2))

# This returns a Series with the data type of each column.
print(titanic.dtypes)

# 将数据存储到 excel中
# index=False the row index labels are not saved
titanic.to_excel('../../../data/titanic.xlsx',sheet_name='passengers',index=False)

# read_excel() will reload the data to a DataFrame:
reloadDf = pd.read_excel('../../../data/titanic.xlsx',sheet_name='passengers')
print(reloadDf.describe())

# about a DataFrame including the index dtype and column dtypes, non-null values and memory usage
titanic.info()


