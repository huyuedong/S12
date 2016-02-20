#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
xml模块的练习
"""

import xml.etree.ElementTree as ET

# 解析xml文件
tree = ET.parse("test.xml")
# 获取根
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
	print(child.tag, child.attrib)
	for i in child:
		print(i.tag, i.text)

# 只遍历year节点
for i in root.iter("year"):
	print(i.tag, i.text)


# 修改和删除xml文件
tree = ET.parse("test2.xml")
root = tree.getroot()

# 修改