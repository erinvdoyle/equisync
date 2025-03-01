from .models import Notification

def send_notification(user, message, event_horse=None):
    """Creates a notification for a specific user."""
    Notification.objects.create(user=user, message=message, event_horse=event_horse)
