from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import WeatherListRetrieveViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"weather", WeatherListRetrieveViewSet)

urlpatterns = [
    path("", include(router.urls))
]
