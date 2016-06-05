from django.db import models
from django.utils.html import format_html

# Create your models here.


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "出版社"


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta:
		verbose_name_plural = "作者"


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_Date = models.DateField()
	status_choice = (
		("published", "已出版"),
		("producing", "待出版"),
		("forbidden", "禁书"),
	)
	status = models.CharField(choices=status_choice, max_length=32, default="producing")

	def colored_status(self):
		"""
		在前端给状态字段根据不同状态添加不同的背景色
		Django 1.7之后需要format_html将字符串渲染一下
		用该函数名（colored_status）替换在model Admin中list_display中的status即可。
		:return:
		"""
		global format_td
		if self.status == "published":
			format_td = format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已出版</span>')
		elif self.status == "producing":
			format_td = format_html('<span style="padding:2px;background-color:pink;color:white">待出版</span>')
		elif self.status == "forbidden":
			format_td = format_html('<span style="padding:2px;background-color:orange;color:white">禁书</span>')
		return format_td

	colored_status.short_description = "状态"

	def __str__(self):
		return "《{}》".format(self.title)

	class Meta:
		verbose_name_plural = "书名"
