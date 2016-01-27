#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re
s = "*3+*(*"
result = re.search(r'(\(\*)(\/0)', s)
if result:
	print(result.group())

