from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_type', 'image', 'description', 'contact_info', 'price']  