# Generated by Django 4.2.18 on 2025-02-06 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0003_horseprofile_temp_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horseprofile',
            name='temp_field',
        ),
    ]
