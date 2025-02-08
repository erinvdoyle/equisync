# Generated by Django 4.2.18 on 2025-02-07 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedingChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast_feed', models.CharField(blank=True, max_length=200, null=True)),
                ('breakfast_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lunch_feed', models.CharField(blank=True, max_length=200, null=True)),
                ('lunch_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('dinner_feed', models.CharField(blank=True, max_length=200, null=True)),
                ('dinner_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hay', models.CharField(blank=True, max_length=200, null=True)),
                ('hay_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('supplements', models.CharField(blank=True, max_length=200, null=True)),
                ('medicines', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True)),
                ('approved_users', models.ManyToManyField(blank=True, related_name='feeding_charts', to=settings.AUTH_USER_MODEL)),
                ('horse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feeding_chart', to='horses.horseprofile')),
            ],
        ),
    ]
