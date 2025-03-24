from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from .models import Appointment, ExerciseSchedule, ExerciseScheduleItem


@admin.register(ExerciseSchedule)
class ExerciseScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'horse',
        'date',
        'get_exercise_types',
        'get_durations',
        'created_by'
    )
    list_filter = ('horse', 'date')
    search_fields = ('horse__name', 'notes')
    date_hierarchy = 'date'
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        (None, {
            'fields': ('horse', 'date', 'notes')
        }),
        ('Permissions', {
            'fields': ('created_by',)
        }),
    )

    def get_exercise_types(self, obj):
        return ", ".join([
            item.exercise_type for item in obj.schedule_items.all()
        ])

    get_exercise_types.short_description = 'Exercise Types'

    def get_durations(self, obj):
        return ", ".join([
            str(item.duration) for item in obj.schedule_items.all()
        ])

    get_durations.short_description = 'Durations'

    def get_readonly_fields(self, request, obj=None):
        if not (request.user.is_staff or
                self.has_owner_rider_permission(request.user, obj)):
            return [field.name for field in obj._meta.fields]
        return self.readonly_fields + ['created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.save()

    def has_add_permission(self, request):
        return request.user.is_staff or self.has_owner_rider_permission(
            request.user)

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff or self.has_owner_rider_permission(
            request.user, obj)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff or self.has_owner_rider_permission(
            request.user, obj)

    def has_owner_rider_permission(self, user, obj=None):
        if user.is_superuser:
            return True
        if user.groups.filter(name='Barn Manager').exists():
            return True
        if obj:
            return obj.horse.owner == user or user in obj.horse.riders.all()
        return ExerciseSchedule.objects.filter(
            Q(horse__owner=user) | Q(horse__riders=user)
        ).exists()


@admin.register(ExerciseScheduleItem)
class ExerciseScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'exercise_type', 'duration')
    list_filter = ('exercise_type',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'horse',
        'date',
        'appointment_type',
        'practitioner',
        'time'
    )
    list_filter = ('appointment_type', 'date')
    search_fields = ('horse__name', 'practitioner')
