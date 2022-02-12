from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def Index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    no_of_slides = n//4+ceil(n/4-n//4)
    params = {'no_of_slides': no_of_slides, 'range': range(1,no_of_slides), 'product': 'products'}
    return render(request, 'shop/index.html', params)


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