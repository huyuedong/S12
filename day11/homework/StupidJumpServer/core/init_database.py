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
from sqlalchemy_utils import ChoiceType, PasswordType


engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test01", max_overflow=5, echo=False)
Base = declarative_base()  # 生成一个SQLORM基类

# 堡垒机用户与主机组之间的对应表
UserProfile_2_HostGroup = Table(
		"userprofile_2_hostgroup", Base.metada,
		Column("hostgroup_id", ForeignKey("hostgroup.id"), primary_key=True),
		Column("userprofile_id", ForeignKey("user_profile.id"), primary_key=True),
)

# 堡垒机用户与主机及主机用户一一对应的表，用于指定临时用户
UserProfile_2_HostSysuser = Table(
	"userprofile_2_hostsysuser", Base.metada,
	Column("host_id", ForeignKey("host.id"), primary_key=True),
	Column("sysuser_id", ForeignKey("sysuser.id"), primary_key=True),
	Column("userprofile_id", ForeignKey("user_profile.id"), primary_key=True),
)

# 主机组与主机及主机用户的对应表
HostGroup_2_HostSysuser = Table(
	"hostgroup_2_hostsysuser", Base.metada,
	Column("hostgroup_id", ForeignKey("hostgroup.id"), primary_key=True),
	Column("host_id", ForeignKey("host.id"), primary_key=True),
)


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
	__tablename__ = "host_group"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)

	def __repr__(self):
		return "<id={},name={}>".format(self.id, self.name)


# 堡垒机用户信息表
class UserProfile(Base):
	__tablename__ = "user_profile"
	id = Column(Integer, primary_key=True)
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	host_list = relationship('HostUser', secondary=UserProfile2HostUser, backref='userprofiles')
	groups = relationship('Group', secondary=UserProfile2Group, backref='userprofiles')

	def __repr__(self):
		return "<id={},name={}>".format(self.id, self.username)


# 主机与主机用户表
class HostSysuser(Base):
	__tablename__ = "host_sysuser"
	id = Column(Integer, primary_key=True)
	host_id = Column(Integer, ForeignKey("host.id"))

	# host_id和username联合唯一
	__table_args__ = UniqueConstraint("host_id", "username", name="Host_User")


# 主机用户表
class Sysuser(Base):
	__tablename__ = "sys_user"
	id = Column(Integer, primary_key=True)
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)

# log表
class AuditLog(Base):
	__tablename__ = "AuditLog"
	id = Column(Integer, primary_key=True)
	userprofile_id = Column(Integer, ForeignKey('user_profile.id'))
	hostuser_id = Column(Integer, ForeignKey('host_user.id'))
