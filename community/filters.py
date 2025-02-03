import django_filters
from community.ads.models import Ad

CATEGORY_CHOICES = [
        ("Horse", "Horse"), ("Equipment", "Equipment"), ("Clothing", "Clothing"), ("Machinery/Auto", "Machinery/Auto"), ("Animal", "Animal"), ("Other", "Other"),
    ]

class AdFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label='Search')
    category = django_filters.ChoiceFilter(choices=CATEGORY_CHOICES, label="Category")

    class Meta:
        model = Ad
        fields = ['search', 'category']
