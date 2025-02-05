from django.db import models
from django.contrib.auth.models import User

class HorseProfile(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Mare', 'Mare'), ('Gelding', 'Gelding'), ('Stallion', 'Stallion')])
    description = models.TextField()
    image = models.ImageField(upload_to='horses/images', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    staff = models.ManyToManyField(User, related_name='horse_staff')
    barn_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='horse_barn_manager')
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='horse_rider')

    def __str__(self):
        return f"{self.name} ({self.breed}) - {self.gender} ({self.age})"

    def most_recent_ride(self):
        return self.rider

    def most_recent_barn_manager(self):
        return self.barn_manager

    def most_recent_staff(self):
        return self.staff

    def most_recent_owner(self):
        return self.owner