from django.conf.urls import patterns,url
from . import views

urlpatterns = patterns('',
                       url(r'^$',views.BusinessList.as_view(),name='home'),
                       url(r'^create_business/$',views.BusinessCreate.as_view(),name='create_business'),
                       )
