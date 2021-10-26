"""
Pivot tables
"""
import pandas as pd
import numpy as np
import datetime


def get_df():
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
    return df


def test():
    df = get_df()
    print(df)
    p_df = pd.pivot_table(df, values='D',index=['A','B'],columns='C')
    print(p_df)

def test_2():
    counts = pd.Series()
    df = get_df()
    print(df['C'].value_counts())
    counts = counts.add(df['C'].value_counts(), fill_value=0)
    print(counts.memory_usage())
    counts = pd.to_numeric(counts, downcast='unsigned')
    print(counts.memory_usage())


if __name__ == '__main__':
    # test()
    test_2()
    # print(get_df())





