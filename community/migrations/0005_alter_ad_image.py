# Generated by Django 5.1.7 on 2025-04-01 10:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_ad_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
