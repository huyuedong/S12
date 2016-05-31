# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

course_choices = (
	('LinuxL1',u'Linux中高级'),
	('LinuxL2',u'Linux架构师'),
	('Linux51',u'Linux中高级(51网络)'),
	('LinuxL251',u'Linux中高级+架构合成班(51网络)'),
	('PythonDevOps',u'Python自动化开发'),
	('PythonFullStack',u'Python高级全栈开发'),
	('PythonDevOps51',u'Python自动化开发(51网络)'),
	('PythonFullStack51',u'Python全栈开发(51网络)'),
	('BigDataDev',u"大数据开发课程"),
	('Cloud',u"云计算课程"),
)

class_type_choices = (
	('online', u'网络班'),
	('offline_weekend', u'面授班(周末)',),
	('offline_fulltime', u'面授班(脱产)',),
)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(u"姓名", max_length=32)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u"用户"
		verbose_name_plural = u"用户"


class School(models.Model):
	name = models.CharField(u"校区名称", max_length=64, unique=True)
	addr = models.CharField(u"地址", max_length=128)
	staffs = models.ManyToManyField('UserProfile', blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u"校区"
		verbose_name_plural = u"校区"


class Course(models.Model):
	name = models.CharField(u"课程名称", max_length=128, unique=True)
	price = models.IntegerField(u"面授价格")
	online_price = models.IntegerField(u"网络班价格")
	brief = models.TextField(u"课程简介")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u"课程"
		verbose_name_plural = u"课程"


class ClassList(models.Model):
	course = models.ForeignKey('Course')
	course_type = models.CharField(u"课程类型", choices=class_type_choices, max_length=32)
	semester = models.IntegerField(u"学期")
	start_date = models.DateField(u"开班日期")
	graduate_date = models.DateField(u"结业日期", blank=True, null=True)
	teachers = models.ManyToManyField(UserProfile, verbose_name=u"讲师")

	def __str__(self):
		return "{}({})".format(self.course.name, self.get_course_type_display())

	class Meta:
		verbose_name = u'班级列表'
		verbose_name_plural = u"班级列表"
		unique_together = ("course", "course_type", "semester")

	def get_student_num(self):
		return "{}".format(self.customer_set.select_related().count())
	get_student_num.short_description = u'学员数量'


class Customer(models.Model):
	qq = models.CharField(u"QQ号", max_length=64, unique=True)
	name = models.CharField(u"姓名", max_length=32, blank=True, null=True)
	phone = models.BigIntegerField(u'手机号', blank=True, null=True)
	stu_id = models.CharField(u"学号", blank=True, null=True, max_length=64)
	# id = models.CharField(u"身份证号",blank=True,null=True,max_length=128)
	source_type = (
		('qq', u"qq群"),
		('referral', u"内部转介绍"),
		('51cto', u"51cto"),
		('agent', u"招生代理"),
		('others', u"其它"),
	)
	source = models.CharField(u'客户来源',max_length=64, choices=source_type,default='qq')
	referral_from = models.ForeignKey(
		'self',
		verbose_name=u"转介绍自学员",
		help_text=u"若此客户是转介绍自内部学员,请在此处选择内部学员姓名",
		blank=True,
		null=True,
		related_name="internal_referral"
	)

	course = models.ForeignKey(Course, verbose_name=u"咨询课程")
	class_type = models.CharField(u"班级类型", max_length=64, choices=class_type_choices)
	customer_note = models.TextField(u"客户咨询内容详情", help_text=u"客户咨询的大概情况,客户个人信息备注等...")
	status_choices = (
		('signed', u"已报名"),
		('unregistered', u"未报名"),
		('graduated', u"已毕业"),
	)

	status = models.CharField(u"状态", choices=status_choices, max_length=64, default=u"unregistered", help_text=u"选择客户此时的状态")
	consultant = models.ForeignKey(UserProfile, verbose_name=u"课程顾问")
	date = models.DateField(u"咨询日期", auto_now_add=True)
	class_list = models.ManyToManyField('ClassList', verbose_name=u"已报班级", blank=True)

	def colored_status(self):
		global format_td
		if self.status == "signed":
			format_td =format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已报名</span>')
		elif self.status == "unregistered":
			format_td =format_html('<span style="padding:2px;background-color:gray;color:white">未报名</span>')
		elif self.status == "paid_in_full":
			format_td =format_html('<span style="padding:2px;background-color:orange;color:white">学费已交齐</span>')

		return format_td

	def get_enrolled_course(self):
		return " | ".join(["%s(%s)" %(i.get_course_display(),i.semester) for i in self.class_list.select_related()])

	def __str__(self):
		return "{},{}".format(self.qq, self.name)

	class Meta:
		verbose_name = u"客户"
		verbose_name_plural = u"客户"


class ConsultRecord(models.Model):
	customer = models.ForeignKey(Customer, verbose_name=u"所咨询客户")
	note = models.TextField(u"跟进内容...")
	status_choices = (
		(1, u"近期无报名计划"),
		(2, u"2个月内报名"),
		(3, u"1个月内报名"),
		(4, u"2周内报名"),
		(5, u"1周内报名"),
		(6, u"2天内报名"),
		(7, u"已报名"),
	)
	status = models.IntegerField(u"状态", choices=status_choices, help_text=u"选择客户此时的状态")
	consultant = models.ForeignKey(UserProfile, verbose_name=u"跟踪人")
	date = models.DateField(u"跟进日期", auto_now_add=True)

	def __str__(self):
		return u"{}, {}".format(self.customer, self.status)

	class Meta:
		verbose_name = u'客户咨询跟进记录'
		verbose_name_plural = u"客户咨询跟进记录"


class CourseRecord(models.Model):
	course = models.ForeignKey(ClassList, verbose_name=u"班级(课程)")
	day_num = models.IntegerField(u"节次", help_text=u"此处填写第几节课或第几天课程...,必须为数字")
	date = models.DateField(auto_now_add=True, verbose_name=u"上课日期")
	teacher = models.ForeignKey(UserProfile, verbose_name=u"讲师")

	def __str__(self):
		return u"{} 第{}天".format(self.course, self.day_num)

	class Meta:
		verbose_name = u'上课纪录'
		verbose_name_plural = u"上课纪录"
		unique_together = ('course', 'day_num')

	def get_total_show_num(self):
		total_shows = self.studyrecord_set.select_related().filter(record="checked").count()
		return "<a href='../studyrecord/?course_record__id__exact=%s&record__exact=checked' >%s</a>" % (self.id,total_shows)

	def get_total_late_num(self):
		total_shows = self.studyrecord_set.select_related().filter(record="late").count()
		return "<a href='../studyrecord/?course_record__id__exact=%s&record__exact=late' >%s</a>" % (self.id,total_shows)

	def get_total_noshow_num(self):
		total_shows = self.studyrecord_set.select_related().filter(record="noshow").count()
		return "<a href='../studyrecord/?course_record__id__exact=%s&record__exact=noshow' >%s</a>" % (self.id,total_shows)

	def get_total_leave_early_num(self):
		total_shows = self.studyrecord_set.select_related().filter(record="leave_early").count()
		return "<a href='../studyrecord/?course_record__id__exact=%s&record__exact=leave_early' >%s</a>" % (self.id,total_shows)

	get_total_leave_early_num.allow_tags = True
	get_total_noshow_num.allow_tags = True
	get_total_late_num.allow_tags = True
	get_total_show_num.allow_tags = True
	get_total_show_num.short_description = u"出勤人数"
	get_total_noshow_num.short_description = u"缺勤人数"
	get_total_late_num.short_description = u"迟到人数"
	get_total_leave_early_num.short_description = u"早退人数"


class StudyRecord(models.Model):
	course_record = models.ForeignKey(CourseRecord, verbose_name=u"第几天课程")
	student = models.ForeignKey(Customer,verbose_name=u"学员")
	record_choices = (
		('checked', u"已签到"),
		('late', u"迟到"),
		('noshow', u"缺勤"),
		('leave_early', u"早退"),
	)
	record = models.CharField(u"上课纪录", choices=record_choices, default="checked", max_length=64)
	score_choices = (
		(100, 'A+'),
		(90, 'A'),
		(85, 'B+'),
		(80, 'B'),
		(70, 'B-'),
		(60, 'C+'),
		(50, 'C'),
		(40, 'C-'),
		(0, 'D'),
		(-1, 'N/A'),
		(-100, 'COPY'),
		(-1000, 'FAIL'),
	)
	score = models.IntegerField("本节成绩", choices=score_choices, default=-1)
	date = models.DateTimeField(auto_now_add=True)
	note = models.CharField("备注", max_length=255, blank=True, null=True)

	color_dic = {
		100: "#5DFC70",
		90: "yellowgreen",
		85:  "deepskyblue",
		80: "#49E3F5",
		70: "#1CD4C8",
		60: "#FFBF00",
		50: "#FF8000",
		40: "#FE642E",
		0: "red",
		-1: "#E9E9E9",
		-100: "#585858",
		-1000: "darkred"
	}

	def __str__(self):
		return "{},学员:{},纪录:{}, 成绩:{}".format(self.course_record, self.student.name, self.record, self.get_score_display())

	class Meta:
		verbose_name = '学员学习纪录'
		verbose_name_plural = "学员学习纪录"
		unique_together = ('course_record', 'student')

	def colored_record(self):
		color_dic = {
			'checked': "#5DFC70",
			'late': "#FFBF00",
			'noshow': "#B40404",
			'leave_early': "#FFFF00",
		}
		html_td = '<span style="padding:5px;background-color:%s;">%s</span>' %(
			color_dic[self.record],self.get_record_display()
		)
		return html_td

	def colored_score(self):
		html_td = '<span style="padding:5px;background-color:%s;">%s</span>' %(
			self.color_dic[self.score],self.score
	)
		return html_td

	colored_score.allow_tags = True
	colored_record.allow_tags = True
	colored_score.short_description = u'成绩'
	colored_record.short_description = u'签到情况'


class PaymentRecord(models.Model):
	customer = models.ForeignKey(Customer, verbose_name=u"客户")
	course = models.CharField(u"课程名", choices=course_choices, max_length=64)
	class_type = models.CharField(u"班级类型", choices=class_type_choices, max_length=64)
	pay_type_choices = (
		('deposit', u"订金/报名费"),
		('tution', u"学费"),
		('refund', u"退款"),
	)
	pay_type = models.CharField(u"费用类型", choices=pay_type_choices, max_length=64, default="deposit")
	paid_fee = models.IntegerField(u"费用数额", default=0)
	note = models.TextField(u"备注", blank=True, null=True)
	date = models.DateTimeField(u"交款日期", auto_now_add=True)
	consultant = models.ForeignKey(UserProfile, verbose_name=u"负责老师", help_text=u"谁签的单就选谁")

	def __str__(self):
		return u"{}, 类型:{},数额:{}".format(self.customer, self.pay_type, self.paid_fee)

	class Meta:
		verbose_name = u'交款纪录'
		verbose_name_plural = u"交款纪录"
