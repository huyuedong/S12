from django.db import models

# Create your models here.
from Wolf.models import UserProfile  # 导入单独的一个用户认证的app下的用户model


class Asset(models.Model):
	"""
	资产表
	"""
	asset_type_choices = (
		("server", u"服务器"),
		("switch", u"交换机"),
		("router", u"路由器"),
		("firewall", u"防火墙"),
		("storage", u"存储设备"),
		("NLB", u"NetScaler"),
		("wireless", u"无线APP"),
		("software", u"软件资产"),
		("others", u"其他类"),
	)
	asset_type = models.CharField(verbose_name="设备类型", choices=asset_type_choices, max_length=64, default="server")
	name = models.CharField(verbose_name=u"设备名称", max_length=64, unique=True)
	model = models.CharField(verbose_name=u"型号", max_length=128, null=True, blank=True)
	sn = models.CharField(verbose_name=u"资产的SN号", max_length=128, unique=True)
	manufactory = models.ForeignKey("Manufactory", verbose_name=u"制造商", null=True, blank=True)
	management_ip = models.GenericIPAddressField(verbose_name=u"管理IP", blank=True, null=True)
	contract = models.ForeignKey("Contract", verbose_name=u"合同", null=True, blank=True)
	trade_date = models.DateField(verbose_name=u"购买时间", null=True, blank=True)
	expire_date = models.DateField(verbose_name=u"过保时间", null=True, blank=True)
	price = models.FloatField(verbose_name=u"价格", null=True, blank=True)
	business_unit = models.ForeignKey("BusinessUnit", verbose_name=u"所属业务线", null=True, blank=True)
	tags = models.ManyToManyField("Tag", verbose_name=u"标签", blank=True)
	admin = models.ForeignKey(UserProfile, verbose_name=u"资产管理员", null=True, blank=True)
	idc = models.ForeignKey("IDC", verbose_name=u"IDC机房", null=True, blank=True)

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(blank=True, auto_now_add=True)
	update_date = models.DateTimeField(blank=True, auto_now=True)

	class Meta:
		verbose_name = u"资产总表"
		verbose_name_plural = verbose_name

	def __str__(self):
		return "id:{}, name:{}".format(self.id, self.name)


class Server(models.Model):
	asset = models.OneToOneField("Asset")  # 一对一关联至资产总表
	created_by_choices = (
		("auto", "Auto"),
		("manual", "Manual"),
	)
	created_by = models.CharField(choices=created_by_choices, verbose_name=u"创建类型", max_length=32, default="auto")
	hosted_on = models.ForeignKey("self", related_name="hosted_on_server", verbose_name=u"寄宿于", null=True, blank=True)
	# 服务器如果有多个CPU的话，型号应该都是一样的，所以这里就没有做ForeignKey
	raid_type = models.CharField(verbose_name=u"raid类型", max_length=512, null=True, blank=True)

	os_type = models.CharField(verbose_name=u"操作系统类型", max_length=64, null=True, blank=True)
	os_distribution = models.CharField(verbose_name=u"发行版本", max_length=64, null=True, blank=True)
	os_release = models.CharField(verbose_name=u"操作系统版本", max_length=64, null=True, blank=True)

	create_date = models.DateTimeField(blank=True, auto_now_add=True)
	update_date = models.DateTimeField(blank=True, auto_now=True)

	class Meta:
		verbose_name = u"服务器"
		verbose_name_plural = verbose_name

	def __str__(self):
		return "name:{}, SN:{}".format(self.asset.name, self.asset.sn)


class NetworkDevice(models.Model):
	asset = models.OneToOneField("Asset")  # 一对一关联至资产总表
	vlan_ip = models.GenericIPAddressField(verbose_name=u"VlanIP", null=True, blank=True)
	intranet_ip = models.GenericIPAddressField(verbose_name=u"内网IP", null=True, blank=True)
	firmware = models.CharField(verbose_name=u"固件版本", null=True, blank=True)
	port_num = models.SmallIntegerField(verbose_name=u"端口个数", null=True, blank=True)
	device_detail = models.TextField(verbose_name=u"设置详细配置", null=True, blank=True)

	create_date = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)
	upadte_date = models.DateTimeField(verbose_name=u"最后更新时间", auto_now=True)

	class Meta:
		verbose_name = u"网络设备"
		verbose_name_plural = verbose_name

	def __str__(self):
		return "name:{}, SN:{}".format(self.asset.name, self.asset.sn)


class Software(models.Model):
	os_types_choices = (
		("linux", "Linux"),
		("windows", "Windows"),
		("network_firmware", "Network Firmware"),
		("software", "Software"),
	)
	os_distribution_choices = (
		("windows", "Windows"),
		("centos", "CentOS"),
		("ubuntu", "Ubuntu"),
	)
	os_type = models.CharField(verbose_name=u"系统类型", choices=os_types_choices, max_length=64, default="linux")
	distribution = models.CharField(verbose_name=u'发行版本', choices=os_distribution_choices, max_length=32, default='windows')
	version = models.CharField(verbose_name=u"软件/系统版本", max_length=64, help_text=u'eg. CentOS release 6.5')
	language_choices = (
		("cn", "中文"),
		("en", "英文"),
	)
	language = models.CharField(verbose_name=u"系统语言", choices=language_choices, max_length=32, default="cn")

	class Meta:
		verbose_name = "软件/系统"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.version

