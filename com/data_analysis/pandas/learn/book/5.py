'''
    第五章：
    索引对象 用于存储周标签和其他元数据， 由任意数组或序列构成

'''

import  pandas as pd
import numpy as np

obj = pd.Series(range(3), index=['a','b','c'])
index = obj.index

print(index, index[1:])

# 索引不可变
# index[0] = 1

print(obj)
# 通过重建索引 可以改变索引顺序,  索引对应的值还是引用原有值
obj = obj.reindex(['c','b','a'])
print(obj)

print('*' * 100)

# 返回9个值, 0.0~8.0;  reshape((3,3))  生成 3行3列的矩阵
# print(np.arange(9.0))
df1 = pd.DataFrame(data=np.arange(9.0).reshape((3,3)), columns=list('bcd'),index=['Ohio','Texas','Colorado'])

df2 = pd.DataFrame(data=np.arange(12.0).reshape((4,3)),columns=['b','d','e'],index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1, end='\n')
print(df2)
# 只有 相同的列和索引名相加 才能获取值;  不匹配则返回 NaN
print(df1 + df2)

print('*' * 100)

# 两个不相同的列相加, 结果均为Nan
df3 = pd.DataFrame({'a':[1,2]})
df4 = pd.DataFrame({'CC':[11,12]})
print(df3)
print(df4)
print(df3 + df4)

print('*' * 100)

# 广播机制， 在每一行都进行了减法的操作
arr = np.arange(15.).reshape((3,5))
print(arr)
print(arr[0]) # [0. 1. 2. 3.]
print(arr - arr[0])

print('*' * 100)

# pandas 与 np 类似的操作
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)

# 行专列， 第一行转为 一列显示
series = frame.iloc[0]
print(series)

# 广播每行进行操作
print(frame - series)

print('*' * 100)

# numpy 函数的应用和映射
data = np.random.randn(4,3)  # 4行3列的标准分布值
print(data)
frame = pd.DataFrame(data,
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# 取绝对值, 负值改为相同的正值
print(np.abs(frame))

# 函数的应用 df.apply(np.sqrt) 相同与 `np.sqrt(df)
# 0 or 'index': apply function to each column.(默认为 每列)
#  1 or 'columns': apply function to each row.
f = lambda x: x.max() - x.min()
print(frame.apply(f))  # 每列的处理











