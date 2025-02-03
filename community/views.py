from django.shortcuts import render
from .ads.models import Ad
from .announcements.models import Announcement
from django.core.paginator import Paginator
from .filters import AdFilter


def community_overview(request):
    ads = Ad.objects.filter(approved=True).order_by('-date_posted')

    ad_filter = AdFilter(request.GET, queryset=ads)

    paginator = Paginator(ad_filter.qs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    announcements = Announcement.objects.filter(approved=True)

    return render(request, 'community/community.html', {
        "filter": ad_filter,
        "page_obj": page_obj, 
        'announcements': announcements,
    })