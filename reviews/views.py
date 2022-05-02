from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import datetime

reviewss = []

class AddReview(forms.Form):
    name = forms.CharField(label = "Name", min_length = 1, max_length = 100)
    review = forms.CharField(label = "Review ", min_length = 1, max_length = 100)

# Create your views here.

def reviews(request):
    return render(request, "reviews/reviews.html", {
        "reviews": reviewss
    })

def add(request):
    if request.method =="POST":
        form = AddReview(request.POST)
        if form.is_valid():
            now = datetime.datetime.now()
            review = (form.cleaned_data["name"],form.cleaned_data["review"], now.strftime("%d-%m-%y"))
            reviewss.append(review)
            return HttpResponseRedirect("/reviews")
        else: 
            return render(request, "reviews/add.html",{
                "form": form
            })
    return render(request, "reviews/add.html", {
        "form": AddReview()
    })
