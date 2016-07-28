#_*_coding:utf-8_*_
__author__ = 'Alex Li'
from django.conf.urls import url, include
from rest_framework import  routers

from Sansa import rest_views

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'assets', rest_views.AssetViewSet)
router.register(r'manufactories', rest_views.ManufactoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]