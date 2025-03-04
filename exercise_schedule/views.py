import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExerciseSchedule, ExerciseScheduleItem
from .forms import ExerciseScheduleForm, ExerciseScheduleItemForm
import datetime
from horses.models import HorseProfile
from django.db.models import IntegerField, Sum, Avg
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse


@login_required
def daily_schedule_view(request, date=None, horse_id=None):
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    queryset = ExerciseSchedule.objects.filter(date=date)
    if horse_id:
        queryset = queryset.filter(horse_id=horse_id)

    user_horses = HorseProfile.objects.filter(
        Q(owner=request.user) |
        Q(staff=request.user) |
        Q(barn_manager=request.user) |
        Q(rider=request.user)
    ).distinct()

    schedule_form = ExerciseScheduleForm(initial={'date': date})
    schedule_form.fields['horse'].queryset = user_horses
    item_forms = [ExerciseScheduleItemForm(prefix=str(i)) for i in range(3)]

    if request.method == 'POST':
        schedule_form = ExerciseScheduleForm(request.POST)
        item_forms = [ExerciseScheduleItemForm(request.POST, prefix=str(i)) for i in range(3)]

        if schedule_form.is_valid() and all(form.is_valid() for form in item_forms):
            schedule = schedule_form.save(commit=False)
            schedule.created_by = request.user

            existing_schedule = ExerciseSchedule.objects.filter(horse=schedule.horse, date=date).first()
            if existing_schedule:
                schedule.id = existing_schedule.id
                schedule.save(update_fields=['horse', 'date', 'notes', 'created_by', 'updated_at'])
                ExerciseScheduleItem.objects.filter(schedule=existing_schedule).delete()
            else:
                schedule.save()

            for form in item_forms:
                if form.cleaned_data['exercise_type'] and form.cleaned_data['duration']:
                    item = form.save(commit=False)
                    item.schedule = schedule
                    item.save()

            return redirect('exercise_schedule:daily_schedule_view_date', date=date.strftime("%Y-%m-%d"))

    selected_horse_id = request.GET.get('horse_id')
    existing_schedule = None
    if selected_horse_id:
        selected_horse = get_object_or_404(HorseProfile, id=selected_horse_id)
        existing_schedule = ExerciseSchedule.objects.filter(horse=selected_horse, date=date).first()
        if existing_schedule:
            schedule_form = ExerciseScheduleForm(instance=existing_schedule)
            item_forms = [ExerciseScheduleItemForm(instance=item, prefix=str(i)) for i, item in enumerate(existing_schedule.schedule_items.all())]

    context = {
        'schedules': queryset,
        'date': date,
        'schedule_form': schedule_form,
        'item_forms': item_forms,
        'user_horses': user_horses,
        'existing_schedule': existing_schedule,
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

    all_horses = HorseProfile.objects.all()

    user_horses = HorseProfile.objects.filter(
        Q(owner=request.user) |
        Q(staff=request.user) |
        Q(barn_manager=request.user) |
        Q(rider=request.user)
    ).distinct()

    weekly_schedule = {}
    days_of_week = []

    for i in range(7):
        day = start_week + datetime.timedelta(days=i)
        days_of_week.append(day)

    for horse in all_horses:
        weekly_schedule[horse] = {}
        for i in range(7):
            day = start_week + datetime.timedelta(days=i)
            schedules = ExerciseSchedule.objects.filter(horse=horse, date=day).prefetch_related('schedule_items')
            weekly_schedule[horse][day] = schedules if schedules.exists() else None

    context = {
        'weekly_schedule': weekly_schedule,
        'start_week': start_week,
        'end_week': end_week,
        'horses': all_horses,
        'days_of_week': days_of_week,
        'user_horses': user_horses,
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
def horse_exercise_schedule_view(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)

    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    timeframe = request.GET.get('timeframe', 'week')

    today = datetime.date.today()

    if timeframe == 'day':
        start_date = today
        end_date = today
    elif timeframe == 'week':
        start_date = today - datetime.timedelta(days=today.weekday())
        end_date = start_date + datetime.timedelta(days=6)
    elif timeframe == 'month':
        start_date = today.replace(day=1)
        end_date = (start_date + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    elif timeframe == 'year':
        start_date = today.replace(month=1, day=1)
        end_date = today.replace(month=12, day=31)
    else:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

    exercise_data = ExerciseScheduleItem.objects.filter(
        schedule__horse=horse,
        schedule__date__range=[start_date, end_date]
    ).values('exercise_type').annotate(total_duration=Sum('duration', output_field=IntegerField()))

    labels = [item['exercise_type'] for item in exercise_data]
    data = [item['total_duration'] for item in exercise_data]

    exercise_breakdown_minutes = [
        {'exercise_type': item['exercise_type'], 'total_minutes': item['total_duration'], 'total_hours': round(item['total_duration'] / 60.0 * 2) / 2}
        for item in exercise_data
    ]

    exercise_breakdown_minutes_html = ''.join(
        f'<li>{item["exercise_type"]}: {item["total_minutes"]} minutes ({item["total_hours"]} hours)</li>'
        for item in exercise_breakdown_minutes
    )

    if timeframe != 'day':
        average_exercise_time = [
            {'exercise_type': item['exercise_type'], 'average_minutes': item['average_minutes'], 'average_hours': round(item['average_minutes'] / 60.0 * 2) / 2}
            for item in ExerciseScheduleItem.objects.filter(
                schedule__horse=horse,
                schedule__date__range=[start_date, end_date]
            ).values('exercise_type').annotate(average_minutes=Avg('duration'))
        ]
        average_exercise_time_html = ''.join(
            f'<li>{item["exercise_type"]}: {item["average_hours"]} hours</li>'
            if item['average_hours'] >= 0.5 else f'<li>{item["exercise_type"]}: {item["average_minutes"]} minutes</li>'
            for item in average_exercise_time
        )
    else:
        average_exercise_time = []
        average_exercise_time_html = ''

    date = datetime.date.today()
    start_week = date - datetime.timedelta(days=date.weekday())
    end_week = start_week + datetime.timedelta(days=6)

    weekly_schedule_items = {}
    days_of_week = []

    for i in range(7):
        day = start_week + datetime.timedelta(days=i)
        days_of_week.append(day)

    for day in days_of_week:
        try:
            schedule_items = ExerciseScheduleItem.objects.filter(schedule__horse=horse, schedule__date=day)
            weekly_schedule_items[day] = schedule_items
        except ExerciseScheduleItem.DoesNotExist:
            weekly_schedule_items[day] = None

    previous_weeks = []
    for i in range(10):
        week_start = start_week - datetime.timedelta(weeks=i)
        week_end = week_start + datetime.timedelta(days=6)
        previous_weeks.append({'start_date': week_start, 'end_date': week_end})

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
        'exercise_breakdown_minutes': exercise_breakdown_minutes,
        'exercise_breakdown_minutes_html': exercise_breakdown_minutes_html,
        'average_exercise_time': average_exercise_time,
        'average_exercise_time_html': average_exercise_time_html,
        'timeframe': timeframe,
        'previous_weeks': previous_weeks,
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'labels': labels,
            'data': data,
            'exercise_breakdown_minutes_html': exercise_breakdown_minutes_html,
            'average_exercise_time_html': average_exercise_time_html,
            'weekly_schedule_items': {day.strftime('%Y-%m-%d'): [{'exercise_type': item.get_exercise_type_display(), 'duration': item.duration} for item in items] for day, items in weekly_schedule_items.items()},
        })

    return render(request, 'exercise_schedule/horse_exercise_schedule.html', context)

def weekly_exercise_schedule(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)
    start_date_str = request.GET.get('start_date')
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = start_date + datetime.timedelta(days=6)

    weekly_schedule_items = {}
    for day in (start_date + datetime.timedelta(n) for n in range(7)):
        schedule_items = ExerciseScheduleItem.objects.filter(schedule__horse=horse, schedule__date=day)
        weekly_schedule_items[day.strftime('%Y-%m-%d')] = [{'exercise_type': item.get_exercise_type_display(), 'duration': item.duration} for item in schedule_items]

    return JsonResponse({'weekly_schedule_items': weekly_schedule_items})


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