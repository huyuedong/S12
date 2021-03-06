#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""

"""

import os
import logging
import logging.config
import logging.handlers

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

LOGGING_DIC = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'standard': {
			'format': standard_format
		},
		'simple': {
			'format': simple_format
		},
	},
	'filters': {},
	'handlers': {
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',  # 打印到屏幕
			'formatter': 'simple'
		},
		'default': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',    # 保存到文件
			'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all.log'),
			'maxBytes': 1024*1024*5,    # 5M
			'backupCount': 5,
			'formatter': 'standard',
		},
	},
	'loggers': {
		'': {
			'handlers': ['default', 'console'],
			'level': 'DEBUG',
			'propagate': True,
		},
		'lib.plugins.JX_dev': {
			'handlers': ['default', 'console'],
			'level': 'DEBUG',
			'propagate': False,
		},
	},
}
logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger(__name__)
logger.info('It works!')


