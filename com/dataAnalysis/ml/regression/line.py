"""
    回归：连续目标值，可划分， 如：预测房价，销售业绩，贷款额度
    线性回归： y = k *x +b

"""

import matplotlib.pyplot as plt


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
    draw_point()
