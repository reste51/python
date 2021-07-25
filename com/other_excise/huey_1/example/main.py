"""
    Imports both the config.py module and the tasks.py module.

    相当于生产者
"""
from com.other_excise.huey_1.example.config import huey
from com.other_excise.huey_1.example.task import add, count_beans, \
    hello,nightly_backup, flaky_task, every_three_minutes

if __name__ == '__main__':
    # res = add(1,2)
    # result = res()
    # print(result)

    # 1. will block until it gets data, 取掉数据后，会删除存储在redis中的数据
    # print(res.get(blocking=True))

    # 2. 返回任务的id, 注: 可以根据 任务的id 获取 redis 中的数据
    # print('任务的id为 %s ' % res.id)

    # res = add.schedule((2, 3), delay=10)
    # print(res())

    # beans = input('How many beans? ')
    # count_beans(int(beans))
    # print('Enqueued job to count %s beans' % beans)

    # res = nightly_backup()
    # res.get(blocking=True)

    # every_three_minutes(10)

    res = count_beans(100)
    print(res.get(blocking=True))




