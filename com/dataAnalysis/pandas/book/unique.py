"""
唯一值、计数、和成员属性
"""
import pandas as pd

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

# 去重处理_ 注: 是Series类型
uniquees = obj.unique()
uniquees.sort()  # 原对象操作_ ndarray类型
print(uniquees)

# 包含每个值的个数
v = obj.value_counts()
# print(v, type(v))

# 过滤子集合
filter_df = obj[obj.isin(['b','a'])]
print(filter_df)
