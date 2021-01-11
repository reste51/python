"""
    DF的数据合并
    类似 sql的  inner outer left, right 连接。


    1. 行合并: a.join(b)  相同的index才会合并一起,  当a 和b的行数不一致时, 以a的为准
        详情参考 join的源码 , a有的row b没有的row,则 列值会为Nan

    2. 列合并: a.merge(b)

    :returns joined : DataFrame

   15：00
"""
import pandas as pd
import numpy as np

# pd.DataFrame()

# 行合并_

# join-example

caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],'B': ['B0', 'B1', 'B2']})
print(caller, other,sep='\n')

# 1.1 重复列的标识, 此次key作为重复列, left_suffix 是左侧df的后缀名, right_suffix是右侧df后缀名
joined_df = caller.join(other, lsuffix='_caller', rsuffix='_other')
# print(joined_df)

# 1.2 使用某列进行 join
# 使用列名为key 作为索引名, Set the DataFrame index (row labels) using one or more existing columns.
joined_df = caller.set_index('key').join(other.set_index('key'))
# print(joined_df)

# 1.3 使用on 条件指定列名, 并保留caller的索引列
# 使用 caller的key列作为join, 但 other默认是使用index作为索引列,因此需要设置为key列索引
joined_df = caller.join(other.set_index('key'),on='key')
# print(type(joined_df))
# caller.merge


print('*'*100)

# 列的merge

df_0 = pd.DataFrame(np.zeros((2,4)),index=list('ab'),columns=list('ABCD'))
df_1 = pd.DataFrame(np.ones((3,3)),index=list('abc'), columns=list('ABC'))

df_0.loc['a','A'] = float(1)

print(df_0,df_1,sep='\n')


# 匹配A列中值相同的记录，并返回
# how: 默认是 内连接 inner(值相同)， outer(并集A ∪ B), left(以左侧的值为准,没匹配是Nan), right(以右侧为准)
# left ret.shape ( >= df_0.index, (df_0.columns+df_1.columns)-1 (去重复的列)
# suffixes是重复列名，左右DF所用的标识
ret_merge_df = df_0.merge(df_1, on="A",how='left',suffixes=('_0','_1'))
# shape:  outer (4,6), inner(3,6), left(4, 6), right(3, 6)

# print(ret_merge_df,ret_merge_df.shape)  # Empty DataFrame, 因为0 与1 A列的值没有交集
print(ret_merge_df, ret_merge_df.shape,ret_merge_df.columns)






