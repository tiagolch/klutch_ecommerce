from django.contrib import admin
from .models import Customers, Products, Orders


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'get_created_at', 'get_updated_at']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'get_created_at', 'get_updated_at']


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'get_created_at', 'get_updated_at']


