from rest_framework.viewsets import ModelViewSet
from api.models import Slider
from api.serializers.slider.slider_serializer import SliderSerializer


class SliderViewSet(ModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
