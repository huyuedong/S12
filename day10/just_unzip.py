#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
下载的每次课的视频文件都是手动解压缩，然后再拷贝到以上课时间为名的文件夹下，特烦人。所以写了该解压缩的脚本。
该脚本先解压缩7z文件，然后在目标目录下根据视频文件分类存放，格式为==> <dst_path\\S1*视频\\day**\\**.pbb>
version:0.1
create:2016/3/27

1) 支持Windows环境
2）目前只支持.7z格式的压缩文件且需将7z程序加入环境变量
3）请在main函数下修改源目录及目标目录，并配置解压视频的密码
4）作者只进行了简单测试。如若使用该脚本，一切后果自负。
"""

import os
import re
import shutil


# 找到top_path目录下所有的7z文件，并解压到指定目录。
def get_zip_file(top_path, dst_path, password):
	dst_tmp = None
	for i in os.walk(top_path):
		for j in i[2]:  # 遍历文件
			if j.endswith(".7z"):
				full_path = os.path.join(i[0], j)  # 拼接文件名
				file_path = os.path.normpath(os.path.abspath(full_path))  # 返回.7z文件的路径
				dst_tmp = "{}{}__tmp".format(dst_path, os.sep)  # 存放解压文件的临时目录
				# 7z命令单引号里面用双引号，路径名必须要用双引号。
				unzip_cmd = '7z x "{}" -p"{}" -y -aos -o"{}"'.format(file_path, password, dst_tmp)  # 解压命令
				os.system(unzip_cmd)  # 解压
	return dst_tmp


# 按照学期和上课时间归类解压好的.pbb文件==>dst_path\s1*\day**\**.pbb
def sort_file(dst_path, unzip_files_path):
	"""
	shutil移动文件
	遍历文件，匹配到<s1*>和<day**>，然后判断dst_path下有没有文件夹，没有就新建一个，然后再移动文件到相应目录下。
	:param dst_path: 目标目录
	:param unzip_files_path: 解压文件的临时存放目录
	:return:
	"""
	p = re.compile(r'(s\d+).+(day[\d]+)')  # 贪婪匹配day**
	for i in os.walk(unzip_files_path):
		for j in i[2]:
			result = p.search(j)
			if result:  # 如果匹配到内容的话
				if len(list(result.groups())) == 2:
					session_name = "{}{}".format(list(result.groups())[0], "视频")  # 得到该视频是第几期的
					date_name = list(result.groups())[1]  # 得到该视频是第几天的
					the_file_path = "{}{}{}".format(i[0], os.sep, j)  # 要移动的文件路径
					to_file_path = "{}{}{}{}{}".format(dst_path, os.sep, session_name, os.sep, date_name)  # 目标路径
					if session_name in os.listdir(dst_path):  # 有这个学期的文件夹
						path_tmp = "{}{}{}".format(dst_path, os.sep, session_name)
						if date_name in os.listdir(path_tmp):  # 如果有这个第几天的文件夹
							shutil.move(the_file_path, to_file_path)  # 移动文件
						else:  # 不存在该第几天的文件夹，就新建一个
							os.mkdir(to_file_path)
							shutil.move(the_file_path, to_file_path)
					else:  # 如果既没有学期目录也没有day目录，就递归新建一个
						os.makedirs(to_file_path)
						shutil.move(the_file_path, to_file_path)
				else:
					print("Get too many matching results, can't go on.")
			else:
				print("Can't matching any.")
	else:
		# 删除生成的临时文件夹
		try:
			if os.listdir(unzip_files_path) != 0:  # 有时候视频文件会分包压缩，导致在临时文件夹下还有一层文件夹
				for i in os.listdir(unzip_files_path):
					tmp = os.path.join(unzip_files_path, i)
					os.removedirs(tmp)  # 递归删除目录
					print("OK!")
			else:
				os.removedirs(unzip_files_path)
				print("OK!")
		except OSError:
			print("Unsolved files in {}, Please check!".format(unzip_files_path))


def main():
	# 压缩密码
	password_11 = "ayBo(76twspUS*zy(ouzB&zy08yS98ax8U"  # 11期密码
	password_12 = "&&&SQbtXB1316IPMg%BZHYZnYBB5w7912"  # 12期密码
# =========================运行前请修改下面的配置=====================================

	top_path = "E:\\test"  # 此处填写所有压缩包的存放目录，双反斜杠！！！

	dst_path = "E:\\temp"  # 此处填写要将视频文件存放的目录，双反斜杠！！！

	password = password_11  # 此处修改解压的密码

# =========================运行前请修改上面的配置=====================================
	unzip_files_path = get_zip_file(top_path, dst_path, password)
	if unzip_files_path:
		print("Unzip OK")
		sort_file(dst_path, unzip_files_path)
	else:
		print("Error to unzip!")


# unzip_cmd = '7z x "E:\\test\\上.7z" -p"ayBo(76twspUS*zy(ouzB&zy08yS98ax8U" -y -aos -o"E:\\temp"'  # 解压命令
"""
x:完整路径下解压文件

-y:所有确认选项都默认为是（即不出现确认提示）

-p:设置密码

-aos:跳过已存在的文件

-o:设置输出目录
"""


if __name__ == "__main__":
	main()
