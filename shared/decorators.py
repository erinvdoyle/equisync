from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


def require_approved(model_class, lookup_kwarg='pk', message=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            obj_id = kwargs.get(lookup_kwarg)
            obj = get_object_or_404(model_class, pk=obj_id)

            if not getattr(obj, 'approved', False):
                return HttpResponseForbidden(
                    message or "This item has not been approved."
                )

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
