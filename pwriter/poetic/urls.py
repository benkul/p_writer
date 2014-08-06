from django.conf.urls import patterns, url

from poetic import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),

                       url(r'^logout/$', views.user_logout, name='user_logout'),
                       url(r'^(?P<username>\w+)/$', views.user_profile, name='user_profile'),
                       url(r'^(?P<username>\w+)/(?P<title_slug>\w+)', views.get_poem, name='get_poem'),
                       )