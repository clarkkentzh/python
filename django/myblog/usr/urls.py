#coding=utf-8

from django.conf.urls import url
from usr.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^search_form/$', search_form),
    url(r'^form_post/$', form_post),
    url(r'^form_post/thanks/$', thanks),
    url(r'^request/$', get_request),
    url(r'^formtest/$', formtest),
    url(r'^authorform/$', authorset),
]

###cookie  session
# urlpatterns += [
#     url(r'^login/$', login),
#     url(r'^index1/$', index),
#     url(r'^logout/$', logout),
# ]

###register login logout

urlpatterns += [
    url(r'^reg/$',reg, name="reg"),
    url(r'^login/$',login, name="login"),
    url(r'^logout/$',logout, name="logout"),
    url(r'^login_test/$', login_test,name = "login_test"),
    url(r'^thanks/$', thanks),
    url(r'^avatar/$', avatar),
]

urlpatterns += [
    url(r'^page/$', page),
    url(r'^avatar/$', avatar),
    url(r'^article/$', article),
    url(r'^upload/(?P<dir_name>[^/]+)$',upload),
]

urlpatterns += [
    url(r'^cache/$', cache),
]
