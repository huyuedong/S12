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
			"server": ["model", "cpu_count", "cpu_core_count", "cpu_model", "raid_type", "os_type", "os_distribution", "os_release"],
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

	def __verify_field(self, data_set, field_key, data_type, required=True):
		"""
		检测数据中的指定字段的类型是否正确
		:param data_Set:
		:param field_key:
		:param data_type:
		:param required:
		:return:
		"""
		field_val = data_set.get(field_key)  # 得到数据集中指定字段的值
		if field_val:
			try:
				data_set[field_key] = data_type(field_val)
			except ValueError as e:
				self.response_msg("error", "InvalidField", "The field {}'s data type is invalid,the correct data type should be {}.".format(field_key, data_type))
		elif required is True:
			self.response_msg("error", "LackOfField", "The field {} has no value provided in your reporting data {}".format(field_key, data_set))

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
		create_obj = func()

	def _update_server(self):
		"""
		更新服务器的资产数据
		"""
		self.__update_asset_component(
			data_source=self.clean_data["nic"],
			fk="nic_set",
			update_fields=["name", "sn", "model", "macaddress", "ipaddress", "netmask", "bonding"],
			identify_field="macaddress",
		)
		self.__update_asset_component(
			data_source=self.clean_data["physical_disk_driver"],
			fk="disk_set",
			update_fields=["slot", "sn", "model", "manufactory", "capacity", "iface_type"],
			identify_field="slot",
		)
		self.__update_asset_component(
			data_source=self.clean_data["ram"],
			fk="ram_set",
			update_fields=["slot", "sn", "model", "capacity"],
			identify_field="slot",
		)
		self.__update_cpu_component()
		self.__update_manufactory_component()
		self.__update_server_component()

	def _create_server(self):
		self.__create_server_info()
		self.__create_or_update_manufactory()
		self.__create_cpu_component()
		self.__create_disk_component()
		self.__create_nic_component()
		self.__create_ram_component()

		log_msg = "Asset [<a href='/admin/assets/asset/{}/' target='_blank'>{}</a>] has been created!".format(self.asset_obj.id, self.asset_obj)
		self.response_msg("info", "NewAssetOnline", log_msg)

	def __create_server_info(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, "model", str)
			if not len(self.response["error"]) or ignore_errs is True:  # 如果没有错误或者忽略错误
				data_set = {
					"asset_id": self.asset_obj.id,
					"raid_type": self.clean_data.get("raid_type"),
					"model": self.clean_data.get("model"),
					"os_type": self.clean_data.get("os_type"),
					"os_distribution": self.clean_data.get("os_distribution"),
					"os_release": self.clean_data.get("os_release"),
				}
				obj = models.Server(**data_set)
				obj.save()
				return obj
		except Exception as e:
			self.response_msg("error", "ObjectCreattionException", "Object [server] {}".format(str(e)))

	def __create_or_update_manufactory(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, "manufactory", str)
			manufactory = self.clean_data.get("manufactory")
			if not len(self.response["error"]) or ignore_errs is True:  # 如果没有错误或者忽略错误
				obj_exist = models.Manufactory.objects.filter(manufactory=manufactory)  # 先去数据库里搜索厂商
				if obj_exist:  # 如果厂商存在
					obj = obj_exist[0]
				else:  # 不存在就创建一个厂商
					obj = models.Manufactory(manufactory=manufactory)
					obj.save()
				self.asset_obj.manufactory = obj  # 将该资产的厂商更新
				self.asset_obj.save()  # 保存
		except Exception as e:
			self.response_msg("error", "ObjectCreationException", "Object [manufactory] {}".format(str(e)))

	def __create_cpu_component(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, "model", str)
			self.__verify_field(self.clean_data, "cpu_count", int)
			self.__verify_field(self.clean_data, "cpu_core_count", int)
			if not len(self.response["error"]) or ignore_errs is True:  # 如果没有错误或者忽略错误
				data_set = {
					"asset_id": self.asset_obj.id,
					"cpu_model": self.clean_data.get("cpu_model"),
					"cpu_count": self.clean_data.get("cpu_count"),
					"cpu_core_count": self.clean_data.get("cpu_core_count"),
				}
				obj = models.CPU(**data_set)
				obj.save()
				log_msg = "Asset [{}] --- has added new [CPU] component with data [{}].".format(self.asset_obj, data_set)
				self.response_msg("info", "NewComponentAdded", log_msg)
				return obj
		except Exception as e:
			self.response_msg("error", "ObjectCreationException", "Object [CPU] {}".format(str(e)))

	def __create_disk_component(self):
		disk_info = self.clean_data.get("physical_disk_driver")
		if disk_info:
			for disk_item in disk_info:  # 遍历硬盘数据
				try:
					self.__verify_field(disk_item, "slot", str)
					self.__verify_field(disk_item, "capacity", float)
					self.__verify_field(disk_item, "iface_type", str)
					self.__verify_field(disk_item, "model", str)
					if not len(self.response["error"]):  # 没有错误
						data_set = {
							"asset_id": self.asset_obj.id,
							"sn": disk_item.get("sn"),
							"slot": disk_item.get("slot"),
							"capacity": disk_item.get("capacity"),
							"model": disk_item.get("model"),
							"iface_type": disk_item.get("iface_type"),
							"manufactory": disk_item.get("manufactory"),
						}
						obj = models.Disk(**data_set)
						obj.save()
				except Exception as e:
					self.response_msg("error", "ObjectCreationException", "Object [disk] {}.".format(str(e)))
		else:
			self.response_msg("error", "LackOfData", "Disk info is not provied in your reporting data.")

	def __create_nic_component(self):
		nic_info = self.clean_data.get("nic")
		if nic_info:
			for nic_item in nic_info:
				try:
					self.__verify_field(nic_item, "macaddress", str)
					if not len(self.response["error"]):
						data_set = {
							"asset_id": self.asset_obj.id,
							"name": nic_item.get("name"),
							"sn": nic_item.get("sn"),
							"macaddress": nic_item.get("macaddress"),
							"ipaddress": nic_item.get("ipaddress"),
							"bonding": nic_item.get("bonding"),
							"model": nic_item.get("model"),
							"netmask": nic_item.get("name"),
						}
						obj = models.NIC(**data_set)
						obj.save()
				except Exception as e:
					self.response_msg("error", "ObjectCreationException", "Object [NIC] {}.".format(str(e)))
		else:
			self.response_msg("error", "LackOfData", "NIC info is not provied in your reporting data")

	def __create_ram_component(self):
		ram_info = self.clean_data.get("ram")
		if ram_info:
			for ram_item in ram_info:
				try:
					self.__verify_field(ram_item, "capacity", int)
					if not len(self.response["error"]):
						data_set = {
							"asset_id": self.asset_obj.id,
							"slot": ram_item.get("slot"),
							"sn": ram_item.get("sn"),
							"capacity": ram_item.get("capacity"),
							"model": ram_item.get("model"),
						}
						obj = models.RAM(**data_set)
						obj.save()
				except Exception as e:
					self.response_msg("error", "ObjectCreationException", "Object [RAM] {}.".format(str(e)))
		else:
			self.response_msg("error", "LackOfData", "RAM info is not provied in your reporting data")

	def __update_server_component(self):
		update_fields = ["model", "raid_type", "os_type", "os_distribution", "os_release"]
		if hasattr(self.asset_obj, "server"):
			self.__compare_componet(
				model_obj=self.asset_obj.server,
				fields_from_db=update_fields,
				data_source=self.clean_data,
			)
		else:
			self.__create_server_info(ignore_errs=True)

	def __update_manufactory_component(self):
		self.__create_or_update_manufactory(ignore_errs=True)

	def __update_cpu_component(self):
		update_fields = ["cpu_model", "cpu_count", "cpu_core_count"]
		if hasattr(self.asset_obj, "cpu"):
			self.__compare_componet(
				model_obj=self.asset_obj.cpu,
				fields_from_db=update_fields,
				data_source=self.clean_data,
			)
		else:
			self.__create_cpu_component(ignore_errs=True)

	def __update_asset_component(self, data_source, fk, update_fields, identify_field=None):
		"""

		:param data_source: 汇报上来的组件数据
		:param fk: 每个资产和资产组件的关联KEY
		:param update_fields: 数据库中需要对比和更新的字段
		:param identify_field: 每个资产的标识每个组件
		:return:
		"""
		print(data_source, update_fields, identify_field)
		try:
			component_obj = getattr(self.asset_obj, fk)
			if hasattr(component_obj, "select_related"):  # 反射得到M2M的关系对象
				objects_from_db = component_obj.select_related()
				for obj in objects_from_db:
					key_field_data = getattr(obj, identify_field)  # 反射得到数据库中的值
					if type(data_source) is list:
						for source_data_item in data_source:
							key_field_data_from_source_data = source_data_item.get(identify_field)
							if key_field_data_from_source_data:
								if key_field_data == key_field_data_from_source_data:
									self.__compare_componet(
										model_obj=obj,
										fields_from_db=update_fields,
										data_source=source_data_item
									)
									break  # 必须跳出虚幻
							else:
								self.response_msg("warning", "AssetUpdateWarning", "Asset component [{}]'s key field [{}] is not provided in reporting data.".format(fk, identify_field))
						else:  # 循环完没有退出,表示没有找到匹配的
							print("\033[33;1mError:cannot find any matches in source data by using key field val [{}],component data is missing in reporting data!\033[0m".format(key_field_data))
							self.response_msg("warning", "AssetUpdateWarning", "Cannot find any matches in source data by using key field val [{}],component data is missing in reporting data!".format(key_field_data))
					else:  # 汇报上来的元数据格式不是列表
						print("\033[31;1mMust be sth wrong, logic should not goes to here at all.\033[0m")
				# 比较完了所有的数据
				self.__filter_add_or_deleted_components(
					model_obj_name=component_obj.model_meta.object_name,
					data_from_db=objects_from_db,
					data_source=data_source,
					identify_field=identify_field,
				)
			else:  # 该资产与资产是反向关联的类型
				pass
		except ValueError as e:
			print("\033[41;1m{}\033[0m".format(str(e)))

	def __filter_add_or_deleted_components(self, model_obj_name, data_from_db, data_source, identify_field):
		"""
		找出所有在数据库中有但是汇报数据里没有的组建的数据
		"""
		print(data_from_db, data_source, identify_field)
		data_source_key_list = []
		if type(data_source) is list:  # 确保源数据的格式正确
			for data in data_source:
				data_source_key_list.append(data.get(identify_field))
		print("-->identify field from source:{}.".format(data_source_key_list))
		print("-->identify from db:{}.".format([getattr(obj, identify_field) for obj in data_from_db]))

		data_source_key_list = set(data_source_key_list)
		data_identify_val_from_db = set([getattr(obj, identify_field) for obj in data_from_db])
		data_only_in_db = data_identify_val_from_db - data_source_key_list  # 得到只在数据库中有的（需要删除的）
		data_only_in_data_source = data_source_key_list - data_identify_val_from_db  # 得到只在源数据中有的（需要添加的）
		print("\033[31;1mdata_only_in_db:\033[0m".format(data_only_in_db))
		print("\033[31;1mdata_only_in_data source:\033[0m".format(data_only_in_data_source))
		self.__delete_components(
			all_components=data_from_db,
			delete_list=data_only_in_db,
			identify_field=identify_field,
		)
		if data_only_in_data_source:
			self.__add_components(
				model_obj_name=model_obj_name,
				all_components=data_source,
				add_list=data_only_in_data_source,
				identify_field=identify_field,
			)

	def __add_components(self, model_obj_name, all_components, add_list, identify_field):
		model_class = getattr(models, model_obj_name)
		will_be_creating_list = []
		print("-->add component list:", add_list)
		if type(all_components) is list:
			for data in all_components:
				if data[identify_field] in add_list:
					will_be_creating_list.append(data)
		try:
			for component in will_be_creating_list:
				data_set = {}
				for field in model_class.auto_create_fields:
					data_set[field] = component.get(field)
				data_set["asset_id"] = self.asset_obj.id
				obj = model_class(**data_set)
				obj.save()
				print("\033[32;1mCreated component with data:\033[0m", data_set)
				log_msg = "Asset[{}] --> component[{}] has justed added a new item [{}].".format(self.asset_obj, model_obj_name, data_set)
				self.response_msg("info", "NewComponentAdded", log_msg)
				log_handler(self.asset_obj, "NewComponentAdded", self.request.user, log_msg)
		except Exception as e:
			print("\033[31;1m{}\033[0m".format(str(e)))
			log_msg = "Asset[{}] --> component[{}] has error:{}.".format(self.asset_obj, model_obj_name, str(e))
			self.response_msg("error", "AddingComponentException", log_msg)

	def __delete_components(self, all_components, delete_list, identify_field):
		"""
		delete_list里的都将被删除
		"""
		deleting_obj_list = []
		print("-->deleting components", delete_list, identify_field)
		for obj in all_components:
			val = getattr(obj, identify_field)
			if val in delete_list:
				deleting_obj_list.append(obj)
		for i in deleting_obj_list:
			log_msg = "Asset[{}] --> component[{}] --> is lacking from reporting source data, assume it has been removed or replaced,will also delete it from DB".format(self.asset_obj, i)
			self.response_msg("info", "HardwareChanges", log_msg)
			log_handler(self.asset_obj, "HardwareChanges", self.request.user, log_msg, i)
			i.delete()

	def __compare_componet(self, model_obj, fields_from_db, data_source):
		for field in fields_from_db:
			val_from_db = getattr(model_obj, field)
			val_from_data_source = data_source.get(field)

			if val_from_data_source:
				if type(val_from_db) in (int,):
					val_from_data_source = int(val_from_data_source)
				elif type(val_from_db) is float:
					val_from_data_source = float(val_from_data_source)
				if val_from_db == val_from_data_source:
					pass
				else:
					print("\033[34;1m val_from_db[{}] != val_from_data_source[{}]\033[0m".format(val_from_db, val_from_data_source))
					db_field = model_obj._meta.get_field(field)
					db_field.save_form_data(model_obj, val_from_data_source)
					model_obj.update_date = timezone.now()
					model_obj.save()
					log_msg = "Asset[{}] --> component[{}] --> field[{}] has changed from [{}] to [{}]".format(self.asset_obj, model_obj, field, val_from_db, val_from_data_source)
					self.response_msg("info", "FieldChanged", log_msg)
					log_handler(self.asset_obj, "FieldChanged", self.request.user, log_msg, model_obj)
			else:
				self.response_msg("warning", "AssetUpdateWarning", "Asset component [{}]'s field [{}] is not provided in reporting data".format(model_obj, field))
		model_obj.save()


def log_handler(asset_obj, event_name, user, detail, component=None):
	"""
	(1, u"硬件变更"),
	(2, u"新增配件"),
	(3, u"设备下线"),
	(4, u"设备上线"),
	"""
	log_catelog = {
		1: ["FieldChanged", "HardwareChanges"],
		2: ["NewComponentAdded", ],
	}
	if not user.id:
		user = models.UserProfile.objects.filter(is_admin=True).last()
	event_type = None
	for k, v in log_catelog.items():
		if event_name in v:
			event_type = k
			break
	log_obj = models.EventLog(
		name=event_name,
		event_type=event_type,
		asset_id=asset_obj.id,
		component=component,
		detail=detail,
		user_id=user.id,
	)
	log_obj.save()
