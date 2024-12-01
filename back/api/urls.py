from rest_framework import routers
from django.urls import path, include
from .views.salon.salon_view import SalonViewSet
from .views.slider.slider_view import SliderViewSet
from .views.master.MasterView import MasterViewSet
from .views.tags.TagsView import TagsViewSet

router = routers.DefaultRouter()
router.register(r"salon", SalonViewSet)
router.register(r"slider", SliderViewSet)
router.register(r"master", MasterViewSet)
router.register(r"tags", TagsViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
