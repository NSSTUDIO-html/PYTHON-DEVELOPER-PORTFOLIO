from django.shortcuts import render
from .models import Product  # Assuming you have a Product model

def home(request):
    return render(request, 'inventory_app/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_app/product_list.html', {'products': products})
