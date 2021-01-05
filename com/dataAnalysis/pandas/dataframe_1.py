"""
 二维(行和列), Series容器。
    默认会指定 行索引(axis=0) 和列索引(axis=1); 从0自增

 Series容器的理解：
    因为 每次从DF(二维)取值时,  都会是一个  一维数据，无论是从 某行或 某列取值.
    因此 取值后都会是一个Series 。


"""
# index 代表行，  col 列
# pd.DataFrame(arr_like,index, columns)

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(50,60).reshape(2,5),index=['row1','row2'],columns=list('abcde'))
# print(df)


# DF 传入 字典dict数据

# 1.1 key 为[] 时，会产生多行;  {name:['a','b'],'age':[20,12]}
dict1 = {'name':['李勇','李典','王五'], 'age':[10,20,30]}       # 注: 每个属性的数组长度一致
# df = pd.DataFrame(dict1)
# print(df)

# 1.2  每个json 为一行数据;  [{name:1,age:2},{name:1,age:2}]     # 注: 每个json 的属性可以不一致, 均为 每一列
dict2 = [{'name':'力点','age':32},{'name':'力点','age':32,'salary':5000}]
df = pd.DataFrame(dict2)
# print(df)

# df 的其他属性
# df.index df.columns df.values( 对象值, 二维ndarray数组)

# 行: RangeIndex(start=0, stop=2, step=1) <class 'pandas.core.indexes.range.RangeIndex'>
# print(df.index,type(df.index))

# 列: Index(['age', 'name', 'salary'], dtype='object') <class 'pandas.core.indexes.base.Index'>
# print(df.columns, type(df.columns))

# 值: <class 'numpy.ndarray'>
# print(df.values,type(df.values))

# head(num)  tail(num)  与 spark 类似

# df.info()  展示概览, 内存使用等
# df.describe() 最大/小等 的统计值
# print(df.describe())

# 统计次数最高的前几个名字？
df = pd.read_csv('./dogNames2.csv')
ret = df.sort_values(by='Count_AnimalName',ascending=False).head(3)
print(ret)


# sort学习, 按照index 或 某列的值进行排序; ascending=False 指定排序方式

# 产生 2行4列的 df
obj = pd.DataFrame(np.arange(8).reshape(2,4), index=['three','one'], columns=list('dabc'))
# 按照索引排序
# 1.1 行index , one -> three
print(obj.sort_index())

# 1.2 列 排序;  a ->b ->c ->d
# print(obj.sort_index(axis=1))

# 按照值排序
# 按照 列b 倒序
# print(obj.sort_values(by='b',ascending=False))
# 按多列  倒叙
# print(obj.sort_values(by=list('abcd'),ascending=False))






