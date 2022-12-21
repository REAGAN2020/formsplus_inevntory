from rest_framework import serializers
from .models import Product, Label, Cart

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'labels', 'quantity', 'price']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']