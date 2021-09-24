"""
 分组 学习
 file:///D:/soft/python/module_package/pandas/doc/1.3.3/user_guide/groupby.html#splitting-an-object-into-groups
"""

import pandas as pd
import numpy as np


def get_letter_type(column):
    """
    通过列名 来分组
    :param column:
    :return:
    """
    if column.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'


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


def hive_t():
    from pyhive import hive
    from sqlalchemy.engine import create_engine
    engine = create_engine('hive://user:pass@10.133.12.33:1000/bigdata', connect_args={'auth': 'LDAP'})
    print(engine.connect())


def integer_indexing():
    s = pd.Series(range(5))
    # print(s[-1:])  s[-1]  会报错
    df = pd.DataFrame(np.random.randn(5,4))
    print(df.loc[-2:])


if __name__ == '__main__':
    integer_indexing()
    # split_objects_into_groups()
    # df = pd.DataFrame(
    #     {
    #         "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
    #         "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
    #         "C": np.random.randn(8),
    #         "D": np.random.randn(8),
    #     }
    # )
    # g = df.groupby(get_letter_type, axis=1)
    # print(g.group_keys)







