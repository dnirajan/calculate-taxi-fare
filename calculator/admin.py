from django.contrib import admin
from .models import Fare, Time, Price


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['time']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['time', 'service_charge', 'surge_charge', 'initial_charge', 'km_rate']


@admin.register(Fare)
class FareAdmin(admin.ModelAdmin):
    list_display = ['time', 'distance']
