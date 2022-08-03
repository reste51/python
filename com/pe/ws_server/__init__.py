import asyncio

"""
接收一个协程，返回一个asyncio.Task的实例，
也是asyncio.Future的实例，毕竟Task是Future的子类。
返回值可直接传入run_until_complete()
"""

#
# async def coroutine_example():
#     await asyncio.sleep(1)
#     print('zhihu ID: Zarten')
#
#
# coro = coroutine_example()
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coro)
# print('运行情况：', task)
#
# loop.run_until_complete(task)
# print('再看下运行情况：', task)
# loop.close()

# async def coroutine_example():
#     await asyncio.sleep(1)
#     return 'zhihu ID: Zarten'
#
# coro = coroutine_example()
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coro)
# print('运行情况：', task)
# try:
#     print('返回值：', task.result())
# except asyncio.InvalidStateError:
#     print('task状态未完成，捕获了 InvalidStateError 异常')
#
# loop.run_until_complete(task)
# print('再看下运行情况：', task)
# print('返回值：', task.result())
# loop.close()

import json

s = b'{"name":"xxx"}'
print(type(json.loads(s.decode())))

