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
import glob

sep = os.path.sep  # 目录分隔符
print(sep)


def get_zip(arg):
	for i in os.walk(arg):
		for j in i[2]:
			if j.endswith(".7z"):
				print(os.path.join(i[0], j))

get_zip("E:\\学习资料\\11期视频")

unzip_cmd = '7z x "E:\\test\\上.7z" -p"ayBo(76twspUS*zy(ouzB&zy08yS98ax8U" -y -aos -o"E:\\temp"'  # 解压命令
"""
x:完整路径下解压文件

-y:所有确认选项都默认为是（即不出现确认提示）

-p:设置密码

-aos:跳过已存在的文件

-o:设置输出目录
"""
os.system(unzip_cmd)


