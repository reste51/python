"""
    this module containing the Huey object。
    产生Huey对象， 声明  任务列表的存储位置。

"""

from huey import RedisHuey

huey = RedisHuey(host='localhost',db=15)

