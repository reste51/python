"""
sort

curl -X PUT "nodeM:9200/my_index2?pretty" -H 'Content-Type: application/json' -d'
{
    "mappings": {
        "_doc": {
            "properties": {
                "post_date": { "type": "date" },
                "user": {
                    "type": "keyword"
                },
                "name": {
                    "type": "keyword"
                },
                "age": { "type": "integer" }
            }
        }
    }
}
'

"""
from com.other_excise.elastic_search1.first import handle_resp, cat_summary
from elasticsearch6 import Elasticsearch
import numpy as np

client = Elasticsearch(hosts=['192.168.3.129'])


def create_index():
    """
    创建测试索引
    :return:
    """
    ret = client.index(index='my_index',doc_type='_doc',body={
        "properties": {
            "post_date": {"type": "date"},
            "user": {
                "type": "keyword"
            },
            "name": {
                "type": "keyword"
            },
            "age": {"type": "integer"}
        }
    })
    print(ret)



def query_all_docs():
    """
    查询全部的doc
    :return:
    """
    ret = client.search('my_index2', None, body={
        'query': {'match_all': {}}
    })
    handle_resp(ret)

"""
curl -X PUT "localhost:9200/my_index/_doc/1?refresh&pretty" -H 'Content-Type: application/json' -d'
{
   "product": "chocolate",
   "price": [20, 4]
}
'
curl -X POST "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
   "query" : {
      "term" : { "product" : "chocolate" }
   },
   "sort" : [
      {"price" : {"order" : "asc", "mode" : "avg"}}
   ]
}
'

"""
def sort():
    """
    不支持term，  只支持  bool -> must-> match[]
    :return:
    """
    ret = client.search(index='bank',doc_type=None, body={
        "query": {
            "bool":{'must':[ {'match':{"state": "GA"}} ]}
            # "term": {"state": "WA"}  # 不支持
            # "match_all":{}
        },
        "sort": [
            {"balance": {"order": "desc"}},
        ]

    })
    handle_resp(ret)


# cat_summary()
# create_index()
# query_all_docs()
sort()

