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
from core.db_conn import StupidJumpServerDB
from core import utils
from core import start_ssh

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
		my_db = StupidJumpServerDB()
		# 按输入的用户名和密码去数据库中查询
		user_obj = my_db.session().query(db_modles.UserProfile).filter(
				db_modles.UserProfile.username == username,
				db_modles.UserProfile.password == password
		).first()

		if user_obj:  # 如果查找到记录，就说明用户存在。
			return user_obj
		else:
			print("Invalid username or password!")
			count += 1
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
	session = StupidJumpServerDB().session()
	session.add_all(logs)
	session.commit()


def create_users(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	# 如果解析出内容就将配置文件中的数据更新到数据库
	if source:
		session = StupidJumpServerDB().session()
		for key in source:
			logger.debug("{}==>key:{},value:{}".format(source, key, source[key]))
			# 堡垒机用户的信息
			obj = db_modles.UserProfile(username=key, password=source[key].get("password"))
			# 如果在配置文件中有组信息
			if source[key].get("HostGroups"):
				groups = session.query(db_modles.HostGroup).filter(
					db_modles.HostGroup.name.in_(source[key].get("HostGroups"))
				).all()
				# 如果在数据库中没有找到了这个组名
				if not groups:
					logger.debug("Can't find <{}> in the host_group table.".format(source[key].get("HostGroups")))
					raise SystemExit("Invalid hostgroup name.")
				obj.groups = groups
			if source[key].get("bind_hosts"):
				pass
			session.add(obj)
		session.commit()


def create_groups(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = StupidJumpServerDB().session()
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			obj = db_modles.HostGroup(name=key)
			if source[key].get("bind_hosts"):
				pass

			if source[key].get("user_profiles"):
				pass

			session.add(obj)
		session.commit()


def create_hosts(argvs):
	cfg_file = argv_parser(argvs)
	source = utils.yaml_parser(cfg_file)
	if source:
		session = StupidJumpServerDB().session()
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			obj = db_modles.Host(
					hostname=key,
					ip_addr=source[key].get("ip_addr"),
					port=source[key].get("port") or 22,
			)
			session.add(obj)
		session.commit()


def creae_hostandsysuser(argvs):
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
		session = StupidJumpServerDB().session()
		for key in source:
			logger.debug("{}==>key:{}, value:{}".format(source, key, source[key]))
			obj = db_modles.HostandSysuser()


def create_sysuser(argvs):
	pass


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
			if user.host_list:
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
							for index, host in enumerate(user.groups[choice].host_list):
								print("[{}]. {}@{}({})".format(index, host.sysuser.username, host.host.hostname, host.host.ip_addr))
							# 等待用户选择主机
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
									if choice2 < len(user.groups[choice].host_list):
										start_ssh.ssh_login(user, user.groups[choice].host_list[choice2], log_record)

			else:
				print("Sorry, There is no groups under you.")


def syncdb(argvs):
	print("init database...")
	engine = db_conn.StupidJumpServerDB().engine()
	db_modles.Base.metadata.create_all(engine)
