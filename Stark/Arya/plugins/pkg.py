#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from Arya.backends import base_module


class PKG(base_module.BaseSaltModule):

	def __init__(self, sys_argvs, db_models):
		super().__init__(sys_argvs, db_models)
		print("in pkg module.")
