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
]