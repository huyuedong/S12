#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
外键关联
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test01", max_overflow=5, echo=True)
Base = declarative_base()


# 创建一个中间表，关联其他两个表
host2group = Table("host_2_group", Base.metadata,
                   Column("host_id", ForeignKey("host.id"), primary_key=True),  # 双主键
                   Column("group_id", ForeignKey("group.id"), primary_key=True),  # 双主键
                   )


class Host(Base):
	__tablename__ = "host"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)
	# group_id = Column(Integer, ForeignKey("group_id"))
	groups = relationship("Group", secondary=host2group, backref="host_list")

	def __init__(self, hostname, ip_addr, port=22):
		self.hostname = hostname
		self.ip_addr = ip_addr
		self.port = port


class Group(Base):
	__tablename__ = "group"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)

	def __init__(self, name):
		self.name = name

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 添加group记录
# g1 = Group(name="g1")
# g2 = Group(name="g2")
# g3 = Group(name="g3")
# g4 = Group(name="g4")
#
# session.add_all([g1, g2, g3, g4])
# session.commit()


# 添加主机记录
# h1 = Host(hostname="localhost", ip_addr="127.0.0.1")
# h2 = Host(hostname="Ubuntu", ip_addr="192.168.0.1", port=10000)
# h3 = Host(hostname="CentOS", ip_addr="192.168.10.1",)
h4 = Host(hostname="CentOS3", ip_addr="192.168.10.13", port=11)
h4.groups.append(Group("g1"))

# session.add_all([h1, h2, h3])
session.add(h4)
session.commit()
