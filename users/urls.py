from django.urls import path
from . import views
from .views import view_profile, edit_profile, index

app_name = 'users'

urlpatterns = [
    path('', index, name='home'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]