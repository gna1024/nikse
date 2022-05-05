from django.shortcuts import render

from .models import Price

# Create your views here.

def price(request):
    return render(request, "price/price.html", {
        "price": Price.objects.all()
    })
