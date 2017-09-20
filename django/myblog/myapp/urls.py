#coding=utf-8

#这个文件可以自己创建


from django.conf.urls import url
from myapp.views import *
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^time/$', get_html),
    url(r'^jump/$', jump),
    url(r'^error/$', error),
#两种传参方式
    url(r'^argument/$', argument,{'a':1,'b':2}),
    url(r'^argument1/(\d{1,2})/(\d{1,2})/$', argument1),
]

urlpatterns += [
    url(r'^template/$',template),
    url(r'^tag/$', tag),
    url(r'^filter/$', filter),
    url(r'^extend/$', extend,name="extend"),
    url(r'^include/$', include),
    url(r'^static/$', static),
    url(r'^globa/$', globa),
]

#通用视图
urlpatterns += [
    url(r'^index/$',TemplateView.as_view(template_name="index.html")),
    url(r'^about/$', RedirectView.as_view(url="http://www.baidu.com")),
]

#数据操作
urlpatterns += [
    url(r'^add/(?P<table>author)/$', add_data),
    url(r'^add/(?P<table>book)/$', add_data),
    url(r'^add/(?P<table>publisher)/$', add_data),
    url(r'^del/$',del_data),
    url(r'^update/$', update_data),
    url(r'^select/$', select_data),
    url(r'^foreign/$', foreign),
    url(r'^sql/$', sql),
]
