#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
配置文件
"""

import os
import datetime
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

DATABASE = {
	'engine': 'file_storage',   # support mysql,PostgreSQL in the future
	'path': "{}\db".format(BASE_PATH)
}

GOODS_TYPE = {
	"eat": {
		"六元麻辣烫": {"price": 6, "power_amount": 50},
		"庆丰包子": {"price": 36, "power_amount": 80},
		"金钱豹自助餐": {"price": 238, "power_amount": 100}
	},
	"work": {
		"餐馆服务员": {"pay": 3000, "power_amount": 100, "energy_amount": 20},
		"IT公司运维": {"pay": 10000, "power_amount": 50, "energy_amount": 30},
		"金融公司开发": {"pay": 30000, "power_amount": 10, "energy_amount": 40},
	},
	"learn": {
		"PHP": {"price": 5000, "ability_amount": 200, "energy_amount": 20},
		"JAVA": {"price": 8000, "ability_amount": 500, "energy_amount": 30},
		"Python": {"price": 10000, "ability_amount": 1000, "energy_amount": 40}
	},
	"consume": {
		"奇瑞QQ": {"price": 30000, "confidence_amount": 100},
		"哈弗H6": {"price": 150000, "confidence_amount": 300},
		"特斯拉P90D": {"price": 1000000, "confidence_amount": 1000},
		"三环大房子": {"price": 20000000, "confidence_amount": 20000},
	},
}

TIME_SCALE = {
	"hour": datetime.timedelta(seconds=1),
	"day": datetime.timedelta(seconds=5),
	"year": datetime.timedelta(seconds=10),
	"ten_year": datetime.timedelta(seconds=12),
}

