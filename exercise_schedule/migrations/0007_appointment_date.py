# Generated by Django 4.2.18 on 2025-03-04 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_schedule', '0006_alter_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
