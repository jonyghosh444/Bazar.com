from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def Index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//6 + ceil((n/6)-(n//6))
    allProds = [[products, range(1, nSlides), nSlides],
                [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
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