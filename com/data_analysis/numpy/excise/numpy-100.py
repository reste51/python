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
