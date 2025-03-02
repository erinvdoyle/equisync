import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExerciseSchedule, ExerciseScheduleItem
from .forms import ExerciseScheduleForm, ExerciseScheduleItemForm
import datetime
from horses.models import HorseProfile
from django.db.models import IntegerField, Sum
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def daily_schedule_view(request, date=None, horse_id=None):
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    queryset = ExerciseSchedule.objects.filter(date=date)
    if horse_id:
        queryset = queryset.filter(horse_id=horse_id)

    schedule_form = ExerciseScheduleForm(initial={'date': date})
    item_forms = [ExerciseScheduleItemForm(prefix=str(i)) for i in range(3)]

    if request.method == 'POST':
        schedule_form = ExerciseScheduleForm(request.POST)
        item_forms = [ExerciseScheduleItemForm(request.POST, prefix=str(i)) for i in range(3)]

        if schedule_form.is_valid() and all(form.is_valid() for form in item_forms):
            schedule = schedule_form.save(commit=False)
            schedule.created_by = request.user
            schedule.save()

            for form in item_forms:
                if form.cleaned_data['exercise_type'] and form.cleaned_data['duration']:
                    item = form.save(commit=False)
                    item.schedule = schedule
                    item.save()

            return redirect('exercise_schedule:daily_schedule_view_date', date=date.strftime("%Y-%m-%d"))

    context = {
        'schedules': queryset,
        'date': date,
        'schedule_form': schedule_form,
        'item_forms': item_forms,
        'horse_profiles': HorseProfile.objects.all()
    }
    return render(request, 'exercise_schedule/daily_schedule.html', context)

@login_required
def weekly_schedule_view(request, date=None):
    if request.user.is_staff or request.user.has_perm('exercise_schedule.change_exerciseschedule'):
        template = 'exercise_schedule/weekly_schedule.html'
    else:
        template = 'exercise_schedule/weekly_schedule_readonly.html'

    date_str = request.GET.get('date')
    if date_str:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        date = datetime.date.today()

    start_week = date - datetime.timedelta(days=date.weekday())
    end_week = start_week + datetime.timedelta(days=6)

    horses = HorseProfile.objects.all()

    weekly_schedule = {}
    days_of_week = []

    for i in range(7):
        day = start_week + datetime.timedelta(days=i)
        days_of_week.append(day)

    for horse in horses:
        weekly_schedule[horse] = {}
        for i in range(7):
            day = start_week + datetime.timedelta(days=i)
            schedules = ExerciseSchedule.objects.filter(horse=horse, date=day).prefetch_related('schedule_items')
            weekly_schedule[horse][day] = schedules if schedules.exists() else None

    context = {
        'weekly_schedule': weekly_schedule,
        'start_week': start_week,
        'end_week': end_week,
        'horses': horses,
        'days_of_week': days_of_week,
    }
    return render(request, template, context)


def archive_schedule_view(request):
    search_term = request.GET.get('search')
    queryset = ExerciseSchedule.objects.all()

    if search_term:
        queryset = queryset.filter(
            Q(horse__name__icontains=search_term) |
            Q(notes__icontains=search_term) |
            Q(exercise_type__icontains=search_term)
        )

    context = {
        'schedules': queryset,
        'search_term': search_term,
    }
    return render(request, 'exercise_schedule/archive_schedule.html', context)

def create_schedule_entry(request):
    if request.method == 'POST':
        form = ExerciseScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_schedule:daily_schedule_view')
    else:
        form = ExerciseScheduleForm()
    return render(request, 'exercise_schedule/create_schedule_entry.html', {'form': form})

@login_required
def horse_exercise_schedule_view(request, horse_id, start_date=None, end_date=None):
    horse = get_object_or_404(HorseProfile, pk=horse_id)

    if request.method == 'GET':
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        if start_date_str:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        else:
            start_date = datetime.date.today() - datetime.timedelta(days=7)

        if end_date_str:
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        else:
            end_date = datetime.date.today()

    exercise_data = ExerciseScheduleItem.objects.filter(
        schedule__horse=horse,
        schedule__date__range=[start_date, end_date]
    ).values('exercise_type').annotate(total_duration=Sum('duration', output_field=IntegerField()))

    labels = [item['exercise_type'] for item in exercise_data]
    data = [item['total_duration'] for item in exercise_data]

    date = datetime.date.today()
    start_week = date - datetime.timedelta(days=date.weekday())
    end_week = start_week + datetime.timedelta(days=6)

    weekly_schedule_items = {}
    days_of_week = []

    for i in range(7):
        day = start_week + datetime.timedelta(days=i)
        days_of_week.append(day)

    weekly_schedule_items = {}
    for day in days_of_week:
        try:
            schedule_items = ExerciseScheduleItem.objects.filter(schedule__horse=horse, schedule__date=day)
            weekly_schedule_items[day] = schedule_items
        except ExerciseScheduleItem.DoesNotExist:
            weekly_schedule_items[day] = None

    context = {
        'horse': horse,
        'labels': labels,
        'data': data,
        'start_week': start_week,
        'end_week': end_week,
        'weekly_schedule_items': weekly_schedule_items,
        'days_of_week': days_of_week,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'exercise_schedule/horse_exercise_schedule.html', context)

def exercise_details_view(request, schedule_id):
    schedule = get_object_or_404(ExerciseSchedule, pk=schedule_id)

    am_items = schedule.schedule_items.filter(time_category='am')
    pm_items = schedule.schedule_items.filter(time_category='pm')
    additional_items = schedule.schedule_items.filter(time_category='additional')

    notes = schedule.notes

    context = {
        'am_items': am_items,
        'pm_items': pm_items,
        'additional_items': additional_items,
        'notes': notes,
        'horse_name': schedule.horse.name,
        'date': schedule.date.strftime('%b %d, %Y'),
    }

    return render(request, 'exercise_schedule/exercise_schedule_details.html', context)