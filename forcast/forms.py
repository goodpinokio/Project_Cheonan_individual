# forms.py
from django import forms

class StockSearchForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=100)
