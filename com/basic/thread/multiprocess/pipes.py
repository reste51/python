"""
    Pipes: 管道， 由两端:  头 send, 尾部 receive

    The two connection objects returned by Pipe() represent the two ends of the pipe.
    Each connection object has send() and recv() methods (among others).

"""
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    head_con, tail_con = Pipe()
    p = Process(target=f, args=(head_con,))
    p.start()

    print(f' pip receive data is {tail_con.recv()}')

    p.join()
