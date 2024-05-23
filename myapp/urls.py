from django.urls import path
from . import views
from .views import SalesListAPIView

urlpatterns = [
    path("", views.home, name='home'),
    path('api/sales/', SalesListAPIView.as_view(), name='sales-list'),
]
