"""
 分组 学习
 file:///D:/soft/python/module_package/pandas/doc/1.3.3/user_guide/groupby.html#splitting-an-object-into-groups
"""

import pandas as pd
import numpy as np


def split_objects_into_groups():
    df = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )
    print(df)
    grouped = df.groupby('A')
    print(grouped.sum())
    grouped = df.groupby(['A','B'])
    print(grouped.sum())
    print('*' * 100)

    # multiple index
    arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],['Captive', 'Wild', 'Captive', 'Wild']]
    index = pd.MultiIndex.from_arrays(arrays, names=['animal', 'type'])
    df_m = pd.DataFrame(data={'Max Speed': [390., 350., 30., 20.]}, index= index)
    print(df_m)
    print(df_m.groupby(level=0).mean())  # 也就是 以animal 索引分组
    print(df_m.groupby(level='type').mean())


if __name__ == '__main__':
    split_objects_into_groups()





