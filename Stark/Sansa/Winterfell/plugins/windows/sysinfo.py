#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
windows client 端插件
"""


import platform
import win32com
import wmi


def collect():
	data = {
		"os_type": platform.system(),
		"os_release": "{} {} {}".format(platform.release(), platform.architecture()[0], platform.version()),
		"os_distribution": "Microsoft",
		"asset_type": "server",
	}

	win32obj = Win32Info()
	data.update(win32obj.get_cpu_info())
	data.update(win32obj.get_ram_info())
	data.update(win32obj.get_server_info())
	data.update(win32obj.get_disk_info())
	data.update(win32obj.get_nic_info())

	return data


class Win32Info(object):

	def __init__(self):
		self.wmi_obj = wmi.WMI()
		self.wmi_server_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
		self.wmi_server_connector = self.wmi_server_obj.ConnectServer(".", "root\cimv2")

	def get_cpu_info(self):
		"""
		获取CPU信息
		:return:
		"""
		global cpu_model
		data = {}
		cpu_list = self.wmi_obj.Win32_Processor()
		cpu_core_count = 0

		for cpu in cpu_list:
			cpu_core_count += cpu.NumberOfCores
			cpu_model = cpu.Name
		data["cpu_count"] = len(cpu_list)
		data["cpu_model"] = cpu_model
		data["cpu_core_count"] = cpu_core_count
		# TODO ? or return {"cpu" data}
		return data

	def get_ram_info(self):
		"""
		获取RAM信息
		:return:
		"""
		data = []
		ram_collections = self.wmi_server_connector.ExecQuery("Select * from Win32_PhysicalMemory")
		for item in ram_collections:
			mb = int(1024 * 1024)
			ram_size = int(item.Capacity) / mb
			item_data = {
				"slot": item.DeviceLocator.strip(),
				"capacity": ram_size,
				"model": item.Caption,
				"manufactory": item.Manufacturer,
				"sn": item.SerialNumber,
			}
			data.append(item_data)
		return {"ram": data}

	def get_server_info(self):
		"""
		获取服务信息
		:return:
		"""
		computer_info = self.wmi_obj.Win32_ComputerSystem()[0]
		system_info = self.wmi_obj.Win32_OperatingSystem()[0]
		data = {}
		data["manufactory"] = computer_info.Manufacturer
		data["model"] = computer_info.Model
		data["wake_up_type"] = computer_info.WakeUpType
		data["sn"] = system_info.SerialNumber
		return data

	def get_disk_info(self):
		data = []
		for disk in self.wmi_obj.Win32_DiskDrive():
			item_data = {}
			iface_choices = ["SAS", "SCSI", "SATA", "SSD"]
			for iface in iface_choices:
				if iface in disk.Model:
					item_data["iface_type"] = iface
					break
			else:
				item_data["iface_type"] = "unknown"
			item_data["slot"] = disk.Index
			item_data["sn"] = disk.SerialNumber
			item_data["model"] = disk.Model
			item_data["manufactory"] = disk.Manufacturer
			item_data["capacity"] = int(disk.Size) / (1024*1024*1024)
			data.append(item_data)
		return {"physical_disk_driver": data}

	def get_nic_info(self):
		data = []
		for nic in self.wmi_obj.Win32_NetworkAdapterConfiguration():
			if nic.MACAddress:
				item_data = {}
				item_data["macaddress"] = nic.MACAddress
				item_data["model"] = nic.Caption
				item_data["name"] = nic.Index
				if nic.IPAddress:
					item_data["ipaddrsss"] = nic.IPAddress
					item_data["netmask"] = nic.IPSubnet
				else:
					item_data["ipaddrsss"] = ""
					item_data["netmask"] = ""
				bonding = 0
				data.append(item_data)
		return {"nic": data}

if __name__ == "__main__":
	a = collect()
	print(a)
