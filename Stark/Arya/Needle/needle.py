#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


import sys
import os


if __name__ == "__main__":
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取到Needle目录
	sys.path.append(BASE_DIR)  # 将Needle加入环境变量
	from core import main
	main.CommandManagement(sys.argv)
