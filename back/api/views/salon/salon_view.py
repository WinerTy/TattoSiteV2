from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from api.models import Salon
from api.serializers.salon.salon_serializer import SalonSerializer
from api.filters.salon.salon_filter import SalonFilter
from api.core.pagination import StandardResultsSetPagination


class SalonViewSet(ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    filterset_class = SalonFilter
    filter_backends = [filters.DjangoFilterBackend]
    pagination_class = StandardResultsSetPagination
    allowed_methods = ["get"]
