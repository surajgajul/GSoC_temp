import pandas as pd
from django.contrib.auth.models import User
from myapp.models import Sales
from datetime import datetime

# Read CSV file into a DataFrame
csv_file_path = 'sample.csv'
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    sales_instance = Sales(
        invoice_id=row['Invoice ID'],
        branch=row['Branch'],
        city=row['City'],
        customer_type=row['Customer type'],
        gender=row['Gender'],
        product_line=row['Product line'],
        unit_price=row['Unit price'],
        quantity=row['Quantity'],
        tax=row['Tax 5%'],
        total=row['Total'],
        date=datetime.strptime(row['Date'], '%m/%d/%Y').date(),
        time=datetime.strptime(row['Time'], '%H:%M').time(),
        payment=row['Payment'],
        cogs=row['cogs'],
        gross_margin_percentage=row['gross margin percentage'],
        gross_income=row['gross income'],
        rating=row['Rating']
    )
    sales_instance.save()
    print("Added")

print("CSV data has been loaded into the Django database.")