# Hare krishna
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
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
    thank = False
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phoneno = request.POST.get("phone", "")
        message = request.POST.get("message", "")
        contact = Contact(name=name, email=email, phone=phoneno, message=message)
        contact.save()
        thank = True
    return render(request, 'shop/Contact.html', {'thank':thank})


def Tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get("orderId", "")
        email = request.POST.get("email", "")
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("[]")

        except Exception as e:
            return HttpResponse("{}")



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
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/Checkout.html', {'thank': thank, "id": id})
    return render(request, 'shop/Checkout.html')