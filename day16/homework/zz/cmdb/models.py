from django.db import models

# Create your models here.


class UserInfo(models.Model):
	USER_ROLE_TYPE = (
		(1, "普通用户"),
		(2, "项目经理"),
		(3, "管理员"),
	)
	email = models.EmailField(unique=True)
	password = models.TextField()
	# 创建时间
	create_date = models.TimeField(auto_now=True)
	# 是否锁定
	lock_flag = models.BooleanField(default=False)
	# 用户权限
	role = models.IntegerField(choices=USER_ROLE_TYPE, default=1)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name_plural = "用户信息"


class HostGroup(models.Model):
	group_name = models.CharField(max_length=64)

	def __str__(self):
		return self.group_name

	class Meta:
		verbose_name_plural = "主机组信息"


class IPInfo(models.Model):
	ip = models.GenericIPAddressField(unique=True)

	def __str__(self):
		return self.ip

	class Meta:
		verbose_name_plural = "IP信息"


class HostInfo(models.Model):
	HOST_STATE_TYPE = (
		(1, "在线"),
		(2, "下线"),
	)

	hostname = models.CharField(max_length=64)
	ip = models.ForeignKey(IPInfo)
	port = models.IntegerField()
	service = models.CharField(max_length=128)

	groups = models.ManyToManyField(HostGroup)

	state = models.IntegerField(choices=HOST_STATE_TYPE)

	def __str__(self):
		return "主机名：{}，ip地址：{}，服务：{}，组：{}，状态：{}".format(
			self.hostname,
			self.ip,
			self.service,
			[i.group_name for i in self.groups.all()],
			self.state,
		)

	class Meta:
		verbose_name_plural = "主机信息"
