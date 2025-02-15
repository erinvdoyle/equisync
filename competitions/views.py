from django.shortcuts import render, redirect
from .models import Event
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def calendar_view(request):
    today = timezone.now()
    events = Event.objects.filter(start_time__gte=today)

    context = {
        'events': events,
        'today': today,
    }
    
    return render(request, 'competitions/calendar.html', context)

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

