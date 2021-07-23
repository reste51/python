"""
    现在我们有全球排名靠前的10000本书的数据，那么请统计一下下面几个问题：
        1.不同年份书的数量
        2. 不同年份书的平均评分情况

"""
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

all_df = pd.read_csv('../data/books.csv')
print(all_df.info(),all_df[:1], sep='\n')

year_label = 'original_publication_year'
nonone_label = 'title'

# 1.不同年份书的数量 _ 注: 先排除不为 Nan的数据
df = all_df[pd.notna(all_df[year_label])]
ret_s = df.groupby(by=year_label)[nonone_label].count().sort_values(ascending=False).head(8)
# print(ret_s, type(ret_s))
# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(ret_s.index,ret_s.values,width=0.4,color='orange')
# plt.xticks(range(len(ret_s.index)), ret_s.index)
# plt.show()
# print(range(len(ret_s.index)), ret_s.index)
# print(all_df[year_label][:5])

# 2. 不同年份书的平均评分情况
# 2.1 先去空值的df; 获取 average_rating这一列(Series)
# 2.2 以年份year分组  (但没数据_需要提供year该列Series的数据, 会以 index 进行关联rating 列值,  --> 平均值
mean_df =  df['average_rating'].groupby(by=df[year_label]).mean()
x_arr = mean_df.index
y_arr = mean_df.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(x_arr)),y_arr)

# 设置x 轴坐标,  list 才能做切片,  取step 10( 以年度划分);   倾斜度; 将x轴的float类型转为Int
plt.xticks(range(len(x_arr))[::10], x_arr[::10].astype(int),rotation=45)
# plt.xticks(list(range(len(x_arr)))[::10],x_arr[::10].astype(int),rotation=45)

plt.show()



