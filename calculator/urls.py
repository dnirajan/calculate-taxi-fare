from django.contrib import admin
from django.urls import path
from .views import CalculatorView, FareCreate

urlpatterns = [
    path('home/', CalculatorView.as_view(), name='home'),
    path('', FareCreate.as_view(), name='calculate')
]
