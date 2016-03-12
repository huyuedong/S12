#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
url
"""

import gevent
from urllib.request import urlopen
from gevent import monkey
monkey.patch_all()


def f(url):
	print("GET:", url)
	resp = urlopen(url)
	data = resp.read()
	print("{} bytes received from {}.".format(len(data), url))

gevent.joinall([
	gevent.spawn(f, "https://www.baidu.com"),
	gevent.spawn(f, "https://www.yahoo.com"),
	gevent.spawn(f, "https://www.github.com"),
])
