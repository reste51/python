"""
    初步学习数据绘画
    1. Figure 所有绘制图都在此处

"""
import  matplotlib.pyplot as plt
import numpy as np

def simple_line():
    """
    简单的线形图
    :return:
    """
    data = np.arange(10)
    plt.plot(data)
    plt.show()

def figure_1():
    """
    figure 学习
    :return:
    """
    # 创建 10*10的 面板
    figure = plt.Figure(figsize=(10,10))
    # 创建子图, 第三个参数为顺序order
    ax1 =figure.add_subplot(2,2,1)
    ax2 =figure.add_subplot(2,2,2)
    ax3 =figure.add_subplot(2,2,3)
    # 默认会在最后一个子图显示
    # 生成shape为(50,)的ndaaray, 创建线图
    # k-- 是黑色分段线的style_ 默认会使用最后一个ax3
    plt.plot(np.random.rand(50).cumsum(),'k--')

    # 直方图_柱状图
    ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
    # 散点图
    ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))

    plt.show()



if __name__ == '__main__':
    # simple_line()
    figure_1()
    # print( np.random.rand(50).cumsum())



