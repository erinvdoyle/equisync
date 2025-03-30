from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from feeding_management.models import FeedingChart
from notifications.utils import send_notification


@receiver(pre_save, sender=FeedingChart)
def cache_last_updater(sender, instance, **kwargs):
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)
        instance._previous_updater = original.last_updated_by


@receiver(post_save, sender=FeedingChart)
def notify_owner_on_feeding_chart_update(sender, instance, created, **kwargs):
    if not created:
        updater = instance.last_updated_by
        owner = instance.horse.owner

        if updater and updater != owner:
            message = (
                f"The feeding chart for your horse {instance.horse.name} was "
                f"updated "
                f"by {updater.get_full_name() or updater.username}."
            )
            send_notification(owner, message)
