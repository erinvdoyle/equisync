from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm


# Create your views here.
def community(request):
    return render(request, 'community/community.html')


@login_required
def submit_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  
            ad.save()
            return redirect('community_overview') 
    else:
        form = AdForm()

    return render(request, 'ads/submit_ad.html', {'form': form})