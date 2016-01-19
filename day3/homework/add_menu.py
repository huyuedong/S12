#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
实现在配置文件下对应的url下添加server信息的功能
    -输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }
    -添加到对应的backend下
"""

import json


def add_menu(arg):
	arg = json.loads(arg)
	url = arg['backend']
	with open('haproxy.cfg', 'w+'):
		pass
