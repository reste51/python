"""
    星巴克统计
        1.使用matplotlib呈现出店铺总数排名前10的国家
        2.使用matplotlib呈现出每个中国每个城市的店铺数量  - 第二个问题

"""
import pandas as pd
from matplotlib  import  pyplot as plt

# 注： 显示全部列
pd.set_option('display.max_columns', None)

all_df = pd.read_csv('../data/starbucks_store_worldwide.csv')

# 1. 先获取 中国的国家, 再按照 City分组
#  select count(Brand) from starbars where Country='CN' group by City
cn_df = all_df[all_df['Country'] == 'CN']
ret_df = cn_df.groupby(by='City').count()['Brand'].sort_values(ascending=False).head(10)
print(ret_df)

# 绘制图表 离散数据:使用 Bar图
x_arr = ret_df.index
y_arr = ret_df.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(x_arr,y_arr)
# plt.bar(x_arr,y_arr,width=0.4,color='orange',label="starbars distribute map")  # 传入x,y 轴的数组
plt.show()





