from django import template
import calendar
from datetime import date, timedelta
from competitions.models import Event

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
            day_events = [event for event in self.events if event.start_time.date() <= today <= event.end_time.date()]
            event_links = ''.join(f'<div><a href="{event.get_absolute_url()}">{event.title}</a></div>' for event in day_events)

            return f'<td class="{self.cssclasses[weekday]}">{day}{event_links}</td>'
    
    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join('<th class="%s">%s</th>' % (self.cssclasses[i], calendar.weekheader(3)[i]) for i in range(7))
        return '<tr class="days">%s</tr>' % s

@register.simple_tag
def month_calendar(year, month, events):
    cal = EventCalendar(events, year, month)
    html_calendar = cal.formatmonth(year, month)
    html_calendar = html_calendar.replace('<table', '<table class="calendar"')
    
    return html_calendar

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
