from django.shortcuts import render

from .models import Aboutcoffee

# Create your views here.

def aboutcoffee(request):
    if request.user.is_authenticated:
        return render(request, 'aboutcoffee/aboutcoffee.html',{
            "message": 'logout',
            "aboutcoffee": Aboutcoffee.objects.all()
        })
    else:
        return render(request, 'aboutcoffee/aboutcoffee.html',{
            "message": 'login',
            "aboutcoffee": Aboutcoffee.objects.all()
        })