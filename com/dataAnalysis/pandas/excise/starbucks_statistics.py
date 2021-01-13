"""
    星巴克统计
        1.使用matplotlib呈现出店铺总数排名前10的国家
        2.使用matplotlib呈现出每个中国每个城市的店铺数量

"""
import pandas as pd

starbucks_df = pd.read_csv('../data/starbucks_store_worldwide.csv')

print(starbucks_df)

