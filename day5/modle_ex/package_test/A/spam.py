#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from A import grok  # 导入同一个目录中的模块grok
from B import bar    # 导入不同目录中的模块B.bar

grok.grok()

bar.bar()

