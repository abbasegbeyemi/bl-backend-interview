from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Weather
from .serializers import WeatherSerializer


class WeatherListRetrieveViewSet(ReadOnlyModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [AllowAny]
    lookup_field = "city"
