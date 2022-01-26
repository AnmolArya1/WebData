from django.contrib import admin
from django.urls import reverse
from .models import ProductData
from .models import OrderData

# Register your models here.
@admin.register(ProductData)
class ProductDataModelAdmin(admin.ModelAdmin):
 list_display = ['PRODUCT_NAME', 'DESCRIPTION', 'PRICE', 'IMAGE']

@admin.register(OrderData)
class OrderDataModelAdmin(admin.ModelAdmin):
    list_display = ['ORDER_ID', 'PRODUCT_ID', 'DATE', 'PRICE', 'QTY', 'IMAGE']
    
