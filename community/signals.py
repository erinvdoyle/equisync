from community.announcements.models import Announcement
from community.ads.models import Ad
from community.models import Comment, CommunityEvent
from competitions.models import Event as CompetitionEvent
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
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


def get_approvers():
    """
    Returns all users who can approve content:
    - is_staff (Django admins)
    - OR profile.role == "Barn Manager"
    """
    return User.objects.filter(
        is_active=True
    ).filter(
        Q(is_staff=True) |
        Q(profile__role='Barn Manager')
    )


@receiver(post_save, sender=Ad)
def notify_admin_new_ad(sender, instance, created, **kwargs):
    if created and not instance.approved:
        message = (
            f"New ad submitted by {instance.user.username} — needs approval"
        )
        for approver in get_approvers():
            send_notification(approver, message)


@receiver(post_save, sender=Announcement)
def notify_admin_new_announcement(sender, instance, created, **kwargs):
    if created and not instance.approved:
        message = (
            f"New announcement from {instance.user.username} — "
            f"pending approval"
        )
        for approver in get_approvers():
            send_notification(approver, message)


@receiver(post_save, sender=CommunityEvent)
def notify_admin_new_event(sender, instance, created, **kwargs):
    if created and not instance.approved:
        message = (
            f"New event: '{instance.title}' — awaiting approval"
        )
        for approver in get_approvers():
            send_notification(approver, message)


@receiver(pre_save, sender=Ad)
@receiver(pre_save, sender=Announcement)
@receiver(pre_save, sender=CommunityEvent)
@receiver(pre_save, sender=CompetitionEvent)
def store_original_approval_state(sender, instance, **kwargs):
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)
        instance._was_approved = original.approved
    else:
        instance._was_approved = False


@receiver(post_save, sender=Ad)
def notify_user_ad_approved(sender, instance, created, **kwargs):
    if not created and instance.approved and not getattr(
        instance, '_was_approved', False
    ):
        title = instance.title or 'Ad'
        message = f"Your ad '{title}' has been approved!"
        send_notification(instance.user, message)


@receiver(post_save, sender=Announcement)
def notify_user_announcement_approved(sender, instance, created, **kwargs):
    if not created and instance.approved and not getattr(
        instance, '_was_approved', False
    ):
        send_notification(
            instance.user,
            "Your announcement has been approved!"
        )


@receiver(post_save, sender=CommunityEvent)
def notify_user_event_approved(sender, instance, created, **kwargs):
    if not created and instance.approved and not getattr(
        instance, '_was_approved', False
    ):
        message = (
            f"Your community event '{instance.title}' has been approved!"
        )
        send_notification(instance.created_by, message)


@receiver(post_save, sender=CompetitionEvent)
def notify_user_competition_event_approved(
    sender, instance, created, **kwargs
):
    if not created and instance.approved and not getattr(
        instance, '_was_approved', False
    ):
        message = (
            f"Your competition event '{instance.title}' has been approved!"
        )
        send_notification(instance.created_by, message)
