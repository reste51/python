"""
    DF中缺失数据
        判断：  pd.notna()  与 isna 相反
        删除： df2.dropna(axis=0,how='all', inplace=False)
        填充缺省值（一般使用中间值填充） ：df2.fillna(df2.mean())

        注：0是参与中间值的计算，但 Nan不会,计算时直接忽略。

    ----
    dropna(axis=0,how="any") --》 参考源码

    axis : {0 or 'index', 1 or 'columns'}, default 0
        0, or 'index' : Drop rows which contain missing values.
        1, or 'columns' : Drop columns which contain missing value.
    how : {'any', 'all'}, default 'any'
            Determine if row or column is removed from DataFrame, when we have
            at least one NA or all NA.

            * 'any' : If any NA values are present, drop that row or column.
            * 'all' : If all values are NA, drop that row or column.

    inplace : bool, default False    原地操作, 直接修改当前对象的值，返回None
            If True, do operation inplace and return None.


"""
import numpy as np
import pandas as pd

# df = pd.read_csv('./dogNames2.csv')

# 是否为NAN

# Detect missing values for an array-like object.
print(pd.isna('Dog'), pd.isna(np.nan))  # False True

array = np.array([[1, np.nan, 3], [4, 5, np.nan],[np.nan,np.nan,np.nan],[10,6,7]])
# print(array.shape)  # (2,3)
print(pd.isna(array))   # [[False  True False] [False False  True]]

# pd.notna()  与 isna 相反

print('*'*100)

# 通过Boolean索引获取不为 null的值
# 满足w列中, 不为null的  行,  返回的是 行
# df[pd.notnull( df["w"])]
df2 = pd.DataFrame(array,columns=list('abc'))
print(df2)

# 筛选 a b 两列均不为空的情况
not_row_df = df2[ (pd.notna( df2['a'])) &(pd.notna( df2['b'])) ]
print(not_row_df,type(not_row_df))

# 删除NAN

# all 为某行或列全部为NAN才会删除, any 出现一次则会删除
df_drop_na = df2.dropna(axis=0,how='all', inplace=False)
print(df2)

# 填充数据-- 14:08; @返回被替换的df 或 series
# 全部替换: 将指定的值 替换为原有的Nan;一般会填充某一列的均值
df_filledna = df2.fillna(df2.mean())
print(df_filledna)

print('*'*100)

# 指定的列替换, 返回的是 Series
df2['c'] = df2['c'].fillna(df2['c'].mean())
print(df2)

# 17:00
