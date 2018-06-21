from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class ProductAdmin(ImportExportModelAdmin):
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

class ProductCategoryAdmin(ImportExportModelAdmin):
    list_display = (
        'parent',
        'name',
        'created_at',
        'updated_at',
        'active'
    )

admin.site.register(ProductCategory, ProductCategoryAdmin)

class InventoryAdmin(ImportExportModelAdmin):
    list_display = (
        'product',
        'quantity',
        'created_at',
        'updated_at',
    )

admin.site.register(Inventory, InventoryAdmin)

class OrderProductInline(admin.StackedInline):
    model = OrderProduct

class OrderAdmin(ImportExportModelAdmin):
    inlines = [OrderProductInline,]
    
    list_display = (
        'table',
        'finished',
        'created_at',
        'updated_at',
        'active',
    )
    # filter_horizontal = ()

admin.site.register(Order, OrderAdmin)

class TableAdmin(ImportExportModelAdmin):
    list_display = (
        'uid',
        'created_at',
        'updated_at',
        'active',
    )

admin.site.register(Table, TableAdmin)