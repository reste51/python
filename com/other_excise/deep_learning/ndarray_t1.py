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

# dot 做矩阵的乘法,



