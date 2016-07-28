
from django.conf.urls import url,include
from  Robb import views

urlpatterns = [
    #url(r'report/$',views.asset_report),
    url(r'api/',include('Robb.rest_urls')),

]
