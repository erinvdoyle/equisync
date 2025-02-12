from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .announcements.models import Announcement, Reaction
from django.db.models import Count

@login_required
def react_to_announcement(request):
    if request.method == 'POST':
        announcement_id = request.POST.get('announcement_id')
        emoji = request.POST.get('emoji')

        announcement = get_object_or_404(Announcement, id=announcement_id)
        user = request.user

        try:
            reaction, created = Reaction.objects.get_or_create(user=user, announcement=announcement, emoji=emoji)
            if not created:
                reaction.delete()
                status = 'removed'
            else:
                status = 'added'

            # Recalculate most clicked emoji
            most_clicked = Reaction.objects.filter(announcement=announcement).values('emoji').annotate(emoji_count=Count('emoji')).order_by('-emoji_count').first()
            most_clicked_emoji = most_clicked['emoji'] if most_clicked else None

            return JsonResponse({
                'status': status,
                'emoji': emoji,
                'announcement_id': announcement_id,
                'most_clicked_emoji': most_clicked_emoji
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'invalid request'})

