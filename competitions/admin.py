from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_by', 'approved')
    list_filter = ('approved', 'created_by')
    search_fields = ('title', 'description')
    actions = ['approve_events']

    def approve_events(self, request, queryset):
        queryset.update(approved=True)
    approve_events.short_description = "Approve selected events"