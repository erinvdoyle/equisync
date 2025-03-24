from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from django.contrib.auth import get_user_model
from competitions.models import Event
from notifications.utils import send_notification

User = get_user_model()


def get_approvers():
    """Return users who are admins or Barn Managers."""
    return User.objects.filter(
        is_active=True
    ).filter(
        Q(is_staff=True) |
        Q(profile__role='Barn Manager')
    )


@receiver(post_save, sender=Event)
def notify_admins_of_new_event(sender, instance, created, **kwargs):
    if created and not instance.approved:
        message = f"New event '{instance.title}' submitted by {instance.created_by.username} — pending approval."
        for approver in get_approvers():
            send_notification(approver, message)

@receiver(post_save, sender=Event)
def notify_creator_on_approval(sender, instance, created, **kwargs):
    if not created and instance.approved:
        if 'approved' in instance.__dict__ and instance.__dict__.get('approved') is False:
            return
        message = f"Your event '{instance.title}' has been approved!"
        send_notification(instance.created_by, message)
