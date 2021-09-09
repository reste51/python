"""
es  查询的功能
"""
from elasticsearch6 import Elasticsearch
from com.other_excise.elastic_search1.first import handle_resp, cat_summary, get_client


# cat_summary()

client = get_client()


def query_first():
    """
    初步查询
    :return:
    """
    # 'firstname': 'Virginia', 'lastname':'Ayala'
    resp  =client.search(index='bank',body={
        "query": {
            "match": {
                "firstname": "Virginia"
            }
        }
    })
    handle_resp(resp)


# query_first()

def match_1():
    """
    :return:
    """
    ret = client.search('bank',body={
        "query": {
            "match": {
                "lastname": {
                    "query": "Ayala",
                    "operator": "and"
                }
            }
        }
    })
    handle_resp(ret)

# match_1()


def fuzzy_match():
    """

    :return:
    """
    resp = client.search(index='bank',params={'size':20},body={
        "query": {
            "match": {
                "employer": {
                    "query": "Filodyne",
                    "fuzziness": "AUTO"
                }
            }
        }
    })
    handle_resp(resp)


def range_query():
    resp = client.search('bank',body={
        "query":{
            'range':{
                'age': {
                    'gte': 28,
                    'lte': 30,
                    'boost': 2.0
                }
            }
        }
    })
    handle_resp(resp)




# range_query()
cat_summary()

# fuzzy_match()





