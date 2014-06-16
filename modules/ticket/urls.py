from django.conf.urls import patterns, url

urlpatterns = patterns('ticket.views',
    url(r'^$', 'ticket'),
)