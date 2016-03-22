#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
redis练习
"""

import redis

r = redis.Redis()
print(r.keys())
r.set("name", "alex")

print(r.get("name").decode())

# setbit修改的是ASCII码对应的二进制的指定下标的值
r.set("ID", 3)
print(r.get("ID"))
print("ASCII=>{}".format(ord(r.get("ID").decode())))    # 获得ID值对应的ASCII码
print("ASCII码的二进制=>{}".format(bin(ord(r.get("ID").decode()))))    # 获得ID值对应的ASCII码的二进制值
print("=" * 50)
print("初始ID=>{}".format(r.get("ID").decode()))
# 修改3对应的ASCII码对应的二进制值的下标1的值为1
r.setbit("ID", 1, 1)
print("ASCII码的二进制=>{}".format(bin(ord(r.get("ID").decode()))))   # 打印修改后的ID值对应的ASCII码的二进制值
print("ASCII=>{}".format(ord(r.get("ID").decode())))   # 打印ID值对应的ASCII码
print("=" * 50)
print("修改后的ID=>{}".format(r.get("ID").decode()))


# setbit的应用==>：UV_count 独立访问用户,
print(r.bitcount("UV_count"))
r.setbit("UV_count", 3, 1)
r.setbit("UV_count", 7, 1)
r.setbit("UV_count", 100, 1)
r.setbit("UV_count", 10000, 1)
print(r.bitcount("UV_count"))   # 按位计算，比按字节计算节省了非常多的空间

# 使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
# 默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。

pool = redis.ConnectionPool()
r2 = redis.Redis(connection_pool=pool)
r2.set("age", 18)
print(r2.get("age"))

# 操作
# String操作，redis中的String在在内存中按照一个name对应一个value来存储。
# set(name, value, ex=None, px=None, nx=False, xx=False)
# ex:过期时间（秒）；px:过期时间（毫秒）；nx:设为True，则name不存在才执行set，xx:设为True，则name存在才执行set
