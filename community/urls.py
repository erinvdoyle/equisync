from django.urls import path
from .ads.views import submit_ad
from .announcements.views import submit_announcement, edit_announcement  
from .views import community_overview
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('ads/submit/', submit_ad, name='submit_ad'),
    path('announcements/edit/', edit_announcement, name='edit_announcement'),
    path('announcements/submit/', submit_announcement, name='submit_announcement'),
    path('', community_overview, name='community_overview'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)