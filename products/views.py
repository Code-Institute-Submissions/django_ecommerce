from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})
    
def product_information(request, pk):
    product_information = get_object_or_404 (Product, pk=pk)
    return render(request, "product_information.html", {"product_information": product_information})
    
    
def brand_products(request, BRAND_CHOICES):
    BRAND_CHOICES = Product.objects.filter(brand=BRAND_CHOICES)
    return render(request, "brand_products.html", {"product_brand":BRAND_CHOICES})
    
    
def age_products(request, AGE_CHOICES):
    AGE_CHOICES = Product.objects.filter(age=AGE_CHOICES)
    return render(request, "age_products.html", {"age_products":AGE_CHOICES})