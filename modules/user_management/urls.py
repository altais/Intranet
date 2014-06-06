#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

urlpatterns = patterns('user_management.views',
	url(r'^login/$', login,{'template_name':'user/login.html'}),
	url(r'^logout/$', logout, {'next_page':'/user/login/'}),
	url(r'^succes/$',TemplateView.as_view(template_name="user/succes.html")),
	url(r'^register/$', 'create_account'),
)