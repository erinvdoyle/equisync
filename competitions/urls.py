from django.urls import path
from . import views
from .views import event_detail, edit_event_horse, remove_event_horse, horse_results_archive
from competitions.views import mark_event_notification_as_read


app_name = 'competitions'

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('add/', views.add_event, name='add_event'),
    path('favorite/<int:event_id>/', views.favorite_event, name='favorite_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('month/<int:year>/<int:month>/', views.calendar_view, name='month_view'),
    path('week/<int:year>/<int:month>/<int:day>/', views.week_view, name='week_view'),
    path('day/<int:year>/<int:month>/<int:day>/', views.day_view, name='day_view'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events_json/', views.events_json, name='events_json'),
    path('event-horse/edit/<int:event_horse_id>/', edit_event_horse, name='edit_event_horse'),
    path('event-horse/remove/<int:event_horse_id>/', remove_event_horse, name='remove_event_horse'),
    path('event-horse/edit/<int:event_horse_id>/<str:source>/', edit_event_horse, name='edit_event_horse_source'),
    path('horse/<int:horse_id>/results/', views.horse_results_archive, name='horse_results_archive'),
    path('mark-read/event/<int:notification_id>/', mark_event_notification_as_read, name='mark_event_notification_as_read'),
]