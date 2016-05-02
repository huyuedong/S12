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
	hostname = models.CharField(max_length=64)
	ip = models.GenericIPAddressField(unique=True)
	port = models.IntegerField()
	group = models.IntegerField(choices=HOST_GROUP_TYPE)
	state = models.IntegerField(choices=HOST_STATE_TYPE)
