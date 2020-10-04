from django.shortcuts import render
from .models import Product 


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'frontend/index.html',{'products':products})

def about(request):
    return render(request,'frontend/about.html')

def contract(request):
    return render(request,'frontend/contract.html')    

