#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

l1 = list([1, 2, 3, ])
l1.append(4)
print(l1)

l1.extend((5, 6, ))
print(l1)

l1.insert(0, 0)
print(l1)

l1.reverse()
print(l1)

a = l1.pop()
print(a)
print(l1)
