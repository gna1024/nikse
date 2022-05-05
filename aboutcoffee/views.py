from django.shortcuts import render

from .models import Aboutcoffee

# Create your views here.

def aboutcoffee(request):
    return render(request, "aboutcoffee/aboutcoffee.html", {
        "aboutcoffee": Aboutcoffee.objects.all()
    })