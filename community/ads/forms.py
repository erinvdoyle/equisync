from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        field = ['ad_type', 'image', 'description', 'price', 'contact_info']