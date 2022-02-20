# Hare krishna
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil
# Create your views here.


def Index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//6 + ceil((n/6) - (n//6))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
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
    if request.method == 'POST':
        item_json = request.POST.get("itemJson", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phoneno =request.POST.get("phone", "")
        adress = request.POST.get("adress1", "")+""+request.POST.get("adress2", "")
        city = request.POST.get("city", "")
        division = request.POST.get("division", "")
        zip_code = request.POST.get("zip_code", "")
        order = Order(item_json=item_json,name=name, email=email, phone=phoneno, adress=adress, city=city, division=division, zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/Checkout.html', {'thank': thank, "id": id})
    return render(request, 'shop/Checkout.html')