from celery import shared_task
import pandas as pd
from app.models import CSVFile, ProcessedResult

@shared_task
def process_csv(file_id):
    csv_file = CSVFile.objects.get(id=file_id)  
    df = pd.read_csv(csv_file.file.path)

    # Process only numeric columns
    for column in df.select_dtypes(include=['number']).columns:
        sum_value = df[column].sum()
        avg_value = df[column].mean()
        count_value = df[column].count()

        
        ProcessedResult.objects.create(
            csv_file=csv_file,  
            column_name=column,
            sum_value=sum_value,
            average_value=avg_value,
            count_value=count_value
        )
    # Additional Metrics
    total_revenue = df['Sales'].sum() if 'Sales' in df.columns else None
    avg_discount = df['Discount'].mean() if 'Discount' in df.columns else None
    best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax() if 'Product' in df.columns else None
    most_profitable_product = df.groupby('Product')['Profit'].sum().idxmax() if 'Product' in df.columns else None
    max_discount_product = df.groupby('Product')['Discount'].max().idxmax() if 'Product' in df.columns else None

    return {
        'total_revenue': total_revenue,
        'avg_discount': avg_discount,
        'best_selling_product': best_selling_product,
        'most_profitable_product': most_profitable_product,
        'max_discount_product': max_discount_product
    }
