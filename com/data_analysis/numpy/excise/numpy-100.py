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

#


