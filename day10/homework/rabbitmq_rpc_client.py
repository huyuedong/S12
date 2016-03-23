#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
RPC client端
client端向server端发送一个数，并接收server端返回斐波那契数列的和
"""
import pika
import uuid


class CmdRpcClient(object):
    def __init__(self):
        self.response = None  # 初始化一个变量用于存放结果
        self.corr_id = str(uuid.uuid4())  # 随机生成一个ID值
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # 声明一个链接
        self.channel = self.connection.channel()  # 声明一个频道
        # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
        result = self.channel.queue_declare(exclusive=True)

        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, cmd):
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id,
                                         ),
                                   body=str(cmd))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


if __name__ == "__main__":
    cmd = input("Input the instruction:").strip()
    cmd_rpc = CmdRpcClient()
    print(" [x] sent instruction:{}".format(cmd))
    response = cmd_rpc.call(cmd)
    print(" [.] Got {}.".format(response))
