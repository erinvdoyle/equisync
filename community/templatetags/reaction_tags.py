from django import template

register = template.Library()


@register.filter(name='is_user_reaction')
def is_user_reaction(user_reactions, announcement_id, emoji):
    """
    Check if a user has reacted with a specific emoji to an announcement.
    Returns "active" if the user has reacted, "" otherwise.
    """
    if not user_reactions:
        return ""

    for reaction in user_reactions.all():
        if str(reaction.announcement_id) == str(
                announcement_id) and reaction.emoji == emoji:
            return "active"
    return ""


@register.filter(name='get_item')
def get_item(dictionary, key):
    if dictionary is None:
        return ""
    return dictionary.get(key)