from django.db import models

# Create your models here.

class Sales(models.Model):
    invoice_id = models.CharField(max_length=20)
    branch = models.CharField(max_length=1)
    city = models.CharField(max_length=50)
    customer_type = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    product_line = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    tax = models.FloatField()
    total = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    payment = models.CharField(max_length=20)
    cogs = models.FloatField()
    gross_margin_percentage = models.FloatField()
    gross_income = models.FloatField()
    rating = models.FloatField()
