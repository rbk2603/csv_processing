from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProcessedResult(models.Model):
    csv_file = models.ForeignKey(CSVFile, on_delete=models.CASCADE)  # ✅ Ensure this ForeignKey exists
    column_name = models.CharField(max_length=255)
    sum_value = models.FloatField()
    average_value = models.FloatField()
    count_value = models.IntegerField()
