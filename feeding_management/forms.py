from django import forms
from .models import FeedingChart

class FeedingChartForm(forms.ModelForm):
    class Meta:
        model = FeedingChart
        fields = ['breakfast_feed', 'breakfast_quantity', 'lunch_feed', 'lunch_quantity', 'dinner_feed', 'dinner_quantity', 'hay', 'hay_quantity', 'supplements', 'medicines', 'notes', 'approved_users']
