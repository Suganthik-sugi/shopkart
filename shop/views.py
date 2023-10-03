from django.shortcuts import render,redirect
from . models import Catagory,Product
from django.contrib import messages

def home(request):
    return render(request,"shop/index.html")

def collection(request):
    category=Catagory.objects.all()
    return render(request,"shop/collection.html",{"category":category})

def collectionview(request,name):
    if(Catagory.objects.filter(name=name)):
     products=Product.objects.filter(category__name=name)
     return render(request,"shop/products/index.html",{"products":products})
    else:
       messages.warning(request,"No Such category found")
       return redirect('collection')
       

