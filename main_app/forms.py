from django import forms
from .models import Coin,Coincollector

class CollectorForm(forms.ModelForm):
    class Meta:
        model = Coincollector
        fields = ['name','country','moto','age']

class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['category','name','datefound','metal']