#! -*- coding: utf8 -*-

"""
分布式监控系统
"""

from django.db import models

# Create your models here.


class Host(models.Model):
	name = models.CharField(max_length=64, unique=True)
	ip_addr = models.GenericIPAddressField(unique=True)
	host_groups = models.ManyToManyField("HostGroup", blank=True)
	templates = models.ManyToManyField('Template', blank=True)
	monitored_by_choice = (
		("agent", "Agent"),
		("snmp", "SNMP"),
		("wget", "WGET"),
	)
	monitored_by = models.CharField(verbose_name=u"监控方式", max_length=64, choices=monitored_by_choice)
	status_choices = (
		(1, "Online"),
		(2, "Down"),
		(3, "Underahable"),
		(4, "Offline"),
	)
	status = models.IntegerField(verbose_name=u"状态", choices=status_choices, default=1)
	memo = models.TextField(verbose_name=u"备注", blank=True, null=True)

	def __str__(self):
		return self.name


class HostGroup(models.Model):
	name = models.CharField(max_length=64, unique=True)
	templates = models.ManyToManyField("Template", blank=True)
	memo = models.TextField(verbose_name=u"备注", blank=True, null=True)

	def __str__(self):
		return self.name


class ServiceIndex(models.Model):
	name = models.CharField(max_length=64)


