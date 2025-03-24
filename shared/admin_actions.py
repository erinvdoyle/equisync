from django.contrib import messages


def approve_selected(modeladmin, request, queryset):
    """
    Admin action to approve selected items with
    an 'approved' field.
    """
    if hasattr(queryset.model, 'approved'):
        updated = queryset.update(approved=True)
        modeladmin.message_user(
            request,
            f"{updated} item(s) marked as approved.",
            level=messages.SUCCESS
        )
    else:
        modeladmin.message_user(
            request,
            "This model does not have an 'approved' field.",
            level=messages.ERROR
        )


approve_selected.short_description = "Approve selected items"
