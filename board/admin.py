from django.contrib import admin
from models import *

class PhotoInline(admin.TabularInline):
    model = Photo

class AdAdmin (admin.ModelAdmin):
	list_display = ('name', 'category', 'city', 'user', 'status', 'date')
	date_hierarchy = 'date'
	list_filter = ('status', 'priority')
	search_fields = ('name',)
	inlines = [
        PhotoInline,
    ]
	
class UserAdmin (admin.ModelAdmin):
	list_display = ('name', 'city', 'email', 'ip_user')
	search_fields = ('email',)
	
	
class ArtAdmin (admin.ModelAdmin):
	search_fields = ('title',)
	
class IconInline(admin.TabularInline):
    model = IconMainCategory
	
class MainCategoryAdmin(admin.ModelAdmin):
	inlines = [
        IconInline,
    ]
	

admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(User, UserAdmin)
admin.site.register(Feedback)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Ad, AdAdmin)
admin.site.register(Message)
admin.site.register(Photo)
admin.site.register(Description)
admin.site.register(Article, ArtAdmin)
admin.site.register(Verification)
admin.site.register(Subscription)
admin.site.register(IconMainCategory)

