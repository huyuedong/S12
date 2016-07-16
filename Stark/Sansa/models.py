from django.db import models

# Create your models here.
from Wolf.models import UserProfile  # 导入单独的一个用户认证的app下的用户model

ASSET_TYPE_CHOICES = (
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



class Asset(models.Model):
	"""
	资产表
	"""

	asset_type = models.CharField(verbose_name=u"设备类型", choices=ASSET_TYPE_CHOICES, max_length=64, default="server")
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
	firmware = models.CharField(verbose_name=u"固件版本", max_length=64, null=True, blank=True)
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


class CPU(models.Model):
	asset = models.OneToOneField("Asset")  # 这里保存的是该资产的CPU属性（CPU个数可以为多个），并不是单纯的CPU
	cpu_model = models.CharField(verbose_name=u"CPU型号", max_length=128, null=True, blank=True)
	cpu_count = models.SmallIntegerField(verbose_name=u"CPU个数")
	cpu_core_count = models.SmallIntegerField(verbose_name=u"物理核心数")

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = u"CPU"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.cpu_model


class RAM(models.Model):
	asset = models.ForeignKey("Asset")  # 一个资产可以有很多条内存
	sn = models.CharField(verbose_name=u"SN号", max_length=128, null=True, blank=True)
	manufactory = models.CharField(verbose_name=u"制造商", max_length=128, null=True, blank=True)
	model = models.CharField(verbose_name=u"内存型号", max_length=128)
	slot = models.CharField(verbose_name=u"插槽", max_length=64)
	capacity = models.IntegerField(verbose_name=u"内存大小（MB）")

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = u"RAM"
		verbose_name_plural = verbose_name
		unique_together = ("asset", "slot")  # 使用资产号和插槽来联合唯一是因为读取到的虚拟机的内存序列号可能会有重复

	def __str__(self):
		return "{}:{}:{}".format(self.asset_id, self.slot, self.capacity)

	auto_create_fields = ["sn", "solt", "model", "capacity"]  # 标记抓取的数据中必须有的字段


class Disk(models.Model):
	asset = models.ForeignKey("Asset")  # 一个资产可以拥有多块硬盘。而不是资产表里用外键关联硬盘表！！！
	sn = models.CharField(verbose_name=u"SN号", max_length=128, null=True, blank=True)
	slot = models.CharField(verbose_name=u"插槽位", max_length=64)
	manufactory = models.CharField(verbose_name=u"制造商", max_length=128, null=True, blank=True)
	mdoel = models.CharField(verbose_name=u"磁盘型号", max_length=128, null=True, blank=True)
	capacity = models.FloatField(verbose_name=u"磁盘容量GB")
	disk_iface_choice = (
		("SATA", "SATA"),
		("SAS", "SAS"),
		("SCSI", "SCSI"),
		("SSD", "SSD"),
		("other", "其他")
	)
	iface_type = models.CharField(verbose_name=u"接口类型", max_length=64, choices=disk_iface_choice, default="SAS")

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = u"硬盘"
		verbose_name_plural = verbose_name
		unique_together = ("asset", "slot")  # 使用资产号和插槽来联合唯一是因为读取到的虚拟机的硬盘序列号可能会有重复

	def __str__(self):
		return "disk:{} slot:{} capacity:{}".format(self.asset_id, self.slot, self.capacity)

	auto_create_fields = ["sn", "slot", "manufactory", "model", "capacity", "iface_type"]


class NIC(models.Model):
	asset = models.ForeignKey("Asset")  # 这里也是一对多，一个资产对应多个网卡
	name = models.CharField(verbose_name=u"网卡名", max_length=128, null=True, blank=True)
	sn = models.CharField(verbose_name=u"SN号", max_length=128, null=True, blank=True)
	model = models.CharField(verbose_name=u"网卡类型", max_length=128, null=True, blank=True)
	macaddress = models.CharField(verbose_name=u"MAC", max_length=128, unique=True)
	ipaddress = models.GenericIPAddressField(verbose_name=u"IP", null=True, blank=True)
	netmask = models.CharField(verbose_name=u"网关", max_length=64, null=True, blank=True)
	bonding = models.CharField(verbose_name=u"绑定", max_length=64, null=True, blank=True)

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = u"网卡"
		verbose_name_plural = verbose_name

	def __str__(self):
		return "{}:{}".format(self.asset_id, self.macaddress)

	auto_create_fields = ["name", "sn", "model", "macaddress", "ipaddress", "netmask", "bonding"]


class RaidAdaptor(models.Model):
	asset = models.ForeignKey("Asset")
	sn = models.CharField(verbose_name=u"SN号", max_length=128, null=True, blank=True)
	slot = models.CharField(verbose_name=u"插槽", max_length=64)
	model = models.CharField(verbose_name=u"型号", max_length=128, null=True, blank=True)

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True, null=True, blank=True)

	class Meta:
		verbose_name = u"Raid卡"
		verbose_name_plural = verbose_name
		unique_together = ("asset", "slot")

	def __str__(self):
		return self.name


class Manufactory(models.Model):
	manufactory = models.CharField(verbose_name=u"厂商名称", max_length=128, unique=True)
	support_phone = models.CharField(verbose_name=u"支持电话", max_length=64, null=True, blank=True)

	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)

	class Meta:
		verbose_name = u"厂商"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.manufactory


class BusinessUnit(models.Model):
	parent_unit = models.ForeignKey("self", related_name="parent_level", null=True, blank=True)
	name = models.CharField(verbose_name=u"业务线", max_length=128, unique=True)

	memo = models.CharField(verbose_name=u"备注", max_length=64, null=True, blank=True)

	class Meta:
		verbose_name = u"业务线"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Contract(models.Model):
	sn = models.CharField(verbose_name=u"合同号", max_length=128, unique=True)
	name = models.CharField(verbose_name=u"合同名称", max_length=64)
	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)
	price = models.IntegerField(verbose_name=u"合同金额", null=True, blank=True)
	detail = models.TextField(verbose_name=u"合同详情", null=True, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	license_num = models.IntegerField(verbose_name=u"license数量", null=True, blank=True)
	create_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)

	class Meta:
		verbose_name = u"合同"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class IDC(models.Model):
	name = models.CharField(verbose_name=u"机房名称", max_length=128, unique=True)
	memo = models.CharField(verbose_name=u"备注", max_length=128, null=True, blank=True)

	class Meta:
		verbose_name = u"机房"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(verbose_name=u"标签名", max_length=32, unique=True)
	creator = models.ForeignKey(UserProfile)  # 标签的创建者
	create_date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = u"标签"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class EventLog(models.Model):
	name = models.CharField(verbose_name=u"事件名称", max_length=128)
	event_type_choices = (
		(1, u"硬件变更"),
		(2, u"新增配件"),
		(3, u"设备上线"),
		(4, u"设备下线"),
		(5, u"定期维护"),
		(6, u"业务上线/更新/变更"),
		(7, u"其他"),
	)
	event_type = models.SmallIntegerField(verbose_name=u"事件类型", choices=event_type_choices)
	asset = models.ForeignKey("Asset")
	component = models.CharField(verbose_name=u"事件子项", max_length=255, null=True, blank=True)
	detail = models.TextField(verbose_name=u"事件详情")
	date = models.DateTimeField(verbose_name=u"事件时间", auto_now_add=True)
	user = models.ForeignKey(UserProfile, verbose_name=u"事件源")
	memo = models.TextField(verbose_name=u"备注", null=True, blank=True)

	class Meta:
		verbose_name = u"事件记录"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

	def colored_event_type(self):
		"""
		为不同的事件设置不同的背景颜色
		"""
		if self.event_type == 1:
			cell_html = "<span style='background: orange;'>{}</span>"
		elif self.event_type == 2:
			cell_html = "<span style='background: yellowgreen;'>{}</span>"
		else:
			cell_html = "<span>{}</span>"
		return cell_html.format(self.get_event_type_display())
	colored_event_type.allow_tags = True
	colored_event_type.short_description = u"事件类型"


class NewAssetApprovalZone(models.Model):
	sn = models.CharField(verbose_name=u"资产SN号", max_length=128, unique=True)
	asset_type = models.CharField(verbose_name=u"资产类型", choices=ASSET_TYPE_CHOICES, max_length=64, null=True, blank=True)
	manufactory = models.CharField(max_length=64, null=True, blank=True)
	model = models.CharField(verbose_name=u"型号", max_length=128, null=True, blank=True)
	ram_size = models.IntegerField(verbose_name=u"内容大小", null=True, blank=True)
	cpu_model = models.CharField(verbose_name=u"CPU型号", max_length=128, null=True, blank=True)
	cpu_count = models.IntegerField(verbose_name=u"CPU数量", null=True, blank=True)
	cpu_core_count = models.IntegerField(verbose_name=u"CPU核心数", null=True, blank=True)
	os_distribution = models.CharField(max_length=64, null=True, blank=True)
	os_type = models.CharField(verbose_name=u"OS类型", max_length=64, null=True, blank=True)
	os_release = models.CharField(verbose_name=u"OS版本", max_length=64, null=True, blank=True)
	data = models.TextField(verbose_name=u"资产数据")
	date = models.DateTimeField(verbose_name=u"汇报日期", auto_now_add=True)
	approved = models.BooleanField(verbose_name=u"已批准", default=False)
	approved_by = models.ForeignKey(UserProfile, verbose_name=u"批准人", null=True, blank=True)
	approved_date = models.DateTimeField(verbose_name=u"批准日期", null=True, blank=True)  # ???

	class Meta:
		verbose_name = u"新上线待批准资产"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.sn
