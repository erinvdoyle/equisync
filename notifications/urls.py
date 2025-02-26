from django.urls import path
from .views import mark_as_read
from .views import notifications_list

urlpatterns = [
    path("mark-read/<int:notification_id>/", mark_as_read, name="mark_as_read"),
    path('', notifications_list, name='notifications_list'),
]
