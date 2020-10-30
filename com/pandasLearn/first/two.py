'''
    进一步学习pandas

    How do I read and write tabular data?


'''

import pandas as pd
# 使用相对路径 读取文件
titanic = pd.read_csv('../../../data/titanic.csv')
print(titanic)

# I want to see the first 8 rows of a pandas DataFrame.
print(titanic.head(8))

# will return the last 10 rows of the DataFrame.
print(titanic.tail(2))






