#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from Sansa import models
from Sansa import serializer
from rest_framework import serializers, viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializer.UserSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializer.AssetSerializer


class ManufactoryViewSet(viewsets.ModelViewSet):
    queryset = models.Manufactory.objects.all()
    serializer_class = serializer.ManufactorySerializer