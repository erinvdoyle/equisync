from django import forms
from .models import HorseProfile

class HorseForm(forms.ModelForm):
    class Meta:
        model = HorseProfile
        fields = ['name', 'breed', 'age', 'gender', 'image', 'owner', 'staff', 'barn_manager', 'rider']