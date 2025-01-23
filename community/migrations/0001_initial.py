# Generated by Django 4.2.18 on 2025-01-23 10:34

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
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.CharField(choices=[('for_sale', 'For Sale'), ('wanted', 'Wanted')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ads/images')),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('contact_info', models.CharField(max_length=255)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
