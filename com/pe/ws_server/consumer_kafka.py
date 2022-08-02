from kafka import KafkaConsumer
import logging
from com.pe.util.util import get_logger


class Kafka_Consumer:
    """
    自定义kafka消费者
    """

    def __init__(self, topic_name='mytopic'):
        self.logger = get_logger(__name__, logging.DEBUG)

        self.conf = {
            'bootstrap_servers': ['10.68.124.104:9092', '10.68.124.105:9092', '10.68.124.106:9092'],
            'topic_name_user': 'user_data',
            'consumer_id': 'consumer_ai'
        }
        self.consumer = KafkaConsumer(bootstrap_servers=self.conf['bootstrap_servers'],
                                      group_id=self.conf['consumer_id'],
                                      api_version=(0, 10))


        self.logger.info('consumer start to consuming...')
        self.consumer.subscribe((topic_name,))

