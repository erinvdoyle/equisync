from django.contrib import admin
from .announcements.models import Announcement 
from .ads.models import Ad  

class AdAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'user', 'date_posted', 'approved')
    list_filter = ('ad_type', 'approved')
    search_fields = ('description', 'contact_info')

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted')
    search_fields = ('description', 'contact_info')

admin.site.register(Ad, AdAdmin)
admin.site.register(Announcement, AnnouncementAdmin)