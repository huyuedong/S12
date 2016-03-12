#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
queue的练习，
普通队列
后进先出队列
优先级队列
"""

import queue


# 普通队列
q1 = queue.Queue(3)
q1.put(1)
q1.put(2)
q1.put(3, timeout=3)

print(q1.empty())
print(q1.full())

print(q1.get())
print(q1.get(3))
print("=" * 50)

# 后进先出队列
q2 = queue.LifoQueue()

q2.put(3)
q2.put(4)
print(q2.get())
print("=" * 50)


# 优先级队列
q3 = queue.PriorityQueue(2)

q3.put((1, 2))
q3.put((10, "a"))
q3.put((5, [100, 99, 98]), timeout=3)   # 3秒后报错Full

print(q3.get())
print(q3.get())
