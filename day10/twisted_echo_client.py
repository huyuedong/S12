#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
twisted ex client
"""
from twisted.internet import reactor, protocol


# 定义一个自己的类，管理自己与server之间的状态。
class EchoClient(protocol.Protocol):
	"""
	主要功能就是：只要连接建立就发送一个消息，然后打印结果。
	Protocol描述了如何以异步的方式处理网络中的事件，这里继承protocol.Protocol是为了重写里面的一些方法
	Protocol包括如下方法，都可以在继承的基础上进行重写
	makeConnection               在transport对象和服务器之间建立一条连接
	connectionMade               连接建立起来后调用
	dataReceived                 接收数据时调用
	connectionLost               关闭连接时调用
	"""

	# 创建连接，重写了父类的connectionMade方法
	def connectionMade(self):
		"""
		连接一建立就给server端发送一个'Hello Alex!'的消息。
		:return:
		"""
		self.transport.write("Hello Alex.")

	# 数据接收的功能
	def dataReceived(self, data):
		"""
		一收到消息就把消息打印出来，并关闭此链接。
		:param data:
		:return:
		"""
		print("Server said:", data)     # 打印收到的消息
		self.transport.loseConnection()     # 断开连接

	def connectionLost(self, reason):
		"""
		链接被关闭时执行的方法
		:param reason: 关闭链接的原因
		:return:
		"""
		print("connection lost.")   # 打印链接关闭的提示信息。


# 定义一个自己的工厂类，继承protocol.ClientFactory，并复写了一些父类的方法。
class EchoFactory(protocol.ClientFactory):
	protocol = EchoClient

	def clientConnectionFailed(self, connector, reason):
		"""
		建立链接失败时执行的方法
		:param connector: 链接名
		:param reason: 原因
		:return:
		"""
		print("Connection failed - goodbye!")   # 打印链接建立失败的提示信息
		reactor.stop()  # 关闭reactor

	def clientConnectionLost(self, connector, reason):
		"""
		失去链接时执行的方法
		:param connector: 链接名
		:param reason: 原因
		:return:
		"""
		print("Connection lost - goodbye!")     # 打印失去链接时的提示信息
		reactor.stop()  # 关闭reactor


def main():
	f = EchoFactory()   # 实例化一个client端的事件
	# reactor(反应堆)就是twisted的事件驱动，是twisted的核心.
	reactor.connectTCP("localhost", 1234, f)    # 把f的回调函数注册到reactor,并向localhost:1234发起一个链接请求
	reactor.run()   # 启动reactor监测

if __name__ == "__main__":
	main()
