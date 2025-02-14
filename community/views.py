import datetime
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
from .models import Comment, CommunityEvent
from .forms import CommentForm
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string

def community_overview(request, year=None, month=None, day=None):
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
    
    ad_comment_counts = {}
    for ad in ads:
        content_type = ContentType.objects.get_for_model(Ad)
        ad_comment_counts[ad.id] = Comment.objects.filter(content_type=content_type, object_id=ad.id).count()

    announcement_comment_counts = {}
    for announcement in announcements:
        content_type = ContentType.objects.get_for_model(Announcement)
        announcement_comment_counts[announcement.id] = Comment.objects.filter(content_type=content_type, object_id=announcement.id).count()
        
    today = timezone.now().date()
    
    if year and month and day:
        current_date = datetime.date(year, month, day)
    else:
        current_date = today

    start_of_week = current_date - timezone.timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timezone.timedelta(days=6)

    community_events = CommunityEvent.objects.filter(date__range=[start_of_week, end_of_week], approved=True)
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    previous_week = start_of_week - timezone.timedelta(days=7)
    next_week = start_of_week + timezone.timedelta(days=7)

    context = {
        'filter': ad_filter,
        'page_obj': page_obj,
        'announcements': announcements,
        'most_clicked_emojis': most_clicked_emojis,
        'user_reactions': user_reactions,
        'content_type_ad': content_type_ad,
        'content_type_announcement': content_type_announcement,
        'ad_comment_counts': ad_comment_counts,
        'announcement_comment_counts': announcement_comment_counts,
        'community_events': community_events,
        'days_of_week': days_of_week,
        'previous_week': previous_week,
        'next_week': next_week,
    }

    return render(request, 'community/community.html', context)

def get_weekly_events(request, year, month, day):
    current_date = datetime.date(year, month, day)
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    community_events = CommunityEvent.objects.filter(date__range=[start_of_week, end_of_week], approved=True)
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    html = render_to_string('community/weekly_events.html', {
        'community_events': community_events,
        'days_of_week': days_of_week
    })
    return JsonResponse({'html': html})
    
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

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(comment.content_object.get_absolute_url())
    else:
        form = CommentForm(instance=comment)

    return render(request, 'community/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    content_object_url = comment.content_object.get_absolute_url()

    comment.delete()
    return redirect(content_object_url)

def this_weeks_events(request):
    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())
    end_of_week = start_of_week + timezone.timedelta(days=6)
    
    community_events = CommunityEvent.objects.filter(date__range=[start_of_week, end_of_week], approved=True)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


    return render(request, 'community/this_weeks_events.html', {
        'community_events': community_events,
        'days_of_week': days_of_week,
    })


@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')

        event = CommunityEvent.objects.create(
            title=title,
            description=description,
            date=date,
            time=time if time else None,
            created_by=request.user
        )
        return redirect('community:community_overview')
    else:
        return render(request, 'community/create_event.html')
    
def event_detail(request, event_id):
    event = get_object_or_404(CommunityEvent, pk=event_id)
    return render(request, 'community/event_detail.html', {'event': event})
