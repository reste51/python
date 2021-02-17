"""
    回归：连续目标值，可划分， 如：预测房价，销售业绩，贷款额度
    线性回归： y = k *x +b

    矩阵乘法： (m行 * l列) * (l行, n列 ) = （m行 * n列）

"""
import numpy as np
import matplotlib.pyplot as plt


def matrix():
    """
    矩阵的乘法
    shape的推断: shape是从外到内(从高维度到低维度)数的， 如果没有值则 空格 () 或 (4,)
    矩阵的乘法--> 满足线性运行需求，y1(目标值) = x1(特征值) * w1(权重)
    :return:
    """
    # shape的推断：
    # arr = np.array(1)  # numpy.ndarray
    # arr = np.array([[1], [1]])
    # arr = np.array(  [ [1,2,3],[4,5,6] ] ) # (2,3)
    # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # (2,2,3)
    # print(arr.shape)

    # 矩阵的乘法: 满足线性运行需求，y1(目标值) = x1(特征值) * w1(权重)
    samples = np.array([[2, 3, 5], [11, 33, 22], [10, -1, 2]])  # 样本数3, 特征数3, (3,3)
    # weight = np.array([2, 2, 2])  # 映射每个特征的权重值,与 样本的特征数匹配;  (3,)
    # 注：这个相乘是样本的每个特征值与 权重相乘，返回的还是具有3个特征的样本,不符合我们的要求(1个目标值)
    # targets = np.multiply(samples, weight)

    # weight = np.array([2, 2, 2])  # 映射每个特征的权重值,与 样本的特征数匹配;  (3,3) * (3,) = (3,); dot 结果为1维
    weight = np.array([[2], [2], [2]])  # (3,3) * (3,1) = (3,1)
    # dot 是矩阵的相乘， samples决定了最后运算值的个数(取决于 样本_行数), weights决定最后结果维度
    targets = np.dot(samples, weight)

    print(targets)


def draw_point():
    """
  绘制点状图
  :return: None
  """
    # 1.设置面板大小
    plt.figure(figsize=(10, 10))

    # 2.设置数据, 传入特征值 和 目标值
    # y = x * 2.1; k值为 2.1
    plt.scatter([60, 72, 75, 80, 83], [126, 151.2, 157.5, 168, 174.3])

    # 3.显示
    plt.show()


if __name__ == '__main__':
    # draw_point()
    matrix()
