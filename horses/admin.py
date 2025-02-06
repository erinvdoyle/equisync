from django.contrib import admin
from django import forms  
from .models import HorseProfile
from django.contrib.auth.models import User


class HorseProfileAdminForm(forms.ModelForm):
    class Meta:
        model = HorseProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, further customize the widget here, e.g., for filtering.
        # self.fields['owner'].queryset = User.objects.filter(...)


class HorseProfileAdmin(admin.ModelAdmin):
    form = HorseProfileAdminForm 
    raw_id_fields = ('owner', 'barn_manager', 'rider')
    filter_horizontal = ('staff',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Override this method to prevent the "+" button from appearing.
        """
        if db_field.name in ('owner', 'barn_manager', 'rider'):
            return db_field.formfield(widget=forms.Select(
                attrs={'style': 'width:300px'}  
            ))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(HorseProfile, HorseProfileAdmin)
