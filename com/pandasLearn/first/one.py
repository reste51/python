'''
What kind of data does pandasLearn handle?

Many pandas operations return a DataFrame or a Series
DataFrame: 由行和列组成， 类似 表
Series: 无label 的列

• A table of data is stored as a pandas DataFrame
• Each column in a DataFrame is a Series
• You can do things by applying a method to a DataFrame or Series

'''

# 注： 包名不能使用 pandas名称，会引用当前包的__init__文件，而不会使用 第三方依赖包
import pandas as pd
import numpy as np

# print(pd.test())   # 测试是否运行成功

# I want to store passenger data of the Titanic
df = pd.DataFrame({
    'Name': ['Braund, Mr. Owen Harris','Allen, Mr. William Henry',
             'Bonnell, Miss. Elizabeth'],
    'Age':  [22, 35, 58],
    'Sex':  ['male', 'male', 'female']
})
print(df)

# Each column in a DataFrame is a Series
print(df['Age'])

print('*' * 100)

# You can create a Series from scratch as well:
ages = pd.Series([10,11,21],name='newAge')
print(ages)

# Do something with a DataFrame or Series
maxAge = df['Age'].max()
print(maxAge)

# x = np.ndarray((1,2)).argmax()
# print(x)

# some basic statistics of the numerical data
print(df.describe())

