"""
    星巴克统计
        1.使用matplotlib呈现出店铺总数排名前10的国家
        2.使用matplotlib呈现出每个中国每个城市的店铺数量

    10:00
"""
import pandas as pd

# 注： 显示全部列
pd.set_option('display.max_columns', None)

starbucks_df = pd.read_csv('../data/starbucks_store_worldwide.csv')

# print(starbucks_df.info(), starbucks_df.head(5), sep='\n')

# 1. 店铺总数排名前10的国家,  select count(Brand) from t group by Country；
df = starbucks_df.groupby(by='Country').count()[['Brand']]        # 返回时DF, sort_values(by='col')
# df = starbucks_df.groupby(by='Country').count()['Brand']       # 返回的是Series, sort_values()无需指定列

# print(type(df), df)

# sort value desc
# ret_10 = df.sort_values(ascending=False).head(10)     # df为Series类型
# ret_10 = df.sort_values(ascending=False,by='Brand').head(10)    # df 为DF， 需指定列( 与 Count的字段一致)

# 通过 数字下标的方式取
ret_10 = df.sort_values(ascending=False,by='Brand')[:10]    # head(10)
print(ret_10)

print('*'*100)

# 2.每个国中每个城市的店铺数量  Country / City
# print(type(ret_10))





