from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from community.announcements.models import Announcement
from community.ads.models import Ad

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Profile Information', {'fields': ('role', 'contact', 'notes', 'is_approved')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions') #add this back in

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password', 'role', 'contact', 'notes', 'is_approved')}
         ),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Override this method to use a special form during user creation
        """
        if obj is None:
            kwargs['form'] = UserCreationForm
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """
        Override this to properly save the new profile.
        """
        obj.save()

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