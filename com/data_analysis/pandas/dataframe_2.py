"""
    DataFrame的取 行和 列的索引方法
        1. 方括号 写数组, 标识取行, 对行操作
        2. 方括号 写字符串， 取列， 对列操作
            2.1  取多个列使用 [["a","f"]]，嵌套[]方式获取

    行获取的方式:
    df.loc 标签(字符串)获取
    df.iloc 通过position(位置)获取
"""

import  pandas as pd
import  numpy as np

arr = np.arange(50,100).reshape(5,10)
df = pd.DataFrame(arr,columns=list('abcdefghij'))

# 取前2行- 返回 DF
print(df[:2])

# 取前4行的a列  -> Series类型
col_ret = df[:4][["a","d"]]
print(col_ret)

print('*'*100)
print(df)

#  numpy 的方式获取
print(df[4:])

# 取某一列，全部行 --Series类型
print(df['a'])

# 取多行, 截取 slice index
print(df[1:4])

print('*'*100)

# df.loc 标签(字符串)获取
# df.loc["row_label","col_label"]
print(df.loc[1:3,'d'])      # 返回时一个Series 类型
print(df.loc[1:3,['d','j']]) # 取多行/多列 则为DF类型

# 取某一行, 全部列 - Series类型, 注：此时的col会转为 index显示
print(df.loc[1])

# 某一列 (所有行), index 行会从0开始
print(df.loc[:,'i'])

# 取多行,  列不用写时,默认取全部,   返回的是DF
print(df.loc[[2,4]])

# 取多列, 取全部行使用 :,
print(df.loc[:,['b','f']])

# 使用行/列切片的方式, 注:包含 stop的列
print(df.loc[2:4,'d':'f'])

print('*'*100)

# df.iloc 通过position(位置)获取
print(df.iloc[:2,5:]) # 切片, 2(exclude)行前, 5(include)列后

# nan 的赋值, 不会报错;  但numpy 时需要转为float类型
df.iloc[4] = np.nan
print(df)







