import django_filters

from api.models.supplier_model import Supplier


# ----------------------------------------------------------------------------------------------------------------------
# Create filters
class CountryFilter(django_filters.FilterSet):
    """Filter by country for the supplier views"""

    country = django_filters.CharFilter(
        field_name='contact__country',
        lookup_expr='icontains'
    )

    class Meta:
        model = Supplier
        fields: tuple = ('country',)
