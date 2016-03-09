#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化用户数据库
"""

import json

accounts_info = {
	"alex": {"password": "1234", "home_path": "home/alex", "total_space": 500000, "used_space": 0, "lock_flag": 0},
	"qimi": {"password": "1234", "home_path": "home/qimi", "total_space": 500000, "used_space": 0, "lock_flag": 0},
}


with open("accounts.db", "w") as f:
	json.dump(accounts_info, f)

# with open("accounts.db", "r") as f:
# 	info = json.load(f)
#
# for i in info:
# 	print(i, info[i])

