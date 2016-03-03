#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import logging
from conf import setting


class FTPLogger(logging):
	def __init__(self, log_type):
		self.log_type = log_type

	def my_logger(self):
		logger = logging.getLogger(self.log_type)
		logger.setLevel(setting.LOG_LEVEL)

		log_file = "setting.BASE_DIR/log/{}".format(setting.LOG_TYPES[self.log_type])
