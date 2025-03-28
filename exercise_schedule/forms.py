from django import forms

from .models import (
    Appointment,
    ExerciseSchedule,
    ExerciseScheduleItem,
    EXERCISE_CHOICES
)


class ExerciseScheduleForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = ExerciseSchedule
        fields = ['horse', 'date', 'notes']


class ExerciseScheduleItemForm(forms.ModelForm):
    time_category = forms.ChoiceField(
        choices=[('am', 'AM'), ('pm', 'PM'), ('additional', 'Additional')]
    )

    class Meta:
        model = ExerciseScheduleItem
        fields = ['exercise_type', 'duration', 'time_category']
        widgets = {
            'exercise_type': forms.Select(choices=EXERCISE_CHOICES),
            'duration': forms.NumberInput(attrs={'min': 1}),
            'time_category': forms.HiddenInput(),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'horse',
            'date',
            'appointment_type',
            'practitioner',
            'time',
            'contact_details',
            'notes'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
