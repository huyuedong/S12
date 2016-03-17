#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化配置文件
"""

import yaml
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import setting

groups = {}
groups["default"] = []
config["db"] = ["172.18.26.193", "192.168.183.131", ]
config["nginx"] = ["172.18.26.193", ]
config["tomcat"] = ["192.168.183.131", ]

with open(setting.CONFIG, "w") as f:
	json.dump(groups, f)

# with open(setting.CONFIG, "r") as f:
# 	dic = json.load(f)
# for k in dic:
# 	print(k, dic[k])


"""
config = {
	"default": [],
	"db": [
		"172.18.26.193",
		"192.168.183.131",
	],
	"nginx": [
		"172.18.26.193",
	],
	"tomcat": [
		"192.168.183.131",
	],
}
"""
