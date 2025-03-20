from django import forms
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
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }