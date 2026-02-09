from django.urls import path
from django.shortcuts import render

def cart_page(request):
    return render(request, 'cart.html')

urlpatterns = [
    path('cart/', cart_page),
]
