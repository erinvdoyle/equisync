from django.urls import path
from . import views

urlpatterns = [
    path('horse/<int:horse_id>/feeding/', views.horse_feeding_chart, name='horse_feeding_chart'),
    path('feeding/all/', views.all_horses_feeding, name='all_horses_feeding'),
]
