from django.shortcuts import render

from .models import Price

# Create your views here.

def price(request):
    if request.user.is_authenticated:
        return render(request, 'price/price.html',{
            "message": 'logout',
            "price": Price.objects.all()
        })
    else:
        return render(request, 'price/price.html',{
            "message": 'login',
            "price": Price.objects.all()
        })
