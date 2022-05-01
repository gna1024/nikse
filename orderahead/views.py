from django.shortcuts import render

# Create your views here.

def coffee(request):
    return render(request, 'orderahead/orderahead.html')
