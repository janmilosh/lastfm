from django.conf.urls import include, patterns, url

urlpatterns = patterns('events.views',
    url(r'^set_location/$', 'save_location'),
    url(r'^get_events/(?P<location_id>\d+)/$', 'get_events'),
)