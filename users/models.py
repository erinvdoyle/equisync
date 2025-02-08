from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    ROLE_CHOICES = [
        ('Barn Manager', 'Barn Manager'),
        ('Horse Owner', 'Horse Owner'),
        ('Rider', 'Rider'),
        ('Staff Member', 'Staff Member'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Horse Owner', blank=True)
    contact = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile for {self.user.username}"
