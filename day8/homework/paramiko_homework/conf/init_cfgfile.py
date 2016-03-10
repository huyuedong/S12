#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化配置文件
"""

import json
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import setting

config = {}
config["default"] = {}
config["db"] = {}
config["db"]["hostname1"] = {}
config["db"]["hostname1"]["ip"] = "172.18.26.193"
config["db"]["hostname1"]["port"] = "22"
config["db"]["hostname2"] = {}
config["db"]["hostname2"]["ip"] = "192.168.183.131"
config["db"]["hostname2"]["port"] = "22"
config["nginx"] = {}
config["nginx"]["hostname1"] = {}
config["nginx"]["hostname1"]["ip"] = "172.18.26.193"
config["nginx"]["hostname1"]["port"] = "22"
with open(setting.CONFIG, "w") as f:
	json.dump(config, f)

