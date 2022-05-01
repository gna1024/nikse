from django.urls import path

from . import views

urlpatterns = [
    path("", views.coffee, name = "orderahead"),
    path("cart", views.cart, name = "cart")
]