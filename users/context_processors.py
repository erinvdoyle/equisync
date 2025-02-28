from notifications.models import Notification

def unread_notifications_count(request):
    if request.user.is_authenticated:
        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {'unread_notifications_count': count}
    return {'unread_notifications_count': 0}

# def unread_notifications(request):
#     if request.user.is_authenticated:
#         return {'unread_notifications': Notification.objects.filter(user=request.user, is_read=False).count()}
#     return {'unread_notifications': 0}