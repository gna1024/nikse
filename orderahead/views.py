from django.shortcuts import render
from django.http import HttpResponseRedirect

order = []
  
# Create your views here.

def coffee(request):
    if request.method =="POST":
        if 'espresso' in request.POST:
            order.append("espresso")
        if 'doppio' in request.POST:
            order.append("doppio")    
        if 'americano' in request.POST:
            order.append("americano")
        if 'lattemacchiato' in request.POST:
            order.append("lattemacchiato") 
        if 'caramelmacchiato' in request.POST:
            order.append("caramelmacchiato")   
        if 'latte' in request.POST:
            order.append("latte")
        if 'icedlatte' in request.POST:
            order.append("icedlatte")  
        if 'cappuccino' in request.POST:
            order.append("cappuccino")
        if 'flatwhite' in request.POST:
            order.append("flatwhite") 
        if 'irishcoffee' in request.POST:
            order.append("irishcoffee")    
    return render(request, "orderahead/orderahead.html")
    

def cart(request):
    if request.method =="POST":
        if 'del' in request.POST:
            order.clear()
    return render(request, 'cart/cart.html', {
        "order": order,
        "len": len(order)
    })
