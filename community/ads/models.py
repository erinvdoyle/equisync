from django.db import models

# Create your models here.
class Ad(models.Model):
    AD_TYPE_CHOICES = [
        ('for_sale', 'For Sale'),
        ('wanted', 'Wanted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_type = models.CharField(max_length=10, choices=AD_TYPE_CHOICES)
    image = models.ImageField(upload_to='ads/images', blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ad_type} - {self.description[:30]}"