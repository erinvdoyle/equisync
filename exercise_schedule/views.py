from django.shortcuts import render, get_object_or_404
from .models import ExerciseSchedule
from .forms import ExerciseScheduleForm
import datetime
from horses.models import HorseProfile

def daily_schedule_view(request, date=None, horse_id=None):
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    queryset = ExerciseSchedule.objects.filter(date=date)
    if horse_id:
        queryset = queryset.filter(horse_id=horse_id)

    form = ExerciseScheduleForm()
    context = {
        'schedules': queryset,
        'date': date,
        'form': form,
        'horse_profiles': HorseProfile.objects.all()
    }
    return render(request, 'exercise_schedule/daily_schedule.html', context)


def weekly_schedule_view(request, date=None):
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    start_week = date - datetime.timedelta(days=date.weekday())
    end_week = start_week + datetime.timedelta(days=6)

    queryset = ExerciseSchedule.objects.filter(date__range=[start_week, end_week])

    context = {
        'schedules': queryset,
        'start_week': start_week,
        'end_week': end_week,
    }
    return render(request, 'exercise_schedule/weekly_schedule.html', context)

def archive_schedule_view(request):
    search_term = request.GET.get('search')
    queryset = ExerciseSchedule.objects.all()

    if search_term:
        queryset = queryset.filter(
            Q(horse__name__icontains=search_term) |
            Q(exercise_type__icontains=search_term) |
            Q(notes__icontains=search_term)
        )

    context = {
        'schedules': queryset,
        'search_term': search_term,
    }
    return render(request, 'exercise_schedule/archive_schedule.html', context)

from django.shortcuts import render, redirect
from .forms import ExerciseScheduleForm

def create_schedule_entry(request):
    if request.method == 'POST':
        form = ExerciseScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_schedule:daily_schedule_view')
    else:
        form = ExerciseScheduleForm()
    return render(request, 'exercise_schedule/create_schedule_entry.html', {'form': form})

