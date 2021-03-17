"""
 rating 和 runtime的分布图

  “ / ” 为浮点数除法，返回浮点结果
  “ // ” 表示整数除法，返回不大于结果的一个最大整数

    bar图： 数据和组数

"""
import  pandas as pd
import  numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('./data/IMDB-Movie-Data.csv')
# print(df,df.info(),sep="\n")

# runtime_s = df["Runtime (Minutes)"]
runtime_s = df["Rating"]
interval = .5
# print(runtime_s, type(runtime_s))
max_runtime = runtime_s.max()
min_runtime = runtime_s.min()

# 计算组的数量， 极值为125， 因此选5的倍数
num_bin = (max_runtime- min_runtime) //interval

# print('runtime的极值为：%s '%(max_runtime- min_runtime))

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)
plt.hist(runtime_s, num_bin)  # 传入数据和组数

# 设置x轴的数据_  start:min, stop:max, step: interval
plt.xticks(range(min_runtime,max_runtime,interval))

plt.show()

