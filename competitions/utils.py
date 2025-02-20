from django.utils import timezone
from .models import Event, EventHorse, Notification

def create_notifications_for_past_events():
    now = timezone.now()
    past_events = Event.objects.filter(end_time__lt=now)

    for event in past_events:
        for event_horse in EventHorse.objects.filter(event=event):
            user = event_horse.horse.owner
            message = f"Please update the results and notes for {event_horse.horse.name} in {event.title}."
            Notification.objects.get_or_create(user=user, event_horse=event_horse, message=message)
