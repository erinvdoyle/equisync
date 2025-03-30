from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact', 'notes']
        widgets = {
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone, email, or other contact info',
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
                'rows': 4
            }),
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if contact and len(contact) < 5:
            raise forms.ValidationError(
                "Contact info must be at least 5 characters long.")
        return contact
