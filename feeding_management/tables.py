import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import FeedingChart

class HorseLinkColumn(tables.Column):
    def render(self, value, record):
        url = reverse('horse_profile', kwargs={'horse_id': record.horse.id})
        return format_html('<a href="{}">{}</a>', url, value)

class FeedingChartTable(tables.Table):
    horse = HorseLinkColumn(verbose_name="Horse Name", accessor='horse.name')
    breakfast = tables.Column(accessor='get_breakfast_info', verbose_name="Breakfast")
    lunch = tables.Column(accessor='get_lunch_info', verbose_name="Lunch")
    dinner = tables.Column(accessor='get_dinner_info', verbose_name="Dinner")
    hay = tables.Column(accessor='get_hay_info', verbose_name="Hay")
    supplements = tables.Column(accessor='supplements', verbose_name="Supplements")
    medicines = tables.Column(accessor='medicines', verbose_name="Medicines")
    notes = tables.Column(accessor='notes', verbose_name="Notes")

    class Meta:
        model = FeedingChart
        template_name = "django_tables2/bootstrap5.html" 
        fields = []