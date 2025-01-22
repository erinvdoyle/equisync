from django.db import models

# Create your models here.
class Ad(models.Model):
    AD_TYPE_CHOICES = [
        ('for_sale', 'For Sale'),
        ('wanted', 'Wanted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)