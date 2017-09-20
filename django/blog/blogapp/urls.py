#coding=utf-8

from django.conf.urls import url
from blogapp.views import *


urlpatterns = [
    url(r'^page/$',mainpage,{"datas":""}),
    url(r'^page/all/$', mainpage,{"datas":1}),
    url(r'^page/sces/$', mainpage,{"datas":2}),
    url(r'^page/travel/$', mainpage,{"datas":3}),
    url(r'^myself/$',myself),
    url(r'^write/$', write),
    url(r'^look/$', look),
    url(r'^$',login),
    url(r'^reg/$', reg),
    url(r'^logout/$',logout),
]
