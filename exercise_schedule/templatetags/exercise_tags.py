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
