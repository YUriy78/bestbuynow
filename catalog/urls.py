from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
	(r'registration/(\d{1,})/$', views.reg_company),
	(r'index/$', views.catalog_index),
	(r'company/(\d{1,})/$', views.all_company ),
	(r'pagefirm/(\d{1,})/$', views.page_firm ),
	(r'firms/(\d{1,})/$', views.user_firms),
	(r'changefirm/(\d{1,})/(\d{1,})/$', views.change_firm ),
	
)
