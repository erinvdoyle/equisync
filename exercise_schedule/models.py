from django.db import models
from horses.models import HorseProfile
from django.contrib.auth.models import User


# Create your models here.
class ExerciseSchedule(models.Model):
    horse = models.ForeignKey(HorseProfile, on_delete=models.CASCADE, related_name='exercise_schedules')
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='exercise_schedules_created')
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

class ExerciseScheduleItem(models.Model):
    schedule = models.ForeignKey(ExerciseSchedule, on_delete=models.CASCADE, related_name='schedule_items')
    exercise_type = models.CharField(max_length=50, choices=EXERCISE_CHOICES)
    duration = models.PositiveIntegerField(default=0, help_text="Duration in minutes")

    def __str__(self):
        return f"{self.get_exercise_type_display()} ({self.duration} mins)"