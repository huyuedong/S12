from django.db import models

from bbs.models import UserProfile

# Create your models here.


# 群
class WebGroup(models.Model):
	name = models.CharField(u"群名", max_length=64)
	brief = models.CharField(u"群简介", max_length=255)
	owner = models.ForeignKey(UserProfile, related_name="group_owner", verbose_name=u"拥有者")
	admins = models.ManyToManyField(UserProfile, blank=True, related_name="group_admins", verbose_name=u"管理员")
	members = models.ManyToManyField(UserProfile, blank=True, related_name="group_members", verbose_name=u"群成员")
	max_members = models.IntegerField(u"最大成员数", default=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "群组"
		verbose_name_plural = "群组"
