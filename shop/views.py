from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, 'shop/index.html')

def About(request):
    return HttpResponse("About")

def Contact(request):
    return HttpResponse("Contact")

def Tracker(request):
    return HttpResponse("Tracker")

def Search(request):
    return HttpResponse("Search")

def Productview(request):
    return HttpResponse("Product view")

def Checkout(request):
    return HttpResponse("Check out")