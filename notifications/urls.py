from django.urls import path
from notifications.views import (
    mark_as_read,
    mark_notification_as_read,
    notification_detail,
    notifications_list,
)

urlpatterns = [
    path('', notifications_list, name='notifications_list'),
    path(
        '<int:notification_id>/', notification_detail,
        name='notification_detail'),
    path(
        'mark-as-read/<int:notification_id>/',
        mark_as_read,
        name='mark_user_notification_as_read'
    ),
    path(
        'mark-as-read/<int:notification_id>/',
        mark_notification_as_read,
        name='mark_notification_as_read'
    ),
]