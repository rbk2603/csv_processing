
from django.urls import path
from .views import upload_csv, processed_results

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),  # Upload CSV file
    path('results/<int:file_id>/', processed_results, name='processed_results'),  # View processed results
]

