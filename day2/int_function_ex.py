#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
"""
int类的几个内建方法
"""

# 返回商和余数的元祖
all_pages = 95
per_page = 10
pages = all_pages.__divmod__(per_page)
print(pages)

# __ceil__ ？？
num = 19
print(num.__ceil__())

# 绝对值
num1 = -19
print(abs(num1))
print(num1.__abs__())

# 相加
num2 = 5
print(num1+num2)
print(num2.__add__(num1))

# 布尔值，非零返回真,
num3 = 0
print(num2.__bool__())
print(num3.__bool__())

# 判断是是否相等
print(num3.__eq__(num2))

# 返回浮点
print(num2.__float__())

# 地板除 19//5
print(num.__floordiv__(num2))

# 大于等于
print(num.__ge__(num2))

# 大于
print(num.__gt__(num2))

# 哈希
print(num.__hash__())

# __index__ :索引 用于切片，数字无意义
# x[y: z] <==> x[y.__index__(): z.__index__()]

# __init__ :构造方法

# 转换为整数
# x.__int__() <==> int(x)

# __invert__ :取反 x.__invert__() <==> ~x
print(num.__invert__())

# 小于等于
print(num.__le__(num2))

# 小于
print(num.__lt__(num2))

# __lshift__ :左移位
int_temp1 = 1
int_temp2 = 4
print(int_temp1.__lshift__(int_temp2))

# 求模 x.__mod__(y) <==> x%y
print(num.__mod__(num2))

# 相乘 x.__mul__(y) <==> x*y
print(num.__mul__(num2))

# 取反
print(num.__neg__())

# 不等于
print(num.__ne__(num2))

# 取正数 ？？？
print(num1.__pos__())

# 乘方
print(num.__pow__(2))

# 右加（以下前缀为r的都是右；前缀为l的都是左）
print(num.__radd__(num1))

# 右或
print(int_temp1.__rand__(int_temp2))

# 右除以左，返回商和余数
print(per_page.__rdivmod__(all_pages))

# 转换为解释器可读取的形式
print(num.__repr__())

# 转换为字符串
print(num.__str__())
print(type(num.__str__()))

# 求差 x.__sub__(y) <==> x-y
print(num.__sub__(num2))

# x.__truediv__(y) <==> x/y
print(num.__truediv__(num2))

# 异或 ：按位不一样的为真，一样的为假。x.__xor__(y) <==> x^y

# 返回->表示该数字时占用的最少位数
print(bin(37))
print((37).bit_length())

# 返回->共轭数
int_temp1 = 37
print(int_temp1.conjugate())

'''这俩方法暂时没搞懂。。。
def from_bytes(cls, bytes, byteorder, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    int.from_bytes(bytes, byteorder, *, signed=False) -> int

    Return the integer represented by the given array of bytes.

    The bytes argument must be a bytes-like object (e.g. bytes or bytearray).

    The byteorder argument determines the byte order used to represent the
    integer.  If byteorder is 'big', the most significant byte is at the
    beginning of the byte array.  If byteorder is 'little', the most
    significant byte is at the end of the byte array.  To request the native
    byte order of the host system, use `sys.byteorder' as the byte order value.

    The signed keyword-only argument indicates whether two's complement is
    used to represent the integer.
    """
    pass

def to_bytes(self, length, byteorder, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    int.to_bytes(length, byteorder, *, signed=False) -> bytes

    Return an array of bytes representing an integer.

    The integer is represented using length bytes.  An OverflowError is
    raised if the integer is not representable with the given number of
    bytes.

    The byteorder argument determines the byte order used to represent the
    integer.  If byteorder is 'big', the most significant byte is at the
    beginning of the byte array.  If byteorder is 'little', the most
    significant byte is at the end of the byte array.  To request the native
    byte order of the host system, use `sys.byteorder' as the byte order value.

    The signed keyword-only argument determines whether two's complement is
    used to represent the integer.  If signed is False and a negative integer
    is given, an OverflowError is raised.
    """
    pass
'''

