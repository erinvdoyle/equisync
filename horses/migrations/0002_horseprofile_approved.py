# Generated by Django 4.2.18 on 2025-03-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horseprofile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
