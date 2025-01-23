from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm


# Create your views here.
def community(request):
    return render(request, 'community/community.html')


@login_required
def submit_ad(request):
    return render(request, 'ads/submit_ad.html', {'form': form})