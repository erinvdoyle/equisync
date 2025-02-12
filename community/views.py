from django.shortcuts import render, get_object_or_404, redirect
from .ads.models import Ad
from .announcements.models import Announcement, Reaction
from django.core.paginator import Paginator
from django_filters.views import FilterView
from .filters import AdFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Count, OuterRef, Exists, BooleanField
from django.db.models import Case, When
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentForm


def community_overview(request):
    ads = Ad.objects.filter(approved=True).order_by('-date_posted')
    ad_filter = AdFilter(request.GET, queryset=ads)

    paginator = Paginator(ad_filter.qs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    announcements = Announcement.objects.filter(approved=True)

    most_clicked_emojis = {}
    for announcement in announcements:
        most_clicked_emoji = Reaction.objects.filter(announcement=announcement).values('emoji').annotate(emoji_count=Count('emoji')).order_by('-emoji_count').first()
        most_clicked_emojis[announcement.id] = most_clicked_emoji['emoji'] if most_clicked_emoji else None

    user_reactions = {}
    if request.user.is_authenticated:
        for announcement in announcements:
            reactions = Reaction.objects.filter(user=request.user, announcement=announcement).values_list('emoji', flat=True)
            user_reactions[announcement.id] = list(reactions)
            
    content_type_ad = ContentType.objects.get_for_model(Ad)
    content_type_announcement = ContentType.objects.get_for_model(Announcement)

    return render(request, 'community/community.html', {
        "filter": ad_filter,
        "page_obj": page_obj,
        'announcements': announcements,
        'most_clicked_emojis': most_clicked_emojis,
        'user_reactions': user_reactions,
        'content_type_ad': content_type_ad,
        'content_type_announcement': content_type_announcement, 
    })
    
@login_required
def add_comment(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    obj = get_object_or_404(content_type.model_class(), id=object_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                content_type=content_type,
                object_id=object_id,
                content_object=obj,
                user=request.user,
                text=form.cleaned_data['text']
            )
            comment.save()
            return redirect(obj.get_absolute_url())
    else:
        form = CommentForm()

    return render(request, 'community/add_comment.html', {'form': form, 'object': obj})