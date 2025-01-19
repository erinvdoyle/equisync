from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """
    extends user class for automatic profile creation
    """

    ROLE_CHOICES = [
        ('Horse Owner', 'Horse Owner'),
        ('Rider', 'Rider'),
        ('Staff Member', 'Staff Member'),
    ]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    horse = models.ForeignKey('Horse', on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return f"Profile for {self.user.username}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    signal handler function to create a user profile when a new user is created
    Source for explanation: Codu, as credited in README.md
    """
    if created:
        Profile.objects.create(user=instance)

class Horse(models.Model):
    """
    temporary model to be removed when horse management app is created
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name