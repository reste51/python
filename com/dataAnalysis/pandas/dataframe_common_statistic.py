"""
    Pandas 的常用统计方法
"""
import pandas as pd

df = pd.read_csv('./data/IMDB-Movie-Data.csv')
# print(df.info())

# 获取评分的 平均分
score_mean = df['Metascore'].mean()
print(score_mean)

# 导演的人数
#  col -> list集合 -> set 去重 --> len()  取长度
director_num = len( set(df['Director'].tolist()))
print(director_num)

# 09-统计方法和字符串离散化 --》 02padas的常用统计方法 (05:17)


