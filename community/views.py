from django.shortcuts import render
from .ads.models import Ad

def community_overview(request):
    ads = Ad.objects.filter(approved=True)

    return render(request, 'community/community.html', {
        'ads': ads,
    })