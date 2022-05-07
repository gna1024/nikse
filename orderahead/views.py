from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from requests import delete
from .models import Order, Cart

x = 0

# Create your views here.

def coffee(request):
    if request.method =="POST":
        if 'Espresso' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Espresso.jpeg" , name = "Espresso", price ="1.1")
                cart.save()
        if 'Doppio' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Doppio.jpeg" , name = "Doppio", price ="1.25")
                cart.save()    
        if 'Americano' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Americano.jpeg" , name = "Americano", price ="1.25")
                cart.save()
        if 'Latte Macchiato' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Lattemacchiato.jpeg" , name = "Latte Macchiato", price ="1.7")
                cart.save()
        if 'Caramel Macchiato' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Caramelmacchiato.jpeg" , name = "Caramel Macchiato", price ="1.9")
                cart.save() 
        if 'Latte' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Latte.jpeg" , name = "Latte", price ="2.1")
                cart.save()
        if 'Iced Latte' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Lattemacchiato.jpeg" , name = "Iced Latte", price ="2.25")
                cart.save()  
        if 'Cappuccino' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Cappuccino.jpeg" , name = "Cappuccino", price ="2.15")
                cart.save()
        if 'Flat White' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Flatwhite.jpeg" , name = "Flat White", price ="1.8")
                cart.save()
        if 'Irish Coffee' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login")
            else:
                cart = Cart(img = "Irishcoffee.jpeg" , name = "Irish Coffee", price ="2.5")
                cart.save()   
    if request.user.is_authenticated:
        return render(request, 'orderahead/orderahead.html',{
            "message": 'logout',
            "order": Order.objects.all()
        })
    else:
        return render(request, 'orderahead/orderahead.html',{
            "message": 'login',
            "order": Order.objects.all()
        })    

def cart(request):
    if request.method =="POST":
        if request.POST.get('del'):
            Cart.objects.all().delete()
    if request.user.is_authenticated:
        return render(request, 'cart/cart.html',{
            "message": 'logout',
            "order": Cart.objects.all(),
            "len": Cart.objects.count()
        })
    else:
        return render(request, 'cart/cart.html',{
            "message": 'login',
            "order": Cart.objects.all(),
            "len": Cart.objects.count()
        })
