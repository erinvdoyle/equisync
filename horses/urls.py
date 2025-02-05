from django.urls import path
from . import views

urlpatterns = [
    path('<int:horse_id>/', views.horse_profile, name='horse_profile'),
    path('add/', views.add_horse, name='add_horse'),
    path('edit/<int:horse_id>/', views.edit_horse_profile, name='edit_horse_profile'),
    path('delete/<int:horse_id>/', views.delete_horse, name='delete_horse'),
]