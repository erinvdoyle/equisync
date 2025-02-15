from django.urls import path
from .views import calendar_view, add_event

app_name = 'competitions'

urlpatterns = [
    path('', calendar_view, name='calendar_view'),
    path('add/', add_event, name='add_event'),
]