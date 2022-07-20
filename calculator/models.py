from django.db import models


class Time(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.time)


class Price(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='price')
    service_charge = models.CharField(max_length=10)
    surge_charge = models.CharField(max_length=10)
    initial_charge = models.CharField(max_length=10)
    km_rate = models.CharField(max_length=10)

    def __str__(self):
        return str(self.time)


class Fare(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    distance = models.CharField(max_length=5)
