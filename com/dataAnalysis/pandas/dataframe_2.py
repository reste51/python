"""
    DataFrame的取 行和 列的索引方法
        1. 方括号 写数组, 标识取行, 对行操作
        2. 方括号 写字符串， 取列， 对列操作
            2.1  取多个列使用 [["a","f"]]，嵌套[]方式获取

    df.loc 标签(字符串)获取
    df.iloc 通过position(位置)获取
"""

import  pandas as pd
import  numpy as np

arr = np.arange(50,100).reshape(5,10)
df = pd.DataFrame(arr,columns=list('abcdefghij'))

print(df)

print('*'*100)

# 取前2行- 返回 DF
print(df[:2])

# 取前4行的a列  -> Series类型
col_ret = df[:4][["a","d"]]
print(col_ret, type(col_ret))


# TODO 03dataFrame的索引 - 8:00

# df.loc 标签(字符串)获取
# df.loc["row_label","col_label"]

# 取行 --> 列

# 取某一行, 全部列 - Series类型, 注：此时的col会转为 index显示

# 取某一列，全部行 --Series类型

# 取多行....



# df.iloc 通过position(位置)获取




