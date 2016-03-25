from django.conf.urls import patterns,url
from . import views

urlpatterns = patterns('',
                       url(r'^$',views.BusinessList.as_view(),name='home'),
                       )
