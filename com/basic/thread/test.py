import threading
"""
    基础 多线程处理
"""



def test1(args):
    for i in range(100):
        print(f'{i} -  {args}')

if __name__ =='__main__':
    t1 = threading.Thread(target=test1,args=('thread1',))
    t2 = threading.Thread(target=test1,args=('thread2',))

    t1.start()
    t2.start()
