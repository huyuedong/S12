#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import importlib
from Arya.backends.base_module import BaseSaltModule


class State(BaseSaltModule):
	"""
	定义每个模块特有的方法
	"""
	def load_state_files(self, state_filename):
		from yaml import load, dump
		try:
			from yaml import CLoader as Loader, CDumper as Dumper
		except ImportError:
			from yaml import Loader, Dumper
		state_file_path = "{}/{}".format(self.settings.SALT_CONFIG_FILES_DIR, state_filename)  # 配置文件路径
		if os.path.isfile(state_file_path):
			with open(state_file_path) as f:
				data = load(f.read(), Loader=Loader)
				return data
		else:
			exit("{} is not a valid yaml config file".format(state_filename))

	def apply(self):
		"""
			1. load the configurations file
			2. parse it
			3. create a task and sent it to the MQ
			4. collect the result with task-callback id
		:return:
		"""

		if '-f' in self.sys_argvs:
			yaml_file_index = self.sys_argvs.index('-f') + 1
			try:
				yaml_filename = self.sys_argvs[yaml_file_index]
				state_data = self.load_state_files(yaml_filename)

				for os_type, os_type_data in self.config_data_dic.items():  # 按照不同的操作系统单独生成一份配置文件
					for section_name, section_data in state_data.items():
						print('Section:', section_name)

						for mod_name, mod_data in section_data.items():
							base_mod_name = mod_name.split(".")[0]
							plugin_file_path = "{}/{}.py".format(self.settings.SALT_PLUGINS_DIR, base_mod_name)  # 插件路径
							if os.path.isfile(plugin_file_path):
								# 导入模块
								# TODO 使用importlib 导入模块
								module_plugin = __import__('plugins.{}'.format(base_mod_name))  # 导入包
								print("==>", module_plugin)
								module_plugin = importlib.import_module('plugins.{}'.format(base_mod_name))
								print("===>", module_plugin)
								special_os_module_name = "{}{}".format(os_type.capitalize(), base_mod_name.capitalize())
								module_file = getattr(module_plugin, base_mod_name)  # 这里才是真正导入模块（反射包内的类）
								if hasattr(module_file, special_os_module_name):  # 判断有没有根据操作系统的类型进行特殊解析的类，在这个文件里
									module_instance = getattr(module_file, special_os_module_name)
								else:
									module_instance = getattr(module_file, base_mod_name.capitalize())

								# 开始调用此module 进行配置解析
								module_obj = module_instance(self.sys_argvs, self.db_models, self.settings)
								module_obj.syntax_parser(section_name, mod_name, mod_data)
							else:
								exit("module [%s] is not exist" % base_mod_name)

			except IndexError as e:
				exit("state file must be provided after -f")

		else:
			exit("statefile must be specified.")
