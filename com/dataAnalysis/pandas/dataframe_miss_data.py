"""
    DF中缺失数据


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

df = pd.read_csv('./dogNames2.csv')

# 是否为NAN
# pd.isnull(df)

# pd.notnull


# 获取不为 null的值

# 满足w列中, 不为null的  行,  返回的是 行
# df[pd.notnull( df["w"])]


# 删除NAN


df.dropna(axis=0,how="any")

# 填充数据-- 14:08



