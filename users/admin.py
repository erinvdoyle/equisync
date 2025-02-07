from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileInline(admin.StackedInline):  
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'  

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login') 
    list_filter = ('is_staff', 'is_superuser', 'is_active')  
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(get_user_model())  
admin.site.register(get_user_model(), CustomUserAdmin)
