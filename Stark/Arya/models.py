from django.db import models

# Create your models here.


class Host(models.Model):
	hostname = models.CharField(max_length=128, unique=True, verbose_name=u"主机名")
	key = models.TextField(verbose_name=u"KEY")

	status_choices = (
		(0, "Waiting Approval"),
		(1, "Accepted"),
		(2, "Rejected"),
	)
	status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name=u"主机状态")
	os_type_choices = (
		("redhat", "RedHat\CentOS"),
		("ubuntu", "Ubuntu"),
		("suse", "Suse"),
		("windows", "Windows"),
	)
	os_type = models.CharField(choices=os_type_choices, max_length=64, default="redhat")

	def __str__(self):
		return self.hostname


class HostGroup(models.Model):
	name = models.CharField(max_length=255, verbose_name=u"组名")
	hosts = models.ManyToManyField(Host, blank=True, verbose_name=u"包含主机")

	def __str__(self):
		return self.name


class Task(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.id
