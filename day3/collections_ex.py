#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
collections里常见的几个类
"""

# Counter 计数器
from collections import Counter
c = Counter('afaafsdqadsa')
print(c)


# OrdereDict 有序字典:记住了字典元素添加的顺序
from collections import OrderedDict
dic_tmp = OrderedDict()
dic_tmp['k1'] = 'v1'
dic_tmp['k2'] = 'v2'
dic_tmp['k3'] = 'v3'
print(dic_tmp)
print(type(dic_tmp))


# defaultdict 默认字典:默认给字典的值设置一个类型
from collections import defaultdict
dic_tmp = defaultdict(list)
dic_tmp['k1'] = 'v1'
dic_tmp['k2'] = 'v2'
dic_tmp['k3'] = 'v3'
print(dic_tmp)
print(type(dic_tmp))


# namedtuple 可命名元祖
from collections import namedtuple
# 例如用于定义x,y,x轴等
MyNamedtupleClass = namedtuple('MyNamedtupleClass', ['x', 'y', 'z'])
namedtuple_tmp = MyNamedtupleClass(11, 22, 33)
print(namedtuple_tmp.x)
print(namedtuple_tmp.y)
print(namedtuple_tmp.z)


# deque 一个线程安全的双向队列:左右皆可进出
from collections import deque
deque_tmp = deque()
deque_tmp.append((11, 22, 33))
print(deque_tmp)
deque_tmp.pop()


# queue.Queue 单向队列:先进先出
from queue import Queue
queue_tmp = Queue()
queue_tmp.put(11, 22, 33)
print(queue_tmp)
queue_tmp.get(11)

