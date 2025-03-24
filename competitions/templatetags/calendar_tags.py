from django import template
import calendar
from datetime import date, timedelta
from competitions.models import Event
from django.utils.html import format_html


register = template.Library()


class EventCalendar(calendar.HTMLCalendar):
    def __init__(self, events, year, month):
        super().__init__()
        self.events = events
        self.year = year
        self.month = month

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            today = date(self.year, self.month, day)
            day_events = [
                event for event in self.events
                if event.start_time.date() <= today <= event.end_time.date()
            ]

            event_links = ''.join(
                f'<div class="month-view">'
                f'<a href="{event.get_absolute_url()}" class="event-link">'
                f'<span class="event-text">{event.title}</span>'
                f'<i class="fas fa-trophy event-icon"></i>'
                f'</a>'
                + (
                    f' <i class="fas fa-heart" style="color: red;"></i>'
                    if getattr(event, 'is_favorited', False)
                    else ''
                )
                + '</div>'
                for event in day_events
            )

            return (
                f'<td class="{self.cssclasses[weekday]}">'
                f'{day}{event_links}</td>'
            )

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        s = ''.join(
            f'<th class="{day.lower()}">{day}</th>' for day in weekdays
        )
        return f'<tr class="days">{s}</tr>'


@register.simple_tag
def month_calendar(year, month, events):
    cal = EventCalendar(events, year, month)
    week_header = " "
    html_calendar = cal.formatmonth(year, month)
    html_calendar = html_calendar.replace(
        '<table border="0" cellpadding="0" cellspacing="0" class="month">',
        f'<table class="calendar">{week_header}'
    )
    return html_calendar


@register.simple_tag
def current_day():
    today = date.today()
    return today.day


@register.simple_tag
def weekly_events(year, month, day):
    start_date = date(year, month, day)
    end_date = start_date + timedelta(days=6)
    events = Event.objects.filter(
        start_time__date__range=[start_date, end_date]
    )
    return events


@register.simple_tag
def daily_events(year, month, day):
    current_date = date(year, month, day)
    events = Event.objects.filter(start_time__date=current_date)
    return events
