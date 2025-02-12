from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Announcement, Reaction
from .forms import AnnouncementForm

@login_required
def submit_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user  
            announcement.save()
            return render(request, 'announcements/preview_announcement.html', {'announcement': announcement, 'form': form})  
    else:
        form = AnnouncementForm()

    return render(request, 'announcements/submit_announcement.html', {'form': form})

@login_required
def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id) 
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)  
        if form.is_valid():
            form.save()  
            return redirect('community_overview')  
    else:
        form = AnnouncementForm(instance=announcement) 

    return render(request, 'announcements/edit_announcement.html', {'form': form, 'announcement': announcement})

def community_overview(request):
    ads = Ad.objects.filter(approved=True)  
    announcements = Announcement.objects.all()  

    return render(request, 'community/community_overview.html', {
        'ads': ads,
        'announcements': announcements,
    })

def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})