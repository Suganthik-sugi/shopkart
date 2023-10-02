from django.shortcuts import render
from . models import Catagory

def home(request):
    return render(request,"shop/index.html")

def collection(request):
    category=Catagory.objects.all()
    return render(request,"shop/collection.html",{"category":category})
