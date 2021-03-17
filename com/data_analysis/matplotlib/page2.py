'''
调整 图片的大小
'''
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


xArr = range(0,120)
# 生成 120个元素， 范围在[20,35)
yArr = [random.randint(20,35) for i in range(120)]


#另外一种设置字体的方式
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


# 设置图片大小
# figsize: tuple of integers width, height;  dpi: integer
plt.figure(figsize=(20,8),dpi=80)
plt.plot(xArr,yArr)

# 调整x轴的刻度
step = 10
x_list = list(xArr)
xtick_label_list = ["10点{}分".format(i) for i in range(60)]
xtick_label_list += ["11点{}分".format(i) for i in range(60)] # += 为累加 集合
plt.xticks(x_list[::step],xtick_label_list[::step],rotation=20)  # rotation 倾斜度


plt.show()

