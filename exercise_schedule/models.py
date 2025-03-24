from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from horses.models import HorseProfile


class ExerciseSchedule(models.Model):
    horse = models.ForeignKey(
        HorseProfile,
        on_delete=models.CASCADE,
        related_name='exercise_schedules'
    )
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='exercise_schedules_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'horse']

    def __str__(self):
        return f"{self.horse.name} - {self.date}"


EXERCISE_CHOICES = [
    ('walker', 'Walker'),
    ('lunge', 'Lunge'),
    ('hand_walk', 'Hand Walk'),
    ('graze', 'Graze'),
    ('turnout', 'Turnout'),
    ('ride', 'Ride'),
    ('groundwork', 'Groundwork'),
    ('other', 'Other'),
]

TIME_CATEGORY_CHOICES = [
    ('am', 'AM'),
    ('pm', 'PM'),
    ('additional', 'Additional'),
]


class ExerciseScheduleItem(models.Model):
    schedule = models.ForeignKey(
        ExerciseSchedule,
        on_delete=models.CASCADE,
        related_name='schedule_items'
    )
    exercise_type = models.CharField(
        max_length=50,
        choices=EXERCISE_CHOICES
    )
    duration = models.PositiveIntegerField(
        default=0,
        help_text="Duration in minutes"
    )
    time_category = models.CharField(
        max_length=20,
        choices=TIME_CATEGORY_CHOICES,
        default='am'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_exercise_type_display()} ({self.duration} mins)"


class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ('farrier', 'Farrier'),
        ('vet', 'Vet'),
        ('physio', 'Physio'),
        ('dentist', 'Dentist'),
        ('other', 'Other'),
    ]

    horse = models.ForeignKey(
        HorseProfile,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date = models.DateField(default=timezone.now)
    appointment_type = models.CharField(
        max_length=50,
        choices=APPOINTMENT_TYPE_CHOICES
    )
    practitioner = models.CharField(max_length=100)
    time = models.TimeField()
    contact_details = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.get_appointment_type_display()} for {self.horse.name} "
            f"on {self.created_at.strftime('%Y-%m-%d')}"
        )
