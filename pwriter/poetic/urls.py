from django.conf.urls import patterns, url

from poetic import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='user_logout'),
                       url(r'^(?P<username>[0-9a-zA-Z\-\+@_\.]+)/$', views.user_profile, name='user_profile'),
                       url(r'^(?P<username>[0-9a-zA-Z\-\+@_\.]+)/(?P<title_slug>[0-9a-zA-Z\-\+@_\.]+)/$',
                           views.retrieve_poem, name='retrieve_poem'),
                       url(r'^(?P<username>[0-9a-zA-Z\-\+@_\.]+)/(?P<title_slug>[0-9a-zA-Z\-\+@_\.]+)/delete/$',
                           views.delete_poem, name='delete_poem'),
                       )