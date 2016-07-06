#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
注册的模块
"""

from modules import users, files


modules = {
	"user": users.UserModule,
	"file": files.FileModule
}
