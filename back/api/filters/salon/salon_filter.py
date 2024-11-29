from django_filters import rest_framework as filters

from api.models import Salon


class SalonFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Salon
        fields = ["name"]
