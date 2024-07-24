from rest_framework import serializers
from .models import Tenant, CityMetadata, LatLong

class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = '__all__'

class CityMetadataSerializer(serializers.ModelSerializer):
    latlongs = LatLongSerializer(many=True , read_only=True)

    class Meta:
        model = CityMetadata
        fields = '__all__'

class TenantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

