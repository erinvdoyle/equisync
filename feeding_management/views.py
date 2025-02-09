from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from horses.models import HorseProfile 
from feeding_management.models import FeedingChart
from .tables import FeedingChartTable
from .models import FeedingChart
from .forms import FeedingChartForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def horse_feeding_chart(request, horse_id):
    horse = get_object_or_404(HorseProfile, pk=horse_id)  
    feeding_chart, created = FeedingChart.objects.get_or_create(horse=horse) 
    if request.method == 'POST':
        form = FeedingChartForm(request.POST, instance=feeding_chart)
        if form.is_valid():
            form.save()
            return redirect('horse_feeding_chart', horse_id=horse_id) 
    else:
        form = FeedingChartForm(instance=feeding_chart)

    is_approved_user = request.user in feeding_chart.approved_users.all()

    context = {
        'horse': horse,
        'feeding_chart': feeding_chart,
        'form': form,
        'is_approved_user': is_approved_user,
    }
    return render(request, 'feeding_management/horse_feeding_chart.html', context)

@login_required
def all_horses_feeding(request):
    horses = HorseProfile.objects.all()
    table_data = []
    for horse in horses:
        feeding_chart = getattr(horse, 'feeding_chart', None)
        if feeding_chart:
            table_data.append(feeding_chart)

    table = FeedingChartTable(table_data)

    context = {'table': table}
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



# @login_required
# def all_horses_feeding(request):
#     horses = HorseProfile.objects.all()  
#     feeding_data = []
#     for horse in horses:
#         feeding_chart = getattr(horse, 'feeding_chart', None)
#         if feeding_chart:
#             feeding_data.append({
#                 'horse_name': horse.name,
#                 'breakfast_feed': feeding_chart.breakfast_feed,
#                 'breakfast_quantity': feeding_chart.breakfast_quantity,
#                 'lunch_feed': feeding_chart.lunch_feed,
#                 'lunch_quantity': feeding_chart.lunch_quantity,
#                 'dinner_feed': feeding_chart.dinner_feed,
#                 'dinner_quantity': feeding_chart.dinner_quantity,
#                 'hay': feeding_chart.hay,
#                 'hay_quantity': feeding_chart.hay_quantity,
#                 'supplements': feeding_chart.supplements,
#                 'medicines': feeding_chart.medicines,
#                 'notes': feeding_chart.notes,
#             })
#         else:
#             feeding_data.append({
#                 'horse_name': horse.name,
#                 'breakfast_feed': "Not Set",
#                 'breakfast_quantity': "Not Set",
#                 'lunch_feed': "Not Set",
#                 'lunch_quantity': "Not Set",
#                 'dinner_feed': "Not Set",
#                 'dinner_quantity': "Not Set",
#                 'hay': "Not Set",
#                 'hay_quantity': "Not Set",
#                 'supplements': "Not Set",
#                 'medicines': "Not Set",
#                 'notes': "Not Set",
#             })
#     context = {'feeding_data': feeding_data}
#     return render(request, 'feeding_management/all_horses_feeding.html', context)

