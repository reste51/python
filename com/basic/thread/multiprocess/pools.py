"""
    Pool represents a  pool of worker processes.
    以下是几种方式将任务 分配到 工作进程中
"""
from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x * x


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as p:
        ret = p.map(f,range(10))
        print(ret)

        # print same numbers in arbitrary order
        for i in p.imap_unordered(f, range(10)):
            print(i)

        print('*' * 100)

        # runs in only one process
        res = p.apply_async(f,(20,))
        print(res.get(timeout=1))

        # print the PID of thar process
        res = p.apply_async(os.getpid, ())
        print(res.get())





