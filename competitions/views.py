from django.shortcuts import render, redirect
from .models import Event
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from competitions.models import Event
from datetime import date, timedelta


def calendar_view(request, year=None, month=None):
    today = date.today()
    year = int(year) if year else today.year
    month = int(month) if month else today.month
    return render(request, 'competitions/calendar.html', {'year': year, 'month': month, 'view_type': 'month'})

def week_view(request, year, month, day):
    current_date = date(year, month, day)
    return render(request, 'competitions/calendar.html', {'year': year, 'month': month, 'day': day, 'view_type': 'week'})

def day_view(request, year, month, day):
    current_date = date(year, month, day)
    return render(request, 'competitions/calendar.html', {'year': year, 'month': month, 'day': day, 'view_type': 'day'})

@login_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        event = Event.objects.create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            created_by=request.user
        )
        return redirect('competitions:calendar_view')

    return render(request, 'competitions/add_event.html')

@login_required
def favorite_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        if request.user in event.favorited_by.all():
            event.favorited_by.remove(request.user)
        else:
            event.favorited_by.add(request.user)

        return redirect('competitions:calendar_view')

    return HttpResponseForbidden("Method not allowed")

@login_required
def event_detail(request, event_id):
  event = get_object_or_404(Event, id=event_id)
  return render(request, 'competitions/event_detail.html', {'event': event})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.start_time = request.POST.get('start_time')
        event.end_time = request.POST.get('end_time')
        event.approved = False
        event.save()
        return redirect('competitions:event_detail', event_id=event.id)

    context = {
        'event': event,
    }
    return render(request, 'competitions/edit_event.html', context)

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('competitions:calendar_view')

    return render(request, 'competitions/calendar_view')
