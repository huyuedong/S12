#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django.conf.urls import url
from testapp import views


urlpatterns = [
	url(r'^$', views.test),
]