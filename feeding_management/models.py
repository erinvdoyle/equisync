from django.db import models
from django.contrib.auth.models import User
from horses.models import HorseProfile  

class FeedingChart(models.Model):
    horse = models.OneToOneField(HorseProfile, on_delete=models.CASCADE, related_name='feeding_chart')  
    breakfast_feed = models.CharField(max_length=200, blank=True, null=True)
    breakfast_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) 
    lunch_feed = models.CharField(max_length=200, blank=True, null=True)
    lunch_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dinner_feed = models.CharField(max_length=200, blank=True, null=True)
    dinner_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hay = models.CharField(max_length=200, blank=True, null=True)
    hay_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    supplements = models.CharField(max_length=200, blank=True, null=True)
    medicines = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True)
    approved_users = models.ManyToManyField(User, related_name='feeding_charts', blank=True) 

    def __str__(self):
        return f"Feeding Chart for {self.horse.name}"

