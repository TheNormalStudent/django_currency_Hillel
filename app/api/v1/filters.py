from django_filters import rest_framework as filters

from currency.models import Rate, ContactUs

class RateFilter(filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'sale': ('lt', 'lte', 'gt', 'gte', 'exact'), 
            'type': ('in', ),
            }