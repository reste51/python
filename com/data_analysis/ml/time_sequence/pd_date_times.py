"""
    pandas 创建日期序列： 日期作为索引的处理
    参考源码： Python时间序列 - 放入 jupyter-notebook中
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data_range, 可以指定开始时间与周期_频率的单位; H 小时，D天，M月
# 可用的时间格式: 2016 Jul 1  7/1/2016  1/7/2016   2016-07-01   2016/07/01
# periods=10 可以理解生成10份时间值
rng = pd.date_range('2021-03-17', periods=10, freq='2D')

# 生成 索引为 时间序列的Series; start-> str or datetime-like;  生成datetime 传递int类型的年 月日
time_s = pd.Series(np.random.randn(20), index=pd.date_range(pd.datetime(2021, 1, 17), periods=20))
# print(time_s)

# truncate过滤, 删除之前 或 之后的数据
print(time_s.truncate(before='2021-01-31'))  # 删除 1-31之前的数据
print(time_s.truncate(after='2021-01-20'))  # 删除 1-20之后的数据

print('*' * 100)

# 取某天或  一段时间的值(切片)
print(time_s['2021-01-22'].sum())
print(time_s['2021-01-22': '2021-02-01'])

print('*' * 100)
# 10-11年生成每2个月(有6个), 此时有end 就无需指定 periods周期;  每个日期为月末
data = pd.date_range('2020-01-01', end='2021-01-01', freq='2M')
print(data)

print('*' * 100)

# 时间戳
pd.Timestamp('2016-07-10')
pd.Timestamp('2016-07-10 10:12:11')
pd.Timestamp('2016-07-10 10:15')

import re

def get_language(page):
    """
    返回 国家2位代码
    :param page: 匹配字符串
    :return: 国家2位代码
    """
    res = re.search('[a-z][a-z].wikipedia.org', page)
    if res:
        return res.group()[0:2]  # 'zh.wikipedia.org' -> 截取 前2位
    return 'na'

from collections import  Counter

if __name__ == '__main__':
    code = get_language('4minute_zh.wikipedia.org_all-access_spider')
    print(Counter(code))
