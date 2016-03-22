#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用twisted 接收文件的客户端
notice:Python2.x
"""

import optparse

from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
	# 定义一个解析命令行参数的函数
	usage = """
	%prog [options] [hostname]:port ...
	"""

	parser = optparse.OptionParser(usage)  # 实例化一个optparse.OptionParser对象

	_, addresses = parser.parse_args()  # 解析命令行的选项和参数，这里选项未定义所以把它复制给一个无关变量，主要得到address

	if not addresses:  # 如果没有解析到address就打印提示信息，并退出解析
		print(parser.format_help())
		parser.exit()

	def parse_address(addr):  # 定义一个处理address的函数
		if ":" not in addr:  # 如果解析到的address没有‘:’，就说明用户只输入了port，host就默认为本机
			host = "127.0.0.1"
			port = addr
		else:  # 如果解析到的输入有':'就表明用户输入了host:port，按':'分割一次分别得到host和port
			host, port = addr.split(":", 1)

		if not port.isdigit():  # 对解析出来的端口进行合法性检测
			parser.error("Ports must be integers.")  # 解析出来的端口号不是数字就报错
		return host, int(port)  # 端口号合法就返回host和port
	return map(parse_address, addresses)  # 利用定义好的处理address函数遍历处理从命令行解析到的address,返回所有正确格式


# 定义一个自己的传诗的协议（类）
class PoetryProtocol(Protocol):
	poem = ""  # 初始化文件为一空的字符串

	def dataReceived(self, data):  # 重写父类中接收数据的方法
		self.poem += data  # 拼接收到的数据

	def connectionLost(self, reason):  # 重写父类中连接丢失的方法
		self.poemReceived(self.poem)  # 连接丢失时执行poemReceived()方法

	def poemReceived(self, poem):  # 自定义一个方法
		self.factory.poem_finished(poem)  # 将接收到的文件内容传递给工厂类的poem_finished()方法


# 定义一个client端工厂类，继承ClientFactory
class PoetryClientFactory(ClientFactory):

	protocol = PoetryProtocol  # 重写协议(类)

	def __init__(self, callback):
		"""
		构造方法
		:param callback: 这里要传入一个回调函数
		:return:
		"""
		self.callback = callback  # 将传入的回调函数赋值给self.callback

	def poem_finished(self, poem):  # 自定义一个方法，调用回调函数处理自己的参数
		self.callback(poem)


def get_poetry(host, port, callback):
	"""
	从给定的主机和端口接收数据
	:param host: server主机
	:param port: server端口
	:param callback: 回调函数
	:return:
	"""
	from twisted.internet import reactor  # 导入
	factory = PoetryClientFactory(callback)  # 实例化一个client端的工厂类，并传入一个回调函数
	reactor.connectTCP(host, port, factory)  # 给reactor传入主机和端口号，并且把client端工厂类的实例注册到reactor


def poetry_main():  # 主函数
	addresses = parse_args()  # 调用parser_args()解析命令函参数，得到一个列表
	from twisted.internet import reactor

	poems = []  # 定义一个存放接收数据的空列表

	def got_poem(poem):  # 定义一个接收函数
		poems.append(poem)  # 将受到的数据添加到列表
		if len(poems) == len(addresses):  # 如果接收到的数据个数和传输的地址个数相同，就说明传输完毕
			reactor.stop()  # 关闭reactor

	for address in addresses:  # 遍历地址列表
		host, port = address  # 拼接实际地址
		get_poetry(host, port, got_poem)  # 调用get_poetry()函数接收数据

	reactor.run()  # 启动reactor

	for poem in poems:  # 遍历打印接收到的数据
		print(poem)

if __name__ == "__main__":
	poetry_main()
