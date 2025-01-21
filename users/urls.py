from django.urls import path
from . import views
from .views import view_profile, edit_profile, index

urlpatterns = [
    path('', index, name='index'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]