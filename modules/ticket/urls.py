from django.conf.urls import patterns, url

urlpatterns = patterns('ticket.views',
    url(r'^$', 'ticket'),
    url(r'^new_post$', 'new_post'),
    url(r'^new_ticket$', 'new_ticket'),
    url(r'^close/(?P<id>\d+)$', 'close_ticket'),
	url(r'^(?P<id>\d+)$', 'view_ticket'),
)