from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
import datetime
from calculator.models import Fare, Price, Time
from taxi_fare_calculator.forms import FareForm


class CalculatorView(TemplateView):
    template_name = 'home.html'


class FareCreate(TemplateView):
    model = Fare
    template_name = 'calculate.html'
    success_url = 'home'

    def get(self, request, *args, **kwargs):
        form = FareForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FareForm(request.POST)
        if form.is_valid():
            t1 = form.cleaned_data['time']
            distance = form.cleaned_data['distance']
            distance = int(distance)
            price = Price.objects.get(time__time=str(t1))
            surge = (int(price.surge_charge) / 100) + 1
            service = (int(price.service_charge) / 100) + 1
            result = int(price.initial_charge) + distance * int(price.km_rate) * surge * service
            form = FareForm()
            args = {'form': form, 'result': result, 'time': t1, 'distance': distance}
            return render(request, self.template_name, args)
