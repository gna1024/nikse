from django.shortcuts import render
order = []
  
# Create your views here.

def coffee(request):
    return render(request, 'orderahead/orderahead.html', {
        "order": order
    })

def cart(request):
    return render(request, 'cart/cart.html', {
        "order": order,
        "len": len(order)
    })
