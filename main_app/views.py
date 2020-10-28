from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Coincollector , Coinsymposium

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
    symposium_not_part_of = Coinsymposium.objects.exclude(id__in= collector.symposiums.all().values_list('id'))
    coin_form = CoinForm()
    return render(request,'collectors/detail.html',{
        'collector':collector,
        'coin_form': coin_form,
        'symposiums': symposium_not_part_of
    })

def assoc_symp(request,collector_id,symp_id):
    collector = Coincollector.objects.get(id=collector_id)
    symp = Coinsymposium.objects.get(id=symp_id)
    collector.symposiums.add(symp)
    return redirect('detail',collector_id=collector_id)

def remove_symp(request,collector_id,symp_id):
    collector = Coincollector.objects.get(id=collector_id)
    symp = Coinsymposium.objects.get(id=symp_id)
    collector.symposiums.remove(symp)
    return redirect('detail',collector_id=collector_id)


def add_coin(request,collector_id):
    form = CoinForm(request.POST)
    if form.is_valid():
        new_coin = form.save(commit=False)
        new_coin.coincollector_id = collector_id
        new_coin.save()
    return redirect('detail',collector_id=collector_id)