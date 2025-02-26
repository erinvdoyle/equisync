from .models import Notification

def send_notification(user, message):
    """Creates a notification for a specific user."""
    Notification.objects.create(user=user, message=message)
