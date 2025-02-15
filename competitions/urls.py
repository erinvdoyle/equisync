from django.urls import path
from . import views
from .views import calendar_view, add_event, favorite_event, edit_event, delete_event

app_name = 'competitions'

urlpatterns = [
    path('', calendar_view, name='calendar_view'),
    path('add/', add_event, name='add_event'),
    path('favorite/<int:event_id>/', views.favorite_event, name='favorite_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('month/<int:year>/<int:month>/', views.calendar_view, name='month_view'),
    path('week/<int:year>/<int:month>/<int:day>/', views.week_view, name='week_view'),
    path('day/<int:year>/<int:month>/<int:day>/', views.day_view, name='day_view'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]