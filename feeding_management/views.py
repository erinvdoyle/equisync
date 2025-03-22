from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from horses.models import HorseProfile 
from feeding_management.models import FeedingChart
from .tables import FeedingChartTable
from .models import FeedingChart
from .forms import FeedingChartForm
from django.contrib.admin.views.decorators import staff_member_required
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()

@login_required
def horse_feeding_chart(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)
    feeding_chart = FeedingChart.objects.filter(horse=horse).first()

    is_owner = request.user == horse.owner
    is_staff = request.user.is_staff
    can_edit = is_staff or is_owner

    if not feeding_chart:
        if is_staff:
            feeding_chart = FeedingChart.objects.create(horse=horse, approved=True, last_updated_by=request.user)
            messages.success(request, "New feeding chart created")
        else:
            messages.warning(request, "Only admins can create a feeding plan for this horse")
            return redirect('horses:horse_profile', horse_id=horse.id)

    if request.method == 'POST' and can_edit:
        form = FeedingChartForm(request.POST, instance=feeding_chart)
        if form.is_valid():
            feeding_plan = form.save(commit=False)
            feeding_plan.last_updated_by = request.user

            if is_staff:
                feeding_plan.approved = True
                messages.success(request, "Feeding chart updated successfully")
                feeding_plan.save()
                return redirect('feeding_management:all_horses_feeding')
            else:
                feeding_plan.approved = False
                messages.success(request, "Your updates have been submitted for admin approval")

                staff_users = User.objects.filter(is_staff=True)
                for admin in staff_users:
                    Notification.objects.create(
                        user=admin,
                        message=f"{request.user.username} submitted feeding plan updates for {horse.name}."
                    )
                feeding_plan.save()
                return redirect('feeding_management:horse_feeding_chart_readonly', horse_id=horse.id)

    else:
        form = FeedingChartForm(instance=feeding_chart)

    context = {
        'horse': horse,
        'form': form,
        'can_edit': can_edit,
        'is_staff': is_staff,
        'is_owner': is_owner,
        'feeding_chart': feeding_chart,
    }

    return render(request, 'feeding_management/horse_feeding_chart.html', context)

@login_required
def all_horses_feeding(request):
    user_horses = HorseProfile.objects.filter(
        Q(owner=request.user) | Q(staff=request.user) | Q(barn_manager=request.user) | Q(rider=request.user)
    ).distinct()

    if request.GET.get('from') == 'horse_profile':
        has_chart = FeedingChart.objects.filter(horse__in=user_horses).exists()
        if not has_chart:
            messages.success(request, "Register your horse here.")

    horses = HorseProfile.objects.all()
    table_data = []
    pending_charts = []

    for horse in horses:
        feeding_chart = getattr(horse, 'feeding_chart', None)
        if feeding_chart:
            table_data.append(feeding_chart)
            if not feeding_chart.approved:
                pending_charts.append(feeding_chart)

    table = FeedingChartTable(table_data)

    context = {
        'table': table,
        'pending_charts': pending_charts
    }
    return render(request, 'feeding_management/all_horses_feeding.html', context)

@login_required
def horse_feeding_chart_readonly(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)
    feeding_chart = get_object_or_404(FeedingChart, horse=horse)

    context = {
        'horse': horse,
        'feeding_chart': feeding_chart,
    }
    return render(request, 'feeding_management/horse_feeding_chart_readonly.html', context)

@staff_member_required
def pending_feeding_approvals(request):
    pending_charts = FeedingChart.objects.filter(approved=False)

    context = {
        'pending_charts': pending_charts
    }

    return render(request, 'feeding_management/pending_approvals.html', context)
