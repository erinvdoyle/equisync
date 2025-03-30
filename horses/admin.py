from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from django.db.models import Q
from django.urls import reverse
from .models import HorseProfile
from feeding_management.models import FeedingChart
from notifications.utils import send_notification
from notifications.models import Notification


class HorseProfileAdminForm(forms.ModelForm):
    class Meta:
        model = HorseProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HorseProfileAdmin(admin.ModelAdmin):
    form = HorseProfileAdminForm
    raw_id_fields = ('owner', 'barn_manager', 'rider')
    filter_horizontal = ('staff',)
    list_display = (
        'name', 'owner', 'most_recent_ride', 'most_recent_care', 'approved'
    )
    list_filter = ('approved',)
    actions = ['approve_selected_horses']

    def approve_selected_horses(self, request, queryset):
        updated = 0
        for horse in queryset:
            if not horse.approved:
                horse.approved = True
                super().save_model(request, horse, form=None, change=True)
                self.handle_post_approval(horse)
                updated += 1
        self.message_user(request, f"{updated} horse(s) approved.")

    approve_selected_horses.short_description = "Approve selected horses"

    def save_model(self, request, obj, form, change):
        was_previously_approved = False
        if obj.pk:
            previous = HorseProfile.objects.get(pk=obj.pk)
            was_previously_approved = previous.approved

        super().save_model(request, obj, form, change)

        if obj.approved and not was_previously_approved:
            self.handle_post_approval(obj)

    def handle_post_approval(self, horse):

        FeedingChart.objects.get_or_create(horse=horse)

        existing = Notification.objects.filter(
            user=horse.owner,
            is_read=False
        ).filter(
            Q(message__icontains=horse.name),
            Q(message__icontains="approved")
        ).exists()

        if not existing:
            horse_url = reverse(
                'horses:horse_profile', kwargs={'horse_id': horse.id})
            message = (
                f"Your horse '<strong>{horse.name}</strong>'"
                f" has been approved! "
                f"<a href='{horse_url}'>View Profile</a>"
            )
            send_notification(horse.owner, message)

    def formfield_for_foreignkey(
            self, db_field, request, **kwargs):
        if db_field.name in ('owner', 'barn_manager', 'rider'):
            return db_field.formfield(widget=forms.Select(
                attrs={'style': 'width:300px'}
            ))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(HorseProfile, HorseProfileAdmin)
