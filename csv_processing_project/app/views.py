from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CSVFile, ProcessedResult
import app.forms
from .tasks import process_csv

#  View to Upload CSV File
def upload_csv(request):
    form_class = app.forms.CSVUploadForm  # Import form dynamically
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            return redirect('processed_results', file_id=csv_file.id)
    else:
        form = form_class()
    return render(request, 'upload_csv.html', {'form': form})

def processed_results(request, file_id):
    csv_file = get_object_or_404(CSVFile, id=file_id)
    processed_data = list(ProcessedResult.objects.filter(csv_file=csv_file))  

    return render(request, 'processed_results.html', {'csv_file': csv_file, 'processed_data': processed_data})