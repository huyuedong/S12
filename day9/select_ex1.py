#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
select方法
利用select实现监听终端的操作
"""

import select
import sys

while True:
	readable, writeable, err = select.select([sys.stdin, ], [], [], 1)
	if sys.stdin in readable:
		print("select get stdin:", sys.stdin.readline())
