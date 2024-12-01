from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from api.models import Master
from api.serializers.master.MasterSerializer import MasterSerializer
from api.filters.master.MasterFilter import MasterFilter
from api.core.pagination import SmallResultsSetPagination


class MasterViewSet(ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MasterFilter
    pagination_class = SmallResultsSetPagination
    http_method_names = ["get", "options"]
    allowed_methods = ["get", "options"]
