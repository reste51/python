"""
    星巴克统计
        1.使用matplotlib呈现出店铺总数排名前10的国家   -- 第一个问题
        2.使用matplotlib呈现出每个中国每个城市的店铺数量

    10:00
"""
import pandas as pd
from matplotlib  import  pyplot as plt

# 注： 显示全部列
pd.set_option('display.max_columns', None)

starbucks_df = pd.read_csv('../data/starbucks_store_worldwide.csv')
# print(starbucks_df.info(), starbucks_df.head(5), sep='\n')

# 1. 店铺总数排名前10的国家,  select count(Brand) from t group by Country；
df = starbucks_df.groupby(by='Country').count()['Brand']       # 返回的是Series, sort_values()无需指定列

# print(type(df), df)

# sort value desc
ret_10 = df.sort_values(ascending=False).head(10)     # df为Series类型_  获取行 ->通过 数字下标的方式取  [:10]

# 绘制图表 离散数据:使用 Bar图
x_arr = ret_10.index
y_arr = ret_10.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(x_arr,y_arr,width=0.4,color='orange',label="starbars distribute map")  # 传入x,y 轴的数组
plt.show()

print('*'*100)





