#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
默认消息队列里的数据是按照顺序被消费者拿走，例如：消费者1去队列中获取<奇数 序列>的任务，消费者2去队列中获取<偶数>序列的任务。
只需要在消费者
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.4'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received {}.".format(body))
    import time
    time.sleep(10)
    print('ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)  # 设置谁来谁取

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()