#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
dict类的内建方法
"""
# 增加 ：append object to end
l1 = list([1, 2, 3, ])
l1.append(4)
print(l1)
l1.append([5, 6, 7,])
print(l1)

# 清空
print(l1.clear())

# 复制
l1 = [1, 2, 3, ]
print(l1.copy())

# 计数
l1 = [1, 1, 2, 1, 3, 2]
print(l1.count(1))

# 扩展 ： extend(self, iterable)
l1 = [1, 2, 3, ]
l1.extend((5, 6, ))
print(l1)
l1.extend('abc')
print(l1)

# 索引
print(l1.index(3))

# 插入：index(self, value, start=None, stop=None)
l1.insert(5, 0)
print(l1)

# 弹出 : pop(self, index=None)
print(l1.pop())
print(l1.pop(5))    # 返回l1[5]

# 移除 ：remove(self, value)
l1 = [1, 2, 3, 4, 5, 6, 'a']
l1.remove(6)
print(l1)
print(l1.remove('a'))   # 返回None
print(l1)

print('line:51'.center(20, '='))

# 反转
l1 = [1, 2, 3, 4, 5, ]
l1.reverse()
print(l1)

# 排序 ：sort(self, key=None, reverse=False)
l1 = ['123', 'xyz', '789', 'uvw', '哈哈']
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
