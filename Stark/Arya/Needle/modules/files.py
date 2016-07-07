#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""

"""

import urllib.request
import os
import shutil
from modules.base_module import BaseSaltModule


class FileModule(BaseSaltModule):

	def func__managed(self, *args, **kwargs):
		module_data = kwargs.get("module_data")
		print("\033[41;1m managed module data:\033[0m", module_data)
		target_file_path = module_data["section"]  # 目标文件路径
		if self.has_source:  # 需要把这个文件copy成section指定的文件
			if self.source_file is not None:  # 已经下载
				shutil.copyfile(self.source_file, target_file_path)
				print("copy file from [{}] to [{}]".format(self.source_file, target_file_path))

	def func__directory(selfself, *args, **kwargs):
		module_data = kwargs.get("module_data")
		print("\033[41;1m Directory module data:\033[0m", module_data)

	def func__user(self, *args, **kwargs):
		pass

	def func__group(self, *args, **kwargs):
		pass

	def func__mode(self, *args, **kwargs):
		pass

	def download_http(self, file_path):
		print("Downloading from http:", file_path)
		print("Downloading with urllib2")
		http_server = self.task_obj.main_obj.configs.FILE_SERVER.get("http")
		url_arg = "file_path={}".format(file_path)
		filename = os.path.basename(file_path)  # 根据文件路径获取文件名
		url = "http://{}{}?{}".format(http_server, self.task_obj.main_obj.configs.FILE_SERVER_BASE_PATH, url_arg)
		print("\033[45;1m httpserver\033[0m", url, self.task_obj.task_body["id"])
		f = urllib.request.urlopen(url)
		data = f.read()
		file_save_path = "{}/{}".format(self.task_obj.main_obj.configs.FILE_SERVER_BASE_PATH, self.task_obj.task_body["id"])

		if not os.path.isdir(file_save_path):
			os.mkdir(file_save_path)
		with open(file_save_path, "wb") as code:
			code.write(data)
		return "{}/{}".format(file_save_path, filename)

	def download_salt(self, file_path):
		print("Downloading from salt:", file_path)

	def func__source(self, *args, **kwargs):
		file_url = args[0]
		print("Downloading ...", file_url)
		download_type, file_path = file_url.split(":")  # 分离出下载类型和文件路径
		file_download_func = getattr(self, "download_{}".format(download_type))
		self.source_file = file_download_func(file_path)
		self.has_source = True

	def func__sources(self, *args, **kwargs):  # 多文件
		for file_source in args[0]:
			self.func__source(file_source)

	def func__recurse(self, *args, **kwargs):
		pass
