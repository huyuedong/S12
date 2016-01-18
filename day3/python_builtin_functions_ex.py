#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
Python的内建方法
"""

# abs(x):返回x的绝对值
# all(iterable):所有元素为真，则返回真
result = all([1, ''])
print(result)
result = all([1, 'a'])
print(result)
# any(iterable):有一个元素为真，则返回真
result = any(('', [], ))
print(result)
result = any(('', [], 1))
print(result)
# ascii(object):返回一个可打印对象的字符串，忽略没有编码表示的字符串返回调用转义字符的repr()。
# As repr(), return a string containing a printable representation of an object,
# but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
# This generates a string similar to that returned by repr() in Python 2.

# bin(x): 返回x的二进制数
result = bin(10)
print(result)
# bool(x):返回布尔值
# bytearray([source[, encoding[, errors]]]):返回字节数组
# Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and Bytearray Operations.

# The optional source parameter can be used to initialize the array in a few different ways:
#
# If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().
# If it is an integer, the array will have that size and will be initialized with null bytes.
# If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
# If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.
# Without an argument, an array of size 0 is created.

result = bytearray('周杰伦', encoding='utf-8')
print(result)
# bytes():返回字节
#
result = bytes('周杰伦', encoding='utf-8')
print(result)
# callable():是否可调用
# chr(i):返回Unicode码i代表的字符串 与ord()相反
print(chr(95))
# ord():返回字符串对应的Unicode码
print(ord('_'))
# classmethod(function):返回类方法
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):编译
# complex([real[, imag]]：复数
# delattr(object, name):删除属性
# -This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.
# dict()：创建字典
# dir([object]):返回列表
# -Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
# divmod(a, b):返回一个元祖(a//b, a%b)
# enumerate(iterable, start=0):枚举
# eval(expression, globals=None, locals=None):执行字符串类型的表达式，并返回结果
result = eval('99+1')
print(result)
# exec(object[, globals[, locals]]):执行存储在字符串或文件中的Python语句
result = exec("print(eval('99+1'))")
print(result)
# filter(function, iterable)：筛选,用前面的function去筛选后面的，留下符合条件的。
l1 = [11, 66, 33, 77, 22, 88, 44, 99]
result = filter(lambda x: x > 50, l1)
print(list(result))
# float([x]):返回一个浮点数
print(float('+1.23'))
print(float('     -123456\n'))
print(float('1e-003'))
print(float('+1E6'))
print(float('-Infinity'))
# format(value[, format_spec])：字符串的格式化
# -format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# -fill        ::=  <any character>
# -align       ::=  "<" | ">" | "=" | "^"
# -sign        ::=  "+" | "-" | " "
# -width       ::=  integer
# -precision   ::=  integer
# -type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# frozenset([iterable]):冻结集合
# getattr(object, name[, default])
# globals()
# hasattr(object, name)
# hash(object):返回哈希值
# help([object]):获取帮助信息
# hex(x)：十六进制数
# id(object)：返回ID
# input([prompt])：获取输入
# int()：返回整数
print(int('1010', 2))
print(int('1010', 8))
print(int('1010', 10))
print(int('1010', 16))
# isinstance(object, classinfo)：返回是不是类实例
# issubclass(class, classinfo)：返回是不是父类
# iter(object[, sentinel])：返回一个迭代器
# len(s)：返回对象的长度
# list([iterable])：生成列表
# locals()：更新并返回一个本地符号表的字典
# map(function, iterable, ...)：将函数作用于迭代器每个对象的结果返回一个迭代器
# max(iterable, *[,key, default])：返回最大值
d1 = {'a': 10, 'c': 5, 'f': 3, 'b': 7}
print(max(d1.items(), key=lambda t: t[1]))
# -max(arg1, arg2, *args[,key])
# memoryview(obj)：返回一个给定参数的内存视图
# min(iterable, *[,key, default])：返回最小值
# -min(arg1, arg2, *args[,key])
# next(iterator[, default])
# object()
# oct(x):八进制数
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# ord()
# pow(x, y[, z])：x的y次幂再对z求余数
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)：打印
# property()
# range(stop)
# -range(start, stop[, step])
# repr(object)
# reversed(seq)：反转
# round(number[, ndigits])：返回浮点数的四舍五入值。round(0.5)->0而round(1.5)->2
# set([iterable])：集合
# setattr(objEct，name, value)：对应于getattr()
# slice(stop)：切片
# -slice(start, stop[,step])：切片
# sorted(iterable[,key][,reverse])：排序
# staticmethod(function)
# str(object='')
# -str(object=b'', encoding='utf-8', errors='strict')
# sum(iterable[, start])：求和
# super([type[, object-or-type]])
# tuple([iterable])：元祖
# type(object)：返回对象的类型
# -type(name, bases, dict)：返回一个新类型的对象
# vars([object])：返回对象属性和属性值的字典
# zip(*iterables)：返回一个元素来自每一个迭代器的迭代器
# __import__()：被import声明调用的一个方法
