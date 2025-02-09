# Generated by Django 4.2.18 on 2025-02-09 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseschedule',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='exerciseschedule',
            name='exercise_type',
        ),
        migrations.CreateModel(
            name='ExerciseScheduleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(choices=[('walker', 'Walker'), ('lunge', 'Lunge'), ('hand_walk', 'Hand Walk'), ('graze', 'Graze'), ('turnout', 'Turnout'), ('ride', 'Ride'), ('groundwork', 'Groundwork'), ('other', 'Other')], max_length=50)),
                ('duration', models.PositiveIntegerField(default=0, help_text='Duration in minutes')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_items', to='exercise_schedule.exerciseschedule')),
            ],
        ),
    ]
