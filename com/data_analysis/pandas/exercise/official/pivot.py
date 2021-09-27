"""
 reshape by Pivoting Dataframe objects

 file:///D:/soft/python/module_package/pandas/doc/1.3.3/user_guide/reshaping.html


 note:
    stack在 column 中是一个  向下 👇 开口的  stack结构
    stack 在 index上是一个 向👉 右侧开口的 stack

"""
import pandas._testing as tm
import pandas as pd
import numpy as np


def unpivot(frame):
    N, K = frame.shape
    data = {
        'value': frame.to_numpy().ravel('F'),
        'variable': np.asarray(frame.columns).repeat(N),
        'date': np.tile(np.asarray(frame.index), K)
    }
    return pd.DataFrame(data)


def pivot_test():
    df = unpivot(tm.makeTimeDataFrame(3))
    print(df.loc[df['variable'] == 'A'])

    df['value2'] = df.value * 2
    df_p = df.pivot(index='date', columns='variable')
    # 可以筛选 子集,  返回的是一个 视图
    print(df_p, df_p['value2'], df_p.columns, sep='\n')

def stack_unstack():
    """
    stack (进栈)函数_ 会压缩 成一个 在 index的 最低一层中，
        1. Series 是生成一个 column index
        2. DF 生成 一个 基于多列的 多层索引

    unstack  出栈: default unstacks the last level, 也可以指定层级进行出栈.

    索引index 可以想象成一个栈；
        stack : column ->index, 由于没列了，就会堆叠成一列
        unstack: 出栈最后一个索引到 列中
    :return:
    """
    tuples = list(zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    ))
    index = pd.MultiIndex.from_tuples(tuples, names=['first','second'])
    df = pd.DataFrame(data=np.random.randn(8,4), index=index)
    print(df, df[:4],sep='\n')
    df2 = df[:4]
    # stacked = df2.stack()
    # print(stacked)
    # stacked.to_excel('./xx.xls')

    unstacked = df2.unstack()
    print(unstacked)
    # unstacked.to_excel('./xx.xls')

def multi_levels():
    """
     多个层次的 stack 和 unstack

    :return:
    """
    multi_cols = pd.MultiIndex.from_tuples(tuples=[
        ("A", "cat", "long"),
        ("B", "cat", "long"),
        ("A", "dog", "short"),
        ("B", "dog", "short")], names=["exp", "animal", "hair_length"])

    # print(multi_cols)

    df = pd.DataFrame(data=np.random.randn(10,4), columns=multi_cols)
    print(df)

    # 多个层次的进栈
    stacked = df.stack(level=['animal','hair_length'])
    print(stacked)

    # 多个层的出栈, 注: 0 为 源索引  0,1,2,3,4
    # unstacked = stacked.unstack(level=['animal','hair_length'])
    unstacked = stacked.unstack(level=[1,2])
    print(unstacked)



# stack_unstack()
multi_levels()

