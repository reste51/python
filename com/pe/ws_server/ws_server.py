from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import queue
import threading
import os
import sys
import time
from kafka import KafkaConsumer
import json

session = {}


class WSServerInstance(WebSocket):

    def handleMessage(self):
        """
        session组织: 用于 ywid: client_id映射
        :return:
        """
        # echo message back to client
        print(self.data, self.address)
        print(self.server.connections.items())
        for key, client in self.server.connections.items():
            print(self.address, client.address)
            if self.address == client.address:
                session[self.data] = key
        print(session)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


class WSServer(object):
    def __init__(self, port):
        self.server = SimpleWebSocketServer('192.168.31.238', port, WSServerInstance)
        self.server.data_queue = queue.Queue(1000)
        self.server_thread = None
        self.run()

    def run(self):
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def run_server(self):
        self.server.serveforever()

    def broadcast_message(self, message):
        """
            广播消息，向所有连接中的client发消息
        """

        message = eval(message.decode())
        for key, client in self.server.connections.items():
            if message['dxywzjbh'] in session.keys() and session[message['dxywzjbh']] == key:
                client.sendMessage(str(message))
            else:
                print('没发送', key, message['dxywzjbh'])

    def main_proccess(self):
        """
           主循环，可以加一些其他流程的代码
        """
        print('main_proccess')
        consumer = KafkaConsumer("out_04", group_id="python3",
                                 bootstrap_servers=['10.68.124.104:9092', '10.68.124.105:9092', '10.68.124.106:9092'],
                                 auto_offset_reset='earliest')
        print('connecnted')
        for i in consumer:
            print(i.value)
            self.broadcast_message(i.value)
        # while True:
        #     if (not self.server.data_queue.empty()):
        #         message = self.server.data_queue.get()
        #         print("on get message:", message)
        #         self.broadcast_message(message)
        # other proccess


ws_server = WSServer(8000)
ws_server.main_proccess()

