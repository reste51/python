"""
    DataFrame has the methods add(), sub(), mul(), div()
    and related functions radd(), rsub(), … for carrying out binary operations.
    For broadcasting behavior, Series input is of primary interest. Using these functions,
    you can use to either match on the index or columns via the axis keyword.


"""
import pandas as pd
import numpy as np


def sub_t():

    df = pd.DataFrame(
        {
            "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
            "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
            "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
        }
    )

    print(df)
    # 取 第二行_ index 为b,  返回的是Series
    row = df.iloc[1]

    # 返回的也是 Series
    column = df['two']

    # print(type(row), type(column))

    # 注: 删除的列 与 axis的方向相反

    # 抹去第二行的值，成为默认值 0.00
    print(df.sub(row, axis='columns'))
    print(df.sub(row, axis=1))

    print('*' * 100)

    # 删除某一列
    print(df.sub(column, axis=0))
    print(df.sub(column, axis='index'))


def value_counts():
    """
        对 Series 或 普通的数组进行 数量统计
        Return a Series containing counts of unique values.
    :return:
    """
    data = np.random.randint(0,7, 50)
    # series
    ret = pd.Series(data).value_counts()
    print(ret)

    # regular array
    ret2 = pd.value_counts(data)
    print(ret2)

if __name__ == '__main__':
    value_counts()



