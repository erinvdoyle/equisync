from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Profile
from .forms import ProfileForm
from horses.models import HorseProfile
from feeding_management.models import FeedingChart
from exercise_schedule.models import ExerciseSchedule
from community.ads.models import Ad
from community.announcements.models import Announcement
from competitions.models import Event, Notification, EventHorse
from competitions.utils import create_notifications_for_past_events 


@login_required
def view_profile(request):
    """
    gets the profile for the logged in user
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

def edit_profile(request):
    """
    allows the logged in user to edit profile
    """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})

def index(request):
    """
    renders the index template
    """
    return render(request, 'users/index.html')

@login_required
def dashboard(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    horses = HorseProfile.objects.filter(owner=user)
    feeding_charts = FeedingChart.objects.filter(horse__owner=user)
    exercise_schedules = ExerciseSchedule.objects.filter(horse__owner=user)
    ads = Ad.objects.filter(user=user)
    announcements = Announcement.objects.filter(user=user)
    favorite_events = Event.objects.filter(favorited_by=request.user)
    create_notifications_for_past_events() 
    notifications = Notification.objects.filter(user=request.user, read=False)
    competition_results = EventHorse.objects.filter(horse__owner=user)
    
    
    
    context = {
        'user': user,
        'profile': profile,
        'horses': horses,
        'feeding_charts': feeding_charts,
        'exercise_schedules': exercise_schedules,
        'ads': ads,
        'announcements': announcements,
        'favorite_events': favorite_events,
        'notifications': notifications,
        'competition_results': competition_results,
    }
    
    return render(request, 'users/dashboard.html', context)

@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    
    return redirect('users:dashboard')