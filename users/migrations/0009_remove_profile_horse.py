# Generated by Django 4.2.18 on 2025-02-06 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='horse',
        ),
    ]
