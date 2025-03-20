from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Announcement by {self.user.username} on {self.date_posted}"
    
    def get_absolute_url(self):
        return reverse('community:announcement_detail', kwargs={'announcement_id': self.pk})

class Reaction(models.Model):
    EMOJI_CHOICES = [
        ('👍', '👍'),
        ('❤️', '❤️'),
        ('😂', '😂'),
        ('😮', '😮'),
        ('😢', '😢'),
        ('😡', '😡'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=2, choices=EMOJI_CHOICES)
    count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'announcement', 'emoji')

    def __str__(self):
        return f"{self.user.username} reacted with {self.emoji} to {self.announcement}"
