'''
 How to create plots in pandas?  如何创建 图表
    绘制图表
'''

import pandas as pd
import matplotlib.pyplot as plt

#  the first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp objects
df = pd.read_csv('../../../data/air_quality_no2.csv',index_col=0,parse_dates=True)
print(df.head())

# I want a quick visual check of the data.
print(df.plot())

