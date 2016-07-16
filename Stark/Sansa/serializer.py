#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
序列化
"""

from Sansa import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.UserProfile
		fields = ("url", "email", "name", "is_staff")


class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Asset
		depth = 2  # 查两层
		fields = ("url", "sn", "asset_type", "manufactory", "name", "create_date")


class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Manufactory
		fields = ("url", "manufactory", "support_phone", "memo")

