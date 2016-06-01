from django.db import models

# Create your models here.


class UserInfo(models.Model):
	email = models.EmailField(unique=True)
	password = models.TextField()
	# 创建时间
	create_date = models.TimeField(auto_now=True)
	# 是否锁定
	lock_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.email


class HostInfo(models.Model):
	HOST_STATE_TYPE = (
		(1, "在线"),
		(2, "下线"),
	)
	HOST_GROUP_TYPE = (
		(1, "研发"),
		(2, "测试"),
		(3, "运维"),
	)
	SERVICE_TYPE = (
		(1, "tomcat"),
		(2, "MySQL"),
		(3, "Nginx"),
		(4, "FTP"),
	)
	hostname = models.CharField(max_length=64)
	ip = models.GenericIPAddressField(unique=True)
	port = models.IntegerField()
	service = models.IntegerField(choices=SERVICE_TYPE)
	group = models.IntegerField(choices=HOST_GROUP_TYPE)
	state = models.IntegerField(choices=HOST_STATE_TYPE)

	def __str__(self):
		return "主机名：{}，ip地址：{}，服务：{}，组：{}，状态：{}".format(
			self.hostname,
			self.ip,
			self.service,
			self.group,
			self.state,
		)
