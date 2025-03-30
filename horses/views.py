from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HorseProfile
from .forms import HorseForm
from users.models import Profile
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from notifications.models import Notification
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
import cloudinary
from feeding_management.models import FeedingChart
from exercise_schedule.models import ExerciseSchedule
from competitions.models import EventHorse
from notifications.utils import send_notification
from django.contrib.auth import get_user_model
from django.db.models import Q


@login_required
def horse_profile(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    profiles = Profile.objects.filter(user=horse.owner)

    has_feeding_chart = FeedingChart.objects.filter(horse=horse).exists()
    has_exercise_schedule = ExerciseSchedule.objects.filter(
        horse=horse).exists()
    has_competition_results = EventHorse.objects.filter(horse=horse).exists()

    context = {
        'horse': horse,
        'profiles': profiles,
        'has_feeding_chart': has_feeding_chart,
        'has_exercise_schedule': has_exercise_schedule,
        'has_competition_results': has_competition_results,
    }
    return render(request, 'horses/horse_profile.html', context)


@login_required
def edit_horse_profile(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)

    if request.user != horse.owner and not request.user.is_staff:
        messages.error(request, "You are not authorized to edit this horse.")
        return redirect('horses:horse_profile', horse_id=horse.id)

    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES, instance=horse)
        if form.is_valid():
            form.save()
            messages.success(request, "Horse updated successfully.")
            return redirect('horses:horse_profile', horse_id=horse.id)
    else:
        form = HorseForm(instance=horse)

    return render(
        request,
        'horses/edit_horse_profile.html',
        {'form': form, 'horse': horse}
    )


User = get_user_model()


@login_required
def add_horse(request):
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES)
        if form.is_valid():
            horse = form.save(commit=False)
            horse.owner = request.user
            horse.barn_manager = request.user
            horse.rider = request.user
            horse.save()
            form.save_m2m()
            horse.staff.add(request.user)

            messages.success(
                request,
                f"Your horse has been submitted for admin approval. "
                f"You will receive notification once your barn manager has "
                f"approved and set your horse's feeding chart"
            )

            approvers = User.objects.filter(
                Q(is_staff=True) | Q(profile__role="Barn Manager")
            ).distinct()

            for approver in approvers:

                already_notified = Notification.objects.filter(
                    user=approver,
                    is_read=False
                ).filter(
                    Q(message__icontains=horse.name) & Q(
                        message__icontains="awaiting approval")
                ).exists()

                if not already_notified:
                    Notification.objects.create(
                        user=approver,
                        message=(
                            f"{request.user.get_full_name() "
                            f"or request.user.username} "
                            f"added a new horse '{horse.name}' "
                            f"that is awaiting approval. "
                            f"Please set their feeding chart"
                        )
                    )

            return redirect('horses:horse_profile', horse_id=horse.id)
        else:
            messages.error(
                request,
                "There was an error saving your horse. Please " +
                "check the form below."
            )
    else:
        form = HorseForm()

    return render(request, 'horses/add_horse.html', {'form': form})


@login_required
def delete_horse(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    horse_name = horse.name
    horse.delete()
    messages.success(request, f"{horse_name} has been deleted")
    return redirect('horses:horse_list')


def horse_list(request):
    horses = HorseProfile.objects.filter(approved=True)
    return render(request, 'horses/horse_list.html', {'horses': horses})


@staff_member_required
def pending_horses(request):
    horses = HorseProfile.objects.filter(approved=False)
    return render(request, 'horses/pending_horses.html', {'horses': horses})


@staff_member_required
def approve_horse(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)

    if not horse.approved:
        horse.approved = True
        horse.save()
        print(f"Approved: {horse.name} (ID {horse.id})")

        if not FeedingChart.objects.filter(horse=horse).exists():
            FeedingChart.objects.create(horse=horse)
            print(f"Feeding chart created for {horse.name}")
        else:
            print(f"Feeding chart already exists for {horse.name}")

        send_notification(
            horse.owner,
            f"Your horse '{horse.name}' has been approved by admin")
        print(f"📨 Notification sent to {horse.owner.username}")
    else:
        print(f"🔁 Horse {horse.name} was already approved")

    messages.success(request, f"{horse.name} has been approved")
    return redirect('horses:pending_horses')