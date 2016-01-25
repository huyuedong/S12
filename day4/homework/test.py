#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re

s = "1+3*(6/2)+4"
result = re.search(r'\(.+\)', s)
if result:
	print(result.group())
