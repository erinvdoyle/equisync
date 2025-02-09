from django import forms
from .models import ExerciseSchedule

class ExerciseScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ExerciseSchedule
        fields = ['horse', 'date', 'exercise_type', 'duration', 'notes']
