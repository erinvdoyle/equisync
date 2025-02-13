from django.contrib import admin
from .announcements.models import Announcement 
from .ads.models import Ad
from .models import CommunityEvent

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

@admin.register(CommunityEvent)
class CommunityEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_by', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('title', 'description')
    actions = ['approve_events']

    @admin.action(description='Approve selected events')
    def approve_events(self, request, queryset):
        queryset.update(approved=True)