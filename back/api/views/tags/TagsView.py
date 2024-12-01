from rest_framework.viewsets import ModelViewSet
from api.models import Tags
from api.serializers.tags.TagsSerializer import TagsSerializer
from api.filters.tags.TagFilter import TagFilter
from django_filters import rest_framework as filters
from api.core.pagination import SmallResultsSetPagination


class TagsViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filterset_class = TagFilter
    filter_backends = [filters.DjangoFilterBackend]
    pagination_class = SmallResultsSetPagination
