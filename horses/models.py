from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class HorseProfile(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, choices=[('Mare', 'Mare'), (
                'Gelding', 'Gelding'), ('Stallion', 'Stallion')])
    image = CloudinaryField('image', blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='horse_owner')
    staff = models.ManyToManyField(User, related_name='horse_staff')
    barn_manager = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='horse_barn_manager')
    rider = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='horse_rider')
    approved = models.BooleanField(default=False)

    most_recent_ride = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='horses_ridden'
    )
    last_ridden_at = models.DateTimeField(null=True, blank=True)

    most_recent_care = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='horses_cared_for'
    )
    last_cared_for_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.breed}) - {self.gender} ({self.age})"