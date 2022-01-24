from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100, primary_key=True, unique=True)
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
