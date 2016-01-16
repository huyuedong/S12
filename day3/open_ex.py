#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
open()文件操作
"""

f = open('open_ex_test.txt', 'r', encoding='utf-8')
print(f.tell())
# 按照字符读
f.read(2)
# tell()返回的是根据字节得到的位置
print(f.tell())
# seek()指定当前指针位置，seek()用的是字节
# 由于有中文，所以把指针指向1，就会报错，因为一个中文包括三个字节
# f.seek(1)
# print(f.read())

# truncate():把当前指针位置之前的数据保留下来，舍去后面的（需用a+模式）
f.close()
