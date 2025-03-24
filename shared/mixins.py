from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


class RequireApprovedMixin:
    model = None
    lookup_url_kwarg = 'pk'
    message = "This item has not been approved."

    def dispatch(self, request, *args, **kwargs):
        obj_id = kwargs.get(self.lookup_url_kwarg)
        obj = get_object_or_404(self.model, pk=obj_id)

        if not getattr(obj, 'approved', False):
            return HttpResponseForbidden(self.message)

        return super().dispatch(request, *args, **kwargs)
