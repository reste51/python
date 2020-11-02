'''
 聚合统计
'''

import  pandas as pd

titanic = pd.read_csv('../../../data/titanic.csv')
print(titanic.head())

# What is the average age of the Titanic passengers?
print(titanic['Age'].mean())

# 两列的中间值
print(titanic[['Age','Fare']].median())

# 详细信息
print(titanic[['Age','Fare']].describe())

# 分组： 1. 选择列 2.聚合 3. 取值( 平均值)
print(titanic[['Age','Sex']].groupby("Sex").mean())


