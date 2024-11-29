from rest_framework import routers
from django.urls import path, include
from .views.salon.salon_view import SalonViewSet

router = routers.DefaultRouter()
router.register(r"salon", SalonViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
