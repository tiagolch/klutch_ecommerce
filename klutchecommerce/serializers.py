from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Customers, Products, Orders


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'name', 'email', 'get_created_at', 'get_updated_at']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name','price','quantity','get_created_at','get_updated_at']


class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='Customers.id')
    # products_id = serializers.IntegerField(source='Products.id')
    # productSerializer_set = ProductsSerializer(many=True)
    # products = SerializerMethodFields()

    class Meta:
        model = Orders
        fields = ['customer_id', 'products', 'get_created_at', 'get_updated_at']

    def cria_produtos(self, products, orders):
        for product in products:
            p = Products.objects.create(**product)
            orders.produtcts_id.add(p)

    def create(self, validated_data):
        order_product = validated_data['Products']
        del validated_data['Products']
        products = Products.objects.create(**validated_data)
        self.cria_produtos(products, order_product)
