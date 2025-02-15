from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(User, related_name='favorite_events', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('competitions:event_detail', args=[str(self.id)])
