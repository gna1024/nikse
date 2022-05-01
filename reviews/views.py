from django.shortcuts import render
from django import forms

reviewss = ["The best coffee", "Great!!!"]

# Create your views here.

def reviews(request):
    return render(request, "reviews/reviews.html", {
        "reviews": reviewss
    })

def add(request):
    return render(request, "reviews/add.html")
