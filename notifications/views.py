from django.shortcuts import redirect, render
from .models import Notification

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect("notifications_list")

def notifications_list(request):
    notifications = request.user.notifications.all().order_by("-created_at")
    return render(request, "notifications/notifications_list.html", {"notifications": notifications})
