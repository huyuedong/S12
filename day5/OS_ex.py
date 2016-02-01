#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import os

# os模块，提供对操作系统进行调用的接口
# 获取当前的工作目录
print(os.getcwd())

# 改变当前脚本的工作目录
os.chdir("D:\qimi_WorkSpace\S12\day5")

# 返回当前目录的字符串名
print(os.curdir)    # 输出=>.

# 返回当前目录的父目录字符串名
print(os.pardir)    # 输出=>..

# 生成多层目录
# os.makedirs("D:\qimi_WorkSpace\S12\day5\dirname1\dirname2")

# 生成单层目录
# os.mkdir("D:\qimi_WorkSpace\S12\day5\dirname1")

# 删除目录，如果目录为空则递归删除上一级目录
# os.removedirs("D:\qimi_WorkSpace\S12\day5\dirname1\dirname2")

# 删除单层空目录，目录为空无法删除。
# os.rmdir("D:\qimi_WorkSpace\S12\day5\dirname1")

# 列出指定目录下的所有文件盒子目录，包含隐藏文件，并以列表形式打印
os.listdir("D:\qimi_WorkSpace\S12\day5")

# 删除一个文件
# os.remove("文件路径")

# 重命名文件/目录
# os.rename("ordname", "newname")

# 获取文件/目录信息
# os.stat("path/filename")

# 输出当前操作系统下的路径分隔符
print(os.sep)   # 输出=>'\\'

# 输出当前操作系统下的行中止符
print(os.linesep)   # 输出=>'\t\n'

# 输出当前系统下用于分割文件路径的字符串
print(os.pathsep)   # 输出';'

# 输出当前平台
print(os.name)

# 运行shell命令
os.system("dir")

# 获取系统环境变量
print(os.environ)

# 返回path规范化的绝对路径
os.path.abspath("D:\qimi_WorkSpace\S12\day5")

# 将path分割成目录和文件名二元组返回(仅以后面跟不跟\为依据)
os.path.split("D:\qimi_WorkSpace\S12\day5")    # 输出=>("D:\qimi_WorkSpace\S12", "day5")

# 返回path的目录
os.path.dirname("D:\qimi_WorkSpace\S12\day5")   # 输出=>"D:\qimi_WorkSpace\S12"

# 返回path的文件名
os.path.basename("D:\qimi_WorkSpace\S12\day5")  # 输出=>"day5"

# 判断路径是否存在
os.path.exists("D:\qimi_WorkSpace\S12\day5")    # 输出=>True

# 判断path是不是绝对路径
os.path.abspath("D:\qimi_WorkSpace\S12\day5")   # 输出=>True

# 判断path是不是一个存在的文件
os.path.isfile("D:\qimi_WorkSpace\S12\day5")    # 输出=>False

# 判断path是不是一个存在的目录
os.path.isdir("D:\qimi_WorkSpace\S12\day5")    # 输出=>True

# 将多个路径组合后返回,第一个绝对路径之前的参数被忽略
os.path.join("D:\qimi_WorkSpace\S12\day5", "day5_1")  # 输出=>"D:\qimi_WorkSpace\S12\day5\day5_1"
os.path.join("day5_01", "D:\qimi_WorkSpace\S12\day5", "day5_1")    # 输出=>"D:\qimi_WorkSpace\S12\day5\day5_1"

# 返回path指向的文件或者目录的最后存取时间
os.path.getatime("D:\qimi_WorkSpace\S12\day5\day5_1")   # 输出=>1454321491.5017765

# 返回path指向的文件或者目录的最后修改时间
os.path.getmtime("D:\qimi_WorkSpace\S12\day5\day5_1")   # 输出=>1454321491.5017765

# 返回path指向的文件或者目录的创建时间
os.path.getctime("D:\qimi_WorkSpace\S12\day5")    # 输出=>1454164372.8629067

# 返回path指向的文件或者目录的大小
os.path.getsize("D:\qimi_WorkSpace\S12\day5")    # 输出=>4096
