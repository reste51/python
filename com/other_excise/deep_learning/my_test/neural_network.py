"""
 神经网络
 参考链接: https://mxnet.apache.org/versions/1.8.0/api/python/docs/tutorials/getting-started/crash-course/2-nn.html
"""
from mxnet import nd
from mxnet.gluon import nn
import pandas as pd


def test():
    # Let’s start with a dense layer with 2 output units.
    layer = nn.Dense(2)
    print(layer)

    # Then initialize its weights with the default initialization method,
    # which draws random values uniformly from  [−0.7,0.7] .
    layer.initialize()

    # 传递一个(3,4)随机数据 到 layer层，并计算输出
    x = nd.random.uniform(-1, 1, (3, 4))
    print('111111')
    print(layer(x), layer.weight.data())


def pd_test():
    df = pd.DataFrame(data=[[1, 2, 'aaa'], [1, 2, 'aa1'], [1, 2, 'aa2']], columns=['a', 'b', 'c'])
    print(df.groupby('a').sum())


pd_test()


