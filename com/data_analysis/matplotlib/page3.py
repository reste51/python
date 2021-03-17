'''
在 同一个画布中 绘制两张 散点图

显示 3 和10月的气温
'''

from matplotlib import pyplot as plt
from matplotlib import  font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/Hiragino Sans GB.ttc")

# 3 和 10月的气温值
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# 3 10月的日期 (每个月均是 31天)
x_3 = range(1,32)
# 注: [51,82);  为了使 3月和10月在用一个x轴上，  间隔增大
x_10 = range(51,82)

# 设置图像大小
plt.figure(figsize=(20,8),dpi=60)

# plt.scatter(x_3,y_3)  # 绘制散点图
# 使用scatter方法绘制散点图,和之前绘制折线图的唯一区别
plt.scatter(x_3,y_3,label="3Month")
plt.scatter(x_10,y_10,label="10Month")

# 添加图例
plt.legend(loc="upper left")
# plt.legend(loc="best")

# 添加描述信息
plt.xlabel("date")
plt.ylabel("temperature")
plt.title("title")

plt.show()



