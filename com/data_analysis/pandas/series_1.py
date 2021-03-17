'''
    pandas 的Series:  一维带标签（索引）的数组
         One-dimensional ndarray with axis labels (including time series)
    安装： pip install (xx.whl)


'''

import  pandas as pd

# 0    a
# 1    b
# 2    c
# s = pd.Series(list('abcde'))  # 默认带 字典序

# name    张三
# age     15
# dtype: object          # key 为index, value 为data 值
dict_v = {'name':'张三', 'age': 15}
s = pd.Series(dict_v)
# print(s)


# 手工指定 索引的值 , index=array_like
# 注: 索引的个数 需与 值的个数一致, 否则会报错，无法引用.
# s2 = pd.Series(list(range(5))*10,index=list('abcde'*10))
s2 = pd.Series(range(5),index=list('abcde'))
print(s2)

# 取值, 接收  index / position( 从0开始)
# print(s2['e'], s2[1])

# 获取不连续的值
# print(s2[[0,2,4]])

# 布尔索引
s2[s2 >= 3] = 10
# print(s2)

# 获取 index 和 具体的值;  t.index  t.values
# print(s2.index)  # dtype='object'
# print(type(s2.index), len(s2.index))  # pandas.core.indexes.base.Index

print(s2.values)  # [ 0  1  2 10 10]
print(type(s2.values), len(s2.values))  # numpy.ndarray

# 与 布尔索引类似，  满足条件显示原值, 未满足则 为NaN
s_ret = s2.where(s2>=10)
print(s_ret)













