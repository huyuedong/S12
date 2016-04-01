#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
管理员的具体操作实现代码
	可以用命令行直接增加的：
		- 增加堡垒机用户
		- 增加主机分组
		- 增加主机
		- 增加主机系统用户
	文件导入的：
		- 管理用户分组的               --> 对 User_HostGroup 表进行操作
		- 管理用户关联的主机系统用户    --> 对 User_HostSysuser 表进行操作
		- 管理主机关联的分组           --> 对 Host_HostGroup 表进行操作

"""
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import db_modles, db_conn
from core import utils
from core import start_ssh
from core import info_filter
import sqlalchemy.exc

logger = logging.getLogger(__name__)


def login():
	"""
	堡垒机登陆函数
	:return:
	"""
	count = 0
	while count < 3:
		username = input("UserName:").strip()
		if len(username) == 0:
			continue
		password = input("PassWord:").strip()
		try:
			session = db_conn.session
			# 按输入的用户名和密码去数据库中查询
			user_obj = session.query(db_modles.UserProfile).filter(
					db_modles.UserProfile.username == username,
					db_modles.UserProfile.password == password
			).first()

			if user_obj:  # 如果查找到记录，就说明用户存在。
				return user_obj
			else:
				print("Invalid username or password!")
				count += 1
		except sqlalchemy.exc.ArgumentError as e:
			logger.warn(e)
			raise SystemExit("Plaes start the database first.")
		except Exception as e:
			logger.warn(e)
			raise SystemExit("Please client to the database.Error:{}".format(e))
	else:
		print("Sorry, too many attempts.")


# 解析参数
def argv_parser(argvs):
	help_msg = """instruction -f cfg_name
	cfg_file must be yaml type.
	cfg_file need to be in the directory<'../StupidJumpServer/home/'>
	"""

	# 暂时只支持文件导入
	if "-f" in argvs:
		config_file = argvs[argvs.index("-f") + 1]
		return config_file
	else:
		print(help_msg)
		raise SystemExit("Invalid agrvs!")


def log_record(logs):
	session = db_conn.session
	session.add_all(logs)
	session.commit()


def create_users(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	# 如果解析出内容就将配置文件中的数据更新到数据库
	if source:
		session = db_conn.session
		for key in source:
			logger.debug("{}==>key:{},value:{}".format(source, key, source[key]))
			if source[key].get("admin_tag"):
				# 判断配置文件中是否有管理员的项
				obj = db_modles.UserProfile(username=key, password=source[key].get("password"), admin_tag=True)
			else:
				obj = db_modles.UserProfile(username=key, password=source[key].get("password"))
			# 如果在配置文件中有组信息
			if source[key].get("HostGroups"):
				groups = session.query(db_modles.HostGroup).filter(
					db_modles.HostGroup.name.in_(source[key].get("HostGroups"))
				).all()
				# 如果在数据库中没有找到了这个组名
				if not groups:
					logger.debug("Can't find <{}> in the host_group table.".format(source[key].get("HostGroups")))
					raise SystemExit("Invalid hostgroup parameters in the cfg_file.")
				obj.groups = groups
			if source[key].get("bind_hosts"):
				pass
			session.add(obj)
		session.commit()


def create_groups(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = db_conn.session
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			obj = db_modles.HostGroup(name=key)
			# 如果配置文件中有host_list选项
			if source[key].get("host_list"):
				host_list = info_filter.get_host_list(source[key])
				obj.host_and_sysusers = host_list
			# 如果配置文件中有user_profiles选项
			if source[key].get("user_profiles"):
				user_profiles = info_filter.get_user_profiles(source[key])
				obj.user_profiles = user_profiles
			session.add(obj)
		session.commit()


def create_hosts(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = db_conn.session
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			obj = db_modles.Host(
					hostname=key,
					ip_addr=source[key].get("ip_addr"),
					port=source[key].get("port") or 22,
			)
			session.add(obj)
		session.commit()


def create_hostandsysuser(argvs):
	"""
	host.id -- sysuser.id 将Host表和Sysuser表通过id关联起来
	eq:
		10.10.10.1 -- root
		10.10.10.1 -- mysql
		10.10.10.1 -- tomcat
		10.10.10.2 -- root
	:param argvs:
	:return:
	"""
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = db_conn.session
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			# 先根据配置文件中的hostname从Host表中找到host对象
			host_obj = session.query(db_modles.Host).filter(
				db_modles.Host.hostname == source[key].get("hostname")
			).first()
			assert host_obj  # 确保找得到该host对象
			sys_users_list = source[key]["sys_users"]
			for item in sys_users_list:
				assert item["auth_type"]  # 确保item有"auth_type"这个项
				if item.get("auth_type") == "ssh-password":
					sys_user_obj = session.query(db_modles.Sysuser).filter(
						db_modles.Sysuser.username == item.get("username"),
						db_modles.Sysuser.password == item.get("password"),
					).first()
				else:
					sys_user_obj = session.query(db_modles.Sysuser).filter(
						db_modles.Sysuser.username == item.get("username"),
						db_modles.Sysuser.auth_type == item.get("auth_type"),
					).first()
				if not sys_user_obj:
					logger.info("Can't find {} in <sys_user> table.".format(item.get("username")))
					raise SystemExit("Invalid sys_users parameters in cfg_file.")
				host_and_sysusers_obj = db_modles.HostandSysuser(host_id=host_obj.id, sysuser_id=sys_user_obj.id)
				session.add(host_and_sysusers_obj)
				# 如果配置文件中有groups项
				if source[key].get("groups"):
					host_group_objs = session.query(db_modles.Group).filter(
						db_modles.Group.name.in_(source[key].get("groups"))
					).all()
					assert host_group_objs
					host_and_sysusers_obj.groups = host_group_objs
				# 如果配置文件中有user_profiles项
				if source[key].get("user_profiles"):
					user_profiles_objs = session.query(db_modles.UserProfile).filter(
						db_modles.UserProfile.username.in_(source[key].get("user_profiles"))
					).all()
					assert user_profiles_objs
					host_and_sysusers_obj.user_profiles = user_profiles_objs
			session.commit()


def create_sysusers(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = db_conn.session
		for key in source:
			obj = db_modles.Sysuser(
				username=source[key].get("username"),
				auth_type=source[key].get("auth_type"),
				password=source[key].get("password"),
			)
			session.add(obj)
		session.commit()


def start(argv):
	print("This is StupidJumpServer.")
	user = login()
	if user:
		logger.info("{} login.".format(user.username))
		print("Welcome login StupidJumpServer!")
		exit_flag = False
		x_flag = False  # 是否有未分组的菜单的标志，如果有未分组的主机，就启用x菜单
		while not exit_flag:
			# 如果有未分组的主机，就打印一个x选项，列出未分组的主机数量
			if user.host_and_sysusers:
				print("[x]. Ungroup hosts: {}.".format(len(user.host_list)))
				x_flag = True
			# 如果有分组的主机，就打印选项和主机
			if len(user.groups) > 0:
				print("Host groups:")
				for index, group in enumerate(user.groups):
					print("[{}]. {}".format(index, group))
				while not exit_flag:
					# 让用户输入想连接的主机组,或者输入x进入未分组的主机列表
					choice = input("[{}] (b)back,(q)quit:".format(user.username)).strip()
					if len(choice) == 0:
						continue
					if choice.upper() == "B":
						break
					elif choice.upper() == "Q":
						logger.info("{} quit.".format(user.username))
						exit_flag = True
					# 进入到未分组的主机列表
					elif choice == 'x' and x_flag:
						print("Ungroup hosts:")
						for index, host in enumerate(user.host_list):
							print("[{}]. {}@{}({})".format(index, host.sysuser.username, host.host.hostname, host.host.ip_addr))

						# 在未分组的主机列表中直接选择主机去连接
						while not exit_flag:
							choice2 = input("[{}] (b)back,(q)quit:".format(user.username)).strip()
							if len(choice2) == 0:
								continue
							if choice2.upper() == "B":
								break
							elif choice2.upper() == "Q":
								logger.info("{] quit.".format(user.username))
								exit_flag = True
							elif choice2.isdigit():
								choice2 = int(choice2)
								# 连接用户选择的主机
								if choice2 < len(user.host_list):
									start_ssh.ssh_login(user, user.host_list[choice2], log_record)

					# 进入到选择的主机分组
					elif choice.isdigit():
						choice = int(choice)
						if choice < len(user.groups):
							# 打印出该主机组的主机列表
							print("Group: {}".format(user.groups[choice].name))
							for index, host in enumerate(user.groups[choice].host_and_sysusers):
								print("[{}]. {}@{}({})".format(index, host.sysuser.username, host.host.hostname, host.host.ip_addr))
							# 等待用户选择主机
							while not exit_flag:
								choice2 = input("[{}] (b)back,(q)quit:".format(user.username)).strip()
								if len(choice2) == 0:
									continue
								if choice2.upper() == "B":
									break
								elif choice2.upper() == "Q":
									logger.info("{} quit.".format(user.username))
									exit_flag = True
								elif choice2.isdigit():
									choice2 = int(choice2)
									# 连接用户选择的主机
									if choice2 < len(user.groups[choice].host_list):
										start_ssh.ssh_login(user, user.groups[choice].host_list[choice2], log_record)

			else:
				print("Sorry, There is no groups under you.")


def syncdb(argvs):
	print("init database, create table structure...")
	engine = db_conn.engine
	db_modles.Base.metadata.create_all(engine)
