from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    (r'^$', views.index),
	(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^board/', include('board.urls')),
	url(r'^catalog/', include('catalog.urls')),
	url(r'^burse/', include('burse.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
