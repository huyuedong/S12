#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


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

# update_list = []
# delete_list = []

set_old = set(old_dict.keys())
set_new = set(new_dict.keys())
update_list = list(set_old.intersection(set_new))
delete_list = list(set_old.difference(set_new))
add_list = list(set_new.difference(set_old))

s_tmp = 'update_list:{0}\ndelete_list:{1}\nadd_list:{2}'
print(s_tmp.format(update_list, delete_list, add_list))

print(list(old_dict.values())[0])
