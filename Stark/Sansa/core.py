#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import json
from django.core.exceptions import ObjectDoesNotExist
from Sansa import models
from django.utils import timezone


class Asset(object):
	def __init__(self, request):
		self.request = request
		self.mandatory_fields = ["sn", "asset_id", "asset_type"]  # 必须包含"sn", "asset_id", "asset_type
		self.field_sets = {
			"asset": ["manufactory"],
			"server": ["model", "cpu_count", "cpu_core_count", "cpu_model", "raid_type", "os_type", "os_distribution", "os_release"]
			"networkdevice": []
		}
		self.response = {  # 存放系统响应信息
			"error": [],
			"info": [],
			"warning": []
		}

	def response_msg(self, msg_type, key, msg):
		if msg_type in self.response:  # 收集指定的响应信息
			self.response[msg_type].append({key: msg})
		else:
			raise ValueError  # 有其他错误就抛出异常

	def mandatory_check(self, data, only_check_sn=False):  # 强制检查
		for field in self.mandatory_fields:
			if not field in data:
				self.response_msg("error", "MandatoryCheckFailed", "The field {} is mandatory and not provided in your reporting data".format(field))
		else:
			if self.response["error"]:return False  # 如果上面的循环有报错就退出
		try:
			if only_check_sn:  # 如果配置了只检查SN号
				self.asset_obj = models.Asset.objects.get(sn=data["sn"])
			else:
				self.asset_obj = models.Asset.objects.get(id=int(data["asset"]), sn=data["sn"])
			return True
		except ObjectDoesNotExist as e:  # 数据库里没有
			# TODO data里一定会有asset_id和sn的值
			self.response_msg("error", 'AssetDataInvalid', "Cannot find asset object in DB by using asset_id:{} and SN:{}".format(data['asset_id'],data['sn']))
			self.waiting_approval = True  # 设置待批准的标志位
			return False

	def get_asset_id_by_sn(self):
		"""
		资产数据第一次汇报过来的时候没有资产ID，
		:return:
		"""
		data = self.request.POST.get("asset_data")  # 获取发送过来的数据
		if data:
			try:
				data = json.loads(data)
				if self.mandatory_check(data, only_check_sn=True):  # 资产已经存在，就返回他的资产ID
					response = {"asset_id": self.asset_obj.id}
				else:
					if hasattr(self, "waiting_approval"):  # 如果需要审批
						response = {"needs_aproval": "This is a new asset,needs IT admin's approval to create the new asset id."}
						self.clean_data = data
						self.save_new_asset_to_approval_zone()  # 将待批准的新资产提交到待批准区
						print(response)
					else:
						response = self.response
			except ValueError as e:
				self.response_msg("error", "AssetDataInvalid", str(e))
				response = self.response
		else:
			self.response_msg("error", "AssetDataInvalid", "The reported asset data is not valid or provided")
			response = self.response
		return response

	def save_new_asset_to_approval_zone(self):
		"""
		找到新资产就将他保存在待批准区，等待IT管理员的批准
		"""
		asset_sn = self.clean_data.get("sn")
		asset_already_in_approval_zone = models.NewAssetApprovalZone.objects.get_or_create(
			sn=asset_sn,
			data=json.dumps(self.clean_data),
			manufactory=self.clean_data.get("manufactory"),
			model=self.clean_data.get("model"),
			asset_type=self.clean_data.get("asset_type"),
			ram_size=self.clean_data.get("ram_size"),
			cpu_model=self.clean_data.get("cpu_model"),
			cpu_count=self.clean_data.get("cpu_count"),
			cpu_core_count=self.clean_data.get("cpu_core_count"),
			os_type=self.clean_data.get("os_type"),
			os_distribution=self.clean_data.get("os_distribution"),
			os_release=self.clean_data.get("os_release"),
		)
		return True

	def data_is_valid(self):
		data = self.request.POST.get("asset_data")  # 获取资产数据
		if data:
			try:
				data = json.loads(data)
				self.mandatory_check(data)
				self.clean_data = data
				if not self.response["error"]:  # 没有报错
					return True
			except ValueError as e:
				self.response_msg("error", "AssetDataInvalid", str(e))
		else:  # 没数据就报错
			self.response_msg("error", "AssetDataInvalid", "The reported asset data is not valid or provided")

	def __is_new_asset(self):
		if hasattr(self.asset_obj, self.clean_data["asset_type"]):  # 如果有资产属性，就代表不是新资产
			return False
		else:
			return True

	def data_inject(self):
		"""
		保存数据到数据库，数据必须通过有效性检测。
		"""
		if self.__is_new_asset():  # 是新资产就创建
			print("\033[32;1m---new asset,going to create---\033[0m")
			self.create_asset()
		else:
			print("\033[33;1m---asset already exist ,going to update---\033[0m")
			self.update_asset()

	def data_is_valid_without_id(self):
		"""
		如果在上报的数据中没有资产ID，就先运行该方法
		"""
		data = self.request.POST.get("asset_data")
		if data:
			try:
				data = json.loads(data)
				asset_obj = models.Asset.objects.get_or_create(
					sn=data.get("sn"),
					name=data.get("name"),
				)
				data["asset_id"] = asset_obj[0].id  # 这里把数据库中的资产ID值赋给data
				self.mandatory_check(data)
				self.clean_data = data
				if not self.response["error"]:
					return True
			except ValueError as e:
				self.response_msg("error", "AssetDataInvalid", str(e))
		else:
			self.response_msg("error", "AssetDataInvali", "The reported asset data is not valid or provided")

	def create_asset(self):
		"""
		创建资产
		这里根据资产数据中的‘asset_type’，反射不同的创建方法
		"""
		func = getattr(self, "_create_{}".format(self.clean_data["asset_type"]))
		create_obj = func()

	def update_asset(self):
		"""
		更新资产的数据
		"""
		func = getattr(self, "_update_{}".format(self.clean_data["asset_type"]))
		create_obj = func

	def _update_server(self):
		"""
		更新服务器的资产数据
		"""
		nic = self.__update_asset_component(
			data_source=self.clean_data["nic"],
			fk="nic_set",
			update_fields=["name", "sn", "model", "macaddress", "ipaddress", "netmask", "bonding"],
			identify_field="macaddress",
		)
		disk = self.__update_asset_component(
			data_source=self.clean_data["physical_disk_driver"],
			fk="disk_set",
			update_fields=["slot", "sn", "model", "manufactory", "capacity", "iface_type"],
			identify_field="slot",
		)
		ram = self.__update_asset_component(
			data_source=self.clean_data["ram"],
			fk="ram_set",
			update_fields=["slot", "sn", "model", "capacity"],
			identify_fiels="slot",
		)
		cpu = self.__update_cpu_component()
		manufactory = self.__update_manufactory_component()
		server = self._update_server_component()

	def _create_server(self):
		self.__create_server_info()
		self.__create_or_update_manufactory()
		self.__create_cpu_component()
		self.__create_disk_component()
		self.__create_nic_component()
		self.__create_ram_component()

		log_msg = ""

