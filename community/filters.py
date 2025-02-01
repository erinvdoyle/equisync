import django_filters
from community.ads.models import Ad

class AdFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label='Search')
    category = django_filters.ChoiceFilter(choices=[("Horse", "Horse"), ("Equipment", "Equipment"), ("Clothing", "Clothing"), ("Machinery/Auto", "Machinery/Auto"), ("Animal", "Animal"), ("Other", "Other")], label='Category')

    class Meta:
        model = Ad
        fields = ['search', 'category']
