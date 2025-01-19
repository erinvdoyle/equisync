from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ("username", "password")
    inlines = [ProfileInline]

admin.site.unregister(User)  
admin.site.register(User, UserAdmin)
