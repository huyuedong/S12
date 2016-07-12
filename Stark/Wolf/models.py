from django.db import models

# Create your models here.
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		"""
		根据给定的email、name和password创建并保存一个用户
		"""
		if not email:
			raise ValueError(u"必须输入邮箱。")

		user = self.model(
			email=self.normalize_email(email),
			name=name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):
		"""
		根据给定的email、name和password创建并保存一个超级用户
		"""

		user = self.create_user(
			email,
			password=password,
			name=name,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser):
	email = models.EmailField(
		verbose_name=u"邮箱",
		max_length=255,
		unique=True,
	)
	name = models.CharField(max_length=32)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["name"]

	def get_full_name(self):
		# 邮件作为唯一认证
		return self.email

	def get_short_name(self):
		# 邮件作为唯一认证
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"""
		这个用户是否有特定权限
		"""
		return True

	def has_module_perms(self, app_label):
		"""
		该用户是否有查看app：app_label的权限
		"""
		return True

	@property
	def is_staff(self):
		"""
		该用户是否为职员
		"""
		return self.is_admin
