from django.db.models.signals import post_save
from django.dispatch import receiver
from horses.models import HorseProfile
from feeding_management.models import FeedingChart
from notifications.utils import send_notification


@receiver(post_save, sender=HorseProfile)
def notify_and_create_chart_on_approval(sender, instance, created, **kwargs):

    if not created:

        try:
            previous = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            previous = None

        if previous and not previous.approved and instance.approved:

            send_notification(
                instance.owner,
                f"Your horse {instance.name} has been approved!")

            FeedingChart.objects.get_or_create(horse=instance)
