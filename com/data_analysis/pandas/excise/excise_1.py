import pandas as pd
import numpy as np



df = pd.DataFrame({
    'animal': 'cat dog fish cat dog cat cat'.split(),
    'size': list('LSMMSLM'),
    'weight':[60,20,12,11,9,9,10],
    'adult':[False]*5 + [True]*2
})

def GrowUp(x):
    """
    应用 一组group的df
    :param x: 一组group的df
    :return:
    """
    avg_weight = sum(x[x['size']=='S']['weight']*1.5)
    avg_weight += sum(x[x['size']=='M']['weight']*1.25)
    avg_weight += sum(x[x['size']=='L']['weight'])
    avg_weight /= len(x)   # 除以 数量
    return pd.Series(['L',avg_weight,True],index=['size','weight','adult'])

ret = df.groupby(['animal']).apply(GrowUp)
print(ret)

print('*'*100)

import functools

s = pd.Series([i/100.0 for i in range(1,11)])

def cum_ret(x,y):
    return x* (1+y)

def red(x):
    return functools.reduce(cum_ret,x,1.0)


ret = s.expanding().apply(red,raw=True)
print(ret)

print('*'*100)


df = pd.DataFrame({"A": [1, 1, 2, 2], "B": [1, -1, 1, 2], 'c':[1,2,3,4]})
print(df)

def replace(g):
    mask = g < 0
    return g.where(mask, g[~mask].mean())

gb = df.groupby('A')
# for val,df in gb:
#     print(val, df,sep='\n')
#     print('----')

df[['t_b','tt_c']] = gb.transform(replace)

print(df)

print('*'*100)

# transform doc
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two'],
                   'C' : [1, 5, 5, 2, 5, 5],
                   'D' : [2.0, 5., 8., 1., 2., 9.]})
print(df)

def standard_values(series):
    """
    按列 分割， 传递每组的值 - 向量化
    :param series:
    :return:
    """
    return (series - series.mean()) / series.std()

grouped = df.groupby('A')
print(grouped.get_group('foo'), grouped.get_group('bar'), sep='\n')
# df 的向量化操作 -  标准化处理，  x-u/s  , s 为标准差
# note: 由于B列为字符串，因此无法标准化处理， 只能返回 C和D的转换参数
df[['C_TR','D_TR']] = grouped.transform(standard_values)
print(df)

# return a scalar, then broadcast result of the transformation
df[['C_DV','D_DV']] = grouped.transform(lambda x : x.max()/x.min())
print(df,f'当前使用内存量: {df.memory_usage().sum()} bytes' ,df.info(), sep='\n')
print('*'*100)

# Sort groups by aggregated data
df = pd.DataFrame(
    {
        "code": ["foo", "bar", "baz"] * 2,
        "data": [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],
        "flag": [False, True] * 3,
    }
)
gb = df.groupby('code')
df['data_g_sum'] = gb[['data']].transform(sum)
print(df)
df.sort_values(by='data',inplace=True)
print(df)


# Create a value counts column and reassign back to the DataFrame
df = pd.DataFrame({
    'Color':'red red red blue'.split(),
    'Value':[100,150,50,50]
})
print(df)

df['count'] = df.groupby('Color',as_index=False).transform(len)
# df['count'] = df.groupby('Color').transform('count')
print(df)

print('*' * 100)


df = pd.DataFrame(
    data={
        "Case": ["A", "A", "A", "B", "A", "A", "B", "A", "A"],
        "Data": np.random.randn(9),
    }
)
print(df)

# Partial sums and subtotals
df = pd.DataFrame(
    data={
        "Province": ["ON", "QC", "BC", "AL", "AL", "MN", "ON"],
        "City": [
            "Toronto",
            "Montreal",
            "Vancouver",
            "Calgary",
            "Edmonton",
            "Winnipeg",
            "Windsor",
        ],
        "Sales": [13, 6, 16, 8, 4, 3, 1],
    }
)
print(df)

print('*' * 100)

import datetime
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
    }
)
print(df)

# We can produce pivot tables from this data very easily:
pivot_ret = pd.pivot_table(df, values='D', index=['A','B'],columns=['C'])
print(pivot_ret)

pivot_ret = pd.pivot_table(df, values="D", index=["B"], columns=["A", "C"], aggfunc=np.sum)
print(pivot_ret)






















