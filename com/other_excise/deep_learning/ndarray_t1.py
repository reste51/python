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
