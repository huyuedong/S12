#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
import os
from django.db.models import aggregates
# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=255)
	brief = models.CharField(null=True, blank=True, max_length=255)
	category = models.ForeignKey("Category")
	content = models.TextField(u"文章内容")
	author = models.ForeignKey("UserProfile")
	pub_date = models.DateTimeField(blank=True, null=True)
	last_modify = models.DateTimeField(auto_now=True)
	priority = models.IntegerField(u"优先级", default=1000)
	head_img = models.ImageField("文章图片", upload_to="uploads")
	status_choices = (
		('draft', u"草稿"),
		('published', u"已发布"),
		('hidden', u"隐藏"),
	)
	status = models.CharField(choices=status_choices, default='published', max_length=32)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "文章"
		verbose_name_plural = "文章"

	def clean(self):
		# Don't allow draft entries to have a pub_date.
		if self.status == 'draft' and self.pub_date is not None:
			raise ValidationError('草稿不能选择发布时间。')
		# Set the pub_date for published items if it hasn't been set already.
		if self.status == 'published' and self.pub_date is None:
			self.pub_date = datetime.date.today()

	def get_comments_num(self):  # 获取评论中的回复数
		return self.comment_set.filter(comment_type=1).count()

	def get_thumbs_up_num(self):  # 获取评论中的点赞数
		return self.comment_set.filter(comment_type=2).count()


class Comment(models.Model):
	article = models.ForeignKey(Article, verbose_name="所属文章")
	parent_comment = models.ForeignKey('self', related_name='my_children', blank=True, null=True)
	comment_choices = (
		(1, u'评论'),
		(2, u"点赞")
	)
	comment_type = models.IntegerField(choices=comment_choices, default=1)
	user = models.ForeignKey("UserProfile")
	comment = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	# 调用模型的save() 方法时不会引起clean() 方法的调用。
	def clean(self):
		if self.comment_type == 1 and not self.comment:
			raise ValidationError(u'评论内容不能为空，sb')

	def __str__(self):
		if self.parent_comment:
			return "{}-->P:{}-->{}".format(self.article, self.parent_comment.id, self.comment)
		else:
			return "{}-->{}".format(self.article, self.comment)

	class Meta:
		verbose_name = "评论/点赞"
		verbose_name_plural = "评论/点赞"


class Category(models.Model):
	name = models.CharField(max_length=64, unique=True)
	brief = models.CharField(null=True, blank=True, max_length=255)
	set_as_top_menu = models.BooleanField(default=False)
	position_index = models.SmallIntegerField()
	admins = models.ManyToManyField("UserProfile", blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "版块"
		verbose_name_plural = "版块"


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=32)
	signature = models.CharField(max_length=255, blank=True, null=True)
	head_img = models.ImageField(upload_to="uploads", blank=True, null=True)

	def get_head_img(self):
		return "/static/{}".format(str(self.head_img).split("/")[-1])

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = "用户"
