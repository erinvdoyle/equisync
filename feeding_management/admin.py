from django.contrib import admin
from .models import FeedingChart


class FeedingChartAdmin(admin.ModelAdmin):
    list_display = ('horse', 'breakfast_feed', 'lunch_feed', 'dinner_feed', 'hay', 'supplements', 'medicines', 'notes')
    

admin.site.register(FeedingChart, FeedingChartAdmin)
