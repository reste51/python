''''
 pandas 的基础处理
'''

import pandas as pd
import numpy as np

s = pd.Series([1,2,-4,9])
print(s)  # 每行显示索引和值

# 通过 values 和 index 分别获取
print(s.values, s.index)

# 指定一个索引的序列(必须是 可以hashable的  不可变), 索引类型为 dtype='object'
custom_index_series = pd.Series([1,2,4,-1],index=['a','ba','c','d'])
print(custom_index_series,custom_index_series.index)

# 可以使用 索引值取得对应值
print(custom_index_series['a'], custom_index_series[['c','d']],sep=' ** ')

print('*' * 100)

# 筛选值
print(custom_index_series[ custom_index_series>1])

# 每列的值 * 2
print((custom_index_series * 2))
# 每列值的指数
print(np.exp(custom_index_series))





