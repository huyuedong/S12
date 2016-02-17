#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化消费记录的数据库
"""

import os
import pickle

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = "{}\\database\\record.db".format(base_path)

with open(file_name, "ab") as fp:
	a = {}
	pickle.dump(a, fp)
