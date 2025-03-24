from django.contrib import admin
from .announcements.models import Announcement
from .ads.models import Ad
from .models import CommunityEvent
from shared.admin_actions import approve_selected

try:
    from PIL import Image
except ImportError as e:
    import logging
    logging.error(f"PIL could not be imported: {e}")


class AdAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'user', 'date_posted', 'approved')
    list_filter = ('ad_type', 'approved')
    search_fields = ('description', 'contact_info')
    actions = [approve_selected]


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted')
    search_fields = ('description', 'contact_info')
    actions = [approve_selected]


@admin.register(CommunityEvent)
class CommunityEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_by', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('title', 'description')
    actions = [approve_selected]


admin.site.register(Ad, AdAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
