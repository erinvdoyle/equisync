from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventHorse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date, timedelta, datetime
from django.db.models import Q
from django.core.paginator import Paginator
import calendar
from django.urls import reverse
from django.utils import timezone
from horses.models import HorseProfile
from competitions.utils import create_notifications_for_past_events
from notifications.models import Notification
from django.http import JsonResponse
from django.contrib import messages


@login_required
def calendar_view(request, year=None, month=None):
    if request.GET.get('from') == 'horse_profile':
        user_horses = HorseProfile.objects.filter(
            Q(owner=request.user) | Q(staff=request.user) | Q(barn_manager=request.user) | Q(rider=request.user)
        ).distinct()
        has_event_results = EventHorse.objects.filter(horse__in=user_horses).exists()
        if not has_event_results:
            messages.success(request, "Register your horse here.")

    today = timezone.now().date()
    year = int(year) if year else today.year
    month = int(month) if month else today.month

    show_archived = request.GET.get('archived', False) == 'true'
    search_term = request.GET.get('search', '')

    if month == 1:
        prev_year, prev_month = year - 1, 12
    else:
        prev_year, prev_month = year, month - 1

    if month == 12:
        next_year, next_month = year + 1, 1
    else:
        next_year, next_month = year, month + 1

    events = Event.objects.filter(start_time__year=year, start_time__month=month, approved=True, is_archived=False)
    if show_archived:
        events = Event.objects.filter(is_archived=True)

    if search_term:
        events = events.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        for event in events:
            event.is_favorited = request.user in event.favorited_by.all()

    context = {
        'year': year,
        'month': month,
        'view_type': 'month',
        'page_obj': page_obj,
        'show_archived': show_archived,
        'search_term': search_term,
        'events': events,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'today': today,
        'day': 1,
    }

    if request.user.is_authenticated:
        user_event = Event.objects.filter(created_by=request.user).first()
        context['user_has_events'] = bool(user_event)
        if user_event:
            context['user_event'] = user_event

    return render(request, 'competitions/calendar.html', context)

def week_view(request, year, month, day):
    today = timezone.now().date()
    current_date = date(year=int(year), month=int(month), day=int(day))
    start_date = current_date - timedelta(days=current_date.weekday())
    end_date = start_date + timedelta(days=6)

    search_term = request.GET.get('search', '')

    events = Event.objects.filter(start_time__range=[start_date, end_date], approved=True)

    if search_term:
        events = events.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

    week_days = []
    for i in range(7):
        current_day = start_date + timedelta(days=i)
        events_for_day = Event.objects.filter(
            start_time__date__lte=current_day,
            end_time__date__gte=current_day,
            approved=True
        )
        if search_term:
            events_for_day = events_for_day.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

        if request.user.is_authenticated:
            for event in events_for_day:
                event.is_favorited = request.user in event.favorited_by.all()

        week_days.append({
            'date': current_day,
            'events': events_for_day,
        })

    prev_week_start = start_date - timedelta(days=7)
    next_week_start = start_date + timedelta(days=7)

    prev_year, prev_month, prev_day = prev_week_start.year, prev_week_start.month, prev_week_start.day
    next_year, next_month, next_day = next_week_start.year, next_week_start.month, next_week_start.day

    context = {
        'year': year,
        'month': month,
        'day': day,
        'view_type': 'week',
        'week_days': week_days,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'prev_day': prev_day,
        'next_year': next_year,
        'next_month': next_month,
        'next_day': next_day,
        'search_term': search_term,
        'today': today,
    }
    
    if request.user.is_authenticated:
        user_event = Event.objects.filter(created_by=request.user).first()
        if user_event:
            context['user_has_events'] = True
            context['user_event'] = user_event
        else:
            context['user_has_events'] = False

    return render(request, 'competitions/week_calendar.html', context)

def day_view(request, year, month, day):
    today = timezone.now().date()
    current_date = date(year=int(year), month=int(month), day=int(day))

    search_term = request.GET.get('search', '')

    events = Event.objects.filter(
        start_time__date__lte=current_date,
        end_time__date__gte=current_date,
        approved=True
    )

    if search_term:
        events = events.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

    if request.user.is_authenticated:
        for event in events:
            event.is_favorited = request.user in event.favorited_by.all()

    prev_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    prev_year, prev_month, prev_day = prev_date.year, prev_date.month, prev_date.day
    next_year, next_month, next_day = next_date.year, next_date.month, next_date.day
    
    try:
        display_date = date(year, month, day)
    except ValueError:
        display_date = date(year, month, 1)

    context = {
        'year': year,
        'month': month,
        'day': day,
        'view_type': 'day',
        'events': events,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'prev_day': prev_day,
        'next_year': next_year,
        'next_month': next_month,
        'next_day': next_day,
        'search_term': search_term,
        'today': today,
        'display_date': display_date,
    }
    
    if request.user.is_authenticated:
        user_event = Event.objects.filter(created_by=request.user).first()
        if user_event:
            context['user_has_events'] = True
            context['user_event'] = user_event
        else:
            context['user_has_events'] = False

    return render(request, 'competitions/day_calendar.html', context)


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
        
        messages.success(request, "Your event has been submitted for approval")
        
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

    if request.method == 'POST':
        horse_ids = request.POST.getlist('horses')

        for horse_id in horse_ids:
            class_details = request.POST.get('class_details')
            notes = request.POST.get('notes')
            horse = get_object_or_404(HorseProfile, id=horse_id)

            EventHorse.objects.update_or_create(
                event=event,
                horse=horse,
                defaults={
                    'class_details': class_details,
                    'notes': notes,
                }
            )
        
        return redirect('competitions:event_detail', event_id=event.id)

    user_horses = HorseProfile.objects.filter(owner=request.user)
    event_horses_data = EventHorse.objects.filter(event=event)

    context = {
        'event': event,
        'user_horses': user_horses,
        'event_horses_data': event_horses_data,
    }

    return render(request, 'competitions/event_detail.html', context)

@login_required
def edit_event(request):
    upcoming_events = Event.objects.filter(start_time__gte=timezone.now(), created_by=request.user)
    event = None

    event_id = request.POST.get('event_id') or request.GET.get('event_id')
    if event_id:
        event = get_object_or_404(Event, id=event_id, created_by=request.user)

    if request.method == 'POST' and event:
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.start_time = request.POST.get('start_time')
        event.end_time = request.POST.get('end_time')
        event.approved = False
        event.save()

        messages.success(request, "Your event has been edited")
        return redirect('competitions:event_detail', event_id=event.id)

    context = {
        'event': event,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'competitions/edit_event.html', context)

def get_event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event_data = {
        "title": event.title,
        "description": event.description,
        "start_time": event.start_time.strftime("%Y-%m-%dT%H:%M"),
        "end_time": event.end_time.strftime("%Y-%m-%dT%H:%M"),
    }
    return JsonResponse(event_data)

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Your event was deleted")
        return redirect('competitions:calendar_view')

    return redirect('competitions:edit_event') 

def events_json(request):
    events = Event.objects.filter(approved=True)
    data = [{'title': event.title,
             'start': event.start_time.isoformat(),
             'end': event.end_time.isoformat(),
             'url': reverse('competitions:event_detail', args=[event.id])} for event in events]
    
    return JsonResponse(data, safe=False)

# @login_required
# def edit_event_horse(request, event_horse_id, source='event_detail'):
#     event_horse = get_object_or_404(EventHorse, id=event_horse_id)

#     if request.method == 'POST':
#         event_horse.class_details = request.POST.get('class_details')
#         event_horse.notes = request.POST.get('notes')
#         jump_height_value = request.POST.get('jump_height')

#         if jump_height_value and jump_height_value != "Other":
#             try:
#                 event_horse.jump_height = float(jump_height_value.replace('m', '').replace('cm', '').strip())
#                 event_horse.jump_height_str = jump_height_value
#             except ValueError:
#                 event_horse.jump_height = None
#                 event_horse.jump_height_str = None

#         number_of_faults_value = request.POST.get('number_of_faults')
        
#         if number_of_faults_value.isdigit():
#             event_horse.number_of_faults = int(number_of_faults_value)
#         else:
#             event_horse.number_of_faults = None

#         if source == 'dashboard':
#             event_horse.results = request.POST.get('results')
#             event_horse.performance_rating = request.POST.get('performance_rating')

#         event_horse.save()
        
#         if source == 'dashboard':
#             notifications = Notification.objects.filter(event_horse=event_horse, user=request.user)
#             for notification in notifications:
#                 notification.read = True
#                 notification.save()

#         if source == 'dashboard':
#             return redirect('users:dashboard')
#         else:
#             return redirect('competitions:event_detail', event_id=event_horse.event.id)

#     context = {
#         'event_horse': event_horse,
#     }
#     return render(request, 'competitions/edit_event_horse.html', context)

@login_required
def edit_event_horse(request, event_horse_id):
    event_horse = get_object_or_404(EventHorse, id=event_horse_id)

    if request.method == 'POST':
        event_horse.class_details = request.POST.get('class_details', event_horse.class_details)
        event_horse.notes = request.POST.get('notes', event_horse.notes)
        event_horse.results = request.POST.get('results', event_horse.results)
        event_horse.performance_rating = request.POST.get('performance_rating', event_horse.performance_rating)

        jump_height_value = request.POST.get('jump_height')

        if jump_height_value and jump_height_value != "Other":
            try:
                event_horse.jump_height = float(jump_height_value.replace('m', '').replace('cm', '').strip())
                event_horse.jump_height_str = jump_height_value
            except ValueError:
                event_horse.jump_height = None
                event_horse.jump_height_str = None

        number_of_faults_value = request.POST.get('number_of_faults')
        if number_of_faults_value and number_of_faults_value.isdigit():
            event_horse.number_of_faults = int(number_of_faults_value)

        event_horse.save()

        return redirect('competitions:event_detail', event_id=event_horse.event.id)

    context = {
        'event_horse': event_horse,
    }
    return render(request, 'competitions/edit_event_horse.html', context)


@login_required
def remove_event_horse(request, event_horse_id):
    event_horse = get_object_or_404(EventHorse, id=event_horse_id)
    event_id = event_horse.event.id

    if request.method == 'POST':
        event_horse.delete()

        return redirect('competitions:event_detail', event_id=event_id)

    context = {
        'event_horse': event_horse,
    }
    return render(request, 'competitions/remove_event_horse.html', context)

@login_required
def horse_results_archive(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    results = EventHorse.objects.filter(horse=horse).order_by('-event__start_time')

    context = {
        'horse': horse,
        'results': results,
    }
    
    return render(request, 'competitions/horse_results_archive.html', context)

@login_required
def horse_performance(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    results = EventHorse.objects.filter(horse=horse).order_by("event__start_time")

    context = {
        "horse": horse,
        "results": results,
    }

    return render(request, "competitions/horse_results_archive.html", context)

@login_required
def mark_event_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return redirect('users:dashboard')