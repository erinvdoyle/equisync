from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date, timedelta
from django.db.models import Q
from django.core.paginator import Paginator


def calendar_view(request, year=None, month=None):
    today = date.today()
    year = int(year) if year else today.year
    month = int(month) if month else today.month
    
    show_archived = request.GET.get('archived', False) == 'true'
    search_term = request.GET.get('search', '')

    if show_archived:
        events = Event.objects.filter(is_archived=True)
    else:
        events = Event.objects.filter(start_time__year=year, start_time__month=month, approved=True, is_archived=False)

    if search_term:
        events = events.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'competitions/calendar.html', {
        'year': year,
        'month': month,
        'view_type': 'month',
        'page_obj': page_obj,
        'show_archived': show_archived,
        'search_term': search_term,
        'events': events
    })

def week_view(request, year, month, day):
    current_date = date(year, month, day)
    start_date = current_date - timedelta(days=current_date.weekday())
    end_date = start_date + timedelta(days=6)
    events = Event.objects.filter(start_time__range=[start_date, end_date], approved=True)
    return render(request, 'competitions/calendar.html', {'year': year, 'month': month, 'day': day, 'view_type': 'week', 'events':events})

def day_view(request, year, month, day):
    current_date = date(year, month, day)
    events = Event.objects.filter(start_time__date=current_date, approved=True)
    return render(request, 'competitions/calendar.html', {'year': year, 'month': month, 'day': day, 'view_type': 'day', 'events':events})

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

def events_json(request):
    events = Event.objects.filter(approved=True)
    data = [{'title': event.title,
             'start': event.start_time.isoformat(),
             'end': event.end_time.isoformat(),
             'url': reverse('competitions:event_detail', args=[event.id])} for event in events]
    
    return JsonResponse(data, safe=False)