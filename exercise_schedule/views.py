import datetime
from datetime import datetime, date as dt, timedelta
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import IntegerField, Sum, Avg, Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExerciseSchedule, ExerciseScheduleItem, Appointment

from horses.models import HorseProfile
from .forms import (
    ExerciseScheduleForm,
    ExerciseScheduleItemForm,
    AppointmentForm,
)


@login_required
def daily_schedule_view(request, date=None, horse_id=None):
    if date is None:
        date = dt.today()
    else:
        date = datetime.strptime(date, "%Y-%m-%d").date()

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
        item_forms = [
            ExerciseScheduleItemForm(request.POST, prefix=str(
                i)) for i in range(3)]

        if schedule_form.is_valid() and all(
                form.is_valid() for form in item_forms):
            schedule = schedule_form.save(commit=False)
            schedule.created_by = request.user

            existing_schedule = ExerciseSchedule.objects.filter(
                horse=schedule.horse,
                date=date
            ).first()

            if existing_schedule:
                schedule.id = existing_schedule.id
                schedule.save(
                    update_fields=[
                        'horse', 'date', 'notes', 'created_by', 'updated_at'])
                ExerciseScheduleItem.objects.filter(
                    schedule=existing_schedule).delete()
            else:
                schedule.save()

            for form in item_forms:
                if form.cleaned_data[
                        'exercise_type'] and form.cleaned_data['duration']:
                    item = form.save(commit=False)
                    item.schedule = schedule
                    item.save()

            return redirect(
                'exercise_schedule:daily_schedule_view_date',
                date=date.strftime("%Y-%m-%d")
            )

    selected_horse_id = request.GET.get('horse_id')
    existing_schedule = None
    if selected_horse_id:
        selected_horse = get_object_or_404(HorseProfile, id=selected_horse_id)
        existing_schedule = ExerciseSchedule.objects.filter(
            horse=selected_horse,
            date=date
        ).first()

        if existing_schedule:
            schedule_form = ExerciseScheduleForm(instance=existing_schedule)
            item_forms = [
                ExerciseScheduleItemForm(instance=item, prefix=str(i))
                for i, item in enumerate(
                    existing_schedule.schedule_items.all())
            ]

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
def weekly_schedule_view(request, selected_date=None):
    from_profile = request.GET.get('from') == 'horse_profile'

    user_horses = HorseProfile.objects.filter(
        Q(owner=request.user) |
        Q(staff=request.user) |
        Q(barn_manager=request.user) |
        Q(rider=request.user)
    ).distinct()

    if from_profile:
        has_any_schedule = ExerciseSchedule.objects.filter(
            horse__in=user_horses).exists()
        if not has_any_schedule:
            messages.success(request, "Register your horse here.")

    date_str = request.GET.get('date')
    if date_str:
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            selected_date = dt.today()
    else:
        selected_date = dt.today()

    start_week = selected_date - timedelta(days=selected_date.weekday())
    end_week = start_week + timedelta(days=6)
    days_of_week = [start_week + timedelta(days=i) for i in range(7)]

    weekly_schedule = {}
    all_horses = HorseProfile.objects.all()
    for horse in all_horses:
        weekly_schedule[horse] = {}
        for day in days_of_week:
            schedules = ExerciseSchedule.objects.filter(
                horse=horse, date=day
            ).prefetch_related('schedule_items')
            appointments = Appointment.objects.filter(horse=horse, date=day)

            weekly_schedule[horse][day] = {
                'schedules': schedules if schedules.exists() else None,
                'appointments': list(appointments)
            }

    template_name = (
        'exercise_schedule/weekly_schedule.html'
        if request.user.is_staff or request.user.has_perm(
            'exercise_schedule.change_exerciseschedule')
        else 'exercise_schedule/weekly_schedule_readonly.html'
    )

    context = {
        'weekly_schedule': weekly_schedule,
        'start_week': start_week,
        'end_week': end_week,
        'horses': all_horses,
        'days_of_week': days_of_week,
        'user_horses': user_horses,
    }
    return render(request, template_name, context)


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

    return render(
        request, 'exercise_schedule/create_schedule_entry.html', {'form': form}
        )


logging.basicConfig(level=logging.DEBUG)


@login_required
def horse_exercise_schedule_view(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)

    # Optional: Prevent access to unapproved horses
    if hasattr(horse, 'approved') and not horse.approved:
        return HttpResponseForbidden("This horse has not been approved by an admin.")

    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    timeframe = request.GET.get('timeframe', 'week')

    today = dt.today()

    if timeframe == 'day':
        start_date = today
        end_date = today
    elif timeframe == 'week':
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
    elif timeframe == 'month':
        start_date = today.replace(day=1)
        end_date = (
            start_date + timedelta(days=32)
        ).replace(day=1) - timedelta(days=1)
    elif timeframe == 'year':
        start_date = today.replace(month=1, day=1)
        end_date = today.replace(month=12, day=31)
    elif timeframe == 'custom' and start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    else:
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
    
    current_date = dt.today()
    start_week = current_date - timedelta(days=current_date.weekday())
    end_week = start_week + timedelta(days=6)
    days_of_week = [start_week + timedelta(days=i) for i in range(7)]
    weekly_schedule_items = {day: [] for day in days_of_week}

    if timeframe == 'day':
        weekly_schedule_items = {
            day: ExerciseScheduleItem.objects.filter(
                schedule__horse=horse,
                schedule__date=day
            ) for day in days_of_week
        }

    exercise_data = ExerciseScheduleItem.objects.filter(
        schedule__horse=horse,
        schedule__date__range=[start_date, end_date]
    ).values('exercise_type').annotate(
        total_duration=Sum('duration', output_field=IntegerField())
    )

    labels = [item['exercise_type'] for item in exercise_data]
    data = [item['total_duration'] for item in exercise_data]

    exercise_breakdown_minutes = [
        {
            'exercise_type': item['exercise_type'],
            'total_minutes': item['total_duration'],
            'total_hours': round(item['total_duration'] / 60.0 * 2) / 2
        }
        for item in exercise_data
    ]

    exercise_breakdown_minutes_html = ''.join(
        f'<li>{item["exercise_type"]}: {item["total_minutes"]} minutes '
        f'({item["total_hours"]} hours)</li>'
        for item in exercise_breakdown_minutes
    )

    if timeframe != 'day':
        average_data = ExerciseScheduleItem.objects.filter(
            schedule__horse=horse,
            schedule__date__range=[start_date, end_date]
        ).values('exercise_type').annotate(
            average_minutes=Avg('duration')
        )

        average_exercise_time = [
            {
                'exercise_type': item['exercise_type'],
                'average_minutes': item['average_minutes'],
                'average_hours': round(item['average_minutes'] / 60.0 * 2) / 2
            }
            for item in average_data
        ]

        average_exercise_time_html = ''.join(
            (
                f'<li>{item["exercise_type"]}: '
                f'{item["average_hours"]} hours</li>'
                if item['average_hours'] >= 0.5
                else f'<li>{item["exercise_type"]}: '
                f'{item["average_minutes"]} minutes</li>'
            )
            for item in average_exercise_time
        )
    else:
        average_exercise_time = []
        average_exercise_time_html = ''

    previous_weeks = [
        {
            'start_date': start_week - timedelta(weeks=i),
            'end_date': (start_week - timedelta(weeks=i)) + timedelta(days=6)
        }
        for i in range(10)
    ]

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
            'weekly_schedule_items': {
                day.strftime('%Y-%m-%d'): [
                    {
                        'exercise_type': item.get_exercise_type_display(),
                        'duration': item.duration
                    } for item in items
                ] for day, items in weekly_schedule_items.items()
            },
        })

    return render(
        request, 'exercise_schedule/horse_exercise_schedule.html', context
    )

@login_required
def weekly_exercise_schedule(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)
    start_date_str = request.GET.get('start_date')

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    end_date = start_date + timedelta(days=6)

    weekly_schedule_items = {}
    for day in (start_date + timedelta(n) for n in range(7)):
        schedule_items = ExerciseScheduleItem.objects.filter(
            schedule__horse=horse,
            schedule__date=day
        )
        weekly_schedule_items[day.strftime('%Y-%m-%d')] = [
            {
                'exercise_type': item.get_exercise_type_display(),
                'duration': item.duration
            } for item in schedule_items
        ]

    return JsonResponse({'weekly_schedule_items': weekly_schedule_items})


@login_required
def exercise_details_view(request, schedule_id):
    schedule = get_object_or_404(ExerciseSchedule, pk=schedule_id)

    am_items = schedule.schedule_items.filter(time_category='am')
    pm_items = schedule.schedule_items.filter(time_category='pm')
    additional_items = schedule.schedule_items.filter(
        time_category='additional')

    appointments = Appointment.objects.filter(
        horse=schedule.horse, date=schedule.date)

    context = {
        'am_items': am_items,
        'pm_items': pm_items,
        'additional_items': additional_items,
        'notes': schedule.notes,
        'horse_name': schedule.horse.name,
        'date': schedule.date.strftime('%b %d, %Y'),
        'appointments': appointments,
    }

    return render(
        request, 'exercise_schedule/exercise_schedule_details.html', context)


@login_required
def add_appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.created_by = request.user
            appointment.save()
            return redirect('exercise_schedule:weekly_schedule_view')
    else:
        form = AppointmentForm()

    return render(
        request, 'exercise_schedule/add_appointment.html', {'form': form})


@login_required
def appointment_details_view(request, horse_name, date_str):
    try:
        date = datetime.strptime(date_str, "%b %d").replace(
            year=datetime.now().year
        ).date()
    except ValueError:
        return render(
            request,
            'exercise_schedule/error.html',
            {'message': 'Invalid date format'}
        )

    appointments = Appointment.objects.filter(
         horse__name=horse_name, date=date)

    context = {
        'appointments': appointments,
        'horse_name': horse_name,
        'date': date,
    }
    return render(
        request, 'exercise_schedule/appointment_details.html', context)
