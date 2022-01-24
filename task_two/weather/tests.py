from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Weather
from .views import WeatherListRetrieveViewSet


class WeatherModelTests(TestCase):

    def test_can_create_weather_model(self):
        """
        Test that a weather model can be created
        :return:
        :rtype:
        """
        weather = Weather.objects.create(city="London", temperature=280.32)

        # Check that the weather is contained in the db
        db_weather = Weather.objects.get(id=weather.id)

        self.assertEqual(weather, db_weather)


class WeatherRequestTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        for city, temp in [("London", 234.6), ("Bangkok", 200.4), ("Berlin", "240.6")]:
            Weather.objects.create(city=city, temperature=temp)

    def test_can_get_list_of_weather_cities(self):
        """
        Test that querying the weather route will return a list of cities available in the database
        :return:
        :rtype:
        """
        request = self.factory.get("/weather")

