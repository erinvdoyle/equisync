# Generated by Django 4.2.18 on 2025-03-22 11:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0002_horseprofile_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horseprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
