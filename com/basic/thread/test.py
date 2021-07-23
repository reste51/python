import threading
"""
    基础 多线程处理
"""
import schedule


def test1(args):
    # for i in range(100):
    #     print(f'{i} -  {args}')
    return  1

if __name__ =='__main__':
    t1 = threading.Thread(target=test1,args=('thread1',))
    t2 = threading.Thread(target=test1,args=('thread2',))

    print(t1.start())
    t2.start()

    threading.active_count()
    threading.local()
    threading.RLock


