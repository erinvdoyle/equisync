from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Announcement, Reaction
from .forms import AnnouncementForm
from community.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from community.models import Comment
from django.contrib import messages


@login_required
def submit_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user  
            announcement.save()
            return redirect('community:preview_announcement', announcement_id=announcement.id)  
    else:
        form = AnnouncementForm()

    return render(request, 'announcements/submit_announcement.html', {'form': form})

@login_required
def edit_announcement(request, announcement_id=None):
    user_announcements = Announcement.objects.filter(user=request.user)
    selected_announcement = None

    if announcement_id:
        selected_announcement = get_object_or_404(Announcement, id=announcement_id, user=request.user)
        form = AnnouncementForm(instance=selected_announcement)
    else:
        form = AnnouncementForm()

    if request.method == 'POST':
        announcement_id = request.POST.get("announcement_id")
        if announcement_id:
            selected_announcement = get_object_or_404(Announcement, id=announcement_id, user=request.user)
            form = AnnouncementForm(request.POST, request.FILES, instance=selected_announcement)
            if form.is_valid():
                form.save()
                messages.success(request, "Your announcement has been updated")
                return redirect('community:community_overview')
        else:
            form = AnnouncementForm()

    return render(request, 'announcements/edit_announcement.html', {
        'form': form,
        'user_announcements': user_announcements,
        'selected_announcement': selected_announcement
    })

def community_overview(request):
    ads = Ad.objects.filter(approved=True)  
    announcements = Announcement.objects.all()  

    return render(request, 'community/community_overview.html', {
        'ads': ads,
        'announcements': announcements,
    })

@login_required
def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    content_type = ContentType.objects.get_for_model(Announcement)
    comments = Comment.objects.filter(content_type=content_type, object_id=announcement_id).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_type = content_type
            comment.object_id = announcement_id
            comment.user = request.user
            comment.content_object = announcement
            comment.save()
            
            messages.success(request, "Your comment has been added")
            
            return redirect('community:announcement_detail', announcement_id=announcement_id)
    else:
        form = CommentForm()

    return render(request, 'announcements/announcement_detail.html', {
        'announcement': announcement,
        'comments': comments,
        'form': form,
        'content_type': content_type,
    })
    
@login_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id, user=request.user)
    
    if request.method == "POST":
        announcement.delete()
        messages.success(request, "Your announcement has been deleted")
        return redirect('community:community_overview')
    
    return render(request, "announcements/confirm_delete_announcement.html", {"announcement": announcement})

@login_required
def preview_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)

    if request.method == "POST":
        messages.success(request, "Your announcement has been submitted for approval")
        return redirect("community:community_overview")

    return render(request, "announcements/preview_announcement.html", {
        "announcement": announcement
    })

