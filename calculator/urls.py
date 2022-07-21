from django.contrib import admin
from django.urls import path
from .views import FareCreate

urlpatterns = [
    path('', FareCreate.as_view(), name='calculate')
]
