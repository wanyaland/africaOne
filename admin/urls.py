from django.conf.urls import patterns,url
from core.views import *
from djangoratings.views import AddRatingFromModel


urlpatterns = patterns('',
                       url(r'^$',index,name='home'),
                       )
