from django.contrib import admin
from .models import FeedingChart


class FeedingChartAdmin(admin.ModelAdmin):
    list_display = (
        'horse',
        'breakfast_feed', 'lunch_feed', 'dinner_feed', 'hay',
        'supplements', 'medicines',
        'approved', 'last_updated_by'
    )
    list_filter = ('approved',)
    search_fields = (
        'horse__name', 'breakfast_feed',
        'lunch_feed', 'dinner_feed', 'supplements', 'medicines'
        )
    actions = ['approve_selected_plans']

    def approve_selected_plans(self, request, queryset):
        updated_count = queryset.update(approved=True)
        self.message_user(
            request, f"{updated_count} feeding plan(s) approved.")
    approve_selected_plans.short_description = "Approve selected feeding plans"


admin.site.register(FeedingChart, FeedingChartAdmin)