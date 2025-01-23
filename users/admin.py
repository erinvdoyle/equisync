from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from community.announcements.models import Announcement
from community.ads.models import Ad

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ("username", "password")
    inlines = [ProfileInline]

class AdAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'user', 'date_posted', 'approved') 
    list_filter = ('ad_type', 'approved')  
    search_fields = ('description', 'contact_info')

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted')  
    search_fields = ('description', 'contact_info')  

admin.site.unregister(User)  
admin.site.register(User, UserAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Announcement, AnnouncementAdmin)

