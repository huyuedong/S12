#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
Linux下Python的自动补全模块
需要安装readline、readline-devel
放在lib/site-packages/下
"""

import sys
import readline
import rlcompleter
import atexit
import os

# tab completion
readline.parse_and_bind('tab:complete')
# history file
history_file = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
	readline.read_history_file(history_file)
except IOError:
	pass
atexit.register(readline.write_history_file, history_file)
