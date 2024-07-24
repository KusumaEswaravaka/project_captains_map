from django.urls import path
from .views import CSVUploadView

urlpatterns = [
    path('geodata/upload-csv/', CSVUploadView.as_view(), name='upload-csv'),
]