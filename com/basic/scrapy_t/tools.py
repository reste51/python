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
mysql_engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8',encoding='utf8',echo=True)


def read_sql(sql):
    """
    读取mysql数据
    :param sql:
    :return:
    """
    try:
        with mysql_engine.connect() as conn:
            return pd.read_sql(sql,conn)
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
               'Cookie': 'PSTM=1607654896; BIDUPSID=FECB165CC9F489EA6A7514E041074334; CPROID=5BB9120713B1725A3A6044DAFF0B8244:FG=1; BDUSS=BZSTZDWDc1UTdzYjE0QnlhTjJsQVJxQXZFdUNVR3ZhbnlJYmZYWnJMQTM2emxnRVFBQUFBJCQAAAAAAAAAAAEAAACVxjAFcmVzdGU1MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADdeEmA3XhJgdT; BDUSS_BFESS=BZSTZDWDc1UTdzYjE0QnlhTjJsQVJxQXZFdUNVR3ZhbnlJYmZYWnJMQTM2emxnRVFBQUFBJCQAAAAAAAAAAAEAAACVxjAFcmVzdGU1MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADdeEmA3XhJgdT; __yjs_duid=1_13d3ec49865d5f05d5d5eddc3921955d1619662142038; MCITY=-%3A; BAIDUID=64B5506D548EDD5397C9CC8F7BBFD28F:FG=1; BDSFRCVID_BFESS=eiDOJeC6260sMJJHj4houRp7cgP1TKRTH6f312x0t6vx1dcL5r2aEG0PsU8g0KAbC92UogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=fR-JoD85JDvje5rmbtOhq4tHeptDBMRZ5mAqotn7LhA2VqPzLCcl5f4RXnb-bPvHQR7naIQDth30sq8mbfnKeh4XQh6AW-j43bRTQbLy5KJvEj6g3bJ2hP-Uyn7MWh37bbRlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD8KMKImejAhen8t2MoQetQq56r-Q-b25ROsKRrN55RqMf0gyxomtjDqtT7uaqcd2DbsDP5-K5JjbpOL3-RNLUkq5JADotPMbIQ-JKjg-UkhK6D_QttjQnJPfIkjahjt0KIKSJ7TyURibU47yhtj0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OhJRQ2QJ8BJI_hhIJP; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ISBID=64B5506D548EDD5397C9CC8F7BBFD28F:FG=1; ISUS=5BB9120713B1725A3A6044DAFF0B8244:FG=1; delPer=0; BAIDUID_BFESS=64B5506D548EDD5397C9CC8F7BBFD28F:FG=1; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=34834_34886_34445_34530_34068_31660_34584_34517_34830_34578_34813_26350_34828; BA_HECTOR=8080a08l04200525kn1gnd6pe0r'}

    # headers[':authority']= 'lupic.cdn.bcebos.com'
    # headers[':method']= 'GET'
    # headers[':scheme']= 'https'
    # headers['Host']='www.ip138.com'
    return headers


if __name__ == '__main__':
    # get_ip()
    # df = read_sql('select * from person')
    # print(df)
    pass

