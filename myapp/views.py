from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from myapp.models import Sales, Worldmap
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from rest_framework import generics
from .models import Sales
from .serializers import SalesSerializer, WorldmapSerializer

# Create your views here.
class SalesListAPIView(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

def home(request):
    return render(request, 'home.html')

class WorldmapListAPIView(generics.ListAPIView):
    queryset = Worldmap.objects.all()
    serializer_class = WorldmapSerializer

def sales_map(request):
    return render(request, 'salesmap.html')

def get_sales_data(request):
    worldmap_data = WorldmapListAPIView.as_view()(request).data
    countries = [item['country'] for item in worldmap_data]
    sales = [item['sales'] for item in worldmap_data]
    data = {
        'countries': countries,
        'sales': sales,
    }
    return JsonResponse(data)