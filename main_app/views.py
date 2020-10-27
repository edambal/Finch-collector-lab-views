from django.shortcuts import render

from django.http import HttpResponse

from .models import coins

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def coins_index(request):
    return render(request,'coins/index.html',{'coins':coins})