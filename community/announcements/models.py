from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcements/images', blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Announcement by {self.user.username} on {self.date_posted}"