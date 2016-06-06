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
print(obj.comment_set.filter(comment_type=1))
print(obj.comment_set.filter(comment_type=2).count())
# models.Article.objects.annotate(t_n=Count(Q("comment_set"), Q(comment_type=1)))
p = models.Article.objects.annotate(t_n=Count("comment")).filter(comment__comment_type=2)
print(p[0], p[0].t_n)

p1 = models.Article.objects.filter(comment__comment_type=2).annotate(c_n=Count("comment"))
print("文章：《{}》 点赞数：{}".format(p1[0], p1[0].c_n))

print(obj)

# article_list = models.Article.objects.filter(category_id=1, status='published').filter(comment__comment_type=1).annotate(c_n=Count("comment"))