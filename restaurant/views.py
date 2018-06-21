from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Table, Order, OrderProduct
import simplejson, json

def index(request):
    orders = Order.objects.filter(finished=False);
    
    context = {
        'orders': orders,
    }
    return render(request, 'restaurant/index.html', context)
    
def products(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'restaurant/products.html', context)
    
def ws_get_order_products(request, order_id):
    order_products = OrderProduct.objects.filter(order_id=order_id).values(
        'product_id',
        'product__name',
        'quantity',
    )
    
    return JsonResponse({
        'order_products': list(order_products)
    })