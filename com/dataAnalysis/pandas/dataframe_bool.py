"""
    bool 索引
    1. 单一条件
    2. 多个条件 () & ()

    返回的仍是 DF
"""
import numpy as np
import pandas as pd

df = pd.read_csv('./dogNames2.csv')
# print(df)

# 单一条件
ret_df = df[df['Count_AnimalName']>800]  # 取列名为Count大于 800的值
print(ret_df)

# 多个条件() & () ;   | 或，& 且
ret_df = df[(df['Count_AnimalName']>800)  & (df['Count_AnimalName']<1000) ]  # 大于800 并且小于 1000
print(ret_df)

# df中字符串的方法,  col.str.split(',').tolist()  /  len() / contains()
# 会应用到当前 选中列的值



