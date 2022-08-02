"""
web socket server
"""
import asyncio
import websockets
from com.pe.util.util import get_logger
from com.pe.ws_server.consumer_kafka import Kafka_Consumer

logger = get_logger(__name__)

consumer = Kafka_Consumer('comparison_result').consumer


async def comparison(websocket,path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        logger.info(message)
        resp_msg = consume_msg(message)
        await websocket.send(resp_msg)


def consume_msg(ywid):
    """
    消费 kafka消息
    :return:
    """
    logger.info("consumer = ", consumer)
    for message in consumer:
        logger.info('kafka consumer message info is ', message.topic, message.offset, message.key, message.value,
                    message.partition)
        if message.key is ywid:
            return message


asyncio.get_event_loop().run_until_complete(websockets.serve(comparison, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
