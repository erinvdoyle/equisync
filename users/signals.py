from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    signal to create a Profile when a new User is created
    Source for explanation: Codu, as credited in README.md
    Source for hasattr() explanation: Hinty.io, credited in README
    """
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

