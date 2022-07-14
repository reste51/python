import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError
from com.pe.util.util import get_logger
import json

"""
    kafka 推送数据
    注： 推送没有与元数据关联， 因此不用zookeeper
    而获取 topic list则需使用
"""


class Producer:
    def __init__(self, topic):
        self.logger = get_logger(__name__, logging.INFO)
        self.producer = KafkaProducer(
            bootstrap_servers=['10.68.124.104:9092', '10.68.124.105:9092', '10.68.124.106:9092'],
            api_version=(0, 10), retries=5)
        self.topic = topic
        self.partitions = self.producer.partitions_for(topic)

    def producing_msg(self, json_data):
        """
        发送数据
        :param json_data: 格式为{"k":"v"}
        :return:
        """

        resp_data = bytes(json.dumps(json_data), encoding="utf-8")
        try:
            resp_metadata = self.producer.send(self.topic, resp_data)

            self.logger.info(f'send message succeed. the resp metadata is {resp_metadata.get()}')
        except KafkaError as e:
            self.logger.error('send message failed. [e] =', e),


if __name__ == '__main__':
    user_data = [{
        "appToken": "d23ea83dbf7c411aa36e5ab519f41818",
        "appId": "JF_WK_001",
        "mobile": "15950857927",
        "isRealTimeReturn": True,
        "applyTime": 15100226057,
        "uuid": "a91140f54b898w85d7a50d4b95994",
        "customerNo": 1153265851
    }, {
        "appToken": "d23ea83dbf7c411aa36e5ab519f41818",
        "appId": "JF_WK_001",
        "mobile": "15950857927",
        "isRealTimeReturn": True,
        "applyTime": 15100226057,
        "uuid": "a91140f54b898w85d7a50d4b95994",
        "customerNo": 1153265851
    }]
    p = Producer('mytopic')
    p.producing_msg(user_data)
