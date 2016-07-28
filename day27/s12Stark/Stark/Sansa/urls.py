
from django.conf.urls import url,include
from  Sansa import views

urlpatterns = [
    url(r'report/$',views.asset_report),
    url(r'api/',include('Sansa.rest_urls')),
    url(r'report/asset_with_no_asset_id/$',views.asset_with_no_asset_id,name='acquire_asset_id' ),
    url(r'^new_assets/approval/$',views.new_assets_approval,name="new_assets_approval" ),

    #url(r'asset/',include('Sansa.urls')),
]
