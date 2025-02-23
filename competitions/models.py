from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from horses.models import HorseProfile


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(User, related_name='favorite_events', blank=True)
    is_archived = models.BooleanField(default=False)
    horses = models.ManyToManyField(HorseProfile, related_name='events', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('competitions:event_detail', args=[self.id])
    
class EventHorse(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    horse = models.ForeignKey(HorseProfile, on_delete=models.CASCADE)
    class_details = models.CharField(max_length=200, blank=True, null=True)
    results = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    performance_rating = models.CharField(max_length=20, blank=True, null=True)
    jump_height = models.FloatField(blank=True, null=True)
    number_of_faults = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.horse.name} at {self.event.title} - {self.class_details or 'No Class'}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_horse = models.ForeignKey(EventHorse, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"