from django.shortcuts import render
from .ads.models import Ad
from .announcements.models import Announcement

def community_overview(request):
    ads = Ad.objects.filter(approved=True)
    announcements = Announcement.objects.filter(approved=True)

    return render(request, 'community/community.html', {
        'ads': ads,
        'announcements': announcements,
    })