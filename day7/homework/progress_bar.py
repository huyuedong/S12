#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
打印进度条
"""

import sys
import time


def process_bar(start, end, width=50):
	"""
	打印进度条。。。
	:param start: 当前数据量
	:param end: 总数据量
	:param width: 总的进度条长度
	:return:
	"""
	# 当前百分数
	str_num = "{:.2f}%".format(start/end*100)
	# 当前要打印“#“的个数
	front = int(start * width / end)
	front_tag = "#" * front
	end_tag = " " * (width - front)
	tag = "{}{}".format(front_tag, end_tag)
	# 生成当前的进度条
	str_tag = "{:<7} [{}] {:,}\r".format(str_num, tag, end)
	# 打印当前进度条
	sys.stdout.write(str_tag)
	sys.stdout.flush()
	# 如果进度完成，则打印换行
	if len(str_tag) == width:
		sys.stdout.write("\n")
		sys.stdout.flush()


if __name__ == "__main__":
	for i in range(1, 101):
		process_bar(i, 100)
		i += 1
		time.sleep(0.1)
