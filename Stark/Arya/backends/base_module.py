#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import importlib

class BaseSaltModule(object):
	def __init__(self, sys_argvs, db_models, settings):
		self.db_models = db_models
		self.settings = settings
		self.sys_argvs = sys_argvs

	def argv_validation(self, argv_name, val, data_type):
		"""
		参数监测
		:param argv_name:
		:param val:
		:param data_type:
		:return:
		"""
		if type(val) is not data_type:
			exit("Error:[{}]'s data type is invalid!")

	def get_selected_os_types(self):
		"""
		获取已有操作系统类型
		:return:
		"""
		data = {}
		for host in self.host_list:
			data[host.os_type] = []
		return data

	def process(self):
		"""
		处理参数，将主机按OS类型分组
		:return:
		"""
		self.fetch_hosts()
		self.config_data_dic = self.get_selected_os_types()

	def require(self, *args, **kwargs):
		"""
		处理需要解决的依赖
		:return:
		"""
		print("In require...".center(50, "="))
		os_type = kwargs.get("os_type")
		self.require_list = []
		for item in args[0]:
			for mod_name, mod_val in item.items():
				module_obj = self.get_module_instance(base_mod_name=mod_name, os_type=os_type)
				require_condition = module_obj.is_required(mod_name, mod_val)
				self.require_list.append(require_condition)  # 得到依赖

	def fetch_hosts(self):
		"""
		获取主机列表
		:return:
		"""
		print("--fetching hosts---")

		if "-h" in self.sys_argvs or "-g" in self.sys_argvs:
			host_list = []
			if "-h" in self.sys_argvs:  # "-h"
				host_str_index = self.sys_argvs.index("-h") + 1
				if len(self.sys_argvs) <= host_str_index:
					exit("host argument must be provided after -h")
				else:  # get the host str
					host_str = self.sys_argvs[host_str_index]
					host_str_list = host_str.split(',')
					host_list.extend(self.db_models.Host.objects.filter(hostname__in=host_str_list))  # 查询数据库
					print("host list:", host_list)
			if "-g" in self.sys_argvs:  # "-g"
				group_str_index = self.sys_argvs.index("-g") + 1
				if len(self.sys_argvs) <= group_str_index:
					exit("group argument must be provided after -g")
				else:  # get the group str
					group_str = self.sys_argvs[group_str_index]
					group_str_list = group_str.split(",")
					group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list)  # 查询数据库
					for group in group_list:
						host_list.extend(group.hosts.selected_related())
				self.host_list = list(set(host_list))  # 得到主机列表
				print("get host list:", self.host_list)
				return True
			else:
				exit("host [-h] or group[-g] argument must be provided")

	def is_required(self, *args, **kwargs):
		exit("Error:is_required() method must be implemented in module class {}".format(args[0]))

	def get_module_instance(self, *args, **kwargs):
		base_mod_name = kwargs.get("base_mode_name")
		os_type = kwargs.get("os_type")
		plugin_file_path = "{}/{}.py".format(self.settings.SALT_PLUGINS_DIR, base_mod_name)  # 得到插件
		if os.path.isfile(plugin_file_path):  # 如果插件存在
			# 导入模块
			# TODO without test (importlib)...
			module_plugin = importlib.import_module(base_mod_name, package="plugins")
			special_os_module_name = "{}{}".format(os_type.capitalize(), base_mod_name.capitalize())
			module_file = getattr(module_plugin, base_mod_name)
			if hasattr(module_file, special_os_module_name):  # 如果有特殊的方法
				module_instance = getattr(module_file, special_os_module_name)
			else:
				module_instance = getattr(module_file, base_mod_name.capitalize())
			# 调用此模块进行解析
			module_obj = module_instance(self.sys_argvs, self.db_models, self.settings)
			return module_obj
		else:
			exit("Module [{}] is not exist!".format(base_mod_name))

	def syntax_parser(self, section_name, module_name, module_data, os_type):
		"""
		state文件语法检查
		:param section_name:
		:param module_name:
		:param module_data:
		:param os_type:
		:return:
		"""
		print("going to parser state data:", section_name, module_name)
		self.raw_cmds = []
		self.single_line_cmds = []

		for state_item in module_data:
			print("\t", state_item)
			for key in state_item:
				if hasattr(self, key):
					state_func = getattr(self, key)
					state_func(state_item[key])
				else:
					exit("Error:module:{} has no argument:{}.".format(module_name, key))
			else:
				if "." in module_name:
					base_module_name, module_action = module_name.split(".")
					if hasattr(self, module_action):
						mod_action_func = getattr(self, module_action)
						cmd_list = mod_action_func(section=section_name, mod_data=module_data)
						data = {
							"cmd_list": cmd_list,
							"required_list": self.require_list
						}
						if type(cmd_list) is dict:
							data["file_module"] = True
							data["sub_action"] = cmd_list.get("sub_action")
						# 上面代表一个section里的module已经解析完了
						return data
					else:
						exit("Error:module [{}] has no method [{}]".format(module_name, module_action))
				else:
					exit("Error:module action of [{}] must be supplied".format(module_name))
