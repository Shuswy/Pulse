from django_filters import rest_framework as filters

from monitor.models import TrackedTarget


class TargetFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="pricehistory__price", lookup_expr='gt')
    price_max = filters.NumberFilter(field_name="pricehistory__price", lookup_expr='lt')
    name = filters.CharFilter(lookup_expr='icontains')
    scraped_since = filters.DateTimeFilter(field_name="last_scraped_at", lookup_expr='gte')

    class Meta:
        model = TrackedTarget
        fields = ['active', 'website']
