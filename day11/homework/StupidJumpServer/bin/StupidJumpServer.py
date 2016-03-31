#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
主程序入口
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import Mylogging


if __name__ == "__main__":
	from core.actions import start_by_command
	start_by_command()




