from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) : 
    return render(request,'app/home.html')

def cart(request) : 
    return render(request,'app/cart.html')

def checkout(request):
    return render(request,'app/checkout.html')