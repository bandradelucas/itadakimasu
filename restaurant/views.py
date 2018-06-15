from django.shortcuts import render
from .models import Product

def index(request):
    context = {
        'token': 'teste',
    }
    return render(request, 'restaurant/index.html', context)
    
def products(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'restaurant/products.html', context)