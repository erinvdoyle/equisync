from django import template
import calendar
from datetime import date, timedelta
from competitions.models import Event

register = template.Library()

@register.simple_tag
def month_calendar(year, month):
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    return cal

@register.simple_tag
def current_day():
    today = date.today()
    return today.day

@register.simple_tag
def weekly_events(year, month, day):
    start_date = date(year, month, day)
    end_date = start_date + timedelta(days=6)
    events = Event.objects.filter(start_time__date__range=[start_date, end_date])
    return events

@register.simple_tag
def daily_events(year, month, day):
    current_date = date(year, month, day)
    events = Event.objects.filter(start_time__date=current_date)
    return events
