"""
 one can use a lock to ensure that only one process prints to standard output at a time

"""

from multiprocessing import Process, Lock


def f(l, num):
    l.acquire()  # 获取锁
    try:
        print('Hello %d ' % num)
    finally:
        l.release()  # 释放锁


if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
