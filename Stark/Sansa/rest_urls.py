#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
restful URL
"""

from django.conf.urls import url, include
from rest_framework import routers
from Sansa import rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'assets', rest_views.AssetViewSet)
router.register(r'manufactories', rest_views.ManufactoryViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth', include("rest_framework.urls", namespace="restful_framework"))
]
