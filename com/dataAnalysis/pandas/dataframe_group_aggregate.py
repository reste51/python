"""
    Pandas的分组和聚合
    问题:
    现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，
        或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？

    groupby() - 返回的对象:
    1. 可遍历: 每个元素为 tuple: (group_col_val, DF(出现该值的记录))
    2. 调用聚合方法count()



"""
import pandas as pd

starbucks_df = pd.read_csv('./data/starbucks_store_worldwide.csv')

# print(starbucks_df.info(), starbucks_df.head(1), sep="\n")

# 返回DataFrameGroupBy
grouped = starbucks_df.groupby(by="Country")

# 1.遍历: 每个元素为tuple,  (group_col_val, DF)
# for col_val,df in grouped:
#     print(col_val)
#     print('*'*100)
#     print( df[['Country','Store Number']])
#     print('-'*100)

# 2.调用聚合函数_ 默认会把每个列都会 聚合(select count(*) _ group by Country)
# grouped_df = grouped.count()  # count(*)  return DF
grouped_df = grouped["Country"].count()  # count('Country')  指定字段列值分组(尽量选非空值的列) return Series

# print(grouped_df, type(grouped_df))

# 获取索引名为 US 和 CN的数据
us_count = grouped_df.loc['US']
cn_count = grouped_df.loc['CN']
print(f'us_count is  {us_count}, cn_count is {cn_count}')

