from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'lastfm.views.login'),
    url(r'^auth/$', 'lastfm.views.auth_view'),
    url(r'^logout/$', 'lastfm.views.logout'),
    url(r'^loggedin/$', 'lastfm.views.loggedin'),
    url(r'^invalid/$', 'lastfm.views.invalid_login'),
    url(r'^register/$', 'lastfm.views.register_user'),
    url(r'^register_success/$', 'lastfm.views.register_success'),
    url(r'^$', 'lastfm.views.home', name='home'),
    url(r'^events/', include('events.urls')),
)
