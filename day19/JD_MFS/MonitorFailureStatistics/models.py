from django.db import models

# Create your models here.


class Fault(models.Model):
	fault_status_type = (
		("solved", "解决"),
		("follow", "跟进"),
		("unknown", "未知"),
	)
	occ_time = models.DateField("日期")
	str_time = models.DateTimeField("发生时间")
	end_time = models.DateTimeField("结束时间")
	time_consuming = models.CharField("处理耗时", max_length=64)
	fault_info = models.TextField("问题（故障）", max_length=255)
	fault_ip = models.GenericIPAddressField("IP", null=True, blank=True)
	fault_status = models.CharField("处理结果", choices=fault_status_type, max_length=32)
	notify_person = models.CharField("通知人", max_length=64)
	handle_person = models.CharField("处理人", max_length=64)
	responsible_party = models.CharField("故障责任方", max_length=255)
	memo = models.TextField("备注", max_length=255, blank=True, null=True)
	date = models.DateTimeField("记录创建时间", auto_now_add=True)

	def __str__(self):
		return "故障：{}，处理结果：{}，通知人：{}，处理人：{}。".format(
			self.fault_info,
			self.fault_status,
			self.notify_person,
			self.handle_person,
		)

	class Meta:
		verbose_name = "监控故障报警统计"
		verbose_name_plural = "监控故障报警统计"

	# 给状态加颜色
	def colored_status(self):
		color_dic = {
			'solved': "#5DFC70",
			'follow': "#FFBF00",
			'unknown': "#B40404",
		}
		html_td = '<span style="padding:5px;background-color:{};">{}</span>'.format(
			color_dic[self.fault_status], self.get_fault_status_display()
		)
		return html_td

	colored_status.allow_tags = True
	colored_status.short_description = "处理结果"
