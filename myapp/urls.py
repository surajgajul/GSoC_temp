from django.urls import path
from . import views
from .views import SalesListAPIView, WorldmapListAPIView

urlpatterns = [
    path("", views.home, name='home'),
    path('salesmap/', views.sales_map, name='sales_map'),
    path('api/sales/', SalesListAPIView.as_view(), name='sales-list'),
    path('api/get_sales_data/',views.get_sales_data, name='get_sales_data'),
]
