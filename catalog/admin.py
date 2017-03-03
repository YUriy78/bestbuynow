from django.contrib import admin
from models import *

class UserCompanyAdmin (admin.ModelAdmin):
	date_hierarchy = 'date'
	list_filter = ('status',)


admin.site.register(CategoryCompany)
admin.site.register(UserCompany, UserCompanyAdmin)


