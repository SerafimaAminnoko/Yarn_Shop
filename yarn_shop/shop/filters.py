from django_filters import FilterSet

from shop.models import Yarn


class YarnFilter(FilterSet):
    class Meta:
        model = Yarn
        fields = ['name', 'subcat__count']

