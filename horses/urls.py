from django.urls import path
from . import views

app_name = 'horses'

urlpatterns = [
    path('', views.horse_list, name='horse_list'),
    path('<int:horse_id>/', views.horse_profile, name='horse_profile'),
    path('add/', views.add_horse, name='add_horse'),
    path('edit/<int:horse_id>/', views.edit_horse_profile, name='edit_horse_profile'),
    path('delete/<int:horse_id>/', views.delete_horse, name='delete_horse'),
    path('horse/<int:horse_id>/', views.horse_profile, name='horse_profile'),
    path('admin/pending-horses/', views.pending_horses, name='pending_horses'),
    path('admin/approve-horse/<int:horse_id>/', views.approve_horse, name='approve_horse'),
]