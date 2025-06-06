from django.apps import AppConfig


class ExerciseScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exercise_schedule'

    def ready(self):
        import exercise_schedule.signals
