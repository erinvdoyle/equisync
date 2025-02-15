from django.urls import path
from . import views

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
]
