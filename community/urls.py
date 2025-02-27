from django.urls import path, include
from . import views
from .ads.views import submit_ad, edit_ad
from .announcements.views import submit_announcement, edit_announcement  
from .views import community_overview, create_event
from .ads import views as ads_views
from .announcements import views as announcement_views
from . import views_reactions

# from django.conf import settings
# from django.conf.urls.static import static  

app_name = 'community'

urlpatterns = [
    path('ads/', include([
        path('submit/', ads_views.submit_ad, name='submit_ad'),
        path('edit/<int:ad_id>/', ads_views.edit_ad, name='edit_ad'),
        path('<int:ad_id>/', ads_views.ad_detail, name='ad_detail'),
    ])),
    path('announcements/', include([
        path('submit/', announcement_views.submit_announcement, name='submit_announcement'),
        path('edit/<int:announcement_id>/', announcement_views.edit_announcement, name='edit_announcement'),
        path('<int:announcement_id>/', announcement_views.announcement_detail, name='announcement_detail'),
    ])),
    path('react/', views_reactions.react_to_announcement, name='react_to_announcement'),
    path('', views.community_overview, name='community_overview'),
    path('comment/add/<int:content_type_id>/<int:object_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('create/', create_event, name='create_event'),
    # path('this-week/', views.this_weeks_events, name='this_week_events'),
    path('week/<int:year>/<int:month>/<int:day>/', views.community_overview, name='community_overview_week'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('get-weekly-events/<int:year>/<int:month>/<int:day>/', views.get_weekly_events, name='get_weekly_events'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)