from rest_framework import serializers
from api.models import Master

from ..tags.TagsSerializer import TagsSerializer


class MasterSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = Master
        fields = [
            "id",
            "name",
            "phone",
            "image",
            "start_cost",
            "short_description",
            "rating",
            "experience",
            "tags",
        ]
