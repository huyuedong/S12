#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
发布者
exchange_type=fanout:
fanout: 所有bind到此exchange的queue都可以接收消息
"""

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="apple",
                         exchange_type="fanout",
                         )

message = " ".join(sys.argv[1:]) or "info:Hello World!"

channel.basic_publish(exchange="apple",
                      routing_key="",
                      body=message
                      )

print("[x] Sent {}.".format(message))
connection.close()

