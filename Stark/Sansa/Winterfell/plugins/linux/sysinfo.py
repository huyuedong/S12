#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
Linux system info collection script
"""

import os, sys, subprocess
import re


def collect():
	filter_keys = ["Manufacturer", "Serial Number", "Product Name", "UUID", "Wake-up Type"]
	raw_data = {}
	try:
		cmd_result = subprocess.check_output("sudo dmidecode -t system", shell=True)  # 得到系统相关信息
		cmd_result = str(cmd_result, "utf8")  # 将查询系统命令的结果转换成str
		for key in filter_keys:
			re_compile = re.compile(r'{}:(.+?)\\n'.format(key))  # 动态生成正则条件
			val = re_compile.search(cmd_result)  # 从结果中查找指定的内容
			if val:  # 如果匹配到结果
				raw_data[key] = val.group(1)  # 从匹配结果中的值赋给raw_data[key]
			else:
				raw_data[key] = -1  # 没有结果就把值设为-1
	except Exception as e:
		print("error:", str(e, "utf8"))
		raw_data = dict.fromkeys(filter_keys, -2)

	data = {
		"asset_type": "server",
		"manufacory": raw_data["Manufacturer"],
		"sn": raw_data["Serial Number"],
		"model": raw_data["Product Name"],
		"uuid": raw_data["UUID"],
		"wake_up_type": raw_data["Wake-up Type"]
	}
	data.update(cpuinfo())
	data.update(osinfo())
	data.update(raminfo())
	data.update(nicinfo())
	data.update(diskinfo())
	return data


def diskinfo():
	obj = DiskPlugin()
	return obj.linux()


def nicinfo():
	raw_data = subprocess.check_output("ifconfig -a", shell=True)
	raw_data = str(raw_data, "utf8").split("\n")  # 生成一个行列表

	nic_dic = {}
	next_ip_line = False  # 是否继续分析下一行的标志位，只有'HWaddr'在当前行，才继续分析网卡名等
	last_mac_addr = None
	for line in raw_data:
		if next_ip_line:
			next_ip_line = False
			nic_name = last_mac_addr.split()[0]  # 网卡名
			mac_addr = last_mac_addr.split("HWaddr")[1].split()  # mac地址
			raw_ip_addr = line.split("inet addr:")  # 将当前行按'inet addr:'分割
			raw_bcast = line.split("Bcast:")  # 将当前行按'Bcast:'分割
			raw_netmask = line.split("Mask:")  # 将当前行按'Mask:'分割
			if len(raw_ip_addr) > 1:  # 代表有addr
				ip_addr = raw_ip_addr[1].split()[0]
				network = raw_bcast[1].split()[0]
				netmask = raw_netmask[1].split()[0]
			else:
				ip_addr = None
				network = None
				netmask = None
			# 拼接要汇报的数据
			if mac_addr not in nic_dic:
				nic_dic[mac_addr] = {
					"name": nic_name,
					"macaddress": mac_addr,
					"netmask": netmask,
					"network": network,
					"bonding": 0,
					"model": "unknow",
					"ipaddress": ip_addr,
				}
			else:  # mac地址已经存在的话，那么一定就是绑定地址
				if "{}_bonding_addr".format(mac_addr) not in nic_dic:
					random_mac_addr = "{}_bonding_addr".format(mac_addr)
				else:
					random_mac_addr = "()_bonding_addr2".format(mac_addr)
				nic_dic[random_mac_addr] = {
					"name": nic_name,
					"netmask": netmask,
					"network": network,
					"bonding": 1,
					"model": "unknown",
					"ipaddress": ip_addr,
				}
		if "HWaddr" in line:
			next_ip_line = True
			last_mac_addr = line
	return {"nic": nic_dic.values()}


def raminfo():
	raw_data = subprocess.check_output("sudo dmidecode -t 17")
	raw_list = str(raw_data, "utf8").split("\n")
	raw_ram_list = []
	item_list = []
	for line in raw_list:
		if line.startswith("Memory Device"):
			raw_ram_list.append(item_list)
			item_list = []
		else:
			item_list.append(line.strip())
	ram_list = []
	for item in raw_ram_list:
		item_ram_size = 0
		ram_item_to_dic = {}
		for i in item:
			data = i.split(":")
			if len(data) == 2:
				key, val = data
				if key == "Size":
					if val.strip() != "No Module Installed":
						ram_item_to_dic["capacity"] = val.split()[0].strip()  # e.g split "1024 MB"
						item_ram_size = int(val.split()[0])
					else:
						ram_item_to_dic["capacity"] = 0
					if key == "Type":
						ram_item_to_dic["model"] = val.strip()
					if key == "Manufacturer":
						ram_item_to_dic["manufactory"] = val.strip()
					if key == "Serial Number":
						ram_item_to_dic["sn"] = val.strip()
					if key == "Locator":
						ram_item_to_dic["slot"] = val.strip()
		if item_ram_size == 0:  # empty slot
			pass
		else:
			ram_list.append(ram_item_to_dic)

	# 同样还要获取总的RAM
	raw_total_size = subprocess.check_output("cat /proc/meminfo|grep MemTotal", shell=True)
	raw_total_size = str(raw_total_size, "utf8").split(":")  # 将执行结果转换成str格式
	ram_data = {"ram": ram_list}
	if len(raw_total_size) == 2:  # 正确的时候
		total_mb_size = int(raw_total_size[1].split()[0]) / 1024
		ram_data["ram_size"] = total_mb_size

	return ram_data


def osinfo():
	"""
	可选命令： 'cat /proc/version' (gcc ....(发行版本))
	:return:
	"""
	distributor = subprocess.check_output("lsb_release -a|grep 'Distributor ID'")
	distributor = str(distributor, "utf8").split(":")
	release = subprocess.check_output("lsb_release -a |grep Description")
	release = str(release, "utf8").split(":")
	data_dic = {
		"os_distribution": distributor[1].strip() if len(distributor) > 1 else None,
		"os_release": release[1].strip() if len(release) > 1 else None,
		"os_type": "Linux",
	}
	return data_dic


def cpuinfo():
	base_cmd = "cat /proc/cpuinfo"
	raw_data = {
		"cpu_model": "{} |grep 'model name'|head -1".format(base_cmd),
		"cpu_count": "{} |grep 'procesor' |wc -l".format(base_cmd),
		"cpu_core_count": "{} |grep 'cpu cores' |awk -F: '{SUM +=$2} END {print SUM}'".format(base_cmd)
	}
	for key, cmd in raw_data.items():
		try:
			cmd_res = subprocess.check_output(cmd, shell=True)
			cmd_res = str(cmd_res, "utf8").strip()
			raw_data[key] = cmd_res
		except ValueError as e:
			print(str(e, "utf8"))
		except Exception as e:
			print(str(e, "utf8"))

	data = {
		"cpu_count": raw_data["cpu_count"],
		"cpu_core_count": raw_data["cpu_core_count"]
	}
	cpu_model = raw_data["cpu_model"].split(":")
	if len(cpu_model) > 1:
		data["cpu_model"] = cpu_model[1].strip()
	else:
		data["cpu_model"] = -1
	return data


class DiskPlugin(object):

	def linux(self):
		result = {"physical_disk_driver": []}

		try:
			script_path = os.path.dirname(os.path.abspath(__file__))
			shell_command = "sudo {}/MegaCli -PDList -aALL".format(script_path)
			output = subprocess.check_output(shell_command)
			output = str(output, "utf8").strip()
			result["physical_disk_driver"] = self.parse(output[1])
		except Exception as e:
			result["error"] = e
		return result

	def parse(self, content):
		"""
		解析shell 命令返回的结果
		:param content: shell 命令结果
		:return: 解析后的结果
		"""
		response = []
		result = []
		for row_line in content.split("\n\n\n\n"):
			result.append(row_line)
		for item in result:
			tmp_dict = {}
			for row in item.split("\n"):
				if not row.strip():
					continue
				key, val = row.split(":")
				name = self.mega_patter_match(key)
				if name:
					if key == "Raw Size":
						raw_size = re.search("(\d+\.\d+)", val.strip())
						if raw_size:
							tmp_dict[name] = raw_size.group()
						else:
							raw_size = "0"
					else:
						tmp_dict[name] = val.strip()
			if tmp_dict:
				response.append(tmp_dict)
		return response

	def mega_patter_match(self, needle):
		grep_pattern = {
			"Slot": "slot",
			"Raw Size": "capacity",
			"Inquiry": "model",
			"PD Type": "iface_type"
		}
		for key, val in grep_pattern.items():
			if needle.startswith(key):
				return val
		return False

if __name__ == "__main__":
	print(DiskPlugin().linux())
