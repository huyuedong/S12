#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
测试下os模块的功能
"""

import os

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.normcase(os.path.abspath(__file__)))
print(os.path.normpath(os.path.abspath(__file__)))
print(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "test.log"))

