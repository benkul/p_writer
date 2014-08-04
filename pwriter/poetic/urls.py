from django.conf.urls import patterns, url

from poetic import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^(?P<username>\w+)/$', views.user_poems, name='user_poems'),
                       )