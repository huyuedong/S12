#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
集合介绍
"""
# 示例
old_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 80},
    "#2": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 80},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 80},
}
new_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 800},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 80},
    "#4": {'hostname': 'c2', 'cpu_count': 2, 'mem_capacity': 80},
}

# 旧字典没有新字典有的就是需要删除的数据
# 旧字典有新字典没有的就是需要增加的数据
# 旧字典和新字典都有的就是（可能）需要更新的数据

# 该示例主要是字典的第一层key为例：
# 将旧字典的第一层key转换成集合
set_old = set(old_dict.keys())
# 将新字典的第一层key转换成集合
set_new = set(new_dict.keys())
# 需要更新的数据就是取新、旧集合的交集
update_list = list(set_old.intersection(set_new))
# 需要删除的数据就是取旧集合与新集合的不同
delete_list = list(set_old.difference(set_new))
# 需要增加的数据就是取新集合与旧集合的不同
add_list = list(set_new.difference(set_old))

s_tmp = 'update_list:{0}\ndelete_list:{1}\nadd_list:{2}'
print(s_tmp.format(update_list, delete_list, add_list))
