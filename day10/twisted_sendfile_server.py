#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用twisted 发送文件的Server端
notice:Python2.x
"""

import optparse
import os
from twisted.internet.protocol import ServerFactory, Protocol


def parse_args():
	"""
	获取并处理命令行选项和参数的函数
	:return 返回选项和要传输的文件
	"""
	usage = """
	usage %prog [options] transport-file
	这是传送文件的server端，利用twisted实现。

	"""
	# 定义optparse对象，optparse模块主要是用来处理命令行参数，usage表示当命令参数错误或没有参数的时候输出的内容。
	parser = optparse.OptionParser(usage)

	help = "The port to listen on.Default to a random available port"  # --port选项的帮助信息
	parser.add_option("--port", type="int", help=help)  # 添加--port选项，类型为int。

	help = "The interface to listen on. Default is localhost."  # --iface的帮助信息
	parser.add_option("--iface", help=help, default="localhost")    # 添加--iface选项，默认为localhost

	options, args = parser.parse_args()  # 调用parser.parse_args解析命令行选项和参数
	print("arg==>:", options, args)     # 打印解析出来的选项和参数

	if len(args) != 1:  # 必须要指定一个要传的文件参数,否则打印提示信息。
		parser.error("Provide exactly one poetry file.")

	poetry_file = args[0]   # 获取要发送的文件
	# 判断该文件是否存在
	if not os.path.isfile(args[0]):     # 文件不存在就打印提示信息
		parser.error("No such file:{}.".format(poetry_file))

	return options, poetry_file     # 文件存在就返回执行的参数和要发送的文件


# 定义此次发送文件的协议,继承Protocol
class PoetryProtocol(Protocol):

	# 重写connectionMade方法
	def connectionMade(self):
		self.transport.write(self.factory.file)  # 将self.factory.file的内容发送给client端
		#
		self.transport.loseConnection()


# 定义server端的工厂类，继承ServerFactory
class PoetryFactory(ServerFactory):

	protocol = PoetryProtocol  # 重写协议(类)

	def __init__(self, poem):  # 构造方法
		self.poem = poem  # 将传过来的参数赋值给自身


# 主函数
def main():
	options, poetry_file = parse_args()  # 调用parse_args获得命令行的选项和参数
	poem = open(poetry_file).read()  # 读取要发送得文件

	factory = PoetryFactory(poem)  # 实例化一个工厂实例

	from twisted.internet import reactor  # 导入reactor
	# 将factory注册到reactor，返回端口号
	port = reactor.listenTCP(options.port or 9000, factory, interface=options.iface)

	print("Serving {} on {}.".format(poetry_file, port.getHost()))  # 打印提示信息：哪部分文件在哪个端口
	reactor.run()  # 启动reactor，开始监听事件

if __name__ == "__main__":
	main()

