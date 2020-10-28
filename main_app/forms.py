from django import forms
from .models import Coin

class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['category','name','datefound','metal']