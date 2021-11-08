import logging
import time

import pandas as pd
from requests_html import HTMLSession
import uuid

from basic.scrapy_t.province_stations.tools import get_random_headers, \
    read_sql, is_duplicate, to_db

"""
    省 -> 车站 -> 时刻表 -> 车次（途径站）
"""

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

session = HTMLSession()

pause_time = 0.06 * 3600


def get_link_df():
    """
    获取全部省份 及 对应链接
    :return:
    """
    table_name = 'province_link'
    db_df = read_sql(f'select * from {table_name}')
    if db_df.shape[0] == 32:
        logger.info('get_link_df 未从web请求,数据库 已缓存有,直接返回!')
        return db_df

    link_arr = []
    resp = session.get('https://qq.ip138.com/train/', headers=get_random_headers(), timeout=30 * 1000)
    table_arr = resp.html.find('table')
    for table in table_arr:
        if len(table.attrs) > 0:
            for a in table.find('a'):
                link_arr.append({'province_name': a.text, 'link': a.absolute_links.pop()})

    link_df = pd.DataFrame(link_arr)
    to_db(link_df, table_name, logger, '全国省份及对应链接')
    return link_df


def load_province_stations(p_s):
    """
     根据省份 获取 下面对应的 站点数据
    :return:
    """
    table_name = 'province_stations'
    province_name = p_s['province_name']
    # 数据重复检验
    db_df = is_duplicate(table_name, 'province_name', province_name, '站点', logger)
    if db_df is not None:
        return db_df

    station_arr = session.get(p_s['link'], headers=get_random_headers()).html.find('table')
    time.sleep(2 * 10)
    station_table = list(filter(lambda table: len(table.attrs) > 0, station_arr))[0]
    s_df = pd.DataFrame(
        [{'province_name': province_name, 'station_name': a.text, 'link': a.absolute_links.pop()} for a in
         station_table.find('a')])

    to_db(s_df, table_name, logger, f'{province_name}的站点')


def load_timetable_by_station(station):
    """
    获取某个站点对应的  时刻表
    :return:
    """
    try:

        station_name = station['station_name']
        schedule_table = session.get(station['link'], headers=get_random_headers()).html.find(
            'table', first=True)

        s_df = pd.DataFrame(
            [{'province_name': station['province_name'], 'station_name': station_name, 'train_no': a.text,
              'link': a.absolute_links.pop()} for a in
             schedule_table.find('a')])

        to_db(s_df, 'station_timetable', logger, f'{station_name}的时刻表')
    except Exception as e:
        logger.error(f'获取时刻表内的 每个车次的途径站时 出错, 出错信息为:{e}, 再等 {pause_time / 3600} 小时后请求')
        time.sleep(pause_time)


def load_trans_by_timetable(timetable):
    """
    获取时刻表内的 每个车次的途径站
    :return:
    """
    try:
        station_name, province_name, train_no, link = timetable['station_name'], timetable['province_name'], timetable[
            'train_no'], timetable['link']

        content = session.get(link, headers=get_random_headers()).html
        # 1.生成列车的概况
        info_arr = [text.replace('：', ':').split(':')[1] for text in content.find('table')[0].text.split('\n')]

        train_id = str(uuid.uuid4())
        train_data = {'id': train_id, 'province_name': province_name, 'station_name': station_name,
                      'train_no': train_no,
                      'site': ','.join([a.text for a in content.find('table')[1].find('a')]),
                      'train_type': info_arr[0], 'full_elapsed': info_arr[1], 'full_distance': info_arr[2]}

        # 2. 生成各个站点的详细信息_并直接落地
        berth_data = [berth.text.split('\n') for berth in content.find('table')[1].find('tr')[1:]]
        berth_df = pd.DataFrame(
            [{'id': str(uuid.uuid4()), 'train_id': train_id, 'order': data[0], 'station_name': data[1],
              'arrive_time': data[2], 'depart_time': data[3], 'elapsed_time': data[4], 'mileage': data[5]} for data in
             berth_data])

        # 3.数据落地_
        to_db(pd.DataFrame(train_data, index=[1]), 'station_trains', logger, '车次的概览数据')
        to_db(berth_df, 'train_berth_detail', logger, '车次的详情数据')

    except Exception as e:
        logger.error(f'获取时刻表内的 每个车次的途径站时 出错, 出错信息为:{e}, 再等 {pause_time / 3600}个小时后请求')
        time.sleep(pause_time)


def start_entry():
    # 1.获取省数据
    p_df = get_link_df()

    logger.info(f'获取全国省的数据成功, 共有 {p_df.shape[0]} 条.')
    # 2.获取每个省的站点数据
    for index, row in p_df.iterrows():
        load_province_stations(row)
        time.sleep(10 * 2)
    logger.info(f'获取站点的数据成功.')


def timetable_entry():
    """
    3. 获取 站点内的时刻表 -- 除已存储的站点
    :return:
    """
    df = read_sql("select * from province_stations ")
    is_stored_stations = read_sql("select DISTINCT(station_name) from station_timetable ")
    df = df[~df['station_name'].isin(is_stored_stations['station_name'].values)]
    logger.info(f' 开始站点内的时刻表信息: 已存储条数:{is_stored_stations.shape[0]}, 剩余数:{df.shape[0]}')

    for index, row in df.iterrows():
        load_timetable_by_station(row)
        time.sleep(10 * 1)

    logger.info(f'获取全部站点中的时刻表数据成功.')


def trains_entry():
    """
    4. 最终结果: 获取时刻表内的 每个车次的途径站, (直接筛选掉 已存储的数据)
    :return:
    """
    df = read_sql("select * from station_timetable where province_name = '四川'")
    df['flag'] = df['station_name'] + '_' + df['train_no']
    is_stored_df = read_sql("select CONCAT(station_name,'_',train_no) flag from station_trains where province_name = '四川' ")
    df = df[~df['flag'].isin(is_stored_df['flag'].values)]
    logger.info(f' 开始获取时刻表内的每个车次的途径站信息: 已存储条数:{is_stored_df.shape[0]}, 剩余数:{df.shape[0]}')

    for index, row in df.iterrows():
        load_trans_by_timetable(row)
        time.sleep(10 * 1)

    logger.info(f'获取时刻表内的 每个车次的途径站数据成功.')


if __name__ == '__main__':
    # timetable_entry()
    trains_entry()
