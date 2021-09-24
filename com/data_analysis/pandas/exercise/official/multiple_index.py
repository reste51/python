"""
    多重层次索引， 对于 复杂数据的分析 和 操作，特别针对 多维数据.

    创建: from_ arrays, tuples, set, frame
"""

import pandas as pd
import numpy as np

def create():
    """
    创建多级索引
    :return:
    """
    arrays = [
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ]
    # array -> tuples;  &arrays作用传递 两个 [],[]
    # [] [] -> zip -> tuple_generator -> list -> list: tuple
    tuples = list(zip(*arrays))

    index = pd.MultiIndex.from_tuples(tuples,names=['first', 'second'])
    # print(index)

    s = pd.Series(data=np.random.randn(8),index=index)
    print(s)

def create_with_others():
    """
    1.every pairing of the elements in two iterables
    2.data frame
    :return:
    """
    pd.option_context('display.multi_sparse',False)
    # 创建 索引的个数; 笛卡尔积 ->    4*2 = 8
    iterators = [['bar','baz','foo','qux'],['one', 'four']]
    m_index = pd.MultiIndex.from_product(iterators,names=['A','B'])
    print(m_index.names)

    # dataframe 创建
    df = pd.DataFrame(data=[['a','b'],['b','c'],['a','d'],['b','a','l']],columns=[1,2,3])
    m_index = pd.MultiIndex.from_frame(df)
    print(m_index)

    # 直接创建一个 ndarrray
    arrays = [
        np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
        np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
    ]
    # 单维度 - Series - vector
    s = pd.Series(data=np.random.randn(8),index=arrays)

    # 多维数据 - df， 索引最大行数只支持8行，因此只能 扩充列
    df = pd.DataFrame(data=np.random.randn(8,2), index= arrays, columns=['first','second'])

    print(df, df.index.names)

def m_index_any_axis():
    arrays = [
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(3,8), index=index[:3], columns=index)

    df = pd.DataFrame(data=np.random.randn(6,6), index=index[:6], columns=index[:6])

    print(df)
    # 获取 指定级别对应索引标签名
    print(index.get_level_values(1))
    print(index.get_level_values('first'))


def basic_index():
    """
    基础的检索
    :return:
    """
    arrays = [
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(3,8), index=['A','B','C'], columns=index)

    print(df)
    print(df['bar'], df['bar','two'], sep='\n')
    print('0'*100)
    # This is done to avoid a recomputation of the levels in order to make slicing highly performant
    print(df.columns.levels) # original MultiIndex
    print(df[['bar','baz']].columns.levels) # sliced

    # see only the used levels
    actual_index = df[['bar','baz']].columns.to_numpy()
    print(actual_index)
    actual_index = df[['bar','baz']].columns.get_level_values('second')
    print(actual_index)


def data_align_reindex():
    arrays = [
        np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
        np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
    ]

    s = pd.Series(np.random.randn(8), index=arrays)
    print(s + s[:-2], s, sep='\n')
    print(s[::2]+s,sep='\n')



if __name__ == '__main__':
    # create()
    # create_with_others()
    # m_index_any_axis()
    # basic_index()
    data_align_reindex()

    import locust
    locust.HttpUser.client.post()




