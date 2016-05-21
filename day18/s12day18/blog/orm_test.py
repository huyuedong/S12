#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
orm 脚本
"""

import os

os.environ["DJANGO_SETTINGS_MODULE"] = "s12day16.settings"
import django
django.setup()

from blog import models

entry = models.Entry.objects.get(pk=1)
print(entry)

# # 创建一个作者
# alex = models.Author.objects.create(name="Alex")
# # 为entry:111添加作者：alex
# entry.authors.add(alex)
# entry.save()
#
# # 多对多对象
# john = models.Author.objects.create(name="John")
# Paul = models.Author.objects.create(name="Paul")
# George = models.Author.objects.create(name="George")
# Ringo = models.Author.objects.create(name="Ringo")
# entry2 = models.Entry.objects.get(pk=3)
# print(entry2)
# entry2.authors.add(john, Paul, George, Ringo)
# entry2.save()
# from django.db import connection
# print(connection.queries)
# print(dir(entry))

from django.db.models import F, Q

# objs = models.Entry.objects.filter(n_comments__lt=F('n_pingbacks'))
# objs = models.Entry.objects.filter(Q(Q(n_comments__gt=F('n_pingbacks')) | Q(pub_date__lt="2016-05-12")))

from django.db.models import Avg, Sum, Min, Max, Count
print(models.Entry.objects.all().aggregate(
	Avg("n_pingbacks"),
	Sum("n_pingbacks"),
	Min("n_pingbacks"),
	Max("n_pingbacks"),
	Count("n_pingbacks")
))

from app01 import models as book_models
pub_obj = book_models.Publisher.objects.last()
# 反响查询，book是反向外键的表明，select_related()把所有字段都取出来
print(pub_obj.name, pub_obj.book_set.select_related())

# 自定义一个聚合属性book_nums
pub_objs = book_models.Publisher.objects.annotate(book_nums=Count("book"))

for publisher in pub_objs:
	print(publisher.book_nums)

# print(objs)


