from django.shortcuts import render
from .models import Product 


# Create your views here.
def index(request):
     return render(request,'frontend/index.html')

def about(request):
    return render(request,'frontend/about.html')

def contract(request):
    return render(request,'frontend/contract.html')    

def signup(request):
    return render(request,'frontend/signup.html')    
 
def random(request):
    return render(request,'frontend/random.html')    

