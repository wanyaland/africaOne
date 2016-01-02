from django.conf.urls import patterns,url
from core.views import *


urlpatterns = patterns('',
                       url(r'^$',index,name='home'),
                       )