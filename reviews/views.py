from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import datetime
from .models import Review

class AddReview(forms.Form):
    name = forms.CharField(label = "Name", min_length = 1, max_length = 100)
    review = forms.CharField(label = "Review ", min_length = 1, max_length = 100)

# Create your views here.

def reviews(request):
    if request.user.is_authenticated:
        return render(request, 'reviews/reviews.html',{
            "message": 'logout',
            "reviews": Review.objects.all()
        })
    else:
        return render(request, 'reviews/reviews.html',{
            "message": 'login',
            "reviews": Review.objects.all()
        })

def add(request):
    if request.method =="POST":
        form = AddReview(request.POST)
        if form.is_valid():
            now = datetime.datetime.now()
            now.strftime("%d-%m-%y")
            review_ = Review(name = form.cleaned_data["name"], review = form.cleaned_data["review"], date = now)
            review_.save()
            return HttpResponseRedirect("/reviews")
        else: 
            return render(request, "reviews/add.html",{
                "form": form
            })
    return render(request, "reviews/add.html", {
        "form": AddReview()
    })
