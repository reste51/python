"""
Numpy仍然是Python做数据分析所必须要掌握的基础库之一，以下题是github上的开源项目，
主要为了检测你的Numpy能力，同时对你的学习作为一个补充。
"""

import numpy as np

# 1.打印输出numpy的版本和配置信息
# print(np.__version__, np.show_config(), sep='\n')

# 2. 创建一个长度为10的空向量
Z = np.zeros(10)
print(Z)

# 数组的内存大小
print('%d bytes!' % (Z.size * Z.itemsize))

# 命令行得到numpy中add函数的说明文档?
np.info(np.add)

# 创建一个长度为10  并且除了 第五个值为1的空向量
Z[4] = 1
print(Z)

# 创建一个 值域范围: 10-49的向量
Z = np.arange(10,50)
print(Z)

# 反转向量
Z = Z[::-1]
print(Z)

print('*'*100)

Z = np.random.randn(3,3,3)
print(Z)

# 10*10的随机数组，并找到对应的 最大和最小值
Z = np.random.randn(10,10)
Z_min, Z_max = Z.min(), Z.max()
print('Z_min %.2f, Z_max: %.5f' % (Z_min, Z_max))

# 对于 一个存在的数组，添加一个用0填充的边界
Z = np.zeros((5,5))
Z = np.pad(Z,pad_width=1, mode='constant', constant_values=1)
print(Z)

print(0.3 == 3*0.1, np.nan - np.nan, np.inf > np.nan, np.nan == np.nan)

#  创建一个 5x5的矩阵，并设置值1,2,3,4落在其对角线下方位置
val = 1 + np.arange(4)
print(val)
Z = np.diag(val, k=1)
print(Z)

print('*'*100)

# 19. 创建一个8x8 的矩阵，并且设置成棋盘样式 (★☆☆)
Z = np.zeros((8,8))
Z[1::2, ::2] = 1
Z[::2,1::2] =1

print(Z)

z_index = np.unravel_index(100, (6,7,8))
print(z_index)

# 用tile函数去创建一个 8x8的棋盘样式矩阵(★☆☆)
Z = np.tile(np.array([[0,1], [1,0]]), (4,4))
print(Z)

# 对一个 5x5 的随机矩阵做归一化
Z = np.random.random((5,5))
Z_max, Z_min = Z.max, Z.min

# print((Z - Z_min) / (Z_max - Z_min))

# color = np.dtype([('r',np.nbytes,1),('g',np.nbytes,1),('b',np.nbytes,1),('a',np.nbytes,1)])
# print(type(color))

# 5x3 与一个 3x2的矩阵 乘积是：
a = np.ones((5,3))
b = np.ones((3,2))
# print(a,b, sep='\n')
ret = np.dot(a,b)
print(ret, ret.shape )

# 给定一个一维数组，对齐在 3 - 8之间的所有元素取反
Z = np.arange(11)
Z[ (3<Z) & (Z<=8) ] *= -1
print(Z)



