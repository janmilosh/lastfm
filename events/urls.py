from django.conf.urls import include, patterns, url

urlpatterns = patterns('events.views',
    url(r'^set_location/$', 'set_location'),
    url(r'^get_events/(?P<location_id>\d+)/$', 'get_events'),
    url(r'^get_artist/(?P<artist>[-\w]+)/(?P<location_id>\d+)/$', 'get_artist'),
    url(r'^delete/(?P<location_id>\d+)/$', 'delete'),
)