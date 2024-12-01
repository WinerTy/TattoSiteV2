from django_filters import rest_framework as filters
from api.models import Tags, Salon, Master


class TagFilter(filters.FilterSet):
    salon_id = filters.NumberFilter(method="filter_by_salon")
    master_id = filters.NumberFilter(field_name="masters__id")

    class Meta:
        model = Tags
        fields = ["salon_id", "master_id"]

    def filter_by_salon(self, queryset, name, value):
        salon = Salon.objects.get(id=value)
        masters = Master.objects.filter(salon=salon)
        return queryset.filter(masters__in=masters).distinct()
