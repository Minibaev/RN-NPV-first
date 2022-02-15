from django import forms


class NpvForm(forms.Form):
    year = forms.IntegerField(min_value=2020, max_value=2050)
    k = forms.FloatField()
