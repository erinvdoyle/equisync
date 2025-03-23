from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.utils import send_notification


@receiver(post_save, sender=Comment)
def notify_comment(sender, instance, created, **kwargs):
    if created:
        recipient = instance.content_object.user
        message = (
            f"{instance.user.username} commented on your post: "
            f"'{instance.content_object}'"
        )
        send_notification(recipient, message)

