import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import FeedingChart


class HorseLinkColumn(tables.Column):
    def render(self, value, record):
        url = reverse(
            'feeding_management:horse_feeding_chart_readonly',
            kwargs={'horse_id': record.horse.id}
        )
        return format_html(
            '<a href="{}" class="horse-name-link">{}</a>',
            url,
            value
        )


class FeedingChartTable(tables.Table):
    horse = HorseLinkColumn(
        verbose_name="Horse",
        accessor='horse.name',
        orderable=False
    )
    breakfast = tables.Column(
        accessor='get_breakfast_info',
        verbose_name="Breakfast",
        orderable=False
    )
    lunch = tables.Column(
        accessor='get_lunch_info',
        verbose_name="Lunch",
        orderable=False
    )
    dinner = tables.Column(
        accessor='get_dinner_info',
        verbose_name="Dinner",
        orderable=False
    )
    hay = tables.Column(
        accessor='get_hay_info',
        verbose_name="Hay",
        orderable=False
    )
    supplements = tables.Column(
        accessor='supplements',
        verbose_name="Supplements",
        orderable=False
    )
    medicines = tables.Column(
        accessor='medicines',
        verbose_name="Medicines",
        orderable=False
    )
    notes = tables.Column(
        accessor='notes',
        verbose_name="Notes",
        orderable=False
    )

    class Meta:
        model = FeedingChart
        template_name = "django_tables2/bootstrap5.html"
        fields = []


class HorseLinkColumn(tables.Column):
    def render(self, value, record):
        url = reverse(
            'horses:horse_profile',
            kwargs={'horse_id': record.horse.id}
        )
        return format_html(
            '<a href="{}" class="horse-name-link">{}</a>',
            url,
            value
        )

