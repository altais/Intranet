#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 

urlpatterns = patterns('user_profile.views',
    url(r"^/(\w+)/$", "list"),
    url(r"^/$", "list"),
)