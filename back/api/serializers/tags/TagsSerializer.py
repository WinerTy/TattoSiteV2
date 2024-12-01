from rest_framework import serializers
from api.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"
