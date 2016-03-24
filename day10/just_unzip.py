#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
下载的每次课的视频文件都是手动解压缩，然后再拷贝到以上课时间为名的文件夹下，特烦人。
所以写一个解压缩的脚本。
下载的文件基本都是7z格式，
	-先解压缩
	-把解压后的文件拷贝到以上课时间为名的文件夹下。
"""

import os
import re
import shutil


def get_zip_file(top_path):
	zip_list = []
	for i in os.walk(top_path):
		for j in i[2]:  # 遍历文件
			if j.endswith(".7z"):
				full_path = os.path.join(i[0], j)
				zip_list.append(os.path.normpath(os.path.abspath(full_path)))
	return zip_list


def unzip_file(zip_list, dst_path):
	"""
	解压zip文件至指定的目录
	"""
	for file in zip_list:
		unzip_cmd = '7z x {} -p"ayBo(76twspUS*zy(ouzB&zy08yS98ax8U" -y -aos -o{}'.format(file, dst_path)
		os.system(unzip_cmd)





file_list = get_zip_file("E:\\学习资料\\11期视频")

p_session = re.compile(r's\d\d')  # 匹配学期
p_datetime = re.compile(r'day\d+')  # 匹配第几天


unzip_cmd = '7z x "E:\\test\\上.7z" -p"ayBo(76twspUS*zy(ouzB&zy08yS98ax8U" -y -aos -o"E:\\temp"'  # 解压命令
"""
x:完整路径下解压文件

-y:所有确认选项都默认为是（即不出现确认提示）

-p:设置密码

-aos:跳过已存在的文件

-o:设置输出目录
"""
os.system(unzip_cmd)

shutil.move()



