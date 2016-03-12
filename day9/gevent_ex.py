#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
协程
之前讲过一个用yield实现的一个人做包子，两个人吃包子的。

"""

import gevent
import time


def foo():
	print("\033[31;1m fooooooooooooooooooooo\033[0m")
	time.sleep(1)
	print("\033[32;1m back to foo\033[0m")


def bar():
	print("\033[33;1m barrrrrrrrrrrrrrrr\033[0m")
	time.sleep(1)
	print("\033[36;1m back to bar\033[0m")


def exx():
	print("\033[37;1m exxxxxxxxxxxxxxxxxx\033[0m")
	time.sleep(1)
	print("\033[38;1m back to exx\033[0m")

gevent.joinall([
	gevent.spawn(foo),
	gevent.spawn(bar),
	gevent.spawn(exx),
])
