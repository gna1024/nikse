from django.shortcuts import render

# Create your views here.

def aboutcoffee(request):
    return render(request, "aboutcoffee/aboutcoffee.html")