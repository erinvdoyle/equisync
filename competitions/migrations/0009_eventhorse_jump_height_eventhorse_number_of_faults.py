# Generated by Django 4.2.18 on 2025-02-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0008_eventhorse_performance_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventhorse',
            name='jump_height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventhorse',
            name='number_of_faults',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
