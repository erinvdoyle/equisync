import django_tables2 as tables
from .models import FeedingChart

class FeedingChartTable(tables.Table):
    class Meta:
        model = FeedingChart
        template_name = "django_tables2/bootstrap5.html" # Or another template
        fields = ('horse', 'breakfast_feed', 'lunch_feed', 'dinner_feed', 'supplements', 'medicines', 'notes') # Specify the fields you want to display
