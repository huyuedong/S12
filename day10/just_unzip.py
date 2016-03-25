#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
下载的每次课的视频文件都是手动解压缩，然后再拷贝到以上课时间为名的文件夹下，特烦人。
所以写一个解压缩的脚本。
下载的文件基本都是7z格式，由于压缩文件名格式不统一，只能先把所有的7z文件都压缩然后再分类到不同的目录。
	-先解压缩
	-把解压后的文件拷贝到以上课时间为名的文件夹下。
"""

import os
import re
import shutil

# 压缩密码
password_11 = "ayBo(76twspUS*zy(ouzB&zy08yS98ax8U"  # 11期密码
password_12 = "&&&SQbtXB1316IPMg%BZHYZnYBB5w7912"  # 12期密码


# 找到top_path目录下所有的7z文件，并解压到指定目录。
def get_zip_file(top_path, dst_path):
	global password_11
	global password_12
	for i in os.walk(top_path):
		for j in i[2]:  # 遍历文件
			if j.endswith(".7z"):
				full_path = os.path.join(i[0], j)  # 拼接文件名
				file_path = os.path.normpath(os.path.abspath(full_path))  # 返回.7z文件的路径
				dst_tmp = "{}\\tmp000".format(dst_path)  # 存放解压文件的临时目录
				# 7z命令单引号里面用双引号，路径名必须要用双引号。
				unzip_cmd = '7z x {} -p{} -y -aos -o{}'.format(file_path, password_11, dst_tmp)  # 解压命令
				os.system(unzip_cmd)  # 解压
	return True


# 按照学期和上课时间归类解压好的.pbb文件==>dst_path\s1*\day**\**.pbb
def sort_file():
	"""
	shutil移动文件
	遍历文件，匹配到学期和时间，然后判断dst_path下有没有文件夹，没有就新建一个，然后再移动文件到相应目录下。
	"""
	global dst_tmp
	for i in os.walk(dst_tmp):
		for j in i[2]:
			pass
			# shutil.move()


# file_list = get_zip_file("E:\\学习资料\\11期视频")
# p_session = re.compile(r's\d\d')  # 匹配学期
# p_datetime = re.compile(r'day\d+')  # 匹配第几天


# unzip_cmd = '7z x "E:\\test\\上.7z" -p"ayBo(76twspUS*zy(ouzB&zy08yS98ax8U" -y -aos -o"E:\\temp"'  # 解压命令
"""
x:完整路径下解压文件

-y:所有确认选项都默认为是（即不出现确认提示）

-p:设置密码

-aos:跳过已存在的文件

-o:设置输出目录
"""


if __name__ == "__main__":
	pass