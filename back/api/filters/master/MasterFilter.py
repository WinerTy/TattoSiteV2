from django_filters import rest_framework as filters
from api.models import Master


class MasterFilter(filters.FilterSet):
    salon = filters.NumberFilter(field_name="salon_id")

    class Meta:
        model = Master
        fields = ["salon"]
