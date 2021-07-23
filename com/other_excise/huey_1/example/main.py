"""
    Imports both the config.py module and the tasks.py module.
"""
from com.other_excise.huey_1.example.config import huey
from com.other_excise.huey_1.example.task import add, count_beans, hello

if __name__ == '__main__':
    res = add(1,2)
    # result = res()
    # print(result)
    # will block until it gets data.
    print(res.get(blocking=True))

    # res = add.schedule((2, 3), delay=10)
    # print(res())

    # beans = input('How many beans? ')
    # count_beans(int(beans))
    # print('Enqueued job to count %s beans' % beans)


