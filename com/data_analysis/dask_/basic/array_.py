"""
    数组  包含多个Numpy 数组
"""

import numpy as np
import pandas as pd

from glob import glob
from dask import array
from dask import compute

from dask import delayed
from time import sleep

from dask.distributed import Client, LocalCluster


# import dask.dataframe as dd
#
# dd.read_sql_table()

def inc(x):
    sleep(1)
    return x + 1

def add(x, y):
    sleep(1)
    return x + y

# x = delayed(inc)(1)
# y = delayed(inc)(2)
# z = delayed(add)(x, y)

# z.compute()
# z.visualize()

def delayed_first():
    x = delayed(np.arange)(10)
    y = (x + 1)[::2].sum()  # everything here was delayed
    # y.visualize()

    # print(y.compute())

    a = array.arange(10, chunks=2).sum()
    b = array.arange(10, chunks=2).mean()
    # a_sum, b_mean = compute(a,b)pip
    print(compute(a, b))


if __name__ == '__main__':
    delayed_first()
    client = Client(address='tcp://192.168.3.247:8786')
    print(client.get_versions())

    # import dask.bag as bg
    # bg.from_sequence()




