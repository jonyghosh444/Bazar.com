from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Index(request):
    return render(request, 'shop/index.html')

def About(request):
    return render(request, 'shop/About.html')

def Contact(request):
    return render(request, 'shop/Contact.html')

def Tracker(request):
    return render(request, 'shop/Tracker.html')

def Search(request):
    return render(request, 'shop/Search.html')

def Productview(request):
    return render(request, 'shop/Productview.html')

def Checkout(request):
    return render(request, 'shop/Checkout.html')