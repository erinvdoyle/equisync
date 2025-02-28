from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from horses.models import HorseProfile
from feeding_management.models import FeedingChart
from exercise_schedule.models import ExerciseSchedule
from community.ads.models import Ad
from community.announcements.models import Announcement
from competitions.models import Event, EventHorse
from competitions.utils import create_notifications_for_past_events
from django.core.paginator import Paginator
from notifications.models import Notification
from django.http import JsonResponse



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
    
    unread_notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    event_notifications = Notification.objects.filter(user=request.user, event_horse__isnull=False, is_read=False)
    user_notifications = Notification.objects.filter(user=request.user, event_horse__isnull=True, is_read=False)
    
    competition_results = {}
    for horse in horses:
        results = EventHorse.objects.filter(horse=horse).order_by('-event__start_time')
        competition_results[horse] = results
    
    paginated_results = {}
    for horse, results in competition_results.items():
        paginator = Paginator(results, 4)
        page_number = request.GET.get(f'page_{horse.id}')
        page_obj = paginator.get_page(page_number)
        paginated_results[horse] = page_obj
        
    print(f"Notifications count: {notifications.count()} for {user.username}")
    
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
        'paginated_results': paginated_results,
        'user_notifications': user_notifications,
        'event_notifications': event_notifications,
        'unread_notifications_count': unread_notifications_count,
    }
    
    return render(request, 'users/dashboard.html', context)

@login_required
def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return JsonResponse({'success': True})

