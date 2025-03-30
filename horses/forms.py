from django import forms
from .models import HorseProfile


class HorseForm(forms.ModelForm):
    class Meta:
        model = HorseProfile
        fields = ['name', 'breed', 'age', 'gender', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Horse name',
                'required': True
            }),
            'breed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Breed',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': 'Age in years',
                'required': True
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError(
                "Name must be at least 2 characters long.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 0 or age > 50):
            raise forms.ValidationError(
                "Please enter a valid age between 0 and 50.")
        return age
