from django import forms
from .models import ExerciseSchedule, ExerciseScheduleItem, EXERCISE_CHOICES

class ExerciseScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ExerciseSchedule
        fields = ['horse', 'date', 'notes']

class ExerciseScheduleItemForm(forms.ModelForm):
    time_category = forms.ChoiceField(choices=[('am', 'AM'), ('pm', 'PM'), ('additional', 'Additional')])

    class Meta:
        model = ExerciseScheduleItem
        fields = ['exercise_type', 'duration', 'time_category']
        widgets = {
            'exercise_type': forms.Select(choices=EXERCISE_CHOICES),
            'duration': forms.NumberInput(attrs={'min': 1}),
        }
