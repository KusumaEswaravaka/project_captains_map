from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CityMetadata(models.Model):
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.city_name

class LatLong(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    city_metadata = models.ForeignKey(CityMetadata, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"
