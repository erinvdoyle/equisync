from django.apps import AppConfig


class FeedingManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feeding_management'

    def ready(self):
        import feeding_management.signals
