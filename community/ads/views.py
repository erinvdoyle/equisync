from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm
from django.urls import reverse
from community.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from community.models import Comment
from django.contrib import messages


def community(request):
    return render(request, 'community/community.html')


@login_required
def submit_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  
            
            if 'preview' in request.POST:
                return render(request, 'ads/preview_ad.html', {'ad': ad, 'form': form})
            
            ad.save()
            messages.success(request, "Your ad has been submitted for admin approval")
            return redirect('community:community_overview')
    else:
        form = AdForm()

    return render(request, 'ads/submit_ad.html', {'form': form})

@login_required
def edit_ad(request, ad_id=None):
    user_ads = Ad.objects.filter(user=request.user)
    selected_ad = None

    if ad_id:
        selected_ad = get_object_or_404(Ad, id=ad_id, user=request.user)
        form = AdForm(instance=selected_ad)
    else:
        form = AdForm()

    if request.method == 'POST':
        ad_id = request.POST.get("ad_id")
        if ad_id:
            selected_ad = get_object_or_404(Ad, id=ad_id, user=request.user)  
            form = AdForm(request.POST, request.FILES, instance=selected_ad)
            if form.is_valid():
                form.save()
                return redirect('community:community_overview')
        else:
            form = AdForm()

    return render(request, 'ads/edit_ad.html', {
        'form': form,
        'user_ads': user_ads,
        'selected_ad': selected_ad
    })
   
@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    ad.delete()
    messages.success(request, "Your ad has been deleted")
    return redirect('community:community_overview')

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
            
            messages.success(request, "Your comment was added")
            
            return redirect('community:ad_detail', ad_id=ad_id)
    else:
        form = CommentForm()

    return render(request, 'ads/ad_detail.html', {
        'ad': ad,
        'comments': comments,
        'form': form,
        'content_type': content_type,
    })