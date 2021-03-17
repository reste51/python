'''
    numpy 的切片和 索引

    视频: 05-numpy读取本地数据和索引 ,02numpy中的索引和切片

    [行,列]    [2:,:]
    不连续的取值 [[1,4],[1,3]]   # 取 2和4行, 2和3列,  行与列的交叉点


'''

import numpy as np

arr = np.arange(24).reshape(4,6)
print(arr)

# 取 某一行
print(arr[2])

# 连续行, 切片
print(arr[2:])

print('*'*100)
# 取不连续的行, 再套一个[] 获取
print(arr[[0,3]])

print('*'*100)
# 取列
print(arr[1,:]) # 第二行所有列
print(arr[2:,:]) # 第三行-尾部的所有行, 所有列

print('*'*100)
# 取不连续的多列
print(arr[:,[1,5]])      # 取所有行,  第二/6列

# 取第三行/ 第四列的值
# arr = arr.astype(float)  # 更换 浮点类型
val = arr[2,3]
# print(val, type(val))  # numpy.int32

# 取连续的 1-3行, 2-4列的值
ret = arr[0:3,1:4]
print(ret.shape)

# 取不相邻的 几个点, 行与列的交叉点
# 行 和列均用[ [] ,[]] 数组挑选指定的值
print(arr[[2,3],[4,2]])




















