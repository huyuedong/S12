#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
restful views
"""

from Sansa import models
from Sansa import serializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
	queryset = models.UserProfile.objects.all()
	serializer_class = serializer.UserSerializer


class AssetViewSet(viewsets.ModelViewSet):
	queryset = models.Asset.objects.all()
	serializer_class = serializer.AssetSerializer


class ManufactoryViewSet(viewsets.ModelViewSet):
	queryset = models.Manufactory.objects.all()
	serializer_class = serializer.ManufactorySerializer
