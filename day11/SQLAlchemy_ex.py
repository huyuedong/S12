#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

# 定义一个user表
user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

# 定义一个color表
color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
# 建立连接
engine = create_engine("mysql+pymysql://root:rootroot@localhost:3306/test", max_overflow=5)

# 创建所有的表
metadata.create_all(engine)
