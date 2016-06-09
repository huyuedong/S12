#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


import os

os.environ["DJANGO_SETTINGS_MODULE"] = "s12bbs.settings"

import django
import bbs

django.setup()

from bbs import models
from django.db.models import F, Q, Count, Sum, aggregates


obj = models.Article.objects.get(id=1)
# print(obj.comment_set.filter(comment_type=1))
# print(obj.comment_set.filter(comment_type=2).count())
# models.Article.objects.annotate(t_n=Count(Q("comment_set"), Q(comment_type=1)))
# p = models.Article.objects.annotate(t_n=Count("comment")).filter(comment__comment_type=2)
# print(p[0], p[0].t_n)

# p1 = models.Article.objects.filter(comment__comment_type=2).annotate(c_n=Count("comment"))
# p1 = models.Article.objects.all().values("comment__comment_type").annotate(c_n=Count("comment"))
# print("文章：《{}》 点赞数：{}".format(p1[0], p1[0].c_n))

print(obj)

# article_list = models.Article.objects.filter(category_id=1, status='published').filter(comment__comment_type=1).annotate(c_n=Count("comment"))


# def get_comment(article_obj):
# 	models.Comment.objects.filter(article_id=article_obj.id).values('comment_type').annotate(commnum=Count('*'))
# 	print("Count:", common_counts)
# 	for c in commmon_counts:
# 		if c["comment_type"] == 1:
# 			common_count = c["commnum"]
# 		else:
# 			thumb_count = c["commnum"]
# 		commons = {
# 			"comment_count": common_count,
# 			"thumb_count": thumb_count,
# 		}
# 	return commons


# common_counts = models.Comment.objects.filter(article_id=1).values('comment_type').annotate(commnum=Count('*'))
# print("Count:", common_counts)

# comment_counts = models.Comment.objects.all().values("article_id", "comment_type").annotate(comm_num=Count("*"))
print(obj.comment_set.select_related().annotate(comment_num=Count("article__comment__comment_type")))
comment_counts = obj.comment_set.select_related().annotate(comment_num=Count("article__comment__comment_type"))
obj = models.Article.objects.all().values("comment__comment_type").annotate(c_n=Count("comment"))
print(obj)
p1 = models.Article.objects.get(id=1)


