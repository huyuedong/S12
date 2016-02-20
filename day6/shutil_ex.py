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
print(os.stat("D:\qimi_WorkSpace\S12\day6\\test2.txt"))
shutil.copymode(src="D:\qimi_WorkSpace\S12\day6\\test1.txt", dst="D:\qimi_WorkSpace\S12\day6\\test2.txt")
print(os.stat("D:\qimi_WorkSpace\S12\day6\\test2.txt"))


# # 拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copystat(src=,dst=)
#
# # 拷贝文件和权限
# shutil.copy()

#
