#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
float的内建方法
"""

# 返回分子分母数构成的元祖
f1 = 10.0
f2 = 0.0
f3 = -0.25

print(f1.as_integer_ratio())
print(f2.as_integer_ratio())
print(f3.as_integer_ratio())
print(f3.as_integer_ratio())

# 返回共轭复数 conjugate(self, *args, ***kwargs)

# 将十六进制数转换为浮点数
print(float.fromhex('0x1.ffffp10'))

# 将浮点数转换为十六进制数
print(2047.984375.hex())

# 判断浮点数是不是整数
f1 = 10.2
f2 = 10.0
print(f1.is_integer())
print(f2.is_integer())


