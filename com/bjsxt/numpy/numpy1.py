'''

NumPy（Numerical Python的缩写）是一个开源的Python科学计算库。
    使用NumPy，就可以很自然地使用数组和矩阵。 NumPy包含很多实用的数学函数，
    涵盖线性代数运算、傅里叶变换和随机数生成等功能。


    NumPy的主要对象是同种元素的多维数组。这是一个所有的元素都是一种类型。

    在NumPy中维度(dimensions)叫做轴(axes)，轴的个数叫做秩(rank)。NumPy的数组类被称作 ndarray（矩阵也叫数组） 。通常被称作数组。

    常用的ndarray对象属性有：ndarray.ndim(数组轴的个数,轴的个数被称作秩)，ndarray.shape(数组的维度。这是一个指示数组在每个维度上大小的整数元组。
    例如一个n行m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性)，ndarray.size（数组元素的总个数，等于shape属性中元组元素的乘积）

'''

import numpy as np

# 类型
a = np.dtype(np.int_)
print(a)
print(np.dtype('i8'))

# 用np.array从python列表和元组创建数组
arr = np.array([[1,2,3],[4,5,6]], dtype=int)
# shape 为两行三列的二维数组_ （2,3）—— [[1 2 3] [4 5 6]]
print(arr, arr.shape)

# 使用 arange().reshape()创建数组(矩阵)

# 创建一个 2行5列的数组
arr = np.arange(10).reshape(2,5)

# 范围  0-11， shape的每个元素乘积和 需等于 size 12
arr = np.arange(12).reshape(2,3,2)
print(arr)

# 判断下列三维数组的shape:
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #(1, 3, 3)
print(arr.shape)

arr = np.array([[[1,2,3]], [[4, 5, 6]], [[7, 8, 9]]])  # 3 1 3
print(arr.shape)

# 基本运算
a = np.random.random(6)
b = np.random.rand(6)
c = np.random.randn(6)
print(a)
print(b)
print(c)

# 创建矩阵
arr = np.array([1,2,3])
print(arr.ndim, arr.shape, arr.size)  # 轴 1;  (3,), 3

# 3, (3,2,2), 12
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]], [[9,10],[11,12]]])
print(arr.ndim, arr.shape, arr.size)

# 使用arrange 创建数组, 左闭右开 (左边包含临界值)
# 参数列表： ( start, stop, step , dtype)
arr = np.arange(1,10).reshape(3,3)
print(arr.ndim, arr.shape, arr.size, arr)

# 产生12 个数字，范围[0-12], 个数为: 2*2*3
# 注： reshape 的乘积 需等于  12;  cannot reshape array of size 12 into shape (2,2,4)
arr = np.arange(1,13).reshape(2,2,3)
print(arr.ndim,arr.size,arr)

print('*'*100)

# 通过随机数，生成矩阵 [low,high)范围内生成随机数.
# np.random.randint( [low,high) , size, dtype)
arr = np.random.randint(1,10,12).reshape(2,2,3)
print(arr.ndim,arr.size,arr.shape,arr)

# 概率论： [0,1) 均匀分布  Uniformly distributed values.
arr = np.random.rand(9).reshape(3,3)
print(arr)

# 概率论： Normally distributed values 标准正态分布
arr = np.random.randn(9).reshape(3,3)
print(arr)

# 通过固定值生成数组

# empty 是 无限趋近于0
arr = np.empty(9).reshape(3,3)
print(arr)
print('*'*100)

arr = np.ones(9).reshape(3,3)
print(arr)

arr = np.zeros(9).reshape(3,3)
print(arr)

arr = np.empty((2,3))
print(arr)

# where 筛选条件运用: condition, arr, defaultValue
arr = np.random.randint(1,10,9).reshape(3,3)
print(np.where(arr>5, arr, 0.1))

# 遍历数组
print(arr, arr[2][2])

# 切片  [ 行, 列]: [start_row:end_row:step_row,  start_col:end_col:step_col]
# [1,10) size:16;
arr = np.random.randint(1,10,16).reshape(4,4)
print(arr)

print('*'*100)

# 取出第一行的所有值
print(arr[0])
# 取第一列： 行数取所有行, 列取第一个
print(arr[:,0])

# 取第一行和第三行
print(arr[0::2,])

print('*'*100)
# 取第二行和 第四列
print(arr[1::3,3::])

print('*'*100)
# 取第二列和 第四列
print(arr[::,1::2])

print('*'*100)
# 取 第一行和第三行的  第二/四列
print(arr)
print(arr[::2,1::2])

print('*'*100)


c = np.random.randn(6)
print(c)