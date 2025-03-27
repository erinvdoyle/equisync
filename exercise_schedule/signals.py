from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import ExerciseScheduleItem
from notifications.models import Notification
from notifications.utils import send_notification


@receiver(post_save, sender=ExerciseScheduleItem)
def notify_owner_on_exercise(sender, instance, created, **kwargs):
    if not created:
        return

    horse = instance.schedule.horse
    owner = horse.owner
    creator = instance.schedule.created_by

    if owner == creator:
        return

    exercise_type = instance.get_exercise_type_display()
    duration = instance.duration
    date_str = instance.schedule.date.strftime('%b %d, %Y')

    message = (
        f"{creator.get_full_name() or creator.username} "
        f"logged a {exercise_type.lower()} session for {horse.name} "
        f"({duration} min) on {date_str}."
    )

    already_notified = Notification.objects.filter(
        user=owner,
        message__icontains=f"{exercise_type.lower(
            )} session for {horse.name.lower()} on {date_str}",
        is_read=False
    ).exists()

    if not already_notified:
        send_notification(owner, message)

    if exercise_type.lower() == 'ride':
        horse.most_recent_ride = creator
        horse.last_ridden_at = now()
    else:
        horse.most_recent_care = creator
        horse.last_cared_for_at = now()

    horse.save(update_fields=[
        "most_recent_ride", "last_ridden_at",
        "most_recent_care", "last_cared_for_at"
    ])
