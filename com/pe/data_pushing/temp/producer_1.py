import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
from com.pe.util.util import get_logger

"""
    kafka 推送数据
"""

logger = get_logger(__name__, logging.DEBUG)


# kafka的配置文件：（bootstrap_servers：kafka的集群地址，topic_name：主题，consumer_id：消费分组）
conf = {
    'bootstrap_servers': ['10.68.124.104:9092', '10.68.124.105:9092', '10.68.124.106:9092'],
    'topic_name': 'mytopic',
    'consumer_id': 'consumer_ai'
}
logger.info("[setting] =", conf)

producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'],
                         api_version=(0, 10),
                         retries=5)

partitions = producer.partitions_for(conf['topic_name'])
logger.info('Topic下分区: %s' % partitions)
# 需要推送的数据：（推送到kafka的数据类型必须的json类型）
user_data = {
    "appToken": "d23ea83dbf7c411aa36e5ab519f41818",
    "appId": "JF_WK_001",
    "mobile": "15950857927",
    "isRealTimeReturn": True,
    "applyTime": 15100226057,
    "uuid": "a91140f54b898w85d7a50d4b95994",
    "customerNo": 1153265851
}

send_data = bytes(json.dumps(user_data), encoding="utf-8")

try:
    future = producer.send(conf['topic_name'], send_data)
    future.get()
    logger.info('send message succeed.')
except KafkaError as e:
    logger.error('send message failed. [e] =',e),
