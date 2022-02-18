# Hare krishna
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.


def Index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//6 + ceil((n/6)-(n//6))
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//6 + ceil((n/6) - (n//6))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)


def About(request):
    return render(request, 'shop/About.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phoneno = request.POST.get("phone", "")
        message = request.POST.get("message", "")
        contact = Contact(name=name, email=email, phone=phoneno, message=message)
        contact.save()
    return render(request, 'shop/Contact.html')


def Tracker(request):
    return render(request, 'shop/Tracker.html')


def Search(request):
    return render(request, 'shop/Search.html')


def ProductView(request, myid):
    # fetching the product by id
    product = Product.objects.filter(id=myid)
    params = {"product": product[0]}
    return render(request, 'shop/ProductView.html', params)


def Checkout(request):
    return render(request, 'shop/Checkout.html')