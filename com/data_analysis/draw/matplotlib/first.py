'''
 matplotlib 初步
 将数据进行可视化
'''

from matplotlib import  pyplot as plt

# x 轴的坐标点, 作为 时间轴
x = range(2,26,2)
# y轴作为每个时间点 对应的温度值
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

# 绘图
plt.plot(x,y)

# 展示图形
plt.show()






