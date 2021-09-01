from mxnet import nd

"""
    操作教程：
    https://zh.d2l.ai/chapter_prerequisite/ndarray.html
    
    
"""

# 使用 arrange 创建一个 行向量
x = nd.arange(12)
print(x, x.shape, x.size)

# 将一行向量转为  3行4列的矩阵
X = x.reshape(3, 4)
X_1 = x.reshape(-1, 4)  # -1 标识可 推导的数值为 3
print(X, X_1, sep='\n')

# 接下来，我们创建一个各元素为0，形状为(2, 3, 4)的张量。
# 实际上，之前创建的向量 vector和矩阵matrix都是特殊的 张量 tensor。
tensor_1 = nd.zeros((2, 3, 4))
print(tensor_1)

# 创建 元素为1 的张量
tensor_2 = nd.ones((3, 4))
print(tensor_2)

# 传入 python list 指定创建NDArray的每个元素的值
Y = nd.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(Y)

# 随机生成每个元素的值，每个值采样于 均值为0/ 标准差为1的正态分布
X = nd.random.normal(0,1,shape=(3,4))
print(X)

# import numpy as np
# np.std # np.var

# 运算
print('#' * 100)


# 加法: 两个形状相同的的元素相加， 形状不变
Z= X + Y
print(Z, X*Y, X/Y, X-Y ,sep='\n')

X = nd.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
# 指数的运算,  每个幂运算元素 e x幂，  2 -> e^2,  e为 2.718
print(X.exp())

# dot 做矩阵的乘法, 下面将X与Y的转置做矩阵乘法。由于X是3行4列的矩阵，Y转置为4行3列的矩阵，因此两个矩阵相乘得到3行3列的矩阵。
X = x.reshape(3, 4)
Y = nd.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(X, Y.T, sep='\n')

print(nd.dot(X,Y.T))

# concatenate ，指定维度的连接
print(nd.concatenate([X,Y],axis=0))  # 以行的维度连接   6x4
print(nd.concatenate([X,Y], axis=1)) # 列的连接         3x8

# 条件判断 , 1true, 0 反
print(X == Y)

# 所有元素的求和， 只获取一个元素
print(X.sum())

# 矩阵 转换成 一个标量
print(X.norm().asscalar())

# 广播机制， 对于两个形状不同的NDArray, 触发 广播 broadcasting
# 先适当复制元素使这两个NDArray形状相同后再按元素运算。
# 其实就是 拟合成形状相同的矩阵再做运算, 产生的结果就是  3x2列， 对自身数据进行复制
A = nd.arange(3).reshape((3,1))  # 3 x 1
B = nd.arange(3).reshape((1,2))  # 1 x 2
print(A, B)
print('index' * 10)

# 索引  切片
print(X)
# 行的索引截取
print(X[1:3])

# 访问 单个元素的位置， 并赋值
X[1,2] = 999
print(X)

# 赋值 一部分值



