"""
    任务列表的文件
    this module containing any decorated functions.
    it should be import huey object module.


    当使用 装饰器 task() 或 period_task(), 此函数将注册到内存列表中； 当函数被调用后， 他的引用及调用函数的参数 都会被放入队列中。
    注： 消费任务时，需要导入 Huey对象
"""

from com.other_excise.huey_1.example.config import huey


@huey.task()
def add(a, b):
    print('is invoked')
    return a+b

@huey.task()
def count_beans(num):
    print('-- counted %s beans --' % num)


@huey.task()
def hello():
    return ' hello huey'






