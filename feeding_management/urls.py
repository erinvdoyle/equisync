from django.urls import path
from . import views

app_name = 'feeding_management'

urlpatterns = [
    path(
        'horse/<int:horse_id>/feeding/',
        views.horse_feeding_chart, name='horse_feeding_chart'),
    path(
        'horse/<int:horse_id>/feeding/readonly/',
        views.horse_feeding_chart_readonly, name='horse_feeding_chart_readonly'
        ),
    path('all/', views.all_horses_feeding, name='all_horses_feeding'),
    path(
        'admin/approvals/',
        views.pending_feeding_approvals, name='pending_feeding_approvals'),
]
