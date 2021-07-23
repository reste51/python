"""
    Queues : 队列， this is near clone of queue.QUEUE
    They are thread and process safe
"""

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    queue = Queue()
    process = Process(target=f, args=(queue,))
    process.start()
    print(queue.get())

    queue.join()

    # Wait until the thread terminates
    process.join()


