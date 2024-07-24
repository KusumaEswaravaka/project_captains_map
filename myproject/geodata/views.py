from django.shortcuts import render
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tenant, CityMetadata, LatLong
from .serializers import TenantSerializers, CityMetadataSerializer, LatLongSerializer
from django.core.files.storage import default_storage


class CSVUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        file_path = default_storage.save(file.name, file)
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tenant, created = Tenant.objects.get_or_create(name=row['tenant'])
                city_metadata, created = CityMetadata.objects.get_or_create(
                    city_name=row['city_name'],
                    state=row.get('state', ''),
                    country=row['country'],
                )
                

                LatLong.objects.create(
                    latitude = row['longitude'],
                    longitude = row['longitude'],
                    city_metadata = city_metadata,
                    tenant = tenant
                )

        return Response({'status': 'file processed'}, status=status.HTTP_200_OK)
