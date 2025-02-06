from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    """
    extends user class for automatic profile creation
    """

    ROLE_CHOICES = [
        ('Barn Manager', 'Barn Manager'),
        ('Horse Owner', 'Horse Owner'),
        ('Rider', 'Rider'),
        ('Staff Member', 'Staff Member'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile for {self.username}"

class Horse(models.Model):
    """
    temporary model to be removed when horse management app is created
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

