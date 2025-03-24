from django.db import models
from django.contrib.auth.models import User
from horses.models import HorseProfile


class FeedingChart(models.Model):
    horse = models.OneToOneField(
        HorseProfile, on_delete=models.CASCADE, related_name='feeding_chart')
    breakfast_feed = models.CharField(max_length=200, blank=True, null=True)
    breakfast_quantity = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    lunch_feed = models.CharField(max_length=200, blank=True, null=True)
    lunch_quantity = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    dinner_feed = models.CharField(max_length=200, blank=True, null=True)
    dinner_quantity = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    hay = models.CharField(max_length=200, blank=True, null=True)
    hay_quantity = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    supplements = models.CharField(max_length=200, blank=True, null=True)
    medicines = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True)
    approved_users = models.ManyToManyField(
            User, related_name='feeding_charts', blank=True)
    approved = models.BooleanField(default=False)
    last_updated_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    def get_hay_info(self):
        if self.hay and self.hay_quantity:
            quantity = float(self.hay_quantity)
            return f"{quantity} kg {self.hay}"
        return "Not Set"

    def get_breakfast_info(self):
        if self.breakfast_feed and self.breakfast_quantity:
            quantity = float(self.breakfast_quantity)
            return f"{quantity} kg {self.breakfast_feed}"
        return "Not Set"

    def get_lunch_info(self):
        if self.lunch_feed and self.lunch_quantity:
            quantity = float(self.lunch_quantity)
            return f"{quantity} kg {self.lunch_feed}"
        return "Not Set"

    def get_dinner_info(self):
        if self.dinner_feed and self.dinner_quantity:
            quantity = float(self.dinner_quantity)
            return f"{quantity} kg {self.dinner_feed}"
        return "Not Set"

    def __str__(self):
        return f"Feeding Chart for {self.horse.name}"
