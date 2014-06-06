#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',login_required(TemplateView.as_view(template_name="user/dashboard.html"))),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user_management.urls')),
    url(r'^user/profile/$',login_required(TemplateView.as_view(template_name="user/dashboard.html"))),
    url(r'^forum/', include('forum.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^projects/', include('projects.urls')),
)
