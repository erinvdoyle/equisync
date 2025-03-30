from django import forms
from django.utils import timezone
from .models import Comment, CommunityEvent


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class EventForm(forms.ModelForm):
    class Meta:
        model = CommunityEvent
        fields = ['title', 'description', 'date', 'time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a brief description',
                'rows': 4,
                'required': True,
            }),
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
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title.strip()) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if len(description.strip()) < 10:
            raise forms.ValidationError(
                "Description must be at least 10 characters.")
        return description

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:
            event_datetime = timezone.datetime.combine(date, time)
            if event_datetime < timezone.now():
                raise forms.ValidationError(
                    "The event cannot be scheduled in the past.")

        return cleaned_data
