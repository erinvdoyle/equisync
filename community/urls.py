from django.urls import path
from .ads.views import submit_ad  
from .announcements.views import submit_announcement  
from .views import community_overview  

urlpatterns = [
    path('ads/submit/', submit_ad, name='submit_ad'),
    path('announcements/submit/', submit_announcement, name='submit_announcement'),
    path('', community_overview, name='community_overview'),  
]
