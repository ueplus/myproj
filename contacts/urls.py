from django.conf.urls import patterns, include, url
from django.contrib import admin

from contacts import views
#import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.display, name='display'),
)
