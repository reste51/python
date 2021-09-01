"""
 使用python 客户端， 写入 dsl语句， 操作 elastic search
"""
from elasticsearch6 import Elasticsearch

client = Elasticsearch(hosts=['192.168.3.129'])


def cat_summary():
    """
    查询 基本信息及 健康状况 和 索引的全部信息
    :return:
    """
    print(client.info())
    # get all indies info;  _cat/indices?v
    print(client.cat.indices())
    # health info;  /_cat/health?v
    print(client.cat.health())


def get_doc_id(index='twitter', doc_type='_all', id=2):
    """
    通过 doc id查询某个文档
    :return:
    """
    data = client.get(index, doc_type=doc_type, id=id)
    if data['found']:
        print(data['_source'])


def create_or_append_index_doc():
    """
    通过一个新增文档, 创建 或 新增(源index不存在)
    :return:
    """
    ret = client.index('py_index', '_doc', body={
        'name': 'data',
        'age': 45,
        'address': '天津'
    })
    print(ret)


def handle_resp(resp):
    total_num = resp['hits']['total']
    if total_num > 0:
        resp_data = resp['hits']['hits']
        print(f'查询总量为:{total_num}, 返回的数量:{len(resp_data)}')
        print(resp_data)
    else:
        print('查询无结果....')


def query_all_docs():
    """
    查询全部的doc
    :return:
    """
    ret = client.search('bank', None, body={
        'query': {'match_all': {}}
    })
    handle_resp(ret)


def query_by_field():
    """
    查询全部的doc
    :return:
    """
    ret = client.search('py_index', '_doc', body={
        'query': {'bool': {'must': [{'match': {'age': 12}}]}}
    })
    handle_resp(ret)


def query_by_range():
    """
    范围的查询 -  分页的查询 通过 params的 size 和from进行操作
    :return:
    """
    ret = client.search('bank', doc_type=None,params={'size':40, 'from':200}, body={
        'query': {
            'bool': {
                'filter': {
                    'range': {
                        'balance': {
                            'gte': 20000,
                            'lte': 30000
                        }
                    }
                }
            }
        }
    })
    handle_resp(ret)


def delete_by_id(_id='222'):
    """
    删除某个文档的数据
    :param _id:
    :return:
    """
    ret = client.delete(index='bank',doc_type='account',id=_id)
    print(ret)

query_by_range()
# query_all_docs()
# delete_by_id()
# get_doc_id('bank',id='222')

# cat_summary()
