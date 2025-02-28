from django.urls import path
from .views import mark_as_read
from .views import notifications_list, notification_detail, mark_notification_as_read
from notifications.views import mark_notification_as_read


urlpatterns = [
    path('', notifications_list, name='notifications_list'),
    path('<int:notification_id>/', notification_detail, name='notification_detail'),
    path('mark-as-read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
    path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_user_notification_as_read'),
]
