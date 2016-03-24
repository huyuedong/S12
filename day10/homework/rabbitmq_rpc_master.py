#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
RPC master端：消息的发布者
master端向server端发送一个数，并接收server端返回命令的执行结果
"""
import pika
import uuid


class CmdRpcMaster(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials("test", "test")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.18.18.18",
                                                                            port=5672,
                                                                            credentials=self.credentials))  # 声明一个链接
        self.channel = self.connection.channel()  # 声明一个频道
        # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
        result = self.channel.queue_declare(exclusive=True)

        self.channel.exchange_declare(exchange="cmd", exchange_type="fanout")  # 声明交换机名和交换机类型

        self.callback_queue = result.method.queue  # 为回复声明一个独享的回调队列
        # 订阅回调队列，以便接收RPC响应
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        """
        “on_response”回调函数对每一个响应执行一个非常简单的操作，检查每一个响应消息的correlation_id属性是否与我们期待的一致。
        如果一致，将响应结果赋给self.response，然后跳出consuming循环。

        """
        if self.corr_id == props.correlation_id:
            self.response = body

    # 执行真正的RPC请求
    def call(self, cmd):
        self.response = None  # 初始化一个变量用于存放结果
        self.corr_id = str(uuid.uuid4())  # 生成一个唯一的关联标识，便于‘on_response’获取符合要求的响应。
        # 将带有‘reply_to’和‘correlation_id’属性的消息发送出去
        self.channel.basic_publish(exchange='cmd',
                                   routing_key='rpc_queue',  # 消息队列
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,  # 要在发送请求的时候同时发送一个回调队列
                                         correlation_id=self.corr_id,  # 每个请求设置标识
                                         ),
                                   body=str(cmd)
                                   )
        # 判断收到的消息
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)


if __name__ == "__main__":
    cmd = input("Input the instruction:").strip()
    cmd_rpc = CmdRpcMaster()
    print(" [x] sent instruction:{}".format(cmd))
    response = cmd_rpc.call(cmd)
    print(" [.] Got {}.".format(response))
