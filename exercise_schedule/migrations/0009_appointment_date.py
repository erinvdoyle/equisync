# Generated by Django 4.2.18 on 2025-03-04 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_schedule', '0008_remove_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
