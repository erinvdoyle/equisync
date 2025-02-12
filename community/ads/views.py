from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm
from django.urls import reverse
from community.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from community.models import Comment


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
            return render(request, 'ads/preview_ad.html', {'ad': ad, 'form': form}) 
    else:
        form = AdForm()

    return render(request, 'ads/submit_ad.html', {'form': form})


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect(reverse('community:community_overview'))
    else:
        form = AdForm(instance=ad)

    return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})

@login_required
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    content_type = ContentType.objects.get_for_model(Ad)
    comments = Comment.objects.filter(content_type=content_type, object_id=ad_id).order_by('-created_at')
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_type = content_type
            comment.object_id = ad_id
            comment.user = request.user
            comment.content_object = ad
            comment.save()
            return redirect('community:ad_detail', ad_id=ad_id)
    else:
        form = CommentForm()

    return render(request, 'ads/ad_detail.html', {
        'ad': ad,
        'comments': comments,
        'form': form,
        'content_type': content_type,
    })