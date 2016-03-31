#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
查询堡垒机用户的关联的组、主机及主机用户
"""
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import db_modles, db_conn

logger = logging.getLogger(__name__)


# 根据用户名找到所属的HostGroup组。
def get_hostgroup(user_obj):
	"""

	:param user_obj: 用户对象
	:return: 该用户关联的host group信息
	"""
	print("Loading HosGroups...")
	session = db_conn.StupidJumpServer().session()
	hostgroup_list = session.query(db_modles.HostGroup).filter(
			db_modles.HostGroup.user_profiles.username.in_(user_obj.username)
	)
	return hostgroup_list


# 根据配置文件中指定的主机用户名从<Sysuser>表中取出该主机用户信息的id
def get_sysuser_id(arg):
	session = db_conn.StupidJumpServer().session()
	logger.debug("get the id of sysuser in cfg_file from Sysuser table.")
	sysuser_id = session.query(db_modles.Sysuser).filter(
		db_modles.Sysuser.username.in_(arg.get("sys_users")["username"])
	)
	if not sysuser_id:
		logger.debug("Can't find {} in the Sysuser table.".format(arg.get("sys_users")["username"]))
		raise SystemExit("Invalid sysuser.")
	return sysuser_id


# 根据配置文件中指定的主机名从<Host>表中取出该主机对应的id
def get_host_id(arg):
	session = db_conn.StupidJumpServer().session()
	logger.debug("try to get the id of sysuser in cfg_file from Sysuser table.")
	host_id = session.query(db_modles.Host.id).filter(
		db_modles.Host.hostname.in_(arg.get("hostname"))
	)
	if not host_id:
		logger.debug("Can't find {} in the Host table.".format(arg.get("hostname")))
		raise SystemExit("Invalid hostname!")
	return host_id


def get_host_list(vals):
	session = db_conn.StupidJumpServerDB().session()
	host_list = session.query(db_modles.HostandSysuser).filter(
			db_modles.Host.hostname.in_(vals.get("host_list"))
	).all()
	if not host_list:
		logger.warn("Can't find {} in the <HostandSysuser> table".format(vals.get("host_list")))
		raise SystemExit("Invalid host_list parameters in the cfg_file.")
	return host_list


def get_user_profiles(vals):
	session = db_conn.StupidJumpServerDB().session()
	user_profiles = session.query(db_modles.UserProfile).filter(
			db_modles.UserProfile.username.in_(vals.get("user_profiles"))
	).all()
	if not user_profiles:
		logger.warn("Can't find {} in the <UserProfile> table".format(vals.get("user_profiles")))
		raise SystemExit("Invalid user_profiles parameters in the cfg_file.")
	return user_profiles
