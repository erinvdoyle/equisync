"""
URL configuration for equisync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from horses import views as horses_views
from users import views

urlpatterns = [
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('community/', include('community.urls', namespace='community')),
    path('competitions/', include(
            'competitions.urls', namespace='competitions')),
    path(
        'delete/<int:horse_id>/',
        horses_views.delete_horse, name='delete_horse'),
    path('exercise_schedule/', include('exercise_schedule.urls')),
    path('feeding/', include('feeding_management.urls')),
    path('horses/', include('horses.urls')),
    path('notifications/', include('notifications.urls')),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
