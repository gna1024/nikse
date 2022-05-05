from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Order
orders = []
  
# Create your views here.

def coffee(request):
    if request.method =="POST":
        if 'Espresso' in request.POST:
            orders.append("espresso")
        if 'Doppio' in request.POST:
            orders.append("doppio")    
        if 'Americano' in request.POST:
            orders.append("americano")
        if 'Latte Macchiato' in request.POST:
            orders.append("lattemacchiato") 
        if 'Caramel Macchiato' in request.POST:
            orders.append("caramelmacchiato")   
        if 'Latte' in request.POST:
            orders.append("latte")
        if 'Iced Latte' in request.POST:
            orders.append("icedlatte")  
        if 'Cappuccino' in request.POST:
            orders.append("cappuccino")
        if 'Flat White' in request.POST:
            orders.append("flatwhite") 
        if 'Irish Coffee' in request.POST:
            orders.append("irishcoffee")   
    return render(request, "orderahead/orderahead.html", {
        "order": Order.objects.all()
    })
    

def cart(request):
    if request.method =="POST":
        if 'del' in request.POST:
            orders.clear()
    return render(request, 'cart/cart.html', {
        "order": orders,
        "len": len(orders)
    })
