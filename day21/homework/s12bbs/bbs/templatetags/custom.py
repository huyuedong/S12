#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

from django import template
from django.utils.html import format_html
from _datetime import datetime, timezone

register = template.Library()


@register.filter
def truncate_url(img_obj):
    return img_obj.name.split("/", maxsplit=1)[-1]


@register.simple_tag
def filter_comment(article_obj):
    """
    用来统计文章有多少评论、多少赞
    :param article_obj:
    :return:
    """
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments


@register.filter
def readable_date(pub_date):
    current_date = datetime.now(timezone.utc)  # 获得UTC时间,方便比较
    diff_date = current_date - pub_date
    total_seconds = diff_date.total_seconds()
    if total_seconds >= 86400:
        time_interval = str(int(divmod(total_seconds, 86400)[0])) + "天前"
    elif total_seconds >= 3600:
        time_interval = str(int(divmod(total_seconds, 3600)[0])) + "小时前"
    elif total_seconds >= 60:
        time_interval = str(int(divmod(total_seconds, 60)[0])) + "分钟前"
    else:
        time_interval = "刚刚"
    return time_interval
