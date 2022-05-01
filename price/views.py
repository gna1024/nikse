from django.shortcuts import render

# Create your views here.

def price(request):
    return (render(request, "price/price.html"))
