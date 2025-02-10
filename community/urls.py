from django.urls import path
from . import views
from .ads.views import submit_ad, edit_ad
from .announcements.views import submit_announcement, edit_announcement  
from .views import community_overview
# from django.conf import settings
# from django.conf.urls.static import static  

app_name = 'community'

urlpatterns = [
    path('ads/submit/', submit_ad, name='submit_ad'),
    path('ads/edit/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('announcements/edit/<int:announcement_id>/', edit_announcement, name='edit_announcement'),
    path('announcements/submit/', submit_announcement, name='submit_announcement'),
    path('', community_overview, name='community_overview'),  
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)