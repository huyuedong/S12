#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
初始化数据库表结构
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, UniqueConstraint, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship, query
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType, PasswordType

import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.db_conn import StupidJumpServerDB
mydb = StupidJumpServerDB()
engine = mydb.engine()
# from conf.setting import DATABASE
logger = logging.getLogger(__name__)
#
# engine_info = "{}+{}://{}:{}@{}:{}/StupidJumpServer".format(DATABASE.get("db_name"),
#                                                             DATABASE.get("engine"),
#                                                             DATABASE.get("username"),
#                                                             DATABASE.get("password"),
#                                                             DATABASE.get("host"),
#                                                             DATABASE.get("port")
#                                                             )
#
# engine = create_engine(engine_info, max_overflow=5, echo=False)
Base = declarative_base()  # 生成一个SQLORM基类

# 堡垒机用户与主机组之间的对应表
UserProfile_2_HostGroup = Table(
		"userprofile_2_hostgroup", Base.metadata,
		Column("hostgroup_id", ForeignKey("host_group.id"), primary_key=True),
		Column("userprofile_id", ForeignKey("user_profile.id"), primary_key=True),
)

# 堡垒机用户与主机及主机用户一一对应的表，用于指定临时用户
UserProfile_2_HostandSysuser = Table(
		"userprofile_2_hostsysuser", Base.metadata,
		Column("hostandsysuser_id", ForeignKey("host_and_sysuser.id"), primary_key=True),
		Column("userprofile_id", ForeignKey("user_profile.id"), primary_key=True),
)

# 主机组与主机的对应表
HostGroup_2_HostandSysuser = Table(
		"hostgroup_2_hostandsysuser", Base.metadata,
		Column("hostgroup_id", ForeignKey("host_group.id"), primary_key=True),
		Column("hostandsysuser_id", ForeignKey("host_and_sysuser.id"), primary_key=True),
)


# 主机表
class Host(Base):
	__tablename__ = "host"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)
	host_and_sysusers = relationship("HostandSysuser")

	def __repr__(self):
		return "<id={}, hostname={}, ip_addr={}, port={}>".format(self.id, self.hostname, self.ip_addr, self.port)


# 主机组表
class HostGroup(Base):
	__tablename__ = "host_group"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)
	host_and_sysusers = relationship("Host", secondary=HostGroup_2_HostandSysuser, backref="groups")

	def __repr__(self):
		return "<id={},groupname={}>".format(self.id, self.name)


# 堡垒机用户信息表
class UserProfile(Base):
	__tablename__ = "user_profile"
	id = Column(Integer, primary_key=True)
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	lock_tag = Column(Boolean, default=False)  # 是否锁定
	admin_tag = Column(Boolean, default=False)  # 是否为管理员
	host_and_sysusers = relationship('HostandSysuser', secondary=UserProfile_2_HostandSysuser, backref='user_profiles')
	groups = relationship('HostGroup', secondary=UserProfile_2_HostGroup, backref='user_profiles')
	audit_logs = relationship("AuditLog")

	def __repr__(self):
		return "<id={},username={}>".format(self.id, self.username)


# 主机与主机用户表
class HostandSysuser(Base):
	__tablename__ = "host_and_sysuser"
	id = Column(Integer, primary_key=True, autoincrement=True)
	host_id = Column(Integer, ForeignKey("host.id"))  # 主机id
	sysuser_id = Column(Integer, ForeignKey("sys_user.id"))  # 主机用户id,默认同样的主机用户名为同样的密码

	host = relationship("Host")
	sysuser = relationship("Sysuser")
	user_profiles = relationship("UserProfile", secondary=UserProfile_2_HostandSysuser)
	audit_logs = relationship("AuditLog")

	# host_id和username联合唯一,类型为元组或字典
	__table_args__ = (UniqueConstraint("host_id", "sysuser_id", name="_host_sysuser_uc"), )

	def __repr__(self):
		return "<id={},host_id={},sysuser_id={}>".format(self.id, self.host_id, self.sysuser_id)


# 主机用户表
class Sysuser(Base):
	__tablename__ = "sys_user"
	AuthTypes = [
		(u'ssh-password', u'SSH/Password'),
		(u'ssh-key', u'SSH/KEY'),
	]
	id = Column(Integer, primary_key=True)
	auth_type = Column(ChoiceType(AuthTypes))
	username = Column(String(64), unique=True, nullable=False)
	password = Column(String(255), nullable=False)

	__table_args__ = (UniqueConstraint("auth_type", "username", "password", name="_username_password_uc"), )

	def __repr__(self):
		return "<Sysuser(id={}, auth_type={}, username={})>".format(self.id, self.auth_type, self.username)


# log表
class AuditLog(Base):
	__tablename__ = "AuditLog"
	id = Column(Integer, primary_key=True)
	user_profile_id = Column(Integer, ForeignKey('user_profile.id'))
	host_and_sysuser_id = Column(Integer, ForeignKey('host_and_sysuser.id'))
	action_choice = [
		(0, "CMD"),
		(1, "Login"),
		(2, "Logout"),
		(3, "GetFile"),
		(4, "SendFile"),
		(5, "Exception"),
	]
	action_choice2 = [
		(u"cmd", u"CMD"),
		(u"login", u"Login"),
		(u"logout", u"Logout"),
		(u"getfile", u"GetFile"),
		(u"sendfile", u"SendFile"),
		(u"exception", u"Exception"),
	]
	action_type = Column(ChoiceType(action_choice2))
	cmd = Column(String(255))
	data = Column(DateTime)

	user_profiles = relationship("UserProfile")
	host_and_sysusers = relationship("HostandSysuser")

if __name__ == "__main__":
	Base.metadata.create_all(engine)
