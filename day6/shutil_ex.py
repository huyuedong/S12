#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
高级的 文件、文件夹、压缩包 处理模块
"""

import shutil
import os

# 将文件内容(文件对象)拷贝到另一个文件中，可以指定部分拷贝
# with open("D:\qimi_WorkSpace\S12\day6\\test1.txt", "rt") as f1, open("D:\qimi_WorkSpace\S12\day6\\test2.txt", "at")as f2:
# 	shutil.copyfileobj(fsrc=f1, fdst=f2)

# 拷贝文件
# shutil.copyfile(src="D:\qimi_WorkSpace\S12\day6\\test1.txt",dst="D:\qimi_WorkSpace\S12\day6\\test2.txt")

# 仅拷贝权限。内容、组、用户均不变
# print(os.stat("D:\qimi_WorkSpace\S12\day6\\test2.txt"))
# shutil.copymode(src="D:\qimi_WorkSpace\S12\day6\\test1.txt", dst="D:\qimi_WorkSpace\S12\day6\\test2.txt")
# print(os.stat("D:\qimi_WorkSpace\S12\day6\\test2.txt"))


# # 拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copystat(src=,dst=)
#
# # 拷贝文件和权限
# shutil.copy(src, dst)

# 拷贝文件和状态信息
# shutil.copy2(src,dst)

# 递归的去拷贝文件
# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)

# 递归的去删除文件
# shutil.rmtree(path[, ignore_errors[, onerror]])

# 递归的去移动文件
# shutil.move(src, dst)

# 创建压缩包并返回文件路径，例如：zip、tar
# shutil.make_archive(base_name, format,...)

#
# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
# 如：www                        =>保存至当前路径
# 如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
# format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir：	要压缩的文件夹路径（默认当前目录）
# owner：	用户，默认当前用户
# group：	组，默认当前组
# logger：	用于记录日志，通常是logging.Logger对象

# 将D:\qimi_WorkSpace\S12\day6目录下的文件打包成test.tar.gz，放置在当前目录
# et = shutil.make_archive("test", 'gztar', root_dir='D:\\qimi_WorkSpace\\S12\\day6')

# shutil模块对压缩包的处理是调用ZipFile和TarFile两个模块来进行的

# zipfile模块
# import zipfile
#
# # 压缩
# z = zipfile.ZipFile('test.zip', 'w')
# z.write('a.log')
# z.write('a.data')
# z.close()
#
# # 解压
# z = zipfile.ZipFile('test.zip', 'r')
# z.extractall()
# z.close()

# tarfile模块
# import tarfile
#
# # 压缩
# tar = tarfile.open('test.tar','w')
# tar.add('D:\\qimi_WorkSpace\\S12\\day6\\test1.tar', arcname='test1.tar')
# tar.add('D:\\qimi_WorkSpace\\S12\\day6\\test2.tar', arcname='test2.tar')
# tar.close()
#
# # 解压
# tar = tarfile.open('test.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()
