import django_filters
from .models import Products, Customers, Orders


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customers
        fields = ('name', 'email')


