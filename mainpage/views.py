from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    return render(request, 'mainpage/mainpage.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main"))
        else:
            return render(request, 'mainpage/login.html', {
                "message": 'Invalid credentials.'
            })
    return render(request, 'mainpage/login.html')

def logout(request):
    return render(request, 'mainpage/login.html')
