# Generated by Django 4.2.18 on 2025-02-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_ad_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='temp_field',
            field=models.CharField(blank=True, default='temporary', max_length=20, null=True),
        ),
    ]
