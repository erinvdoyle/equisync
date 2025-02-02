"""
URL configuration for equisync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from community.ads.views import submit_ad, edit_ad
from community.announcements.views import submit_announcement, edit_announcement
from community.views import community_overview
from users import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', include('users.urls')),
    path('community/', community_overview, name='community_overview'),
    path('community/submit_ad/', submit_ad, name='submit_ad'),
    path('community/edit_ad/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('community/submit_announcement/', submit_announcement, name='submit_announcement'),
    path('community/edit_announcement/<int:announcement_id>/', edit_announcement, name='edit_announcement'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
