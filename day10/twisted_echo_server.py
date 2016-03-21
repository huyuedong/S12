#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
twisted server
python2.7
"""

import twisted

from twisted.internet import protocol
from twisted.internet import reactor


# 定义一个自己的类：管理自己与client之间的状态。
class Echo(protocol.Protocol):
	def dataReceived(self, data):
		"""
		重写dataReceived方法，收到数据后执行该方法
		:param data: 收到的数据
		:return:
		"""
		print("get data:{}".format(data))
		self.transport.write(data)      # transport表示链接，write(data)表示将data发送给client端。


# 主函数
def main():
	factory = protocol.ServerFactory()      # 实例化一个ServerFactory对象
	factory.protocol = Echo     # 重写protocol

	# reactor(反应堆)就是twisted的事件驱动，是twisted的核心.
	reactor.listenTCP(1234, factory)  # 将factory回调函数注册到reactor中，reactor监听指定端口，根据状态来触发factory中不同的方法
	reactor.run()   # 启动一个TCP服务器， 监听1234端口，reactor则开始监听。

if __name__ == "__main__":
	main()
