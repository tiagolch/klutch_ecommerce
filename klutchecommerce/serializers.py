from rest_framework import serializers
from .models import Customers, Products, Orders


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='Customers.id')
    product_id = serializers.IntegerField(source='Products.id')

    class Meta:
        model = Orders
        fields = '__all__'