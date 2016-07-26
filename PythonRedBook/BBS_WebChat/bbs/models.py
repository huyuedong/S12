from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.


class Article(models.Model):
	title = models.CharField(u"标题", max_length=255)
	brief = models.CharField(u"摘要", max_length=255, null=True, blank=True)
	category = models.ForeignKey("Category")
	content = models.TextField(u"文章内容")
	author = models.ForeignKey("UserProfile")
	pub_date = models.DateTimeField(u"发布日期", null=True, blank=True)
	last_modify = models.DateTimeField(u"最后修改日期", auto_now=True)
	priority = models.IntegerField(u"优先级", default=1000)
	head_img = models.ImageField(u"文章图片", upload_to="articles")
	status_choices = (
		("draft", u"草稿"),
		("published", u"已发布"),
		("hidden", u"隐藏"),
	)
	status = models.CharField(choices=status_choices, default='published', max_length=32)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = u"文章"
		verbose_name_plural = verbose_name

	def clean(self):
		# 确保草稿不能有发布时间
		if self.status == "draft" and self.pub_date is not None:
			raise ValidationError(u"草稿不能有发布时间。")
		# 如果没有设置发布时间，默认就是当前的时间
		if self.status == "published" and self.pub_date is None:
			self.pub_date = datetime.date.today()


class Comment(models.Model):
	article = models.ForeignKey(Article, verbose_name=u"所属文章")
	parent_comment = models.ForeignKey(
		"self",
		related_name="my_children",  # 我的父评论通过'my_children'可以找到我
		verbose_name=u"父评论",  # 该字段适用于保存我的父评论是谁
		blank=True,
		null=True
	)
	comment_choices = (
		(1, u"评论"),
		(2, u"点赞")
	)
	comment_type = models.IntegerField(choices=comment_choices, default=1)
	user = models.ForeignKey("UserProfile", verbose_name=u'评论者')
	comment = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		if self.parent_comment:
			return u"文章:{}-->父评论:{}-->评论内容:{}".format(self.article, self.parent_comment.id, self.comment)
		else:
			return u"文章:{}-->评论内容:{}".format(self.article, self.comment)

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = u"评论/点赞"
		verbose_name_plural = verbose_name

	def clean(self):
		if self.comment_type == 1 and not self.comment:
			raise ValidationError(u"客官，评论内容不能为空哦！")


class Category(models.Model):
	name = models.CharField(max_length=64, unique=True)
	brief = models.CharField(null=True, blank=True, max_length=255)
	set_as_top_menu = models.BooleanField(default=False)
	position_index = models.SmallIntegerField()
	admins = models.ManyToManyField("UserProfile", blank=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = u"版块"
		verbose_name_plural = verbose_name


class UserProfile(models.Model):
	user = models.OneToOneField(User)  # 一对一关联至Django admin 默认的user表
	name = models.CharField(max_length=32)
	signature = models.CharField(max_length=255, blank=True, null=True)
	head_img = models.ImageField(upload_to="users", blank=True, null=True)
	friends = models.ManyToManyField("self", related_name="my_friends", blank=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = u"用户"
		verbose_name_plural = verbose_name
