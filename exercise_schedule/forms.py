from django import forms
from django.utils import timezone
from .models import (
    Appointment,
    ExerciseSchedule,
    ExerciseScheduleItem,
    EXERCISE_CHOICES
)


class ExerciseScheduleForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )

    class Meta:
        model = ExerciseSchedule
        fields = ['horse', 'date', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Add any additional notes'
            }),
        }


class ExerciseScheduleItemForm(forms.ModelForm):
    time_category = forms.ChoiceField(
        choices=[('am', 'AM'), ('pm', 'PM'), ('additional', 'Additional')],
        widget=forms.HiddenInput()
    )

    class Meta:
        model = ExerciseScheduleItem
        fields = ['exercise_type', 'duration', 'time_category']
        widgets = {
            'exercise_type': forms.Select(choices=EXERCISE_CHOICES, attrs={
                'class': 'form-select',
                'required': True,
            }),
            'duration': forms.NumberInput(attrs={
                'min': 1,
                'class': 'form-control',
                'placeholder': 'Duration in minutes',
                'required': True,
            }),
        }

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration and duration > 300:
            raise forms.ValidationError(
                "Duration too long. Please keep under 5 hours.")
        return duration


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
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True,
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'required': True,
            }),
            'contact_details': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email or phone number',
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
            })
        }
