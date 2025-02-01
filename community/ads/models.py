from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ad(models.Model):
    AD_TYPE_CHOICES = [
        ('for_sale', 'For Sale'),
        ('wanted', 'Wanted'),
    ]
    CATEGORY_CHOICES = [
        ("Horse", "Horse"), ("Equipment", "Equipment"), ("Clothing", "Clothing"), ("Machinery/Auto", "Machinery/Auto"), ("Animal", "Animal"), ("Other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_type = models.CharField(max_length=10, choices=AD_TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Other")
    image = models.ImageField(upload_to='ads/images', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ad_type} - {self.description[:30]}"
