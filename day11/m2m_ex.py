#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
M2M练习
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, query
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test01", max_overflow=5, echo=False)
Base = declarative_base()

# 创建一个中间表，关联其他两个表
host2group = Table(
		"host_2_group", Base.metadata,
		Column("host_id", ForeignKey("host.id"), primary_key=True),
		Column("group_id", ForeignKey("group.id"), primary_key=True),
)


class Host(Base):
	__tablename__ = "hosts"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)
	groups = relationship("Group", secondary=host2group, backref="host_list")


class Group(Base):
	__tablename__ = "group"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
