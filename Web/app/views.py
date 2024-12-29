
from django.http import HttpResponse
from django.shortcuts import redirect, render

def index_view(request):
    return redirect('home')


# Create your views here.
def home(request) : 
    return render(request,'app/home.html')

def cart(request) : 
    return render(request,'app/cart.html')

def checkout(request):
    return render(request,'app/checkout.html')