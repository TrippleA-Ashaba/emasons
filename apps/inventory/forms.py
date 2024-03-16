from django import forms


class CalculatorForm(forms.Form):
    weight = forms.FloatField(required=False)
    chemical = forms.CharField(max_length=100, required=False)
    soap_bars = forms.IntegerField(required=False)
