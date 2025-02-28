from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification
from notifications.utils import send_notification
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def mark_as_read(request, notification_id):
    if request.method == "POST":
        notification = get_object_or_404(Notification, id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

@login_required
@csrf_exempt
def mark_notification_as_read(request, notification_id):
    if request.method == "POST":
        try:
            notification = Notification.objects.get(id=notification_id, user=request.user)
            notification.is_read = True
            notification.save()
            return JsonResponse({"success": True, "message": "Notification marked as read."})
        except Notification.DoesNotExist:
            return JsonResponse({"success": False, "message": "Notification not found."})
    return JsonResponse({"success": False, "message": "Invalid request."})

@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})

@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    
    if not notification.is_read:
        notification.is_read = True
        notification.save()
    
    return render(request, "notifications/notification_detail.html", {"notification": notification})
