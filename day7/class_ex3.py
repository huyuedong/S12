#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
类的特殊成员
"""


class A(object):
	"""
	这是一个测试的类。。。
	"""
	pass

# __doc__ 表示类的描述信息
print(A.__doc__)

# __module__ 表示当前操作的对象在那个模块
a = A()
print(A.__module__)    # __main__
print(a.__module__)    # __main__

# __class__ 表示当前操作的对象的类是什么
print(a.__class__)  # <class '__main__.A'>

# __init__ 构造方法，通过类创建对象时，自动触发执行

# __del__ 析构方法，当对象在内存中被释放时，自动触发执行。？用于关闭构造方法中打开的文件或数据库？

# __call__ 实例对象后面加括号直接执行
# 构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()


