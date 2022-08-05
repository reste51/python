"""
web socket server
"""
import asyncio
import websockets

from com.pe.util.util import get_logger
from com.pe.ws_server.consumer_kafka import Kafka_Consumer

logger = get_logger(__name__)

topic = 'out_04'
consumer = Kafka_Consumer(topic).consumer
loop = asyncio.get_event_loop()


async def comparison(websocket, path):
    async for ywid in websocket:
        resp_message = "I got your message: {}".format(ywid)
        logger.info(resp_message)

        await websocket.send('服务器正在开始消费数据....')
        for message in consumer:
            logger.info(f'kafka consumer message info is topic= {message.topic},'
                        f' offset={message.offset}, key={message.key}, value={message.value}, '
                        f'partition={message.partition} ',
                        )
            if message.key is ywid:
                await websocket.send(message.value)
                logger.info(f'比中成功， ywid:{ywid}')


loop.run_until_complete(websockets.serve(comparison, 'localhost', 8765))
loop.run_forever()
