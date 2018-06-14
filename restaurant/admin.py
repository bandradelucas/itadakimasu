from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'price',
        'image',
        'menu',
        'created_at',
        'updated_at',
        'active'
    )

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'parent',
        'name',
        'created_at',
        'updated_at',
        'active'
    )

admin.site.register(ProductCategory, ProductCategoryAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'created_at',
        'updated_at',
    )

admin.site.register(Inventory, InventoryAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'table',
        'finished',
        'created_at',
        'updated_at',
        'active',
    )

admin.site.register(Order, OrderAdmin)