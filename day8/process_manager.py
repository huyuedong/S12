#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
Manager：
进程间去改一个Manager的数据
改同一个字典，同一个列表
Manager是进程安全的。
"""

from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = n
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)
