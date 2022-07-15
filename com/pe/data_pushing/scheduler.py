import threading
import schedule
from com.pe.data_pushing.producer import Producer
import uuid
import json
import os
import time
from com.pe.util.util import get_current_date
import numpy as np

"""
    定时推送数据,模拟感知源定时接口推送至感知引擎
"""


def concurrency_work(job_func):
    """
    并发执行任务
    :param job_func:
    :return:
    """
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


class Scheduler:
    def __init__(self):

        # 模型数据
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/datas/model.json', mode='r+', encoding='utf-8') as fp:
            self.model_data = json.loads(fp.read(), encoding='utf-8')

        # 生产消息对象
        self.netbar_producer = Producer('netbar')
        self.hotel_producer = Producer('hotel')
        self.roadway_producer = Producer('roadway')

    def set_common_msg(self):
        self.model_data['uuid'] = str(uuid.uuid4())
        self.model_data['hdfssj'] = get_current_date()

    def netbar_trails(self):
        """
        网吧消息发送
        :return:
        """
        self.set_common_msg()
        # 产生随机条消息
        datas = [self.model_data for i in range(np.random.randint(1, 10, size=1)[0])]

        self.netbar_producer.producing_msg(datas)

    def hotel_trails(self):
        """
        旅馆消息发送
        :return:
        """
        self.set_common_msg()
        datas = [self.model_data for i in range(np.random.randint(1, 10, size=1)[0])]

        self.hotel_producer.producing_msg(datas)

    def roadway_trails(self):
        """
        卡口消息发送
        :return:
        """
        self.set_common_msg()
        datas = [self.model_data for i in range(np.random.randint(1, 10, size=1)[0])]

        self.roadway_producer.producing_msg(datas)


def run_jobs():
    scheduler = Scheduler()
    schedule.every(12).seconds.do(concurrency_work, scheduler.hotel_trails)
    schedule.every(15).seconds.do(concurrency_work, scheduler.roadway_trails)
    schedule.every(18).seconds.do(concurrency_work, scheduler.netbar_trails)

    while 1:
        schedule.run_pending()


# if __name__ == '__main__':
#     print(__file__)
#     scheduler = Scheduler()
#     schedule.every(12).seconds.do(concurrency_work, scheduler.hotel_trails)
#     schedule.every(15).seconds.do(concurrency_work, scheduler.roadway_trails)
#     schedule.every(18).seconds.do(concurrency_work, scheduler.netbar_trails)
#
#     while 1:
#         schedule.run_pending()
