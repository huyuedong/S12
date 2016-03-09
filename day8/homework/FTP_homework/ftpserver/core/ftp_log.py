#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import logging
from conf import setting


def my_logger(log_type):
	logger = logging.getLogger(log_type)
	logger.setLevel(setting.LOG_LEVEL)

	log_file = "setting.BASE_DIR/log/{}".format(setting.LOG_TYPES[log_type])
	fh = logging.FileHandler(log_file)
	formatter = logging.Formatter('[%(asctime)s] [task_id:%(name)s] [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s')
	fh.setFormatter(formatter)
	logger.addHandler(fh)

	return logger
