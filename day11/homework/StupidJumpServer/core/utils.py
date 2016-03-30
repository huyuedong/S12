#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
工具
"""
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import yaml
from conf import setting

logger = logging.getLogger(__name__)


def yaml_parser(yaml_file_name):
	"""
	load yaml file and return data
	:param yaml_file_name: the name of the yaml file
	:return: data in yaml file
	"""
	yaml_file_path = os.path.join(setting.CONFIGBASEPATH, yaml_file_name)
	try:
		with open(yaml_file_path, "r") as f:
			data = yaml.load(f)
			return data
	except Exception as e:
		print("Error:", e)
