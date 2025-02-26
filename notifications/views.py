from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect("notifications_list")


@login_required
def notifications_list(request):
    notifications = request.user.notifications.all()
    return render(request, "notifications/notifications_list.html", {"notifications": notifications})

@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    
    if not notification.is_read:
        notification.is_read = True
        notification.save()
    
    return render(request, "notifications/notification_detail.html", {"notification": notification})
