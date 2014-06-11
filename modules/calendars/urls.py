#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 

urlpatterns = patterns('forum.views',
    url(r'^$',TemplateView.as_view(template_name="calendar/calendar.html")),
)