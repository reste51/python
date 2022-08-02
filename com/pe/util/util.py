import logging
import time
import datetime


def get_logger(name, level = logging.INFO):
    """
    获取日志对象
    :param name:
    :param level:
    :return:
    """
    logging.basicConfig(format='%(asctime)s %(message)s', level=level)
    return logging.getLogger(name)


def get_current_date(formats='%Y-%m-%d %H:%M:%S'):
    """
    获取当前的时间
    :param formats: 格式
    :return:
    """
    return datetime.datetime.now().strftime(formats)


def get_current_timestamp():
    """
    获取当前时间的时间戳
    :return:
    """
    return int(time.mktime(time.localtime(time.time())))

