from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HorseProfile
from .forms import HorseForm
from users.models import Profile
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@login_required
def horse_profile(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    profiles = Profile.objects.filter(user=horse.owner)
    context = {'horse': horse, 'profiles': profiles}
    return render(request, 'horses/horse_profile.html', context)

@login_required
def edit_horse_profile(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES, instance=horse)
        if form.is_valid():
            form.save()
            return redirect('horse_profile', horse_id=horse.id)
    else:
        form = HorseForm(instance=horse)

    return render(request, 'horses/edit_horse_profile.html', {'form': form, 'horse': horse})

@login_required
def add_horse(request):
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES)
        if form.is_valid():
            horse = form.save(commit=False)
            return redirect('horse_profile', horse_id=horse.id)
    else:
        form = HorseForm()

    return render(request, 'horses/add_horse.html', {'form': form})

@login_required
def delete_horse(request, horse_id):
    horse = get_object_or_404(HorseProfile, id=horse_id)
    horse.delete()
    return redirect('community_overview')

def horse_list(request):
    horses = HorseProfile.objects.all()
    return render(request, 'horses/horse_list.html', {'horses': horses})