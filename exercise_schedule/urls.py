from django.urls import path
from . import views
from .views import exercise_details_view, weekly_exercise_schedule, add_appointment_view, appointment_details_view

app_name = 'exercise_schedule'

urlpatterns = [
    path('daily/', views.daily_schedule_view, name='daily_schedule_view'),
    path('daily/<str:date>/', views.daily_schedule_view, name='daily_schedule_view_date'),
    path('weekly/', views.weekly_schedule_view, name='weekly_schedule_view'),
    path('weekly/<str:date>/', views.weekly_schedule_view, name='weekly_schedule_view_date'),
    path('archive/', views.archive_schedule_view, name='archive_schedule_view'),
    path('create/', views.create_schedule_entry, name='create_schedule_entry'),
    path('horse/<int:horse_id>/exercise/', views.horse_exercise_schedule_view, name='horse_exercise_schedule'),
    path('details/<int:schedule_id>/', exercise_details_view, name='exercise_details'),
    path('horse/<int:horse_id>/weekly_exercise_schedule/', weekly_exercise_schedule, name='weekly_exercise_schedule'),
    path('add_appointment/', views.add_appointment_view, name='add_appointment'),
    path('appointments/<str:horse_name>/<str:date_str>/', views.appointment_details_view, name='appointment_details'),

]
