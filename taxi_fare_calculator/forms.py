from django import forms
from calculator.models import Fare, Price


class FareForm(forms.ModelForm):
    # time = forms.ModelChoiceField(queryset=Price.objects.only('time'), attrs={'type': 'time'})
    # time = forms.DateField(widget=forms.DateInput(attrs={'class': 'timepicker'}))

    class Meta:
        model = Fare
        fields = ['time', 'distance']
        widgets = {
            'time': forms.TimeInput(format='%H:%M'),
        }
