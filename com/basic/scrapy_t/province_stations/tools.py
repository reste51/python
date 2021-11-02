"""
    获取动态的ip
"""

import random
import re
import time
import requests
import pymysql
from sqlalchemy import create_engine
import pandas as pd

cache = []
mysql_engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8', encoding='utf8')


def read_sql(sql):
    """
    读取mysql数据
    :param sql:
    :return:
    """
    try:
        with mysql_engine.connect() as conn:
            return pd.read_sql(sql, conn)
    except Exception as e:
        print(f'执行sql语句:{sql} 出错 ')


def get_ip():
    """
    获取 代理的Ip地址
    :return:
    """
    if len(cache) > 0:
        return cache

    url = 'https://www.kuaidaili.com/free/inha/'
    url_list = [url + str(i + 1) for i in range(5)]  # 生成url列表，5代表只爬取5页
    print(url_list)
    ip_list = []
    for i in range(len(url_list)):
        url = url_list[i]
        html = requests.get(url=url, ).text
        regip = '<td.*?>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>.*?<td.*?>(\d{1,5})</td>'
        matcher = re.compile(regip, re.S)
        ipstr = re.findall(matcher, html)
        time.sleep(1)

        for j in ipstr:
            ip_list.append(j[0] + ':' + j[1])  # ip+port
    print(ip_list)
    print('共收集到%d个代理ip' % len(ip_list))
    return ip_list


def get_proxies():
    """
    获取 代理的数据
    :return:
    """
    ips = get_ip()
    random_index = random.randint(0, len(ips) - 1)

    return {'http': ips[random_index]}


def get_random_headers():
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']

    headers = {'Host': 'qq.ip138.com', 'Connection': 'keep-alive', 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'User-Agent': agents[random.randint(0, len(agents) - 1)],
               'if-none-match': "4a2ef3bada800cae2accaf8b7b4982ab",
               'referer': 'https://pos.baidu.com/qcxm?conwid=953&conhei=286&rdid=5691515&dc=3&di=u5691515&s1=2609530563&s2=557570360&tr=1635163039&mt=d4ba0d880bb91b21&dri=0&dis=0&dai=1&ps=6283x280&enu=encoding&exps=110259,110252,110011&ant=0&aa=1&psi=3049dfea76e47976&dcb=___adblockplus_&dtm=HTML_POST&dvi=0.0&dci=-1&dpt=none&tpr=1635163039511&ti=%E6%A1%82%E6%9E%97%E8%A5%BF%E5%88%97%E8%BD%A6%E6%97%B6%E5%88%BB%E8%A1%A8%20%E6%A1%82%E6%9E%97%E8%A5%BF%E7%81%AB%E8%BD%A6%E6%97%B6%E5%88%BB%E8%A1%A8%20www.ip138.com&ari=2&ver=1021&dbv=2&drs=3&pcs=1263x150&pss=1263x6523&cfv=0&cpl=3&chi=3&cce=true&cec=UTF-8&tlm=1583472252&prot=2&rw=320&ltu=https%3A%2F%2Fqq.ip138.com%2Ftrain%2Fguangxi%2Fguilinxi.htm&ecd=1&uc=1280x680&pis=-1x-1&sr=1280x720&tcn=1635163040&qn=5ce7c33cff62d10e',
               'sec-fetch-mode': 'no-cors', 'sec-fetch-site': 'cross-site', 'Referer': 'https://www.ip138.com/',
               'Cookie': 'PHPSESSID=qrfs816mbt3lsfb9hcah85882a; ASPSESSIONIDSSSRDSDA=PALHOMEDJCKNIADBHMKBDJJN; _ga=GA1.2.1042137714.1635159183; Hm_lvt_ecdd6f3afaa488ece3938bcdbb89e8da=1635159195; Hm_lpvt_ecdd6f3afaa488ece3938bcdbb89e8da=1635159195; Hm_lvt_ee874a70e56b8f2f93f21f9beacd979a=1635307575,1635307581,1635314577,1635318055; Hm_lpvt_ee874a70e56b8f2f93f21f9beacd979a=1635318055'}
    # headers[':authority']= 'lupic.cdn.bcebos.com'
    # headers[':method']= 'GET'
    # headers[':scheme']= 'https'
    # headers['Host']='www.ip138.com'
    return headers


def is_duplicate(table_name, field, field_val, desc, logger, **other_params):
    """
    数据重复请求检验, 单纯的 有无数量的检验
    :return: db_df
    """
    sql = f'select * from {table_name} where {field}="{field_val}"'
    for k, v in other_params.items():
        sql += f' and {k} = "{v}" '

    db_df = read_sql(sql)
    if db_df is not None and db_df.shape[0] > 0:
        logger.info(f'{field_val}的{desc}数据从数据库缓存获取, 总条数为:{db_df.shape[0]}')
        return db_df

    return None


def to_db(df, table_name, logger, desc):
    """
    从web请求的数据落地
    :param df:
    :param table_name:
    :param logger:
    :param desc:
    :return:
    """
    try:
        with mysql_engine.connect() as conn, conn.begin():
            df.to_sql(table_name, conn, index=False, if_exists='append')
            logger.info(f'{desc}数据从web互联网获取,已存储mysql表{table_name}中,总条数为:{df.shape[0]}')
    except Exception as e:
        logger.error(f'存储mysql表{table_name}, 总条数为:{df.shape[0]}  报错, 信息:{e}')


# def t(a, b, **kwargs):
#     print(kwargs, type(kwargs))


if __name__ == '__main__':
    # get_ip()
    # df = read_sql('select * from province_link')
    # print(df)

    # df = pd.DataFrame(
    #     {'province_name': 11, 'station_name': 22, 'train_no': 3123123,
    #      'site': [112,22,33]}
    # )
    # print(df)
    # t(1, 2, de='111',be='ccc')
    # print(5%10)

    # df.to_excel('train_berth_detail.xlsx', index=False)

    detail_df = read_sql('select distinct train_id from train_berth_detail')
    station_df = read_sql('select distinct id from station_trains')

    no_match_df = detail_df.loc[~detail_df['train_id'].isin(station_df['id'])]
    print(f'没有 关联的train_id 的数量是 {no_match_df.shape[0]}')

