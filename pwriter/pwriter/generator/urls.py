from django.conf.urls import patterns, url

from generator import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )