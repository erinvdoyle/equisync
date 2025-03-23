from django.urls import path, include
from . import views
from .ads.views import submit_ad, edit_ad, delete_ad
from .announcements.views import (
    submit_announcement,
    edit_announcement,
    delete_announcement,
)
from community.announcements import views as announcement_views
from .views import community_overview, create_event, edit_event, delete_event
from .ads import views as ads_views
from .announcements import views as announcement_views
from . import views_reactions

app_name = 'community'

urlpatterns = [
    path('', views.community_overview, name='community_overview'),
    path(
        'ads/delete/<int:ad_id>/',
        ads_views.delete_ad,
        name='delete_ad',
    ),
    path('ads/edit/', ads_views.edit_ad, name='edit_ad'),
    path(
        'ads/edit/<int:ad_id>/',
        ads_views.edit_ad,
        name='edit_ad_with_id',
    ),
    path('ads/', include([
        path('<int:ad_id>/', ads_views.ad_detail, name='ad_detail'),
        path('submit/', ads_views.submit_ad, name='submit_ad'),
    ])),
    path(
        'announcements/delete/<int:announcement_id>/',
        announcement_views.delete_announcement,
        name='delete_announcement',
    ),
    path(
        'announcements/edit/',
        announcement_views.edit_announcement,
        name='edit_announcement',
    ),
    path(
        'announcements/edit/<int:announcement_id>/',
        announcement_views.edit_announcement,
        name='edit_announcement_with_id',
    ),
    path(
        'announcements/preview/<int:announcement_id>/',
        announcement_views.preview_announcement,
        name='preview_announcement',
    ),
    path('announcements/', include([
        path(
            '<int:announcement_id>/',
            announcement_views.announcement_detail,
            name='announcement_detail',
        ),
        path(
            'submit/',
            announcement_views.submit_announcement,
            name='submit_announcement',
        ),
    ])),
    path(
        'comment/add/<int:content_type_id>/<int:object_id>/',
        views.add_comment,
        name='add_comment',
    ),
    path(
        'comment/delete/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment',
    ),
    path(
        'comment/edit/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment',
    ),
    path('create/', create_event, name='create_event'),
    path('delete-event/', delete_event, name='delete_event'),
    path('edit-event/', edit_event, name='edit_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path(
        'get-weekly-events/<int:year>/<int:month>/<int:day>/',
        views.get_weekly_events,
        name='get_weekly_events',
    ),
    path(
        'react/',
        views_reactions.react_to_announcement,
        name='react_to_announcement',
    ),
    path(
        'week/<int:year>/<int:month>/<int:day>/',
        views.community_overview,
        name='community_overview_week',
    ),
]