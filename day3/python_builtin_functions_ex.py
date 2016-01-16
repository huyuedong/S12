#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
Python的内建方法
"""

# abs():绝对值
# all():所有为真，则为真
result = all([1, ''])
print(result)
result = all([1, 'a'])
print(result)
# any():有一个为真，就为真
result = any(('', [], ))
print(result)
result = any(('', [], 1))
print(result)

# bin(): 返回二进制数
result = bin(10)
print(result)

# bool():返回布尔值

# bytearray():返回字节数组
result = bytearray('周杰伦', encoding='utf-8')
print(result)
# bytes():返回字节
result = bytes('周杰伦', encoding='utf-8')
print(result)
# callable():是否可调用
# chr():
print(chr(95))
# ord():
print(ord('_'))
# dir()返回列表
# vars()返回一个字典
