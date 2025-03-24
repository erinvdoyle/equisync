from django import template

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def get_appointment_classes(appointments):
    classes = set()
    for appointment in appointments:
        if appointment.appointment_type == 'farrier':
            classes.add('appointment-farrier')
        elif appointment.appointment_type == 'vet':
            classes.add('appointment-vet')
        elif appointment.appointment_type == 'physio':
            classes.add('appointment-physio')
        elif appointment.appointment_type == 'dentist':
            classes.add('appointment-dentist')
        elif appointment.appointment_type == 'other':
            classes.add('appointment-other')
    return ' '.join(classes)


@register.filter
def pretty_exercise(value):
    """ converts exercise types with underscores to title case """
    if isinstance(value, str):
        return value.replace('_', ' ').title()
    return value


@register.filter
def format_hours(value):
    """
    Converts float hours to a readable format:
    - < 0.5 becomes "< 0.5 hour"
    - else shows "x hour(s)"
    """
    try:
        value = float(value)
        if value < 0.5:
            return "< 0.5 hour"
        elif value == .5:
            return ".5 hour"
        else:
            return f"{value} hours"
    except (ValueError, TypeError):
        return value
