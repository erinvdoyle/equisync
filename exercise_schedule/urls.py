from django.urls import path
from . import views

app_name = 'exercise_schedule'

urlpatterns = [
    path('daily/', views.daily_schedule_view, name='daily_schedule_view'),
    path('daily/<str:date>/', views.daily_schedule_view, name='daily_schedule_view_date'),
    path('weekly/', views.weekly_schedule_view, name='weekly_schedule_view'),
    path('weekly/<str:date>/', views.weekly_schedule_view, name='weekly_schedule_view_date'),
    path('archive/', views.archive_schedule_view, name='archive_schedule_view'),
    path('create/', views.create_schedule_entry, name='create_schedule_entry'),
    path('horse/<int:horse_id>/exercise/', views.horse_exercise_schedule_view, name='horse_exercise_schedule'),
]
