#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
初始化数据库表结构
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, UniqueConstraint, DateTime
from sqlalchemy.orm import sessionmaker, relationship, query
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test01", max_overflow=5, echo=False)
Base = declarative_base()


# 主机表
class Host(Base):
	__tablename__ = "host"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)

	def __repr__(self):
		return "<id={}, hostname={}, ip_addr={}, port={}>".format(self.id, self.hostname, self.ip_addr, self.port)


# 主机组表
class HostGroup(Base):
	__tablename__ = "group"
	id = Column(Integer,primary_key=True)
	name = Column(String(64),unique=True,nullable=False)

	def __repr__(self):
		return "<id={},name={}>".format(self.id, self.name)


# 堡垒机用户信息表
class UserProfile(Base):
	__tablename__ = "User"
	id = Column(Integer, primary_key=True)
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	host_list = relationship('HostUser', secondary=UserProfile2HostUser, backref='userprofiles')
	groups = relationship('Group', secondary=UserProfile2Group, backref='userprofiles')

	def __repr__(self):
		return "<id={},name={}>".format(self.id, self.username)


# 主机&用户表
class HoserUser(Base):
	__tablename__ = "HostUser"
	id = Column(Integer, primary_key=True)
	host_id = Column(Integer, ForeignKey("host.id"))
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	# host_id和username联合唯一
	__table_args__ = UniqueConstraint("host_id", "username", name="Host_User")


# log表
class AuditLog(Base):
	__tablename__ = "AuditLog"
	id = Column(Integer, primary_key=True)
	userprofile_id = Column(Integer, ForeignKey('user_profile.id'))
	hostuser_id = Column(Integer, ForeignKey('host_user.id'))
