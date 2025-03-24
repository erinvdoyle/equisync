from django.contrib import admin
from .announcements.models import Announcement
from .ads.models import Ad
from .models import CommunityEvent
try:
    from PIL import Image
except ImportError as e:
    import logging
    logging.error(f"PIL could not be imported: {e}")



class AdAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'user', 'date_posted', 'approved')
    list_filter = ('ad_type', 'approved')
    search_fields = ('description', 'contact_info')
    actions = ['approve_ads']

    @admin.action(description='Approve selected ads')
    def approve_ads(self, request, queryset):
        queryset.update(approved=True)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted')
    search_fields = ('description', 'contact_info')
    actions = ['approve_announcements']

    @admin.action(description='Approve selected announcements')
    def approve_announcements(self, request, queryset):
        queryset.update(approved=True)


@admin.register(CommunityEvent)
class CommunityEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_by', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('title', 'description')
    actions = ['approve_events']

    @admin.action(description='Approve selected events')
    def approve_events(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Ad, AdAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
