from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'mainpage/mainpage.html',{
            "message": 'logout'
        })
    else:
        return render(request, 'mainpage/mainpage.html',{
            "message": 'login'
        })

def login_view(request):
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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main"))

def register(request):
    data = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Hi!"
            return render(request, "mainpage/login.html", data)
    else:
        form = UserCreationForm()
        data['form'] = form
    return render(request, "mainpage/register.html", data)
