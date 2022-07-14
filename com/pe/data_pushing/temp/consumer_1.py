from kafka import KafkaConsumer
import logging
from com.pe.util.util import get_logger

logger = get_logger(__name__, logging.DEBUG)

conf = {
    'bootstrap_servers': ['10.68.124.104:9092', '10.68.124.105:9092', '10.68.124.106:9092'],
    'topic_name': 'mytopic',
    'topic_name_user': 'user_data',
    'consumer_id': 'consumer_ai'
}
consumer = KafkaConsumer(bootstrap_servers=conf['bootstrap_servers'],
                         group_id=conf['consumer_id'],
                         api_version=(0, 10))

logger.info('consumer start to consuming...')
consumer.subscribe((conf['topic_name'],))

logger.info("consumer = ", consumer)
for message in consumer:
    logger.info(message.topic, message.offset, message.key, message.value, message.partition)
