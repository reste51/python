"""
    Melt
    参考连接:
    file:///D:/soft/python/module_package/pandas/doc/1.3.3/user_guide/reshaping.html#reshaping-by-melt
"""

import pandas as pd
import numpy as np


def melt_t():
    """
    Melt分两部:
    1. 指定的是标识符列
    2. 剩余的为 参数的变量名

    进而生成两个列：1. 引用-2作为参数的列，  2. 参数值( 2对应的列值)
    这两个列可以用: var_name and value_name 自定义列名
    :return:
    """
    cheese = pd.DataFrame({
        'first': ['John', 'Mary'],
        'last': ['Doe', 'Bo'],
        'height': [5.5, 5.0],
        'weight': [130, 150],
    })

    melt_df = pd.melt(cheese, id_vars=['first', 'last'], var_name='indicator')
    print(melt_df)


def melt_ignore_index():
    """
    melt 后保持原先的索引数据
    :return:
    """
    index = pd.MultiIndex.from_arrays([['person','person'],['A','B']])
    cheese = pd.DataFrame({
        'first': ['John', 'Mary'],
        'last': ['Doe', 'Bo'],
        'height': [5.5, 5.0],
        'weight': [130, 150],
    }, index=index)
    df = cheese.melt(id_vars=['first','last'], var_name='indicator')
    print(df)
    df = cheese.melt(id_vars=['first','last'], var_name='indicator',ignore_index=False)
    print(df)


def wide_to_long_test():
    dft = pd.DataFrame(
        {
            "A1970": {0: "a", 1: "b", 2: "c"},
            "A1980": {0: "d", 1: "e", 2: "f"},
            "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
            "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
            "X": dict(zip(range(3), np.random.randn(3))),
        }
    )
    dft['id'] = dft.index
    print(dft)
    df = pd.wide_to_long(dft,['A','B'],i='id',j='year')
    print(df)


def get_df():
    columns = pd.MultiIndex.from_tuples(
        [
            ("A", "cat"),
            ("B", "dog"),
            ("B", "cat"),
            ("A", "dog"),
        ],
        names=["exp", "animal"],
    )

    index = pd.MultiIndex.from_product(
        [("bar", "baz", "foo", "qux"), ("one", "two")], names=["first", "second"]
    )

    df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=columns)
    # print(df)
    return df

def combine_group():
    df = get_df()
    print(df)
    # print(df.stack(1).mean(1).unstack())

    # 不同的方法， 同样的结果
    # print(df.groupby(level=1, axis=1).mean())
    # print(df.mean(0).unstack())
    # print(df.stack().groupby(level=1,axis=0).mean())

    print(df.stack(-1).groupby(level=1).mean())


if __name__ == '__main__':
    # melt_t()
    # melt_ignore_index()
    # wide_to_long_test()
    # get_df()
    combine_group()



