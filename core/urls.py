from django.conf.urls import patterns,url
from core.views import *


urlpatterns = patterns('',
                       url(r'^$',index,name='home'),
                       url(r'^logout/',logout_view,name='logout'),
                       )