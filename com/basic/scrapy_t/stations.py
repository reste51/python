from requests_html import HTMLSession
from multiprocessing import Pool
import pandas as pd
import logging,time
from com.basic.scrapy_t.tools import get_random_headers

"""
    省 -> 车站 -> 车次（途径站）
"""

logger = logging.getLogger(__name__)

session = HTMLSession()


def get_link_arr():
    """
    获取全部省份
    :return:
    """
    link_arr = []
    resp = session.get('https://qq.ip138.com/train/', headers=get_random_headers(), timeout=30 * 1000)
    # proxy_ips = get_ip()
    # for ip in proxy_ips:
    #     try:
    #         resp = session.get('https://qq.ip138.com/train/', headers=get_random_headers(), timeout=30 * 1000, proxies={'http':ip})
    #         break
    #     except Exception as e:
    #         logger.error(traceback.print_exc(), f'出错信息: {e}, 并且重新执行')
    table_arr = resp.html.find('table')
    for table in table_arr:
        if len(table.attrs) > 0:
            for a in table.find('a'):
                link_arr.append({'province_name': a.text, 'link': a.absolute_links.pop()})

    return link_arr[:2]

def get_stations(province):
    """
    多线程处理
    :param province:
    :return:
    """
    station_arr = session.get(province['link'], headers=get_random_headers()).html.find('table')
    province.pop('link')
    stations = []

    # 3.生成每个 省份对应的车站
    for table in station_arr:
        if len(table.attrs) > 0:
            for station_a in table.find('a'):
                # 每个车站_ 为了简化_暂时将 Station 和 train 合并
                # station = {'station_name': station_a.text, 'trains': []}

                schedule_table = session.get(station_a.absolute_links.pop(), headers=get_random_headers()).html.find('table',
                                                                                                        first=True)

                for train_a in schedule_table.find('a'):
                    # 每个车次及 途径站
                    train = {'station_name': station_a.text, 'train_no': train_a.text}

                    time_table = session.get(train_a.absolute_links.pop(), headers=get_random_headers()).html.find('table')[1]
                    train['site'] = ','.join([a.text for a in time_table.find('a')])
                    # station.get('trains').append(train)
                    stations.append(train)

    province['stations'] = stations
    return pd.json_normalize(province, ['stations'], ['province_name'], max_level=3)


def parallel():
    # 多线程处理
    pool = Pool(6)
    df = pd.concat(pool.map(get_stations, ret), ignore_index=True)

    logger.info(f'获取全国站点数据成功, 共有 {len(df)} 条.详细数据为:\n{df}')

    df.to_excel('stations2.xls', index=False, )
    logger.info('写入excel成功')

    pool.join()
    pool.close()




if __name__ == '__main__':
    ret = get_link_arr()
    logger.info(f'获取全国省的数据成功, 共有 {len(ret)} 条.')

    df_list = []
    for p in ret:
        df_list.append(get_stations(p))
        time.sleep(10*2)

    df = pd.concat(df_list, ignore_index=True)
    df.to_excel('stations2.xls', index=False, )
    logger.info('写入excel成功')
