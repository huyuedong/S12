#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
"""
贯穿开发周期内都会用到的：hasattr,setattr,getattr,delattr的介绍
传说中的反射，通过名字的字符串获取相应对象的内存地址
"""

import sys


class WebServer(object):
	def __init__(self, host, post):
		self.host = host
		self.post = post

	def start(self):
		print("Server is starting...")

	def stop(self):
		print("Server is stopping...")

	def restart(self):
		self.stop()
		self.start()


# 定义一个类外面的方法
def test_run(res):
	print("{} {} is running...".format(res.host, res.post))

if __name__ == "__main__":
	server = WebServer("localhost", 33)
	# 判断实例中是否有命令行参数同名的方法名
	if hasattr(server, sys.argv[1]):
		func = getattr(server, sys.argv[1])    # 获取对应类方法的内存地址
		# 执行上面获取的方法，可带参数。
		func()

	# setattr   # 把一个类外面的方法绑定到一个类对象中
	setattr(server, "run", test_run)
	server.run(server)

	# delattr   # 删除类方法
	delattr(WebServer, "stop")
	print("=======" * 10)
	server.restart()
