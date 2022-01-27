
from django.shortcuts import render
from .models import ProductData
from .models import OrderData
import requests

#Create your views here.
def Product(request):
    all_data = ProductData.objects.all()
    return render(request,"product.html",{'key1': all_data})


def Order(request):
    all_data1 = OrderData.objects.all()
    return render(request,"Order.html",{'key2': all_data1})

def WebData(request):
    #url ="https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    url = "https://api.covid19api.com/countries"
    response = requests.request("GET", url).json()
    return render(request,"webdata.html",{'Data': response})
    
def Camera(request):
    return render(request,"camera.html")