"""
web socket server
"""
import asyncio
import websockets
import threading
from com.pe.util.util import get_logger
from com.pe.ws_server.consumer_kafka import Kafka_Consumer

logger = get_logger(__name__)

topic = 'out_04'
consumer = Kafka_Consumer(topic).consumer
loop = asyncio.get_event_loop()


async def comparison(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        logger.info(message)

        coroutine = consume_msg(websocket, message)
        task = loop.create_task(coroutine)
        task.result()


async def start_consume(websocket, message):
    """
    创建个协程
    :param websocket:
    :param message:
    :return:
    """
    job_thread = threading.Thread(target=consume_msg, args=(message, websocket))
    job_thread.start()


async def consume_msg(ws, ywid):
    """
    消费 kafka消息
    :return:
    """
    await ws.send('服务器正在开始消费数据....')
    for message in consumer:
        logger.info(f'kafka consumer message info is topic= {message.topic},'
                    f' offset={message.offset}, key={message.key}, value={message.value}, '
                    f'partition={message.partition} ',
                    )
        if message.key is message:
            logger.info(f'比中成功， ywid:{message}')
            await ywid.send(message.value)


loop.run_until_complete(websockets.serve(comparison, 'localhost', 8765))
loop.run_forever()
