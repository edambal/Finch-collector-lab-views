from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Coincollector

from .forms import CoinForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def collectors_index(request):
    collectors = Coincollector.objects.all()
    return render(request,'collectors/index.html',{'collectors':collectors})

def collectors_detail(request,collector_id):
    collector = Coincollector.objects.get(id=collector_id)
    coin_form = CoinForm()
    return render(request,'collectors/detail.html',{
        'collector':collector,
        'coin_form': coin_form
    })

def add_coin(request,collector_id):
    form = CoinForm(request.POST)
    if form.is_valid():
        new_coin = form.save(commit=False)
        new_coin.coincollector_id = collector_id
        new_coin.save()
    return redirect('detail',collector_id=collector_id)
