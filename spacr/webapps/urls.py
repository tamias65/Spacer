from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^$', 'spacr.views.home_page', name='home'),

)
